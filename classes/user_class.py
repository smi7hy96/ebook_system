class User:
    def __init__(self, user_id=None, password=None, first_name=None, last_name=None, email=None, phone_no=None, books=None, booking=None):
        self.user_id = user_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        if books is None:
            self.books = []
        else:
            self.books = books
        if booking is None:
            self.booking = []
        else:
            self.booking = booking
