from classes.user_class import *
from classes.ebook_class import *
from classes.booking_class import *
from db_access.db_user import *
from db_access.db_ebook import *
from db_access.db_booking import *

ebook_1 = EBook(1, 'Lord of the Rings', 'Fantasy', '25/10/1980')
ebook_2 = EBook(2, 'Lord Loss', 'Fantasy', '25/12/2005')
ebook_3 = EBook(3, 'xyz', 'romance', '11/11/2000')
ebook_4 = EBook(4, 'abc', 'def', '12/04/2010')
# user_list_1 = []
# book_list_1 = []
# user_table = DBUsers()
# for row in user_table.get_all():
#     user_list_1.append(User(row[0], row[1], row[2], row[3], row[4], row[5]))
#
#
# ebook_table = DBEbooks()
# for row in ebook_table.get_all():
#     book_list_1.append(EBook(row[0], row[1], row[2], row[3], row[4]))
# book_library_list_1 = book_list_1.copy()
#
# booking_table = DBBooking()
user_1 = User(1, 'hello', 'Ryan', 'Smith', 'smithr@example', '0795231231541')
user_2 = User(2, 'hello1', 'Ryan2', 'Smith', 'smithr@example', '0795231231541')

book_list_buttons = []
rented_books_buttons = []
selected_user=''
user_list = [user_1, user_2]
book_list = [ebook_1, ebook_2, ebook_3, ebook_4]
book_library_list = book_list.copy()
