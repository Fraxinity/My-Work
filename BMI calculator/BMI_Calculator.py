import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import customtkinter


def calculate_bmi_m():
    # Check if height and weight fields are not empty
    if height_entry.get() == "" or weight_entry.get() == "":
        messagebox.showerror("Error", "Please enter a value for height and weight.")
        return

    # Check if height and weight fields are valid numbers
    try:
        height = float(height_entry.get()) / 100
        weight = float(weight_entry.get())
        bmi = round(weight / (height * height), 2)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for height and weight.")
        return

    if bmi < 18.5:
        feedback_label.config(text=f"You're underweight\n\nTo improve health, add healthy calories with\nalmonds, "
                                   f"fruits, and wheat toast. Choose\nnutrient-dense foods avoid junk food, snack\non "
                                   f" fats, and hit the gym for weight-\nlifting and yoga. Prioritize getting enough\n"
                                   f"sleep.\n\n{nickname_entry.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)
    elif bmi < 25:
        feedback_label.config(text=f"You're normal weight\n\nMaintain your healthy weight\n"
                                   f"\n{nickname_entry.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)
    elif bmi < 30:
        feedback_label.config(text=f"You're overweight\n\nTo improve your diet, add fiber-rich green\nleafy vegetables,"
                                   f" while avoiding sugar and\nrefined carbohydrates. Regular exercise, like\nwalking "
                                   f"or jogging, is beneficial, and staying\nhydrated is important for overall health."
                                   f"\n\n{nickname_entry.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)
    else:
        feedback_label.config(text=f"You're obese\n\nObesity is unhealthy and can lead to heart\nstroke and other "
                                   f"health complications. Seek\ndoctor to know more about your current\nhealth\n"
                                   f"\n{nickname_entry.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)

def calculate_bmi_i():
    # Check if height and weight fields are not empty
    if height_entry2.get() == "" or weight_entry2.get() == "":
        messagebox.showerror("Error", "Please enter a value for height and weight.")
        return
    # Check if height and weight fields are valid numbers
    try:
        height = float(height_entry2.get()) * 12 + float(inches_entry.get())
        weight = float(weight_entry2.get())
        bmi = round(weight / (height * height) * 703, 2)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for height and weight.")
        return

    if bmi < 18.5:
        feedback_label.config(text=f"You're underweight\n\nTo improve health, add healthy calories with\nalmonds, "
                                   f"fruits, and wheat toast. Choose\nnutrient-dense foods avoid junk food, snack\non "
                                   f"good fats, and hit the gym for weight-\nlifting and yoga. Prioritize getting "
                                   f"enough\nsleep.\n\n{nickname_entry2.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)
    elif bmi < 25:
        feedback_label.config(text=f"You're normal weight\n\nMaintain your healthy weight\n"
                                   f"n{nickname_entry2.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)
    elif bmi < 30:
        feedback_label.config(text=f"You're overweight\n\nTo improve your diet, add fiber-rich green\nleafy vegetables,"
                                   f" while avoiding sugar and\nrefined carbohydrates. Regular exercise, like\nwalking "
                                   f"or jogging, is beneficial, and staying\nhydrated is important for overall health."
                                   f"\n\n{nickname_entry2.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)
    else:
        feedback_label.config(text=f"You're obese\n\nObesity is unhealthy and can lead to heart\nstroke and other "
                                   f"health complications. Seek\ndoctor to know more about your current\nhealth\n"
                                   f"\n{nickname_entry2.get()}'s BMI score is " + str(bmi),
                              font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", anchor=W)


window = customtkinter.CTk()
window.title("BMI Calculator")
window.minsize(width=500, height=1)
window.maxsize(width=500, height=1000)

frame = tkinter.Frame(window)
frame.pack()

# create frames
top_frame = tkinter.Frame(window, bg="#ecdcbc")
bottom_frame = tkinter.Frame(window)

# place frames in the window
top_frame.pack(side="top", fill="both", expand=True, padx=1, pady=(5, 5))
bottom_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=(5, 5))

# notebook

notebook = ttk.Notebook(window)
tab1 = Frame(notebook) # frame for tab 1
tab2 = Frame(notebook)

notebook.add(tab1, text="Metric")
notebook.add(tab2, text="Imperial")
notebook.pack()

# User information in Metric
title_label = tkinter.Label(tab1, text="User Information", font=('Microsoft YaHei', 12, 'bold'))
title_label.grid(row=0, column=0)

nickname_entry = customtkinter.CTkEntry(master=tab1, placeholder_text="Nickname")
nickname_entry.grid(row=2, column=0)
height_entry = customtkinter.CTkEntry(master=tab1, placeholder_text="Height (cm)")
height_entry.grid(row=2, column=1)
weight_entry = customtkinter.CTkEntry(master=tab1, placeholder_text="Weight (kg)")
weight_entry.grid(row=2, column=2)

submit_button = customtkinter.CTkButton(master=tab1, text="Submit", border_width=0, corner_radius=15, fg_color="gray",
                                        command=calculate_bmi_m)
submit_button.grid(row=3, column=1, sticky="news", pady=10, padx=20)

feedback_label = tkinter.Label(top_frame, text="WELCOME TO\nBMI CALCULATOR\n---",
                               font=('Hagrid Text Trial Extrabold', 34, 'bold'),
                               bg="#ecdcbc", fg="#c54333", justify="left")
feedback_label.pack(padx=10, pady=(0, 0), anchor=W)

feedback_label = tkinter.Label(top_frame, text="This is designed to help you calculate your\nBody Mass Index and "
                                               "provide necessary\ndetails for you to improve it.\n",
                               font=('RocaOne-Rg', 12, 'bold'), bg="#ecdcbc", fg="#c54333", justify="left")
feedback_label.pack(padx=10, pady=(10, 10), anchor=W)

# User information in Imperial

title_label2 = tkinter.Label(tab2, text="User Information", font=('Microsoft YaHei', 12, 'bold'))
title_label2.pack(anchor=W)

entry_frame = tkinter.Frame(tab2)
entry_frame.pack()

nickname_entry2 = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Nickname")
nickname_entry2.pack(side="left", padx=5)

height_entry2 = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Feet", width=70)
height_entry2.pack(side="left", padx=5)

inches_entry = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Inches", width=70)
inches_entry.pack(side="left", padx=5)

weight_entry2 = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Weight (lbs)")
weight_entry2.pack(side="left", padx=5)

submit_button2 = customtkinter.CTkButton(master=tab2, text="Submit", border_width=0, corner_radius=15, fg_color="gray",
                                         command=calculate_bmi_i)
submit_button2.pack(pady=10)

# To add alignment to the widget
for widget in bottom_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()