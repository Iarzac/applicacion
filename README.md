Esta aplicación interactiva fue creada utilizando Streamlit, una biblioteca de Python que permite construir interfaces web de manera sencilla. La aplicación está diseñada para resolver 10 ejercicios diferentes sobre funciones en Python, y cada uno de ellos está implementado en su propia sección. A continuación, se explicará cómo se implementó cada función y qué realiza.
1. Función de saludo simple
Función: saludar(nombre)
Descripción: Esta función recibe un nombre como parámetro y genera un saludo personalizado, por ejemplo, 'Hola, Juan'. El usuario ingresa su nombre mediante una caja de texto y al presionar el botón, se muestra el saludo en pantalla.
2. Suma de dos números
Función: sumar(a, b)
Descripción: La función toma dos números como parámetros, los suma y devuelve el resultado. El usuario ingresa dos números y la aplicación muestra el resultado de la suma.
3. Área de un triángulo
Función: calcular_area_triangulo(base, altura)
Descripción: Esta función calcula el área de un triángulo usando la fórmula: (1/2) × base × altura. El usuario ingresa la base y la altura y la aplicación calcula el área.
4. Calculadora de descuento
Función: calcular_precio_final(precio, descuento=10, impuesto=16)
Descripción: Esta función calcula el precio final de un producto después de aplicar un descuento y sumar un impuesto. Los valores por defecto son 10% de descuento y 16% de impuesto, pero el usuario puede modificarlos.
5. Suma de una lista de números
Función: sumar_lista(lista)
Descripción: La función toma una lista de números y devuelve la suma de todos ellos. El usuario ingresa una lista y la aplicación muestra la suma total.
6. Funciones con valores predeterminados
Función: producto(nombre, cantidad=1, precio=10)
Descripción: Esta función calcula el costo total de un producto. La cantidad por defecto es 1 y el precio por unidad es 10. El usuario puede cambiar estos valores y la aplicación muestra el precio total.
7. Números pares e impares
Función: numeros_pares_e_impares(lista)
Descripción: La función toma una lista de números y separa los números en dos listas: una con los pares y otra con los impares.
8. Multiplicación con *args
Función: multiplicar_todos(*args)
Descripción: Esta función recibe una cantidad indefinida de números y los multiplica todos. Si no se pasan argumentos, devuelve 1.
9. Información de una persona con **kwargs
Función: informacion_personal(**kwargs)
Descripción: Esta función recibe varios datos personales en formato clave:valor y los muestra organizadamente en pantalla.
10. Calculadora flexible
Función: calculadora_flexible(a, b, operacion='suma')
Descripción: La función realiza una operación matemática (suma, resta, multiplicación o división) entre dos números. El usuario selecciona la operación a realizar.
Navegación en la Aplicación
Para organizar los ejercicios de manera clara, se utilizó un sidebar donde el usuario puede seleccionar el ejercicio que desea realizar. Esto hace que la aplicación sea fácil de navegar y cada ejercicio tenga su propia sección.
