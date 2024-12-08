from utils import *

st.set_page_config(layout="wide")
st.header(f"{STR_MENU_DB} 💻")

cfg_data = db_current_cfg()
DB_NAME = cfg_data.get("db_name")
DB_URL = cfg_data.get("db_url")

db_info = {
    "chinook": f"""  
    ##### <span style="color: blue;">Chinook music store </span>
    https://www.sqlitetutorial.net/sqlite-sample-database/
    """,

    "movie": f"""
    ##### <span style="color: blue;">Movies DB</span>
    https://pypi.org/project/imdb-sqlite/
    """,

    "company_rank": f"""
    ##### <span style="color: blue;">World Top Company Ranks</span>
    https://www.kaggle.com/datasets/patricklford/largest-companies-analysis-worldwide
    """,
}

def _execute_code_sql(code, db_url=DB_URL):
    with DBConn(db_url) as _conn:
        if code.strip().lower().startswith("select") or code.strip().lower().startswith("with"):
            df = pd.read_sql(code, _conn)
            st.dataframe(df)
        elif code.strip().split(" ")[0].lower() in ["create", "insert","update", "delete", "drop"]:
            cur = _conn.cursor()
            cur.executescript(code)
            _conn.commit()

def do_database():

    st.markdown(f"""
    #### SQL Editor
    """, unsafe_allow_html=True)

    db_type = cfg_data.get("db_type")
    if db_type != "SQLite":
        st.error(f"Unsupported DB Type: {db_type}")
        return    

    avail_dbs = list_datasets(db_type)
    db_names = sorted(list(avail_dbs.keys()))
    c1, c2, c3  = st.columns([2,2,4])
    with c1:
        db_name = st.selectbox(
            "DB Name",
            options=(db_names + [META_DB_NAME]),
            index=db_names.index(DB_NAME),
            key="select_db_name"
        )
        db_url = CFG["META_DB_URL"] if db_name == META_DB_NAME else avail_dbs[db_name].get("db_url")

        tables = db_list_tables_sqlite(db_url)
        idx_default = 0
        schema_value = st.session_state.get("TABLE_SCHEMA", "")

    with c2:
        table_name = st.selectbox(
            "Table:", 
            options=tables, 
            index=idx_default, 
            key="select_table_name"
        )
        if st.button("Show Schema"):
            with DBConn(db_url) as _conn:
                df_schema = pd.read_sql(f"select sql from sqlite_schema where name = '{table_name}'; ", _conn)
                schema_value = df_schema["sql"].to_list()[0]
                st.session_state.update({"TABLE_SCHEMA" : schema_value})

    with c3:
        st.text_area("Schema:", value=schema_value, height=150)

    sql_stmt = st.text_area(
        "SQL Console:", 
        value=f"select * from {table_name} limit 10;", 
        height=100
    )
    if st.button("Execute Query ..."):
        try:
            _execute_code_sql(code=sql_stmt, db_url=db_url)
            st.success(f"Success!")
        except:
            st.error(format_exc())


    if db_name == "chinook":
        st.image("https://github.com/gongwork/data-copilot/blob/main/docs/sqlite-sample-database-chinook.jpg?raw=true")


## sidebar Menu
def do_sidebar():
    with st.sidebar:
        with st.expander("Show Configuration", expanded=False):
            cfg_show_data(cfg_data)

def main():
    do_sidebar()
    do_database()

if __name__ == '__main__':
    main()
