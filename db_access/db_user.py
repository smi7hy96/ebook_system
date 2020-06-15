from db_access.db_connection import DBConnection


class DBUsers(DBConnection):

    def __init__(self):
        super().__init__()

    def __create_table(self):
        self.sql_query("""CREATE TABLE Users
(
users_ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
password VARCHAR(20),
first_name VARCHAR(20),
last_name VARCHAR(20),
email VARCHAR(100),
phone_No VARCHAR(15)
);""")

    def get_all(self):
        result_list = []
        q_result = self.sql_query('SELECT * FROM Users')
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)
            return result_list

    def create_user(self, password, first_name, last_name, email):
        self.sql_query(f"""INSERT INTO Users
(
password, first_name, las_name, email
)
VALUES
(
'{password}', '{first_name}', '{last_name}', '{email}'
);""")
        self.conn.commit()