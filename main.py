import tkinter as tk

def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)







window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2)
button_add.place(x=100, y=200)
button_add = tk.Button(window, text="-", width=2, height=2)
button_add.place(x=150, y=200)
button_add = tk.Button(window, text="*", width=2, height=2)
button_add.place(x=200, y=200)
button_add = tk.Button(window, text="/", width=2, height=2)
button_add.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=150)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второ число:')
number2.place(x=100, y=125)
answer = tk.Label(window, text='ОТВЕТ:')
answer.place(x=100, y=275)
window.mainloop()