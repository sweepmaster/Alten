from Operaciones import *
from tkinter import ttk

if __name__=="__main__":

    total=SumaDeCuadrados(123).resultado()+ SumaDeCubos(123).resultado()
    total2= SumaDeCuadrados(589).resultado()+ SumaDeCubos(589).resultado()

    print(f"el resultado de total es {total}")
    print(f"el resultado de total2 es {total2}")



