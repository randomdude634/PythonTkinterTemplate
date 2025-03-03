import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def popup1(self):
    popup_window = tk.Toplevel(self.master)
    popup_window.title("Create New Button")
    popup_window.geometry("400x300")
    popup_window.configure(bg='lightblue')

    tk.Label(popup_window, text="Enter Button Name:", bg='lightblue', fg='black', font=("Ebrima", 14)).pack(pady=10)

    Popup_Enter = tk.Entry(popup_window, width=30, font=("Ebrima", 12, 'bold'))
    Popup_Enter.pack(pady=5)

    self.CreateButton = tk.Button(popup_window, text="Create Button", bg='DeepskyBlue3', fg='midnight blue', font=("Ebrima", 12), command=lambda: self.create_new_Button(Popup_Enter.get(), popup_window, self.master))
    self.CreateButton.pack(pady=20)

def create_new_Button(self, Button_name, popup_window):
    if Button_name:

        new_Button = tk.Button(self, text=Button_name, fg="black", bg="DeepskyBlue3", font=("Ebrima", 24, "bold"))

        max_y = 900
        x_offset = 270
        y_offset = 250
        button_spacing_y = 100
        button_spacing_x = 270

        y_position = y_offset + len(self.Buttons) * button_spacing_y

        if y_position > max_y:
            row = (len(self.Buttons) // (max_y // button_spacing_y))
            x_position = x_offset + (row * button_spacing_x)
            y_position = y_offset + ((len(self.Buttons) % (max_y // button_spacing_y)) * button_spacing_y)
        else:
            x_position = x_offset
            y_position = y_offset + len(self.Buttons) * button_spacing_y

        new_Button.place(x=x_position, y=y_position)

        self.Buttons.append(new_Button)

        popup_window.destroy()

        messagebox.showinfo("Success", f"Button '{Button_name}' created successfully!")
    else:
        messagebox.showwarning("No Name", "You must provide a Button name.")
