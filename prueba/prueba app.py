# C_name = "Tom"
# Character_age = "60"
# is_Male = True

# print("   /| " + C_name + " hello")
# print("  / | " + Character_age)

# C_name = "mike"
# print(" /  | " + C_name)
# print("/___| " + Character_age)

# Cash = 21.2
# print(pow(Cash, 2))

# U_name = input("Enter your Name: ")
# U_age = input("Enter your Age: ")
# print("Hello " + U_name + " Welcome to the school! " + "you're " + U_age + " huh?, not bad buddy")
# if (U_age < 20) : True
# print('getta out of here you stupid creep')

#        CALCULATOR
# num1 = input("Enter a Number: ")
# num2 = input("Enter another Number: ")
# resultado = float(num1) + float(num2)
# print(resultado)

#           Madlibs

# color = input("Enter a color: ")
# noun = input("Enter a noun: ")
# person = input("Enter a person: ")
#
# print("Roses are " + color)
# print(noun + " are blue")
# print("but i can certainly say")
# print("I Love You " + person + "<3")

#           Lists
# food = ["Pizza", "Burger", "Pasta", "2Creamer", "Tasta", "2Cream"]
# Comensal = [16, 2, 8, 7, 9, 3]
# food.insert(2, "Soup")
# food.sort()
# food[1] = "Pussy"
# print(food)
# Comensal.reverse()
# print(Comensal)

#           TUPLES
# cord1 = input("cord1: ")
# cord2 = input("cord2: ")
# cordenadas = (cord1, cord2)
# print(cordenadas[0:2])

#           FUNCTIONS
#
#
# def say_hi(name, age):
#    print("Hello " + name + "you're " + str(age))
#
#
# say_hi("Tom ", 32)
# say_hi("Carl ", 70)
#
#       RETURN STATEMENTE
#
#
# def cube(number):
#    return number*number*number
#
#
# result = cube(5)
# print(cube(5))
# print(result)
#

#           IF STATEMENT
#
# genera = float(input("Your're 1(female) or 2(male)?: "))
#
# if genera == float(1):
#     print("You're a Female")
#     is_Male = False
# elif genera == float(2):
#     print("Male")
#     is_Male = True
# else:
#    print("Enter a Number Please")
#    is_Male = None
#
# if is_Male is True:
#    print("Your are a male")
# elif is_Male is None:
#    print("Seriously do it")
# else:
#    print("Female lol, you sure buddy?")
#
#           DICTIONARY (NOT DONE)
#
#           WHILE LOOP
#
#
# i = 1
# while i <= 10:
#    print(i)
#    i += 1
# print("Done with loop")
#
#           GUESSING GAME
#
# secret_word = "Giraffe"
# guess_value = ""
# fail_value = 0
# limit_Value = 3
# failure = False
# while guess_value != secret_word and not failure:
#    if fail_value < limit_Value:
#        guess_value = input("Enter Guess: ")
#        fail_value += 1
#    else:
#        failure = True
# if failure:
#    print("LOOOOOOOOSERRRRR!!!")
# print("You Win!")
#
#               FOR LOOP
#
#
# for letter in "Unet":
#    print(letter)
#
# --------------------
#
# amigos = ["Yago", "Hugo", "Yara"]
# for index in range(len(amigos)):
#    if index == 0:
#        print(amigos[0])
#    elif index == 1:
#        print(amigos[1])
#    elif index == 2:
#        print(amigos[2])
#    elif index == 3:
#        print("4ta vuelta")
#    elif index == 4:
#        print("ultima vuelta")
#
#           EXPONENT FUNCTION
#
# def elevado_al_poder(num_base, num_elev):
#    resultado = 1
#    for index in range(num_elev):
#        resultado = resultado * num_base
#    return resultado
#
# print(elevado_al_poder(2, 3))
#
#           2D LISTS & NESTED LOOPS
#
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [20]
# ]
# for row in number_grid:
#     for col in row:
#         print(col)

#           TRANSLATOR
#
# NPI Language
# vocal -> NPI
# ------
# def translate(frase):
#    translation = ""
#    for letter in frase:
#        if letter.lower() in "aeuoi":
#            if letter.isupper():
#                translation = translation + "NPI"
#            else:
#                translation = translation + "npi"
#        else:
#            translation = translation + letter
#    return translation
#
# print(translate(input("Enter a Frase: ")))
#
#           COMMENTS
# all that you have been doing fucker
#
#               TRY/EXCEPT
#
# err_value = 0
# while err_value < 3:
#    try:
#        divion = int(input("divide: "))
#        value = 10 / divion
#        number = int(input("Enter a Number: "))
#        print(number)
#    except ValueError:
#        print("Invalid Input")
#    except ZeroDivisionError as err:
#        err_value += 1
#        print("Don't use Zero Please")
# print("You F@ck it up, thx")
#
#               READING FILES
#
# empleados_file = open("empleados.txt", "r")
# for name in empleados_file.readlines():
#     print(name)
# empleados_file.close()

#           WRITING TO FILES
#
# empleados_file = open("hello.html", "w")
# empleados_file.write("<p>This is HTML </p>")
# empleados_file.close()

#               MODULES AND PIP
#
# import añadir
#
# print(añadir.roll_dice(10))
#
#           CLASSES AND OBJECTS
#
# from student import Student
#
# student1 = Student("Hugo", "Ingenieria", 3.1, False)
# student2 = Student("Sam", "Art", 10.1, False)
# student3 = Student("Pob", "Ingenieria", 7.1, False)
# print(student1.gpa)
#
#               MULTIPLE CHOICE QUIZ
#
# from Question import Question
#
# question_prompts = [
#    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#    "What Color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# questions = [
#    Question(question_prompts[0], "a"),
#    Question(question_prompts[1], "c"),
#    Question(question_prompts[2], "b"),
# ]
#
#
# def run_test(questions):
#    score = 0
#    for question in questions:
#        answer = input(question.prompt)
#        if answer == question.answer:
#            score += 1
#    print("Your got " + str(score) + "/" + str(len(questions)) + "Correct")
# run_test(questions)
#
#               OBJECT FUNCTIONS
#
# from student import Student
#
# student1 = Student("Juan", "Sports", 3.1)
# student2 = Student("Ross", "Hooking", 3.6)
#
# print(student2.on_honor_roll())
#
#           INHERITANCE
#
# from Chef import Chef
# from ChineseChef import ChineseChef
#
# myChef = Chef()
# myChef.make_special_dish()
#
# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()
#
#           PYTHON INTERPRETER
#
#
#
#           MICHAEL AND TOAST THINGY
#
#    txt = "Hello_World_cum"
#
#
#    def double_char(txt):
#        answer = ""
#        for i in txt:
#            answer = answer + i + i
#        return answer
#
#
#    def number_syllables(word):
#        return len(word.split('_'))
#
#
#    print(number_syllables(txt))
#
#
#
#
#
#
#
################################# Ya yo solo we,[Docstrings]
# from doc_string_and_annotations import anno_tation as ant
# import doc_string_and_annotations as doc_ant
#
# helo = 2
# doc_ant.doc_string.docstring("")
# ant.annotation(None, 3, "")
# doc_ant.anno_tation.annotation(None, 4, "nope")
# doc_ant.Pru.prueba(33, 27)
#
#
#
#
#
#
#
# ##################### [Tkinter]
# import tkinter

# window = tkinter.Tk(className="no tk")
# greeting = tkinter.Label(text="Bye madafaka", fg="orange", bg="#34A2FE", width=25, height=5)
# button = tkinter.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="#34A2FE",
#     fg="yellow"
# )
# entry = tkinter.Entry()
# button.pack()
# greeting.pack()
# entry.pack()
# name = entry.get()
# name
# window.mainloop()


# import tkinter as tk

# window = tk.Tk()

# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)

# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)

# window.mainloop()

#################  [Excersice]
# import tkinter as tk
# import random

# def roll_dic():
#     label["text"] = str(random.randint(0, 6))

# window = tk.Tk()

# frame = tk.Frame()
# frame.rowconfigure([0, 1], minsize=50, weight=1)
# frame.columnconfigure([0], minsize=50, weight=1)
# frame.pack(fill=tk.BOTH)

# button = tk.Button(master=frame, text="Roll", command=roll_dic)

# label= tk.Label(master=frame, text="0")

# button.grid(row=0, column=0, sticky="nsew")
# label.grid(row=1, column=0)

# window.mainloop()

################# [Temperature Converter]
# import tkinter as tk

# def fahrenheit_to_celsius():
#     """Covierte el valor de Farenheit a Celsios e inserta el resultado en 'label_result'
#     """
#     fahren = entry_temp.get()
#     celsius = (5/9)*(float(fahren) -32)
#     label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# window = tk.Tk()
# window.title("Temp Convert")
# window.resizable(width=False, height=False)

# frame_entry = tk.Frame(master=window)
# entry_temp = tk.Entry(master=frame_entry, width=10)
# label_temp = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")

# entry_temp.grid(row=0, column=0, sticky="e")
# label_temp.grid(row=0, column=1, sticky="w")

# button_convert = tk.Button(
#     master=window,
#     text="\N{RIGHTWARDS BLACK ARROW}",
#     command=fahrenheit_to_celsius
# )
# label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# frame_entry.grid(row=0, column=0, padx=10)
# button_convert.grid(row=0, column=1, pady=10)
# label_result.grid(row=0, column=2, padx=10)

# window.mainloop()