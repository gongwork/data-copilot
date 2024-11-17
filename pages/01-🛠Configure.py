from utils import *

st.set_page_config(layout="wide")
st.header(f"{STR_MENU_CONFIG} 🛠")


TABLE_NAME = CFG["TABLE_CONFIG"]
KEY_PREFIX = f"col_{TABLE_NAME}"

llm_model_list = list(LLM_MODEL_MAP.keys())

def db_upsert_cfg(data):
    llm_vendor=data.get("llm_vendor")
    llm_model=data.get("llm_model")
    vector_db=data.get("vector_db")
    db_type=data.get("db_type")
    db_url=data.get("db_url")
    with DBConn() as _conn:
        sql_stmt = f"""
            select 
                *
            from {TABLE_NAME}
            where 1=1
                and llm_vendor='{llm_vendor}'
                and llm_model='{llm_model}'
                and vector_db='{vector_db}'
                and db_type='{db_type}'
                and db_url='{db_url}'
                and is_active='Y'
            order by ts desc
            limit 1
            ;
        """
        # print(sql_stmt)
        df = pd.read_sql(sql_stmt, _conn)
        curr_ts = get_ts_now()

        if df is None or df.empty:
            id_new = get_uuid()
            # insert
            sql_script = f"""
                insert into {TABLE_NAME} (
                    id,
                    vector_db,
                    llm_vendor,
                    llm_model,
                    db_type,
                    db_url,
                    created_ts,
                    ts,
                    is_active
                ) values (
                    '{id_new}',
                    '{vector_db}',
                    '{llm_vendor}',
                    '{llm_model}',
                    '{db_type}',
                    '{db_url}',
                    '{curr_ts}',
                    '{curr_ts}',
                    'Y'
                );
            """
        else:
            curr_data = df.to_dict("records")[0]
            id_old = curr_data.get("id")
            # update        
            sql_script = f"""
                update {TABLE_NAME} 
                set ts = '{curr_ts}'
                where id = '{id_old}'
                ;
            """
        # print(sql_script)
        db_run_sql(sql_script, _conn)

def get_config_data(LIMIT=10):
    with DBConn() as _conn:
        sql_stmt = f"""
            select 
                *
            from {TABLE_NAME}
            order by ts desc
            limit {LIMIT}
            ;
        """
        # print(sql_stmt)
        return pd.read_sql(sql_stmt, _conn)

def main():
    cfg_data = db_query_config()
    # st.write(cfg_data)
    st.markdown(f"""
    ##### Data Base

    """, unsafe_allow_html=True)
    
    with st.expander("Specify data source: (default - SQLite)", expanded=True):
        db_list = sorted(SQL_DIALECTS)
        c1, c2 = st.columns([2,6])
        with c1:
            db_type = st.selectbox(
                "DB Type",
                options=db_list,
                index=db_list.index(cfg_data.get("db_type"))
            )

        with c2:
            avail_dbs = list_datasets(db_type)
            db_url = st.selectbox(
                "DB URL",
                options=avail_dbs,
                index=avail_dbs.index(cfg_data.get("db_url"))
            )

    st.markdown(f"""
    ##### Knowledge Base
    """, unsafe_allow_html=True)    

    with st.expander("Specify vector store: (default - ChromaDB)", expanded=True):
        vector_db_list = sorted(VECTOR_DB_LIST)
        vector_db = st.selectbox(
            "Vector DB Type",
            options=vector_db_list,
            index=vector_db_list.index(cfg_data.get("vector_db"))
        )

    st.markdown(f"""
    ##### GenAI Model

    """, unsafe_allow_html=True)    

    with st.expander("Specify LLM model: (default - Alibaba QWen 2.5 Coder) ", expanded=True):
        llm_model_name = LLM_MODEL_REVERSE_MAP.get(cfg_data.get("llm_model"), DEFAULT_LLM_MODEL)
        model_selected = st.radio(
            "Model name",
            options=llm_model_list,
            index=llm_model_list.index(llm_model_name),
        )
        # st.write(f"selected model: {model_selected}")
        llm_vendor, llm_model = parse_llm_model_spec(model_selected)

    if st.button("Save"):
        cfg_data = dict(
            llm_vendor=llm_vendor, 
            llm_model=llm_model, 
            vector_db=vector_db, 
            db_type=db_type, 
            db_url=db_url
        )
        db_upsert_cfg(cfg_data)


if __name__ == '__main__':
    main()

    with st.expander("Show Config Data:", expanded=False):
        data = get_config_data()
        st.dataframe(data)
