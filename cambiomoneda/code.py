import tkinter as tk
from tkinter import *
from tkinter import messagebox

import pandas as pd
xls = pd.ExcelFile('cambio_moneda.xlsx')
df = xls.parse('Hoja1')

dicc = df.set_index('nombre').T.to_dict()
print(dicc)



ROOT = tk.Tk()
ROOT.geometry("600x600")
ROOT.title("conversion de monedas")
Label(ROOT, text="selecciona a la moneda que deseas cambiar", font=("arial", 20)).pack()




def bf1():
    dolar_screen = tk.Toplevel(ROOT)
    dolar_screen.geometry("400x400")
    dolar_screen.title("DOLAR")
    Label(dolar_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("\xa0\xa0 USD")
    d2= d.get("valor")


    def calcdol():
        montoda = valordol.get()
        if montoda == 0 or not valordol.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        montodafl = float(montoda)
        total = montodafl * d2
        print(str(montodafl) + " dolares son: " + str(total) + " pesos mexicanos")
    valordol = tk.Entry(dolar_screen, width=200)
    valordol.pack()
    Button(dolar_screen, text="CONVERTIR",command=calcdol ,height=5, width=15).pack()




def bf2():
    euro_screen = tk.Toplevel(ROOT)
    euro_screen.geometry("400x400")
    euro_screen.title("EURO")
    Label(euro_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("\xa0\xa0\xa0 EUR")
    d2 = d.get("valor")
    def calceur():
        montoeur = valoreur.get()
        if montoeur == 0 or not valoreur.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        monteurfl = float(montoeur)
        total = monteurfl * d2
        print(str(monteurfl) + " euros son: " + str(total) + " pesos mexicanos")
    valoreur = tk.Entry(euro_screen, width=200)
    valoreur.pack()
    Button(euro_screen, text="convertir",command=calceur, font=(50)).pack()



def bf3():
    libra_screen = tk.Toplevel(ROOT)
    libra_screen.geometry("400x400")
    libra_screen.title("LIBRA")
    Label(libra_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("\xa0\xa0\xa0 GBP")
    d2 = d.get("valor")
    def calclib():
        montolib = valorlib.get()
        if montolib == 0 or not valorlib.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        montlibfl = float(montolib)
        total = montlibfl * d2
        print(str(montlibfl) + " libras son: " + str(total) + " pesos mexicanos")
    valorlib = tk.Entry(libra_screen, width=200)
    valorlib.pack()
    Button(libra_screen, text="convertir", command=calclib, font=(50)).pack()


def bf4():
    yen_screen = tk.Toplevel(ROOT)
    yen_screen.geometry("400x400")
    yen_screen.title("YEN")
    Label(yen_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("\xa0\xa0\xa0 JPY")
    d2 = d.get("valor")
    def calcyen():
        montoyen = valoryen.get()
        if montoyen == 0 or not valoryen.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        montyenfl = float(montoyen)
        total = montyenfl * d2
        print(str(montyenfl) + " yenes son: " + str(total) + " pesos mexicanos")
    valoryen = tk.Entry(yen_screen, width=200)
    valoryen.pack()
    Button(yen_screen, text="convertir",command=calcyen, font=(50)).pack()




def bf5():
    franco_screen = tk.Toplevel(ROOT)
    franco_screen.geometry("400x400")
    franco_screen.title("Franco")
    Label(franco_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("\xa0\xa0\xa0 CHF")
    d2 = d.get("valor")
    def calcfran():
        montofran = valorfran.get()
        if montofran == 0 or not valorfran.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        montfranfl = float(montofran)
        total = montfranfl * d2
        print(str(montfranfl) + " fancos son: " + str(total) + " pesos mexicanos")
    valorfran = tk.Entry(franco_screen, width=200)
    valorfran.pack()
    Button(franco_screen, text="convertir",command=calcfran, font=(50)).pack()


def bf6():
    dolarc_screen = tk.Toplevel(ROOT)
    dolarc_screen.geometry("400x400")
    dolarc_screen.title("DOLAR CANADIENCE")
    Label(dolarc_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("\xa0\xa0\xa0 CAD")
    d2 = d.get("valor")
    def calcdolc():
        montodolc = valordolc.get()
        if montodolc == 0 or not valordolc.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        montdolcfl = float(montodolc)
        total = montdolcfl * d2
        print(str(montdolcfl) + " Dolares canadiences son: " + str(total) + " pesos mexicanos")
    valordolc = tk.Entry(dolarc_screen, width=200)
    valordolc.pack()
    Button(dolarc_screen, text="convertir", command=calcdolc).pack()



def bf7():
    dolara_screen = tk.Toplevel(ROOT)
    dolara_screen.geometry("400x400")
    dolara_screen.title("DOLAR AUSTRALIANO")
    Label(dolara_screen, text="Ingresa el monto que deseas convertir", font=(20)).pack()
    d = dicc.get("AUD")
    d2 = d.get("valor")
    def calcdola():
        montodola = valordola.get()
        if montodola == 0 or not valordola.get():
            messagebox.showwarning(title="ERROR", message="INGRESA UN VALOR VALIDO")
        montdolafl = float(montodola)
        total = montdolafl * d2
        print(total)
    valordola = tk.Entry(dolara_screen, width=200)
    valordola.pack()
    Button(dolara_screen, text="convertir",command=calcdola ,font=(50)).pack()




    



b1 = Button(ROOT, text="Dolar", command=bf1, height=5, width=15).pack()
b2 = Button(ROOT, text="euro", command=bf2, height=5, width=15).pack()
b3 = Button(ROOT, text="libra", command=bf3, height=5, width=15).pack()
b4 = Button(ROOT, text="yen", command=bf4, height=5, width=15).pack()
b5 = Button(ROOT, text="franco suizo", command=bf5, height=5, width=15).pack()
b6 = Button(ROOT, text="Dolar canadience", command=bf6, height=5, width=15).pack()
b7 = Button(ROOT, text="Dolar australiano", command=bf7, height=5, width=15).pack()





ROOT.mainloop()