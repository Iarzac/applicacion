import streamlit as st

def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return precio_final

def sumar_lista(lista):
    return sum(lista)

def producto(nombre, cantidad=1, precio_unitario=10):
    return cantidad * precio_unitario

def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    if args:
        for num in args:
            resultado *= num
    return resultado

def informacion_personal(**kwargs):
    return kwargs

def calculadora_flexible(a, b, operacion="suma"):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicación":
        return a * b
    elif operacion == "división":
        return a / b if b != 0 else "Error: División por cero"

st.title("Aplicación Interactiva - Ejercicios de Python")

ejercicio = st.sidebar.selectbox("Selecciona un ejercicio", 
    ("Saludo", "Suma de dos números", "Área de un triángulo", "Calculadora de descuento",
     "Suma de una lista", "Producto", "Números pares e impares", 
     "Multiplicación con *args", "Información personal", "Calculadora flexible"))

if ejercicio == "Saludo":
    nombre = st.text_input("Ingresa tu nombre")
    if nombre:
        st.write(saludar(nombre))

elif ejercicio == "Suma de dos números":
    num1 = st.number_input("Ingresa el primer número", value=0)
    num2 = st.number_input("Ingresa el segundo número", value=0)
    st.write("Resultado:", sumar(num1, num2))

elif ejercicio == "Área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo", value=0)
    altura = st.number_input("Ingresa la altura del triángulo", value=0)
    st.write("Área:", calcular_area_triangulo(base, altura))

elif ejercicio == "Calculadora de descuento":
    precio = st.number_input("Precio original", value=0)
    descuento = st.number_input("Descuento (%)", value=10)
    impuesto = st.number_input("Impuesto (%)", value=16)
    st.write("Precio final:", calcular_precio_final(precio, descuento, impuesto))

elif ejercicio == "Suma de una lista":
    lista_numeros = st.text_input("Ingresa los números separados por comas")
    if lista_numeros:
        lista = [float(num) for num in lista_numeros.split(",")]
        st.write("Suma:", sumar_lista(lista))

elif ejercicio == "Producto":
    nombre_prod = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio = st.number_input("Precio por unidad", value=10)
    st.write("Total a pagar:", producto(nombre_prod, cantidad, precio))

elif ejercicio == "Números pares e impares":
    lista_numeros = st.text_input("Ingresa los números separados por comas")
    if lista_numeros:
        lista = [int(num) for num in lista_numeros.split(",")]
        pares, impares = numeros_pares_e_impares(lista)
        st.write("Pares:", pares)
        st.write("Impares:", impares)

elif ejercicio == "Multiplicación con *args":
    lista_numeros = st.text_input("Ingresa los números separados por comas")
    if lista_numeros:
        lista = [int(num) for num in lista_numeros.split(",")]
        st.write("Resultado:", multiplicar_todos(*lista))

elif ejercicio == "Información personal":
    nombre = st.text_input("Nombre")
    edad = st.text_input("Edad")
    direccion = st.text_input("Dirección")
    info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
    st.write(info)

elif ejercicio == "Calculadora flexible":
    num1 = st.number_input("Ingresa el primer número", value=0)
    num2 = st.number_input("Ingresa el segundo número", value=0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicación", "división"])
    st.write("Resultado:", calculadora_flexible(num1, num2, operacion))
