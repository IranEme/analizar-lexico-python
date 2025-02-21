#JUAN IRAN LOPEZ MERCADO
#21760719

#Buen dia maestro, no logre hacer que detectera con el punto . 
# modifique mi expresion regular pero me limitaba por mi estructura y se aplicaba a todos. encontre una posible solucion, solo que por el tiempo
#tendria que re escribir mi codigo y no alcanze. Gracias.

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import re

# Definición de palabras reservadas, tipos de datos y operadores (Diccionarios)
palabras_reservadas = {'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'}
operadores = {'+', '-', '*', '/', '>', '<', '==', '<=', '>=', 'cos', 'sen', 'log'}
tipos = {'int', 'float', 'str', 'bool'}

# Funciones del analizador léxico
def analizar_codigo(codigo):
    simbolos = []
    lineas = codigo.split('\n')

   
    
    for num_linea, linea in enumerate(lineas, 1):
        # Regex para ignorar comentarios
        linea = re.split(r'#.*', linea)[0]
        #Regex para tokens permitidos
        tokens = re.findall(r'[\w.]+|==|<=|>=|.', linea)
        

        for token in tokens:
            if token.strip() == '':
                continue  # Ignora los espacios y caracteres vacíos
            descripcion = ""
            es_reservada = "No"
            if token in palabras_reservadas:
                descripcion = 'PALABRA_RESERVADA'
                es_reservada = "Sí"
            elif re.match(r'^[a-zA-Z_]\w*$', token):
                if token in tipos:
                    descripcion = 'TIPO DE DATO'
                else:
                    descripcion = 'IDENTIFICADOR'
            elif re.match(r'^\d+$', token):
                descripcion = 'NUMERO_ENTERO'
            elif re.match(r'^\d+\.\d+$', token):
                descripcion = 'NUMERO_DECIMAL'
            elif token in operadores:
                descripcion = 'OPERADOR'
            elif token.strip() in {'{', '}', '(', ')', ';', ',', }:
                continue  # Ignorar los delimitadores y puntuaciones simples
            else:
                continue  # Ignora los espacios y caracteres no reconocidos

            simbolos.append((token, descripcion, es_reservada))
    return simbolos
    #Funcion para cargar el archivo desde la computadora


def cargar_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if ruta:
        with open(ruta, 'r') as archivo:
            texto.delete('1.0', tk.END)
            texto.insert('1.0', archivo.read())
def mostrar_tabla(simbolos):
    # Limpia la vista de tabla si ya contiene datos
    for i in tabla.get_children():
        tabla.delete(i)
    # Rellena la tabla con los símbolos
    for token, descripcion, es_reservada in simbolos:
        tabla.insert("", "end", values=(token, descripcion, es_reservada))

def analizar():
    try:
        codigo = texto.get('1.0', tk.END)
        if not codigo.strip():
            raise ValueError("El archivo o captura está vacío")
        simbolos = analizar_codigo(codigo)
        
        #Borra los datos anteriores en la tabla para proceder a analizar a otros cuando se requiera
        for i in tabla.get_children():
            tabla.delete(i)
        
        mostrar_tabla(simbolos)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

        

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador Léxico")

texto = scrolledtext.ScrolledText(ventana, width=60, height=20)
texto.pack()

nombre_label = tk.Label(ventana, text="Nombre: Juan Iran Lopez Mercado")
nombre_label.pack()

matricula_label = tk.Label(ventana, text="Matrícula: 21760719")
matricula_label.pack()

tabla = ttk.Treeview(ventana, columns=("Token", "Descripción", "Reservada"), show="headings")
tabla.heading("Token", text="Token")
tabla.heading("Descripción", text="Descripción")
tabla.heading("Reservada", text="Reservada")
tabla.pack(expand=True, fill='both')

ttk.Button(ventana, text="Cargar Archivo", command=cargar_archivo).pack(fill='x')
ttk.Button(ventana, text="Analizar", command=analizar).pack(fill='x')

ventana.mainloop()