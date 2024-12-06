-- drop table t_user;
CREATE TABLE IF NOT EXISTS t_user
(
	id INTEGER PRIMARY KEY AUTOINCREMENT
	, email TEXT NOT NULL UNIQUE
	, username TEXT NOT NULL
	, password BLOB NOT NULL
	, is_admin INTEGER DEFAULT 0 CHECK(is_admin IN (0, 1))
	, is_active INTEGER DEFAULT 1 CHECK(is_active IN (0, 1))
	, profile TEXT
	, note TEXT

	, created_ts TEXT
	, ts TEXT
);
/*
insert into t_user(email,username,password) 
values('joe_coder@gmail.com', 'joe_coder', 'joe_coder');
select * from t_user;
*/

-- drop table t_config;
CREATE TABLE if not exists t_config
(
    id text NOT NULL

    , vector_db text
	, llm_vendor text
	, llm_model text
	, db_name text   -- logic dataset name
	, db_type text
	, db_url text
	, db_instance text
	, db_username text
	, db_password text
	, db_port INTEGER

	, note text
	, created_ts text
	, ts text
	, is_active text  DEFAULT 'Y'

	, email text  NOT NULL -- user email
);

-- drop table t_qa;
CREATE TABLE if not exists t_qa
(
    id text NOT NULL
    , id_config text NOT NULL

    , question text NOT NULL
	, question_hash text

	, sql_generated text
	, sql_ts_delta float
	, sql_revised text
	, sql_hash text
	, sql_is_valid INTEGER  DEFAULT 0

	, df_ts_delta float

	, py_generated text
	, py_ts_delta float
	, py_revised text
	, py_hash text
	, py_is_valid text  DEFAULT 'Y'

	, fig_generated text
	, fig_ts_delta float
	
	, summary_generated text
	, summary_ts_delta float

	, note text
	, created_ts text
	, ts text
	, is_active text  DEFAULT 'Y'

	, email text  NOT NULL -- user email
);


-- drop table t_note;
CREATE TABLE if not exists t_note
( 
    id text NOT NULL
    , note_name text NOT NULL
    , url text 
	, note_type TEXT DEFAULT '' CHECK(note_type IN ('', 'learning', 'research', 'project', 'journal'))
	, note text
	, tags text

	, created_ts text
	, ts text
	, is_active text  DEFAULT 'Y'

	, email text  NOT NULL -- user email
);
-- select * from t_note;


