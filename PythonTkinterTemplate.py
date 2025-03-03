import tkinter as tk
from tkinter import ttk

# ---------------------------- IMPORTANT CLASS -------------------------------
class Navigating(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("1000x600")
        self.title("PythonTkinter")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Page1, Page2, Page3, Page4):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#---------------------------- IMPORTANT CLASS END ----------------------------

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.config(bg='black')

        tk.Label(self, text="Walltell Template", background='black', foreground='gold',
                 font=("Ebrima", 30, 'bold')).place(x=340, y=20)

        buttons = [
            ("Page 1", Page1, 125),
            ("Page 2", Page2, 200),
            ("Page 3", Page3, 275),
            ("Page 4", Page4, 350),
        ]

        for text, page, y in buttons:
            tk.Button(self, text=text, command=lambda p=page: controller.show_frame(p),
                      height=1, width=10, background='gold', foreground='black',
                      font=("Ebrima", 20, 'bold')).place(x=430, y=y)

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='black')

        tk.Label(self, text="Page 1", background='black', foreground='gold',
                 font=("Ebrima", 30, 'bold')).place(x=440, y=20)

        tk.Button(self, text="Open Popup", command=self.popup1,
                  font=("Ebrima", 18, 'bold'), height=1, width=10,
                  background='white', foreground='midnight blue').place(x=430, y=390)

    def popup1(self):
        popup_window = tk.Toplevel(self.controller)
        popup_window.title("Popup Window")
        popup_window.geometry("400x300")
        popup_window.configure(bg='midnight blue')

        tk.Label(popup_window, text="This is a label:", bg='midnight blue',
                 fg='white', font=("Ebrima", 14)).pack(pady=10)

        Popup_Enter = tk.Entry(popup_window, width=30, font=("Ebrima", 12, 'bold'))
        Popup_Enter.pack(pady=5)

        tk.Button(popup_window, text="Close", bg='white', fg='midnight blue',
                  font=("Ebrima", 12), command=popup_window.destroy).pack(pady=20)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='black')

        tk.Label(self, text="Page 2", background='black', foreground='gold',
                 font=("Ebrima", 30, 'bold')).place(x=440, y=20)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='black')

        tk.Label(self, text="Page 3", background='black', foreground='gold',
                 font=("Ebrima", 30, 'bold')).place(x=440, y=20)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='black')

        tk.Label(self, text="Page 4", background='black', foreground='gold',
                 font=("Ebrima", 30, 'bold')).place(x=440, y=20)

app = Navigating()
app.mainloop()