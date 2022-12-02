import tkinter as tk
import random


## 10	DEC-число 6 знаков
# XXXXX-XXXXX XXXX

# 1 и 2 блок должны содержать 4,5,6 и 1,2,3 цифры введенного числа соответственно, остальное - случайные буквы
# 3 блок - результат сложения чисел, получившихся в 1 и 2 блоках

def rand_char(n):
    if n <= 0:
        return ''
    return ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnm')) for x in range(n)])


def clicked():
    number = arg_A.get()

    if len(number) != 6 or not number.isdigit():
        lbl_result.configure(text='Error')
        return

    s = 0
    for x in number:
        s += int(x)

    code = f'{number[3:6]}{rand_char(2)}-{number[0:3]}{rand_char(2)} {int(number[3:6]) + int(number[0:3])}'

    lbl_result.configure(text=code)


def close():
    window.destroy()


window = tk.Tk()
window.title("Генеретор кода")
window.geometry('900x550')
bg = tk.PhotoImage(file='HM_dude.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='c')


label_bg = tk.Label(frame, image=bg)
label_bg.place(x=0, y=0)

lbl_A = tk.Label(frame, text='Введите 6 цифр', font=("Arial", 20), bg='#999900')
lbl_A.grid(column=0, row=0, padx=10, pady=10)

arg_A = tk.Entry(frame, width=15)
arg_A.insert(0, '')
arg_A.grid(column=0, row=1, padx=10, pady=20)

lbl_result = tk.Label(frame, text='Enter the values')
lbl_result.grid(column=0, row=2, padx=10, pady=10)

btn = tk.Button(frame, text='Calculate', font=("Arial", 15), command=clicked)
btn.grid(column=0, row=3, pady=150)
exit = tk.Button(frame, text='Cancel', font=("Arial", 15), command=close)
exit.grid(column=1, row=1, padx=200, pady = 30)

window.mainloop()