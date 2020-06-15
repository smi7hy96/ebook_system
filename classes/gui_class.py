import tkinter as tk
from preset_variables import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        page_1_frame = tk.Frame(self, bg="white")
        label = tk.Label(page_1_frame, text="Create User!")
        label.pack(side="top", fill="both", expand=True)

        self.user_first_name = tk.Entry(page_1_frame)
        self.user_first_name.insert(0, 'First Name')
        self.user_first_name.bind("<FocusIn>", lambda args: self.focus_in("fn"))
        self.user_first_name.bind("<FocusOut>", lambda args: self.focus_out())
        self.user_first_name.pack()

        self.user_last_name = tk.Entry(page_1_frame)
        self.user_last_name.insert(0, 'Last Name')
        self.user_last_name.bind("<FocusIn>", lambda args: self.focus_in("ln"))
        self.user_last_name.bind("<FocusOut>", lambda args: self.focus_out())
        self.user_last_name.pack()

        self.user_email = tk.Entry(page_1_frame)
        self.user_email.insert(0, 'Email')
        self.user_email.bind("<FocusIn>", lambda args: self.focus_in("em"))
        self.user_email.bind("<FocusOut>", lambda args: self.focus_out())
        self.user_email.pack()

        self.user_password = tk.Entry(page_1_frame, show="*")
        self.user_password.insert(0, 'Password')
        self.user_password.bind("<FocusIn>", lambda args: self.focus_in("pass"))
        self.user_password.bind("<FocusOut>", lambda args: self.focus_out())
        self.user_password.pack()

        self.response_string = tk.StringVar(value="")
        response = tk.Label(page_1_frame, textvariable=self.response_string)
        response.configure(bg="white")
        response.pack()

        submit_button = tk.Button(page_1_frame, text="Create User", command=self.check_input)
        submit_button.configure(bg="light blue")
        submit_button.pack()

        page_1_frame.grid(row=0, column=0)
        page_1_frame.grid_rowconfigure(0, weight=1)
        page_1_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def check_input(self):
        if self.user_first_name.get() == "First Name" or self.user_last_name.get() == "Last Name" or self.user_email.get() == "Email" or self.user_password.get() == "Password":
            self.response_string.set("Invalid Details")
        elif self.user_first_name.get() == " " or self.user_last_name.get() == " " or self.user_email.get() == " " or self.user_password.get() == " ":
            self.response_string.set("Invalid Details")
        elif self.user_first_name.get() == "" or self.user_last_name.get() == "" or self.user_email.get() == "" or self.user_password.get() == "":
            self.response_string.set("Invalid Details")
        else:
            first_name = self.user_first_name.get()
            last_name = self.user_last_name.get()
            email = self.user_email.get()
            password = self.user_password.get()
            self.user_first_name.delete("0", "end")
            self.user_first_name.insert(0, 'First Name')
            self.user_last_name.delete("0", "end")
            self.user_last_name.insert(0, 'Last Name')
            self.user_email.delete("0", "end")
            self.user_email.insert(0, 'Email')
            self.user_password.delete("0", "end")
            self.user_password.insert(0, 'Password')
            self.create_user(first_name, last_name, email, password)

    def create_user(self, first_name, last_name, email, password): # ADD CLASS OBJECT TO STORE USER/ SQL QUERY
        self.response_string.set("User Created!!")
        user_list.append(User((len(user_list) + 1), password, first_name, last_name, email))
        # user_table.create_user(password, first_name, last_name, email)
        print(user_list[-1].user_id)
        print(user_list[-1].first_name)

    def focus_in(self, type):
        if type == "fn":
            if self.user_first_name.get() == "First Name":
                self.user_first_name.delete("0", "end")
        elif type == "ln":
            if self.user_last_name.get() == "Last Name":
                self.user_last_name.delete("0", "end")
        elif type == "em":
            if self.user_email.get() == "Email":
                self.user_email.delete("0", "end")
        elif type == "pass":
            if self.user_password.get() == "Password":
                self.user_password.delete("0", "end")

    def focus_out(self):
        if not self.user_first_name.get():
            self.user_first_name.insert(0, 'First Name')
        if not self.user_last_name.get():
            self.user_last_name.insert(0, 'Last Name')
        if not self.user_email.get():
            self.user_email.insert(0, 'Email')
        if not self.user_password.get():
            self.user_password.insert(0, 'Password')


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        page_2_frame = tk.Frame(self, bg="white")
        label = tk.Label(page_2_frame, text="Create Book!")
        label.pack(side="top", fill="both", expand=True)

        self.book_title = tk.Entry(page_2_frame)
        self.book_title.insert(0, 'Title')
        self.book_title.bind("<FocusIn>", lambda args: self.focus_in("bt"))
        self.book_title.bind("<FocusOut>", lambda args: self.focus_out())
        self.book_title.pack()

        self.book_genre = tk.Entry(page_2_frame)
        self.book_genre.insert(0, 'Genre')
        self.book_genre.bind("<FocusIn>", lambda args: self.focus_in("bg"))
        self.book_genre.bind("<FocusOut>", lambda args: self.focus_out())
        self.book_genre.pack()

        self.book_release_date = tk.Entry(page_2_frame)
        self.book_release_date.insert(0, 'Release Date')
        self.book_release_date.bind("<FocusIn>", lambda args: self.focus_in("brl"))
        self.book_release_date.bind("<FocusOut>", lambda args: self.focus_out())
        self.book_release_date.pack()

        self.response_string = tk.StringVar(value="")
        response = tk.Label(page_2_frame, textvariable=self.response_string)
        response.configure(bg="white")
        response.pack()

        submit_button = tk.Button(page_2_frame, text="Create Book", command=self.check_input)
        submit_button.configure(bg="light blue")
        submit_button.pack()

        page_2_frame.grid(row=0, column=0)
        page_2_frame.grid_rowconfigure(0, weight=1)
        page_2_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def check_input(self):
        if self.book_title.get() == "Title" or self.book_genre.get() == "Genre" or self.book_release_date.get() == "Release Date":
            self.response_string.set("Invalid Details")
        elif self.book_title.get() == " " or self.book_genre.get() == " " or self.book_release_date.get() == " ":
            self.response_string.set("Invalid Details")
        elif self.book_title.get() == "" or self.book_genre.get() == "" or self.book_release_date.get() == "":
            self.response_string.set("Invalid Details")
        else:
            title = self.book_title.get()
            genre = self.book_genre.get()
            release_date = self.book_release_date.get()
            self.book_title.delete("0", "end")
            self.book_title.insert(0, 'Title')
            self.book_genre.delete("0", "end")
            self.book_genre.insert(0, 'Genre')
            self.book_release_date.delete("0", "end")
            self.book_release_date.insert(0, 'Release Date')
            self.create_book(title, genre, release_date)

    def create_book(self, title, genre, release_date):  # ADD CLASS OBJECT TO STORE USER/ SQL QUERY
        self.response_string.set("Book Created!!")
        book_list.append(EBook((len(book_library_list) + 1), title, genre, release_date))
        # ebook_table.create_book(title, genre, release_date, selected_user)
        book_library_list.append(book_list[-1])
        print(book_list[-1].book_id)
        print(book_list[-1].title)

    def focus_in(self, type):
        if type == "bt":
            if self.book_title.get() == "Title":
                self.book_title.delete("0", "end")
        elif type == "bg":
            if self.book_genre.get() == "Genre":
                self.book_genre.delete("0", "end")
        elif type == "brl":
            if self.book_release_date.get() == "Release Date":
                self.book_release_date.delete("0", "end")

    def focus_out(self):
        if not self.book_title.get():
            self.book_title.insert(0, 'Title')
        if not self.book_genre.get():
            self.book_genre.insert(0, 'Genre')
        if not self.book_release_date.get():
            self.book_release_date.insert(0, 'Release Date')


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page_3_frame = tk.Frame(self, bg="white")
        self.success_string = tk.StringVar(value="Select a Book to Rent")
        label = tk.Label(self.page_3_frame, textvariable=self.success_string)
        label.pack(side="top", fill="both", expand=True)
        self.book_number_final = 0

        self.book_buttons = []

        self.book_details_string = tk.StringVar(value="")
        self.book_details_label = tk.Label(self.page_3_frame, textvariable=self.book_details_string)
        self.book_details_label.configure(bg="white")
        self.book_details_label.pack()

        self.submit_button = tk.Button(self.page_3_frame, text="Confirm Booking", state='disabled', command=self.confirm_booking)
        self.submit_button.configure(bg="light blue")
        self.submit_button.pack()
        self.page_3_frame.grid(row=0, column=0)
        self.page_3_frame.grid_rowconfigure(0, weight=1)
        self.page_3_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def refresh_books(self):
        global book_list_buttons
        # for book_result_id in booking_table.get_all_by_id(selected_user):
        #     for book in ebook_table.get_book_by_id(book_result_id):
        #         selected_user.books.append(EBook(book[0], book[1], book[2], book[3]. book[4]))
        # for x in range(len(selected_user.books)):
        #     for y in range(len(book_list_1)):
        #         if selected_user.books[x] == book_list_1[y]:
        #             book_list_1.pop(y)
        if len(book_list) == 0:
            self.book_details_string.set("No more books left!")
            self.submit_button['state'] = 'disabled'
        else:
            self.book_details_string.set("")
            # self.submit_button['state'] = 'normal'
        for book in book_list_buttons:
            book.pack_forget()
        book_list_buttons = []
        for button in self.get_books():
            book_list_buttons.append(button)
        self.submit_button.pack_forget()
        for book in book_list_buttons:
            book.pack()
        self.submit_button.pack()

    def get_books(self):
        global book_list_buttons
        buttons = []
        for book in book_list_buttons:
            book.pack_forget()
        book_list_buttons = []
        for i in range(len(book_list)):
            buttons.append(tk.Button(self.page_3_frame, text=book_list[i].title, command=lambda i=i: self.open_this(i)))
        return buttons

    def open_this(self, i):
        self.submit_button['state'] = 'normal'
        self.book_number_final = i
        self.book_details_string.set(f"{book_list[i].title} selected. Are you sure?")

    def confirm_booking(self):
        book_title = book_list[self.book_number_final].title
        self.book_details_string.set("")
        self.book_details_label.pack_forget()
        self.submit_button.pack_forget()
        global book_list_buttons
        for book in book_list_buttons:
            book.pack_forget()

        book_list_buttons = []
        selected_user.books.append(book_list[self.book_number_final])
        # booking_table.create_booking(book_list_1[self.book_number_final].book_id, selected_user)
        book_list.pop(int(self.book_number_final))
        if len(self.get_books()) > 0:
            for book in self.get_books():
                book_list_buttons.append(book)

            for book_button in book_list_buttons:
                book_button.pack()
            self.book_details_label.pack()
            self.submit_button.pack()
        else:
            self.book_details_string.set("No more books left!")
            self.book_details_label.pack()
        print(f"{book_title} Confirmed! Enjoy!")

    def rent_book_page_open(self):
        self.submit_button['state'] = 'disabled'
        self.refresh_books()
        self.lift()


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page_4_frame = tk.Frame(self, bg="white")
        self.success_string = tk.StringVar(value="Select a Book to Return")
        label = tk.Label(self.page_4_frame, textvariable=self.success_string)
        label.pack(side="top", fill="both", expand=True)
        self.book_number_final = 0

        self.book_details_string = tk.StringVar(value="")
        self.book_details_label = tk.Label(self.page_4_frame, textvariable=self.book_details_string)
        self.book_details_label.configure(bg="white")
        self.book_details_label.pack()

        self.submit_button = tk.Button(self.page_4_frame, text="Confirm Return", state='disabled',
                                       command=self.confirm_return)
        self.submit_button.configure(bg="light blue")
        self.submit_button.pack()
        self.page_4_frame.grid(row=0, column=0)
        self.page_4_frame.grid_rowconfigure(0, weight=1)
        self.page_4_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def refresh_books(self):
        if len(selected_user.books) == 0:
            self.book_details_string.set("No more books left!")
            self.submit_button['state'] = 'disabled'
        else:
            self.book_details_string.set("")
            self.submit_button['state'] = 'normal'
        global rented_books_buttons
        for book in rented_books_buttons:
            book.pack_forget()
        rented_books_buttons = []
        for button in self.get_books():
            rented_books_buttons.append(button)
        self.submit_button.pack_forget()
        for book in rented_books_buttons:
            book.pack()
        self.submit_button.pack()

    def get_books(self):
        global rented_books_buttons
        buttons = []
        for book in rented_books_buttons:
            book.pack_forget()
        rented_books_buttons = []
        for i in range(len(selected_user.books)):
            buttons.append(tk.Button(self.page_4_frame, text=selected_user.books[i].title, command=lambda i=i: self.open_this(i)))
        return buttons

    def open_this(self, i):
        self.submit_button['state'] = 'normal'
        self.book_number_final = i
        self.book_details_string.set(f"{selected_user.books[i].title} selected. Are you sure?")

    def confirm_return(self):
        book_title = selected_user.books[self.book_number_final].title
        self.book_details_string.set("")
        self.book_details_label.pack_forget()
        self.submit_button.pack_forget()
        global rented_books_buttons
        for book in rented_books_buttons:
            book.pack_forget()
        rented_books_buttons = []
        book_list.append(selected_user.books[self.book_number_final])
        book_list.sort(key=lambda x: x.title)
        selected_user.books.pop(int(self.book_number_final))
        # booking_table.return_book(selected_user.books[self.book_number_final].book_id, selected_user)
        if len(self.get_books()) > 0:
            for book in self.get_books():
                rented_books_buttons.append(book)

            for book_button in rented_books_buttons:
                book_button.pack()
            self.book_details_label.pack()
            self.submit_button.pack()
        else:
            self.book_details_string.set("No more books left!")
            self.book_details_label.pack()
        print(f"{book_title} Returned! Hope you enjoyed it!!")

    def rent_book_page_open(self):
        self.submit_button['state'] = 'disabled'
        self.refresh_books()
        self.lift()


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        page_5_frame = tk.Frame(self, bg="white")
        self.success_string = tk.StringVar(value="Please Log-in")
        label = tk.Label(page_5_frame, textvariable=self.success_string)
        label.pack(side="top", fill="both", expand=True)
        self.user_id = tk.Entry(page_5_frame)
        self.user_id.insert(0, 'User ID')
        self.user_id.bind("<FocusIn>", lambda args: self.focus_in("id"))
        self.user_id.bind("<FocusOut>", lambda args: self.focus_out())
        self.user_id.pack()
        self.user_password = tk.Entry(page_5_frame, show="*")
        self.user_password.insert(0, 'Password')
        self.user_password.bind("<FocusIn>", lambda args: self.focus_in("pass"))
        self.user_password.bind("<FocusOut>", lambda args: self.focus_out())
        self.user_password.pack()
        self.response_string = tk.StringVar(value="")
        response = tk.Label(page_5_frame, textvariable=self.response_string)
        response.pack()
        page_5_frame.grid(row=0, column=0)
        page_5_frame.grid_rowconfigure(0, weight=1)
        page_5_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def incorrect_login(self):
        self.response_string.set("Log-in details incorrect! Try again!")

    def focus_in(self, type):
        if type == "id":
            if self.user_id.get() == "User ID":
                self.user_id.delete("0", "end")
        elif type == "pass":
            if self.user_password.get() == "Password":
                self.user_password.delete("0", "end")

    def focus_out(self):
        if not self.user_id.get():
            self.user_id.insert(0, 'User ID')
        if not self.user_password.get():
            self.user_password.insert(0, 'Password')


class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.landing_message = tk.StringVar(value="WELCOME TO MY EBOOK SYSTEM \n Please Log-In")
        label = tk.Label(self, textvariable=self.landing_message)
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)


        buttonframe = tk.Frame(self, bg="white")
        container = tk.Frame(self, bg="white")
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        def login():
            p5.show()
            if check_login_details():
                p5.user_id.delete(0, 'end')
                p5.user_password.delete(0, 'end')
                b1.config(state="normal")
                b2.config(state="normal")
                b3.config(state="normal")
                b4.config(state="normal")
                b5.config(text="logout", command=logout)
                p6.show()
                p6.landing_message.set(f"HOMEPAGE \n Welcome {selected_user.first_name}! \n Use the buttons above to navigate the application")
            else:
                p5.incorrect_login()


        def check_login_details(): # ADD SQL QUERY TO CHECK PASSWORD
            found = False
            password = ''
            for userid in user_list:
                if p5.user_id.get() == str(userid.user_id):
                    found = True
                    password = userid.password
                    break
            if found:
                if p5.user_password.get() == password:
                    global selected_user
                    selected_user = userid
                    return True
                else:
                    return False
            return False

        def logout():
            p6.show()
            p6.landing_message.set("WELCOME TO MY EBOOK SYSTEM \n Please Log-In")
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(text="login", command=login)

        b1 = tk.Button(buttonframe, text="Create User", state="disabled", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Create Book", state="disabled", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Rent Book", state="disabled", command=p3.rent_book_page_open)
        b4 = tk.Button(buttonframe, text="Return Book", state="disabled", command=p4.rent_book_page_open)
        b5 = tk.Button(buttonframe, text="Login", command=login)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p6.show()

