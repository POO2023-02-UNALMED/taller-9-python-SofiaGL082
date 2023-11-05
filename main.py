from tkinter import END, Tk, Button, Entry
#Commit para calificacion?

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

#Indice de numeros
i = 0
operadores = 0

#Configuracion para entrada de numeros
def obtenerNumeros(n):
    global i
    pantalla.insert(i, n)
    i+=1

# Configuracion entrada de botones de operacion
def obtenerOperador(operador):
    global i
    global operadores
    if operadores == 0:
        pantalla.insert(i, operador)
        i+=1
        operadores+=1
    else:
        clear_pantalla()
        pantalla.insert(0, "ERROR")

# Limpiar pantalla
def clear_pantalla():
    global i
    pantalla.delete(0, END)
    i = 0

# Calcular operaciones
def calcularOperacion():
    global i

    ecuacion = pantalla.get()

    if i!=0:
        try:
            result = str(eval(ecuacion))
            pantalla.delete(0, END)
            pantalla.insert(0, result)
            longitud = len(result)
            i = longitud
        
        except:
            result = "Error"
            pantalla.delete(0, END)
            pantalla.insert(0, result)
    else:
        pass

# Configuración botones
boton_1 = Button(root, text="1", command= lambda:obtenerNumeros(1), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command= lambda:obtenerNumeros(2), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command= lambda:obtenerNumeros(3), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", command= lambda:obtenerNumeros(4), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", command= lambda:obtenerNumeros(5), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command= lambda:obtenerNumeros(6), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command= lambda:obtenerNumeros(7), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command= lambda:obtenerNumeros(8), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command= lambda:obtenerNumeros(9), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)

# Botones operaciones
boton_igual = Button(root, text="=", command= lambda:calcularOperacion(), width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", command= lambda:obtenerOperador("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", command= lambda:obtenerOperador("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", command= lambda:obtenerOperador("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", command= lambda:obtenerOperador("*"),  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, command= lambda:obtenerOperador("/"), height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()