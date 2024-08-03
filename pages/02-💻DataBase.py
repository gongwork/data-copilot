from utils import *

st.set_page_config(layout="wide")
st.header(f"{STR_MENU_DB} 💻")

cfg_data = db_query_config()
DB_URL = cfg_data.get("db_url")

def get_data(table_name):
    with DBConn(DB_URL) as _conn:
        sql_stmt = f"""
            select 
                *
            from {table_name}
            limit 5
            ;
        """
        # print(sql_stmt)
        return pd.read_sql(sql_stmt, _conn)


def _get_tables():
    """get a list of tables from SQLite database
    """
    with DBConn(DB_URL) as _conn:
        sql_stmt = f'''
        SELECT 
            name
        FROM 
            sqlite_schema
        WHERE 
            type ='table' AND 
            name NOT LIKE 'sqlite_%';
        '''
        df = pd.read_sql(sql_stmt, _conn)
    return df["name"].to_list()

def _execute_code_sql(code):
    with DBConn(DB_URL) as _conn:
        if code.strip().lower().startswith("select"):
            df = pd.read_sql(code, _conn)
            st.dataframe(df)
        elif code.strip().split(" ")[0].lower() in ["create", "insert","update", "delete", "drop"]:
            cur = _conn.cursor()
            cur.executescript(code)
            _conn.commit()

def main():


    st.markdown(f"""
    #### SQL Editor
    Current DB URL = {DB_URL}
    """, unsafe_allow_html=True)    

    tables = _get_tables()
    idx_default = 0
    schema_value = st.session_state.get("TABLE_SCHEMA", "")
    c1, _, c2  = st.columns([3,1,8])
    with c1:
        table_name = st.selectbox("Table:", tables, index=idx_default, key="table_name")
        if st.button("Show schema"):
            with DBConn(DB_URL) as _conn:
                df_schema = pd.read_sql(f"select sql from sqlite_schema where name = '{table_name}'; ", _conn)
                schema_value = df_schema["sql"].to_list()[0]
                st.session_state.update({"TABLE_SCHEMA" : schema_value})

    with c2:
        st.text_area("Schema:", value=schema_value, height=150)

    sql_stmt = st.text_area("SQL:", value=f"select * from {table_name} limit 10;", height=100)
    if st.button("Execute Query ..."):
        try:
            _execute_code_sql(code=sql_stmt)
        except:
            st.error(format_exc())


    st.markdown(f"""
    #### Datasets
    
    ##### <span style="color: blue;">Chinook music store </span>
    https://www.sqlitetutorial.net/sqlite-sample-database/
    """, unsafe_allow_html=True)    

    st.image("./docs/sqlite-sample-database-chinook.jpg")

    st.markdown(f"""
    ##### <span style="color: blue;">ImDB movies </span>
    https://pypi.org/project/imdb-sqlite/
    """, unsafe_allow_html=True)    




if __name__ == '__main__':
    main()
