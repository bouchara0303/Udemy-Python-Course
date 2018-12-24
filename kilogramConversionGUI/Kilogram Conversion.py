from tkinter import *
from decimal import *

def testingIf(event):
    if(text1.get("1.0", END) == None):
        kilo = 0
    try:
        kilo = float(text1.get("1.0", 'end-1c'))
    except ValueError:
        kilo = 0
    grams = round(Decimal(kilo * 1000), 3)
    pounds = round(Decimal(kilo * 2.20462), 3)
    ounces = round(Decimal(kilo * 35.274), 3)
    for text in range(1, 4):
        boxes[text].configure(state='normal')
        if boxes[text].get("1.0", END) is not None:
            boxes[text].delete("1.0", END)
    text2.insert(END, grams)
    text3.insert(END, pounds)
    text4.insert(END, ounces)
    
    for text in range(1, 4):
        boxes[text].configure(state='disabled')
    return "break"


window = Tk()

window.title('Kilogram Conversion')
window.configure(background='grey')

for i in range(0, 7):
    window.rowconfigure(i, pad=5, weight=1)
for i in range(0,3):
    window.columnconfigure(i, pad=5, weight=1)
    
label1 = Label(window, text='Kilograms')
label1.grid(row=0, column=1)
text1 = Text(window, width=10, height=1)
text1.grid(row=1, column=1)
text1.configure(highlightbackground='blue')
text1.bind('<Return>', testingIf)

label2 = Label(window, text='Grams')
label2.grid(row=3, column=0)
text2 = Text(window, width=10, height=1)
text2.grid(row=4, column=0)
text2.configure(highlightbackground='green', state='disabled')

label3 = Label(window, text='Pounds')
label3.grid(row=3, column=1)
text3 = Text(window, width=10, height=1)
text3.grid(row=4, column=1)
text3.configure(highlightbackground='green', state='disabled')

label4 = Label(window, text='Ounces')
label4.grid(row=3, column=2)
text4 = Text(window, width=10, height=1)
text4.grid(row=4, column=2)
text4.configure(highlightbackground='green', state='disabled')

submit = Button(window, text='Submit', command=testingIf)
submit.grid(row=6, column=1)
submit.configure(highlightbackground='grey')

boxes = [text1, text2, text3, text4]

window.mainloop()
