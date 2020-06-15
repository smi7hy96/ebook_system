from db_access.db_connection import DBConnection
from datetime import datetime

class DBBooking(DBConnection):

    def __init__(self):
        super().__init__()

    def __create_table(self):
        self.sql_query("""CREATE TABLE Booking(
booking_ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
ebook_ID int,
users_ID int,
booking_date date,
booking_price int,
returned VARCHAR(10),
CONSTRAINT fk_users_ID_bk FOREIGN KEY (users_ID) REFERENCES Users(users_ID),
CONSTRAINT fk_ebook_ID FOREIGN KEY (ebook_ID) REFERENCES Ebooks(ebook_ID)
);""")

    def get_all_by_id(self, id):
        return self.sql_query(f"SELECT ebook_ID FROM Booking WHERE users_id = '{id} AND returned = 'False'")

    def create_booking(self, bookID, userID):
        self.sql_query(f"""INSERT INTO Booking
(
ebook_ID, users_ID, booking_date, booking_price, returned
)
VALUES
(
'{bookID}', '{userID}', '{datetime.date(datetime.now())}', '5', 'False'
)
""")
        self.conn.commit()

    def return_book(self, bookID, userID):
        self.sql_query(f"""UPDATE Booking
SET returned = 'True'
WHERE ebook_ID = '{bookID}' AND users_ID = '{userID}' AND returned = 'False'""")
        self.conn.commit()

