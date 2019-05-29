__author__ = '_aiben.stunner'

from tkinter import *
import math
import parser
import tkinter.messagebox
import sys


root = Tk()
root.title("Calculator")

""" playGround """
global answer
global calcResult
calcResult=""
answer=""

i = 0


#calculates the factorial of the number entered.
def factorial():
    global answer
    number = display.get()
    number = int(number)

    if not(not answer):
        clearAll_1()

    try:
       number_1 = display.get()
       display1.insert(i, number_1 + "!")
       clearAll_2()
       answer = math.factorial(number)
       display.insert(0, answer)

    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")


#calculates the square of a number
def square():
    global answer
    number = display.get()
    number = int(number)

    if not(not answer):
        clearAll_1()

    try:
       number_1 = display.get()
       display1.insert(i, number_1 + "^2")
       clearAll_2()
       result =  math.pow(number, 2)
       answer = int(result)
       display.insert(0, answer)
    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")

#calculates the sine of a number(in radians...)
def sine():
    global answer
    number = display.get()

    if not(not answer):
        clearAll_1()

    try:
        number = int(number)
    except:
        number = float(number)
    try:
       number_1 = display.get()
       display1.insert(i, "sin(" + number_1 + ")")
       clearAll_2()
       answer =  math.sin(number)
       display.insert(0, answer)
    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")

#calculates the ccsine of a number(in radians...)
def cosine():
    global answer
    number = display.get()

    if not(not answer):
        clearAll_1()

    try:
        number = int(number)
    except:
        number = float(number)
    try:
       number_1 = display.get()
       display1.insert(i, "cos(" + number_1 + ")")
       clearAll_2()
       answer =  math.cos(number)
       display.insert(0, answer)
    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")

#calculates the tangent of a number(in radians...)
def tangent():
    global answer
    number = display.get()

    if not(not answer):
        clearAll_1()

    try:
        number = int(number)
    except:
        number = float(number)
    try:
       number_1 = display.get()
       display1.insert(i, "tan(" + number_1 + ")")
       clearAll_2()
       answer =  math.tan(number)
       display.insert(0, answer)
    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")

#calculates the square root of a number
def squareRootF():
    global answer
    number = display.get()

    if not(not answer):
        clearAll_1()

    try:
        number = int(number)
    except:
        number = float(number)
    try:
       number_1 = display.get()
       display1.insert(i, "√" + number_1)
       clearAll_2()
       answer =  math.sqrt(number)
       display.insert(0, answer)
    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")

#calculates the log to the base 10 of a number
def log():
    global answer
    number = display.get()

    if not(not answer):
        clearAll_1()

    try:
        number = int(number)
    except:
        number = float(number)

    try:
       number_1 = display.get()
       display1.insert(i, "log(" + number_1 + ")")
       clearAll_2()
       answer =  math.log10(number)
       display.insert(0, answer)
    except Exception:
        clearAll_2()
        display.insert(0, "Invalid!   Press AC")

#clears the whole display area
def clearAll_1():
    display1.delete(0, END)

def clearAll_2():
    display.delete(0, END)

def clearAll(event = None):
    clearAll_1()
    clearAll_2()

#gets the operands from input and displays it in the display area
def get_variables(number, event = None):
    global i
    global calcResult
    global answer

    if not(not calcResult) or not(not answer):
        calcResult = ""
        answer = ""
        clearAll()
        display.insert(i, number)

    else:
        display.insert(i, number)
        i += 1


#deletes the last input from the display area
def delete():
    number = display.get()

    if len(number):
        newNumber = number[:-1]
        print(newNumber)
        clearAll_2()
        display.insert(0, newNumber)
    else:
        clearAll_2()
        display.insert(0, "Error... Press AC")

#gets the operator the user wants to apply to operands
def get_operation(operator):
    global i
    global calcResult
    length = len(operator)
    display.insert(i, operator)
    i += length

    if not(not calcResult):
        calcResult=""
        display1.insert(i, operator)
        clearAll_2()


    else:
        number = display.get()
        display1.insert(i, number)
        clearAll_2()



#magicButton
def calculate(event = None):
    global calcResult
    number = display.get()
    display1.insert(i, number)
    number = display1.get()

    try:
        expression = parser.expr(number).compile()
        calcResult = eval(expression)
        clearAll_2()
        display.insert(0, calcResult)

    except:
        clearAll_2()
        display.insert(0, "Syntax Error!")

def key(event):
    try:
        operator = event.char
        if operator == ".":
            get_variables(".")

        if operator == "+" or operator == "-" or operator == "/" or operator == "*":
            get_operation(operator)
    except ValueError:
        print("Invalid")

    try:
        num = int(event.char)
        get_variables(num)

    except ValueError:
        print("Not a number")



#Help....
def helper():
    message = "To use functions, enter number before hitting the function.\n\nSine, Cosine and Tangent functions take angles in radians.\nLogarithm is to the base 10.\n\n         :)"
    tkinter.messagebox.showinfo("Number to Text Converter", message)



""" GUI_construct """

root.columnconfigure(0,pad=3)
root.columnconfigure(1,pad=3)
root.columnconfigure(2,pad=3)
root.columnconfigure(3,pad=3)
root.columnconfigure(4,pad=3)

root.rowconfigure(0,pad=3)
root.rowconfigure(1,pad=3)
root.rowconfigure(2,pad=3)
root.rowconfigure(3,pad=3)

display = Entry(root, font=("Times New Roman", 20, "bold"), justify="right")
display.grid(row=2, columnspan=4, sticky=W+E)
display1 = Entry(root, font=("Courier", 12), justify="right")
display1.grid(row=1, columnspan=4, sticky=W+E)


#Numbers....
point =Button(root, text=".", command = lambda : get_variables("."),font=("Times New Roman", 16, "bold"), padx=13, pady=0.5)
point.grid(row=9, column=0)
zero =Button(root, text="0",command = lambda : get_variables(0),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
zero.grid(row=9, column=1)
one =Button(root, text="1",command = lambda : get_variables(1),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
one.grid(row=8, column=0)
two =Button(root, text="2",command = lambda : get_variables(2),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
two.grid(row=8, column=1)
three =Button(root, text="3",command = lambda : get_variables(3),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
three.grid(row=8, column=2)
four =Button(root, text="4",command = lambda : get_variables(4),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
four.grid(row=7, column=0)
five =Button(root, text="5",command = lambda : get_variables(5),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
five.grid(row=7, column=1)
six =Button(root, text="6",command = lambda : get_variables(6),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
six.grid(row=7, column=2)
seven =Button(root, text="7",command = lambda : get_variables(7),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
seven.grid(row=6, column=0)
eight =Button(root, text="8",command = lambda : get_variables(8),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
eight.grid(row=6, column=1)
nine =Button(root, text="9",command = lambda : get_variables(9),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5, bg="white")
nine.grid(row=6, column=2)

#Functions...
clear =Button(root, text="AC", command = clearAll, font=("Times New Roman", 16, "bold"),bg="red")
clear.grid(row=3, column=3)
equal2 =Button(root, text="=", command = calculate, font=("Times New Roman", 18, "bold"), padx=7, pady=1, bg="green")
equal2.grid(row=9, column=3)
delete =Button(root, text="DEL", command = delete, font=("Times New Roman", 13, "bold"), padx=1, pady=3, bg="orange")
delete.grid(row=3, column=2)

#Operations...
plus =Button(root, text="+", command = lambda: get_operation("+"), font=("Times New Roman", 16, "bold"), padx=10, pady=0.5)
plus.grid(row=8, column=3)
minus =Button(root, text="-", command = lambda: get_operation("-"),font=("Times New Roman", 16, "bold"), padx=12, pady=0.5)
minus.grid(row=7, column=3)
multiply =Button(root, text="×", command = lambda: get_operation("*"),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5)
multiply.grid(row=6, column=3)
divide =Button(root, text="÷", command = lambda: get_operation("/"),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5)
divide.grid(row=5, column=3)
factorial =Button(root, text="x!", command = factorial, font=("Times New Roman", 10, "bold"), padx=15, pady=4)
factorial.grid(row=3, column=0)
square =Button(root, text="x^2", command = square,font=("Times New Roman", 10, "bold"), padx=10, pady=4)
square.grid(row=3, column=1)
modulo =Button(root, text="mod", command = lambda: get_operation("%"),font=("Times New Roman", 12, "bold"), padx = 4)
modulo.grid(row=4, column=3)

#Others...
pi =Button(root, text="π", command = lambda: get_operation("*3.14"),font=("Times New Roman", 16, "bold"), padx=10, pady=0.5)
pi.grid(row=9, column=2)
exponent =Button(root, text="exp", command = lambda: get_operation("**"),font=("Times New Roman", 12, "bold"), padx=6, pady=5)
exponent.grid(row=5, column=2)

sine =Button(root, text="sin(x)", command = sine,font=("Times New Roman", 10, "bold"), padx=3, pady=5)
sine.grid(row=4, column=0)
cosine =Button(root, text="cos(x)", command = cosine,font=("Times New Roman", 10, "bold"), padx=4, pady=5)
cosine.grid(row=4, column=1)
tangent =Button(root, text="tan(x)", command = tangent,font=("Times New Roman", 10, "bold"), padx=4, pady=5)
tangent.grid(row=4, column=2)
squareRoot =Button(root, text="√", command = squareRootF,font=("Times New Roman", 12, "bold"), padx=13, pady=2)
squareRoot.grid(row=5, column=0)
logarithm =Button(root, text="log(x)", command = log,font=("Times New Roman", 10, "bold"), padx=4, pady=5)
logarithm.grid(row=5, column=1)

root.bind('<Return>', calculate)
root.bind('<Key>', key)
root.bind('<BackSpace>', clearAll)

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = quit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help", command = helper)
helpMenu.add_command(label="@_aiben.stunner")


root.mainloop()
