from tkinter import *
from calculator import Calculator

calculator = Calculator()

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

# ---------------Pantalla---------------------------------------

resultado = StringVar()

pantalla = Entry(miFrame, textvariable=resultado, state="readonly")
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(fg="black", justify="right")

# --------------Fila 1--------------------------------------------

boton7 = Button(miFrame, text="7", width=3, command=lambda: resultado.set(calculator.add_number(7).print_screen()))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: resultado.set(calculator.add_number(8).print_screen()))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: resultado.set(calculator.add_number(9).print_screen()))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3, command=lambda: resultado.set(calculator.add_operator("/").print_screen()))
botonDiv.grid(row=2, column=4)

# --------------Fila 2--------------------------------------------

boton4 = Button(miFrame, text="4", width=3, command=lambda: resultado.set(calculator.add_number(4).print_screen()))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: resultado.set(calculator.add_number(5).print_screen()))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: resultado.set(calculator.add_number(6).print_screen()))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=3, command=lambda: resultado.set(calculator.add_operator("*").print_screen()))
botonMult.grid(row=3, column=4)

# --------------Fila 3--------------------------------------------

boton1 = Button(miFrame, text="1", width=3, command=lambda: resultado.set(calculator.add_number(1).print_screen()))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: resultado.set(calculator.add_number(2).print_screen()))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: resultado.set(calculator.add_number(3).print_screen()))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3, command=lambda: resultado.set(calculator.add_operator("-").print_screen()))
botonRest.grid(row=4, column=4)

# --------------Fila 4--------------------------------------------

boton0 = Button(miFrame, text="0", width=3, command=lambda: resultado.set(calculator.add_number(0).print_screen()))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda: resultado.set(calculator.calculate().print_screen()))
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=3, command=lambda: resultado.set(calculator.add_operator("+").print_screen()))
botonSum.grid(row=5, column=4)

resultado.set(calculator.print_screen())

raiz.mainloop()
