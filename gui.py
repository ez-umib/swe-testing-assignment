import tkinter as tk
from app.calculator import Calculator

class CalculatorGUI:

    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Quick-Calc")

        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
        ]

        for (text,row,col) in buttons:
            tk.Button(self.root, text=text, width=5, height=2,
                      command=lambda t=text: self.on_click(t)
                      ).grid(row=row, column=col)

    def on_click(self, char):
        if char == "C":
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()