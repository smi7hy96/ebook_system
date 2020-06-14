import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 4")
        label.pack(side="top", fill="both", expand=True)


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        page_5_frame = tk.Frame(self, bg="white")
        self.success_string = tk.StringVar(value="Please Log-in")
        label = tk.Label(page_5_frame, textvariable=self.success_string)
        label.pack(side="top", fill="both", expand=True)
        self.user_id = tk.Entry(page_5_frame)
        self.user_id.pack()
        self.user_password = tk.Entry(page_5_frame, show="*")
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

        def check_login_details():
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




if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()