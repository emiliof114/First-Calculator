from tkinter import *
import re

window = Tk()
window.title("Calculator")
window.geometry("500x600")
window.config(bg="lightblue")

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()

frame3 = Frame(window)

operators_list = ["hi lolol", "+", "-", "*", "/"]
numbers_list = [0,1,2,3,4,5,6,7,8,9]

def print_number(event):
    text_box.config(state="normal")
    button = str(event.widget)
    
    try:
        text_box.insert("end", int(button[-1]))
        # getting the index to retrieve the string icon for the operator
    except ValueError:
        text_box.insert("end", 1)
        # the first button does not include a final character being a number
    first_character = text_box.get(1.0, 1.1)
    second_character = text_box.get(1.1, 1.2)
    # check to see if the text box is empty
    if text_box.get("end-3c", "end-2c") == "0" and text_box.get("end-4c", "end-3c") in operators_list:
        text_box.delete("end-2c", "end-1c")
        # eliminates errors associated with having a 0 followed by any other integer after an operator
    if first_character == "0" and second_character not in operators_list:
        text_box.delete(1.1, 1.2)
        # eliminates errors associated with having a 0 followed by any other integer at the beginning of the text box
    text_box.config(state="disabled")


def clear():
    text_box.config(state="normal")
    # diabled when error message pops up in text box (to disable button pressing) so clearing it will revert to normal state
    text_box.delete(1.0, "end")

def error():
    clear()
    text_box.insert("end", "ERROR")
    text_box.config(state="disabled")



def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def print_operator(event):
    text_box.config(state="normal")
    button = str(event.widget)
    index = int(button[-1])
    operator = operators_list[index]
    end_index = text_box.get("end-2c", "end-1c")
    list = text_box.get(1.0, "end").strip()
    # check to see if the text box is empty
    if list != "":
        if end_index not in operators_list:
            text_box.insert("end", operator)
    text_box.config(state="disabled")


def output():
    if text_box.get("end-2c", "end-1c") not in operators_list:
        try:
            raw_output = text_box.get(1.0, "end").strip()
            # convert text box to string and omit /n
            string_numbers_edition = (re.split(r"[/*+-]", raw_output))
            integer_numbers_edition = []
            for i in string_numbers_edition:
                integer_numbers_edition.append(int(i))
            # create a list where each i in list is an individual number
            operators_edition = []
            # create a list where each i in list is an operator
            multiplier_list = []
            division_list = []
            addition_list = []
            subtraction_list = []
            # create a list for indexes of each individual operator
            for i in raw_output:
                if i in operators_list:
                    operators_edition.append(i)
            for j, x in enumerate(operators_edition):
                if x == "*":
                    multiplier_list.append(j)
            for k in reversed(multiplier_list):
                integer_numbers_edition[k] = (multiply(integer_numbers_edition[k], integer_numbers_edition[k + 1]))
                del integer_numbers_edition[k + 1]
                del operators_edition[k]
                # reverse the list to avoid indexing issues with the operators list
                # iterate through each index and multiply the corresponding value of the integer list by the corresponding value of one plus the index
                # goal of ultimately shortening integer list to one number
            for i, p in enumerate(operators_edition):
                if p == "/":
                    division_list.append(i)
            for g in reversed(division_list):
                integer_numbers_edition[g] = (divide(integer_numbers_edition[g], integer_numbers_edition[g + 1]))
                del integer_numbers_edition[g + 1]
                del operators_edition[g]
            for i, p in enumerate(operators_edition):
                if p == "+":
                    addition_list.append(i)
            for o in reversed(addition_list):
                integer_numbers_edition[o] = (add(integer_numbers_edition[o], integer_numbers_edition[o + 1]))
                del integer_numbers_edition[o + 1]
                del operators_edition[o]
            for i, p in enumerate(operators_edition):
                if p == "-":
                    subtraction_list.append(i)
            for q in reversed(subtraction_list):
                integer_numbers_edition[q] = (subtract(integer_numbers_edition[q], integer_numbers_edition[q + 1]))
                del integer_numbers_edition[q + 1]
                del operators_edition[q]
                # successfully followed the order of operations to obtain our desired result
            clear()
            text_box.insert("end", integer_numbers_edition)
            text_box.config(state="disabled")
        except ZeroDivisionError:
            error()
    else:
        error()
        # display error message if last character is an operator


button1 = Button(frame2, text="1", width=4, height=2, font=("Arial", 25), bg="white")
button1.grid(column=0, row=1)
button1.bind("<Button-1>", print_number)

button2 = Button(frame2, text="2", width=4, height=2, font=("Arial", 25), bg="white")
button2.grid(column=1, row=1)
button2.bind("<Button-1>", print_number)

button3 = Button(frame2, text="3", width=4, height=2, font=("Arial", 25), bg="white")
button3.grid(column=2, row=1)
button3.bind("<Button-1>", print_number)

button4 = Button(frame2, text="4", width=4, height=2, font=("Arial", 25), bg="white") 
button4.grid(column=0, row=2)
button4.bind("<Button-1>", print_number)

button5 = Button(frame2, text="5", width=4, height=2, font=("Arial", 25), bg="white")
button5.grid(column=1, row=2)
button5.bind("<Button-1>", print_number)

button6 = Button(frame2, text="6", width=4, height=2, font=("Arial", 25), bg="white")
button6.grid(column=2, row=2)
button6.bind("<Button-1>", print_number)

button7 = Button(frame2, text="7", width=4, height=2, font=("Arial", 25), bg="white")
button7.grid(column=0, row=3)
button7.bind("<Button-1>", print_number)

button8 = Button(frame2, text="8", width=4, height=2, font=("Arial", 25), bg="white") 
button8.grid(column=1, row=3)
button8.bind("<Button-1>", print_number)

button9 = Button(frame2, text="9", width=4, height=2, font=("Arial", 25), bg="white") 
button9.grid(column=2, row=3)
button9.bind("<Button-1>", print_number)

button0 = Button(frame2, text="0", width=4, height=2, font=("Arial", 25), bg="white") 
button0.grid(column=1, row=4)
button0.bind("<Button-1>", print_number)

add_button = Button(frame2, text="+", width=4, height=2, font=("Arial", 25), bg="white")
add_button.grid(column=3, row=1)
add_button.bind("<Button-1>", print_operator)

subtract_button = Button(frame2, text="-", width=4, height=2, font=("Arial", 25), bg="white")
subtract_button.grid(column=3, row=2)
subtract_button.bind("<Button-1>", print_operator)

multiply_button = Button(frame2, text="*", width=4, height=2, font=("Arial", 25), bg="white")
multiply_button.grid(column=3, row=3)
multiply_button.bind("<Button-1>", print_operator)

divide_button = Button(frame2, text="/", width=4, height=2, font=("Arial", 25), bg="white") 
divide_button.grid(column=3, row=4)
divide_button.bind("<Button-1>", print_operator)

equal_button = Button(frame2, text="=", width=4, height=2, font=("Arial", 25), bg="white", command=output) 
equal_button.grid(column=2, row=4)

clear_button = Button(frame2, text="c", width=4, height=2, font=("Arial", 25), bg="white", command=clear) 
clear_button.grid(column=0, row=4)

text_box = Text(frame2, height=3, width=40, font=("Arial", 12), bg="white")
text_box.grid(column=0, row=0, columnspan=4)

main_label = Label(frame1, height=2, width=26, font=("Arial", 25), anchor="center", text="Emilio's calc", bg="lightblue")
main_label.grid(column=0, row=0, columnspan=4, sticky="we")

text_box.config(state="disabled")
# prevents manual keyboard input

window.mainloop()