class Booking:
    def __init__(self, booking_id=None, booking_date=None, booking_price=None, book_id=None, user_id=None, returned="False"):
        self.booking_id = booking_id
        self.booking_date = booking_date
        self.booking_price = booking_price
        self.book_id = book_id
        self.user_id = user_id
        self.returned = returned
