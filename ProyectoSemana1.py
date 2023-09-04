import re
import itertools
import random
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk  #antes istalar (pip install pillow)

def validar_contrasena(contrasena): 
    longitud_minima = 8
    tiene_mayusculas = re.search(r'[A-Z]', contrasena)
    tiene_numeros = re.search(r'\d', contrasena)
    tiene_caracteres_especiales = re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena)
    es_comun = contrasena.lower() in contrasenas_comunes
    tiene_123 = re.search(r'123', contrasena)
    
    solo_numeros = contrasena.isdigit()
    solo_letras = contrasena.isalpha()    

    if len(contrasena) < longitud_minima:
        return "Débil"
    elif solo_numeros or solo_letras:
        return "Débil"
    elif tiene_123:
        return "Débil"
    elif tiene_mayusculas and tiene_numeros and tiene_caracteres_especiales and not es_comun:
        return "Fuerte"
    else:
        return "Moderada"

def validar_contraseña_personal():
    contrasena_personal = entrada_contraseña.get()
    nivel_seguridad = validar_contrasena(contrasena_personal)
    resultado_personal.config(text=f"Nivel de seguridad: {nivel_seguridad}")

def generar_contraseña_aleatoria(caracteres, longitud):
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def generar_contraseña_aleatoria_interfaz():
    contraseña_aleatoria = generar_contraseña_aleatoria(caracteres, longitud)
    nivel_seguridad = validar_contrasena(contraseña_aleatoria)
    resultado.config(text=f"Contraseña aleatoria generada: {contraseña_aleatoria}\nNivel de seguridad: {nivel_seguridad}")
    
def mostrar_contraseña():
    if entrada_contraseña['show'] == '*':
        entrada_contraseña['show'] = ''
    else:
        entrada_contraseña['show'] = '*'

def copiar_contraseña():
    contraseña_generada = resultado.cget("text").split(": ")[1].split("\n")[0]
    app.clipboard_clear()
    app.clipboard_append(contraseña_generada)
    app.update()
    
contrasenas_comunes = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567", "1234567890"]

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(),.?\":{}|<>"
longitud = 12

app = tk.Tk()
app.title("GVC")
app.geometry("300x300")
app.resizable(0,0) #para que no se pueda modificar el tamaño de la ventana

# Cargar la imagen de fondo
imagen_fondo = Image.open("fondo2.jpg")
imagen_fondo = imagen_fondo.resize((400, 300))
fondo = ImageTk.PhotoImage(imagen_fondo)


# Crear un widget Label para mostrar la imagen de fondo
fondo_label = tk.Label(app, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

font = Font(weight="bold", size=12)


titulo = tk.Label(app, text="Generador y Validador de Contraseñas",font=font)
titulo.pack(pady=10)

boton_generar = tk.Button(app, text="Generar Contraseña Aleatoria", command=generar_contraseña_aleatoria_interfaz)
boton_generar.pack(pady=5)

resultado = tk.Label(app, text="")
resultado.pack()

boton_copiar = tk.Button(app, text="Copiar Contraseña Generada", command=copiar_contraseña)
boton_copiar.pack(pady=5)

label_contraseña = tk.Label(app, text="Compruebe la Seguridad de su Contraseña")
label_contraseña.pack(pady=5)

entrada_contraseña = tk.Entry(app, show="*")
entrada_contraseña.pack(pady=5)

boton_mostrar = tk.Button(app, text="Mostrar Contraseña", command=mostrar_contraseña)
boton_mostrar.pack(pady=5)

boton_validar = tk.Button(app, text="Validar Contraseña", command=validar_contraseña_personal)
boton_validar.pack(pady=5)

resultado_personal = tk.Label(app, text="")
resultado_personal.pack()


app.mainloop()