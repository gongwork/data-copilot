from utils import *

st.set_page_config(layout="wide")
st.header(f"{STR_MENU_TRAIN} 📚")

def main():
    cfg_data = db_query_config()
    
    vn = setup_vanna(cfg_data)


    with st.expander("Manage Knowledge", expanded=False):
        c_1, c_2, c_3 = st.columns([4,1,3])
        df = None
        with c_1:
            if st.button("Show"):
                df = vn.get_training_data()

        with c_3:
            collection_id = st.text_input("Enter collection ID", value="", key="del_collection")
            btn_rm_id = st.button("Remove")
            if btn_rm_id and collection_id:
                vn.remove_training_data(id=collection_id)

        with c_2:
            btn_rm_all = st.button("Remove All")
            if btn_rm_all:
                for c in ["sql", "ddl", "documentation"]:
                    vn.remove_collection(c)

        if df is not None and not df.empty:
            st.dataframe(df)


    with st.expander("Add Schema", expanded=True):
        c1, c2 = st.columns([2,2])
        with c1:
            btn_add_all_ddl = st.button("Add All DDL scripts")
            df_ddl = None
            if btn_add_all_ddl:
                sql_stmt = """
                    select * from sqlite_master where type='table' and name not like 'sqlite%';
                """
                df_ddl = vn.run_sql(sql_stmt)
                for ddl in df_ddl['sql'].to_list():
                    ddl_text = strip_brackets(ddl)
                    vn.train(ddl=ddl_text)
                if df_ddl is not None and not df_ddl.empty:
                    st.dataframe(df_ddl)

        with c2:
            ddl_sample = """CREATE TABLE IF NOT EXISTS t_person (
                id INT PRIMARY KEY,
                name text,
                email text
            );
            """
            ddl_text = st.text_area("DDL script", value="", height=100, key="add_ddl"
                                ,placeholder=ddl_sample)

            btn_add_ddl = st.button("Add DDL")
            if btn_add_ddl and ddl_text:
                ddl_text = strip_brackets(ddl_text)
                result = vn.train(ddl=ddl_text)
                st.write(result)


    with st.expander("Add Question/SQL Pair", expanded=False):
        q_sample, sql_sample = "Get book counts", "select count(*) from t_book;"
        c3, c4 = st.columns([3,5])
        with c3:
            q_text = st.text_input("Question", value="", key="add_sql_q"
                            ,placeholder=q_sample)
        with c4:
            sql_text = st.text_area("SQL query", value="", height=100, key="add_sql"
                            ,placeholder=sql_sample)
        if st.button("Add", key="btn_add_question_sql") and sql_text and q_text:
            result = vn.train(question=q_text, sql=sql_text)
            st.write(result)

    with st.expander("Add Documentation", expanded=False):
        doc_sample = """table "t_book" stores information on book title and author """
        doc_text = st.text_area("Documentation", value="", height=100, key="add_doc"
                            ,placeholder=doc_sample)
        if st.button("Add", key="btn_add_doc") and doc_text:
            result = vn.train(documentation=doc_text)
            st.write(result)


if __name__ == '__main__':
    main()