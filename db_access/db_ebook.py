from db_access.db_connection import DBConnection


class DBEbooks(DBConnection):

    def __init__(self):
        super().__init__()

    def new_table(self):
        self.__create_table()

    def __create_table(self):
        self.sql_query("""CREATE TABLE EBooks
(
ebook_ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
title VARCHAR(40),
genre VARCHAR(40),
release_date DATE,
users_ID int,
CONSTRAINT fk_users_ID FOREIGN KEY (users_ID) REFERENCES Users(users_ID)
);""")

    def get_all(self):
        result_list = []
        q_result = self.sql_query('SELECT * FROM EBooks')
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)
            return result_list

    def get_book_by_id(self, id):
        return self.sql_query(f"SELECT * FROM EBooks WHERE ebook_ID = '{id}'")

    def create_book(self, title, genre, release_date, user_id):
        self.sql_query(f"""INSERT INTO EBooks
(
title, genre, release_date, users_ID
)
VALUES
(
'{title}', '{genre}', '{release_date}', '{user_id}'
);""")
        self.conn.commit()