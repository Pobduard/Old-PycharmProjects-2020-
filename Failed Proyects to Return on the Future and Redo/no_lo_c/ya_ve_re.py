# import os
# import tkinter as tk
# from natsort import natsorted

# def masternox():
#     Path = entry_of_the_path.get()
#     File_name = entry_of_the_file_name.get()
#     number_Files = (entry_of_the_number_files.get() + 0)
#     Real_number_of_files = []
#     Real_number_of_files.join(number_Files)

#     for file in natsorted(os.path.isfile):
#         if number_Files == int:
#             file_not, file_ext = os.path.splitext(file)
#             new_name = os.path.join(Path, (File_name + file_ext))
#         elif int(number_Files) < 
#             file_not, file_ext = os.path.splitext(file)
#             new_name = os.path.join(Path, (File_name + file_ext))


# # -------------------------
# # -------------------------
# # # def fahrenheit_to_celsius():
# # #     """Covierte el valor de Farenheit a Celsios e inserta el resultado en 'label_result'
# # #     """
# # #     fahren = entry_temp.get()
# # #     celsius = (5/9)*(float(fahren) -32)
# # #     label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# # -------------------------
# # -------------------------^^

# # Start of Interface
# window = tk.Tk()
# window.title("Rename File")
# window.resizable(width=True, height=True)
# window.rowconfigure([0, 1, 2, 3], weight=1 ,minsize=1)
# window.columnconfigure([0, 1], weight=1, minsize=1)

# # Path
# frame_of_the_path = tk.Frame(master=window)
# entry_of_the_path = tk.Entry(master=frame_of_the_path, width=40, relief=tk.SUNKEN, justify="center", bg="teal", fg="yellow")
# label_of_the_path = tk.Label(
#     master=frame_of_the_path, width=30, relief=tk.RIDGE, text="Inserte la Direccion de la \nCarpeta en la que Desea Trabajar"
#     )

# #  File Name
# frame_of_the_file_name = tk.Frame(master=window)
# entry_of_the_file_name = tk.Entry(master=frame_of_the_file_name, width=40, relief=tk.SUNKEN, justify="center", bg="teal", fg="yellow")
# label_of_the_file_name = tk.Label(
#     master=frame_of_the_file_name, width=30, relief=tk.RIDGE, text="Inserte el Nombre que le\nDesea Poner a los Archivos"
#     )

# #  Button
# frame_of_the_button = tk.Frame(master=window, borderwidth=3)
# button_action = tk.Button(
#     master=frame_of_the_button, relief=tk.RAISED, padx=10, pady=10, 
#     text="\N{RIGHTWARDS BLACK ARROW}Presione para Renombrar\N{RIGHTWARDS BLACK ARROW}", justify="center", command=masternox, width=60
#     )

# # Number Pf Files
# frame_of_the_number_files = tk.Frame(master=window)
# entry_of_the_number_files = tk.Entry(master=frame_of_the_number_files, width=40, relief=tk.SUNKEN, justify="center", bg="teal", fg="yellow")
# label_of_the_number_files = tk.Label(
#     master=frame_of_the_number_files, width=30, relief=tk.RIDGE, 
#     text="Inserte el Numero de Archivos\n que Desea Renombrar\n(si tiene uno, si no dejelo en blanco)"
#     )

# # Grid Path
# frame_of_the_path.grid(row=0, column=0, sticky="nsew")
# label_of_the_path.grid(row=0, column=0, sticky="nsew")
# entry_of_the_path.grid(row=0, column=1, sticky="nsew")

# # Grid File Name
# frame_of_the_file_name.grid(row=1, column=0, sticky="nsew")
# label_of_the_file_name.grid(row=0, column=0, sticky="nsew")
# entry_of_the_file_name.grid(row=0, column=1, sticky="nsew")

# # Grid Button
# frame_of_the_button.grid(row=2, column=0, sticky="nsew")
# button_action.grid(row=0, column=0, sticky="nsew")

# # Grid Number of Files
# frame_of_the_number_files.grid(row=3, column=0, sticky="nsew")
# label_of_the_number_files.grid(row=0, column=0, sticky="nsew")
# entry_of_the_number_files.grid(row=0, column=1, sticky="nsew")
# # -------------------------^^
# # -------------------------
# # frame_entry = tk.Frame(master=window)
# # entry_temp = tk.Entry(master=frame_entry, width=10)
# # label_temp = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")

# # entry_temp.grid(row=0, column=0, sticky="e")
# # label_temp.grid(row=0, column=1, sticky="w")

# # button_convert = tk.Button(
# #     master=window,
# #     text="\N{RIGHTWARDS BLACK ARROW}",
# #     command=fahrenheit_to_celsius
# # )
# # label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# # frame_entry.grid(row=0, column=0, padx=10)
# # button_convert.grid(row=0, column=1, pady=10)
# # label_result.grid(row=0, column=2, padx=10)

# # window.mainloop()

# # import tkinter as tk

# # window = tk.Tk()

# # window.rowconfigure(0, weight=1 ,minsize=50)
# # window.columnconfigure([0, 1, 2, 3], weight=1, minsize=50)

# # label1 = tk.Label(text="1", bg="black", fg="white")
# # label2 = tk.Label(text="2", bg="black", fg="white")
# # label3 = tk.Label(text="3", bg="black", fg="white")
# # label4 = tk.Label(text="4", bg="black", fg="white")

# # label1.grid(row=0, column=0)
# # label2.grid(row=0, column=1, sticky="ew")
# # label3.grid(row=0, column=2, sticky="ns")
# # label4.grid(row=0, column=3, sticky="nsew")

# window.mainloop()

# &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&
# &&&&&&&&&&&&&&&&&&&&&&

# -----------------------------------
# def num_there(s):
#     return any(i.isdigit() for i in s)
# The function will return True if a digit exists in the string, otherwise False.

# Demo:

# >>> king = 'I shall have 3 cakes'
# >>> num_there(king)
# True
# >>> servant = 'I do not have any cakes'
# >>> num_there(servant)
# False
#
# ----------------------
#
# s = "abc1"
# contains_digit = any(map(str.isdigit, s))

# print(contains_digit)

# ----------------------------------

# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++

# z = input("helo: ")
# try:
#     if isinstance(z, str):
#         print("is a str")
#         print(z + " now")
#     if any(num_on_str.isdigit() for num_on_str in z):
#             z = int(z)
#             print(str(z) + " has benn changed")
#     else:
#         pass
# except ValueError:
#     print("error")
# print("second")
# if type(z) is int:
#     print(str(z) +" is a int")

# -----------------------
# -----------------------
# -----------------------

#     for file in natsorted(os.path.isfile):
#         if number_Files == int:
#             file_not, file_ext = os.path.splitext(file)
#             new_name = os.path.join(Path, (File_name + file_ext))
#         elif int(number_Files) < 
#             file_not, file_ext = os.path.splitext(file)
#             new_name = os.path.join(Path, (File_name + file_ext))

# -----------------------
# -----------------------
# -----------------------

# &&&&&&&&&&&&&&&&&&&&&& Prueba
# number_Files = 3
# Real_number_of_files = []
# if isinstance(number_Files, int):
#     Real_number_of_files.append(number_Files)
# else:
#     pass

# def is_num():
#     if Real_number_of_files == []:
#         print("Is a List")
#         print(Real_number_of_files)
#         print(type(Real_number_of_files))
#     elif Real_number_of_files is not []:
#         print("Is a Num")
#         print(Real_number_of_files)
#         print("1st of the list " + str(Real_number_of_files[0]))
#         print(type(Real_number_of_files[0]))
#         print("restart of : " + str(Real_number_of_files))
#         Real_number_of_files.clear()
#         print(Real_number_of_files)

# # is_num()

# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++

z = "6778"
try:
    if any(num_on_str.isdigit() for num_on_str in z):
            z = int(z)
    else:
        pass
except ValueError:
    pass


def is_num():
    Real_number_of_files = []
    if isinstance(z, int):
        Real_number_of_files.append(z)
    else:
        pass

    if Real_number_of_files == []:
        print("Is a List")
    elif isinstance(Real_number_of_files[0], int):
        print("Is a Num")
        print(Real_number_of_files)
        print("1st of the list " + str(Real_number_of_files[0]))
        print(type(Real_number_of_files[0]))
        print("restart of : " + str(Real_number_of_files))
        Real_number_of_files.clear()
        print(Real_number_of_files)

# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++

z = "6778"
try:
    if any(num_on_str.isdigit() for num_on_str in z):
            z = int(z)
    else:
        pass
except ValueError:
    pass


def is_num():
    Real_number_of_files = []
    if isinstance(z, int):
        Real_number_of_files.append(z)
    else:
        pass

    if Real_number_of_files == []:
        pass
    elif isinstance(Real_number_of_files[0], int):
        Real_number_of_files.clear()

for file in natsorted(os.path.isfile):
    if number_Files == int:
        file_not, file_ext = os.path.splitext(file)
        new_name = os.path.join(Path, (File_name + file_ext))
    elif int(number_Files) < 
        file_not, file_ext = os.path.splitext(file)
        new_name = os.path.join(Path, (File_name + file_ext))