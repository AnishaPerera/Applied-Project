Instructions

Create two databases called users and vulnerabilitiesDB in postgresql

Import both sql files (vulnerabilitiesDB.sql, users.sql) into the correct databases

Change Databases section with your postgesql password (or other details if changed) in settings.py file (located at project folder)

Use user_logins.txt file details for user sign in


Note :-

If unable to import using pgadmin in postgresql, use the SQL shell(psql) with commands below for import


psql -U user_name -W -d db_name -f vulnerabilitiesDB.sql

psql -U user_name -W -d db_name -f users.sql


(replace user_name with your postgres username and db_name with your database name)