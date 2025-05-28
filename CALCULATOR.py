import tkinter as tk
from math import sqrt

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x600")
root.resizable(False, False)
root.configure(bg="#201f1f")  # Dark background

# Global expression
expression = ""

# Entry widget to show current expression
entry = tk.Entry(root, font=("Consolas", 24, "bold"), bd=10, relief=tk.FLAT, justify="right", bg="#2d2d2d", fg="white")
entry.insert(0, "0")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)


# Function to update entry
def update_entry(char):
    global expression
    if expression == "0" and char not in ["+", "-", "*", "/", "."]:
        expression = char
    else:
        expression += char
    entry.delete(0, tk.END)
    entry.insert(0, expression)

# Function to clear entry
def clear_entry():
    global expression
    expression = ""
    entry.delete(0, tk.END)
    entry.insert(0, "0")

# Function to delete last character
def backspace():
    global expression
    expression = expression[:-1]
    if not expression:
        expression = "0"
    entry.delete(0, tk.END)
    entry.insert(0, expression)

# Function to evaluate result
def calculate_result():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# Function to calculate square
def square():
    global expression
    try:
        result = str(eval(expression) ** 2)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# Function to calculate square root
def square_root():
    global expression
    try:
        result = str(sqrt(eval(expression)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# Function to calculate reciprocal
def reciprocal():
    global expression
    try:
        result = str(1 / eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# Function to toggle sign
def toggle_sign():
    global expression
    try:
        if expression.startswith("-"):
            expression = expression[1:]
        else:
            expression = "-" + expression
        entry.delete(0, tk.END)
        entry.insert(0, expression)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

# Button definitions (label, command)
buttons = [
    [('%', lambda: update_entry('%')), ('CE', clear_entry), ('C', clear_entry), ('⌫', backspace)],
    [('1/x', reciprocal), ('x²', square), ('√', square_root), ('/', lambda: update_entry('/'))],
    [('7', lambda: update_entry('7')), ('8', lambda: update_entry('8')), ('9', lambda: update_entry('9')), ('*', lambda: update_entry('*'))],
    [('4', lambda: update_entry('4')), ('5', lambda: update_entry('5')), ('6', lambda: update_entry('6')), ('-', lambda: update_entry('-'))],
    [('1', lambda: update_entry('1')), ('2', lambda: update_entry('2')), ('3', lambda: update_entry('3')), ('+', lambda: update_entry('+'))],
    [('+/-', toggle_sign), ('0', lambda: update_entry('0')), ('.', lambda: update_entry('.')), ('=', calculate_result)]
]

# Create button widgets
for r_index, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")
    for c_index, (label, cmd) in enumerate(row):
        if label == '=':
            bg_color = "#ff9500"  
            fg_color = "white"
        elif label == '⌫':
            bg_color = "#444"
            fg_color = "#ff4d4d"
        else:
            bg_color = "#333"
            fg_color = "white"

        btn = tk.Button(
            frame, text=label, font=("Consolas", 18, "bold"), relief=tk.FLAT,
            bg=bg_color, fg=fg_color, activebackground="#555",
            command=cmd
        )
        btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

# Run the application
root.mainloop()
