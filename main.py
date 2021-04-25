# Python program to create a simple GUI calculator using Tkinter


# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression in the text entry box

def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equal_press():
    # Try and except statement is used for handling the errors like zero division error etc.

    # Put that code inside the try block which may generate the error

    try:

        global expression


        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable by empty string

        expression = ""


    except:

        equation.set(" error ")
        expression = ""


# declare Function to clear the contents of text entry box

def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure(background="green")

    # title of the program
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("370x250")

    equation = StringVar()

    # create the text entry box for showing the expression .
    expression_field = Entry(gui, textvariable=equation)


    expression_field.grid(columnspan=6, ipadx=80)

    # creating Buttons

    button1 = Button(gui, text=' 1 ', fg='black',  command=lambda: press(1), height=2, width=8)

    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', command=lambda: press(2), height=2, width=8)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', command=lambda: press(3), height=2, width=8)

    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', command=lambda: press(4), height=2, width=8)

    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', command=lambda: press(5), height=2, width=8)

    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', command=lambda: press(6), height=2, width=8)

    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', command=lambda: press(7), height=2, width=8)

    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', command=lambda: press(8), height=2, width=8)

    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', command=lambda: press(9), height=2, width=8)

    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', command=lambda: press(0), height=2, width=8)

    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='green', command=lambda: press("+"), height=2, width=8)

    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='green', command=lambda: press("-"), height=2, width=8)

    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='green', command=lambda: press("*"), height=2, width=8)

    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='green',command=lambda: press("/"), height=2, width=8)

    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='yellow', bg='blue',command=equal_press, height=2, width=8)

    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='yellow', bg='blue',command=clear, height=2, width=8)

    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='yellow', bg='blue',command=lambda: press('.'), height=2, width=8)

    Decimal.grid(row=6, column=0)



gui.mainloop()
