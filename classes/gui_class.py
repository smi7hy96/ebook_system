import tkinter as tk


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
        response.pack()

        submit_button = tk.Button(page_1_frame, text="Create User", command=self.check_input)
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
        print(first_name)
        print(last_name)
        print(email)
        print(password)

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
        response.pack()

        submit_button = tk.Button(page_2_frame, text="Create Book", command=self.check_input)
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
            self.create_user(title, genre, release_date)

    def create_user(self, title, genre, release_date):  # ADD CLASS OBJECT TO STORE USER/ SQL QUERY
        self.response_string.set("Book Created!!")
        print(title)
        print(genre)
        print(release_date)

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
        for button in self.get_books():
            self.book_buttons.append(button)

        for book in self.book_buttons:
            book.pack()

        self.book_details_string = tk.StringVar(value="")
        self.book_details_label = tk.Label(self.page_3_frame, textvariable=self.book_details_string)
        self.book_details_label.pack()

        self.submit_button = tk.Button(self.page_3_frame, text="Confirm Booking", state='disabled', command=self.confirm_booking)
        self.submit_button.pack()

        self.page_3_frame.grid(row=0, column=0)
        self.page_3_frame.grid_rowconfigure(0, weight=1)
        self.page_3_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def get_books(self):
        buttons = []
        for i in range(len(book_list)):
            buttons.append(tk.Button(self.page_3_frame, text=book_list[i], command=lambda i=i:self.open_this(i)))
        return buttons

    def open_this(self, i):
        self.submit_button['state'] = 'normal'
        self.book_number_final = i
        self.book_details_string.set(f"{book_list[i]} selected. Are you sure?")

    def confirm_booking(self):
        book_title = book_list[self.book_number_final]
        self.book_details_string.set("")
        self.book_details_label.pack_forget()
        self.submit_button.pack_forget()
        for book in self.book_buttons:
            book.pack_forget()

        self.book_buttons = []
        book_list.pop(int(self.book_number_final))
        if len(self.get_books()) > 0:
            for book in self.get_books():
                self.book_buttons.append(book)

            for book_button in self.book_buttons:
                book_button.pack()
            self.book_details_label.pack()
            self.submit_button.pack()
        else:
            self.book_details_string.set("No more books left!")
            self.book_details_label.pack()
        print(f"{book_title} Confirmed! Enjoy!")


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Select a Book to Return")
        label.pack(side="top", fill="both", expand=True)



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
                user_id = p5.user_id.get()
                p5.user_id.delete(0, 'end')
                p5.user_password.delete(0, 'end')
                b1.config(state="normal")
                b2.config(state="normal")
                b3.config(state="normal")
                b4.config(state="normal")
                b5.config(text="logout", command=logout)
                p6.show()
                p6.landing_message.set(f"HOMEPAGE \n Welcome {user_id}! \n Use the buttons above to navigate the application")
            else:
                p5.incorrect_login()

        def check_login_details(): # ADD SQL QUERY TO CHECK PASSWORD
            print(p5.user_id.get())
            if p5.user_id.get() == '1' and p5.user_password.get() == 'pass':
                return True
            else:
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
        b3 = tk.Button(buttonframe, text="Rent Book", state="disabled", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Return Book", state="disabled", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Login", command=login)


        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p6.show()


book_list = ['book 1', 'book 2', 'book 3', 'book 4']
rented_books = []

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()