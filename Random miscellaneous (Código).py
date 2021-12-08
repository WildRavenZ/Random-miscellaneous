#DEFINICIÓN DE LAS FUNCIONES USADAS:
def NumAleatorio(): #Función de número aleatorio.
    x = 0 #Variable para numerar los resultados.
    inf = int(input("Ingresa el valor inferior del límite: ")) #Ingresa el valor inferior para la función randint.
    sup = int(input("Ingresa el valor superior del límite: ")) #Ingresa el valor superior para la función randint.
    while inf >= sup: #Si el valor inferior es mayor o igual al valor superior para la función randint...
        print("Perdona, el límite inferior es mayor al límite superior, prueba con otros valores") #Describe el error, la manera de soluciuonarlo es redefiniendo las variables.
        inf = int(input("Ingresa el valor inferior del límite: ")) #Redefinir el valor inferior.
        sup = int(input("Ingresa el valor superior del límite: ")) #Redefinir el valor superior.
    else: #Hasta que se cumpla que el valor inferior debe ser menor al valor superior...
        amount = int(input("¿Cuántos numeros aleatorios entre lo limites quieres generar? ")) #Indica el número de resultados que quieres obtener.
        for i in range(0, amount): #Bucle de incremento iterable.
            x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
            print(x, "El número aleatorio es:", randint(inf, sup)) #Imprime el número entero que se generó aleatoriamente.
                
def BarajaAleatoria(): #Función de baraja aleatoria.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuántas cartas aleatorias quieres sacar? ")) #Indica el número de resultados que quieres obtener.
    while amount > 52: #Mientras el número de resultados que quieras obtener es mayor a 52...
        print("Perdona, la baraja solo tiene 52 cartas, por lo que solo puedes sacar menos de 52 ó 52") #Describe el error, la manera de solucionarlo es redefiniendo la variable.
        amount = int(input("¿Cuantas cartas aleatorias quieres sacar? ")) #Redefine el número de resultados.
    else: #Hasta que se cumpla que el número de resultados sea menor o igual a 52...
        baraja = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"] #Lista de los elementos de una baraja.
        print(sample(baraja, amount)) #Imprime las cartas que se eligieron aleatoriamente.

def LanzamientoMoneda(): #Función de lanzamiento de moneda aleatorio.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuántas monedas quieres lanzar? ")) #Indica el número de resultados que quieres obtener.
    moneda = ["Cara", "Cruz"] #Lista de los elementos de una moneda.
    for i in range(0, amount): #Bucle de incremento iterable.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        print(x, "Lanzaste la moneda y salio:", moneda[randint(0, 1)]) #Imprime las caras de la moneda lanzada aleatoriamente.

def LanzamientoDado(): #Función de lanzamiento de dado aleatorio.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuántos dados quieres lanzar? ")) #Indica el número de resultados que quieres obtener.
    for i in range(0, amount): #Bucle de incremento iterable.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        print(x, "Lanzaste el dado y salió:", randint(1,6)) #Imprime los números de las caras de un dado lanzado aleatoriamente.

def DecisionAleatoria(): #Función de desición aleatoria.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuántas desiciones aleatorias quieres hacer? ")) #Indica el número de resultados que quieres obtener.
    siono = ["Si", "No"] #Lista de los elementos de una desición entre si y no.
    for i in range(0, amount): #Bucle de incremento iterable.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        print(x, "Tu decisión entre si o no es:", siono[randint(0, 1)]) #Imprime las desiciones que se eligieron aleatoriamente.

def LetraAleatoria(): #Función de letra aleatoria.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuaántas letras quieres obtener? ")) #Indica el número de resultados que quieres obtener.
    alfabeto = list(range(ord("A"), ord("["))) #Lista de los elementos del alfabeto inglés.
    for i in range(0, amount): #Bucle de incremento iterable.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno). 
        print(x, "La letra aleatoria es:", chr(alfabeto[randint(0,25)])) #Imprime las letras letras del alfabeto inglés que se eligieron aleatoriamente.

def PiedraPapelTijera(): #Función de papel, piedra o tijera.
    x = 0 #Variable para numerar los resultados.
    piedrapapeltijera = ["Piedra", "Papel", "Tijera"] #Lista de los elementos de piedra, papel o tijera.
    print("Tu oponente escogió:", piedrapapeltijera[randint(0, 2)]) #Imprime la desición aleatoria entre piedra, papel o tijera.

def CoordenadaGeografica(): #Función de coordenada geográfica aleatoria.
    x = 0 #Variable para numerar los resultados.
    if menu == 8: #Cuando menú es igual a ocho...
        amount = int(input("¿Cuántas coordenadas en grados decimales quieres obtener? ")) #Indica el número de resultados que quieres obtener.
        for i in range(0, amount): #Bucle de incremento iterable.
            x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
            print(x, "La coordenada aleatoria es latitud:", uniform(-89, 89), "y longitud:", uniform(-179, 179)) #Imprime la latitud aleatoria y longuitud aleatoria en coordenadas grado decimales.

def NumBinarioAleatorio(): #Función de numero binario aleatorio.
    x = 0 #Variable para numerar los resultados.
    bint = int(input("Ingresa la base binaria: ")) #Ingresa el valor para elevar al número 2.
    amount = int(input("¿Cuántos numeros quieres obtener? ")) #Indica el número de resultados que quieres obtener.
    for i in range(0, amount): #Bucle de incremento iterable.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        num = randint(0, 2 ** bint) #Genera un número entero aleatorio con rango de 0 a 2^bint.
        print(x, num, "en binario es ", bin(num)) #Imprime el numero entero que se generó aleatoriamente y tambien lo muestra en binario.

def ListaAleatoria(): #Función de lista aleatoria.
    x = 0 #Variable para numerar los resultados.
    list_ = [] #Genera la lista
    num_elements = int(input("Ingresa el número de valores de la lista: ")) #Ingresa el rango de la lista.
    for i in range(num_elements): #Para cada espacio de la lsita...
        element = input("Ingresa un elemento a la lista: ") #Ingresa un elemento.
        list_.append(element) #Se agrega a la lista.
    amount = int(input("¿Cuántos elementos aleatorios de la lista quiere obtener? ")) #Indica el número de resultados que quieres obtener.
    for i in range(0, amount): #Bucle de incremento iterable.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        print(x, "El elemento aleatorio de la lista es:", list_[randint(0, num_elements - 1)]) #Imprime un elemento aleatorio de la lista.

def ContraseñaAleatoria(): #Función de contraseña aleatoria.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuántas contraseñas quieres generar? ")) #Indica el número de resultados que quieres obtener.
    for i in range(0, amount): #Bucle de incremento iterable.
        password = [] #Genera una contraseña vacía.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        for i in range(0, 16): #Para cada caracter de la contraseña...
            aleatorio = randint(1, 4) #Genera un número del 1 al 4.
            if aleatorio == 1: #Si el número es 1...
                password.append(chr(randint(35, 38))) #Agrega un simbolo.
            if aleatorio == 2: #Si el número es 2...
                password.append(chr(randint(48, 57))) #Agrega un número.
            if aleatorio == 3: #Si el número es 3...
                password.append(chr(randint(65, 90))) #Agrega un caracter en mayúscula.
            if aleatorio == 4: #Si el número es 4...
                password.append(chr(randint(97, 122))) #Agrega un caracter en minusucla.
        print(x, "La contraseña generada es:") #Mensaje de salida.
        print("".join(password)) #Imprime una contraseña aleatoria.

def PersonaAleatoria(): #Función de persona aleatoria.
    x = 0 #Variable para numerar los resultados.
    amount = int(input("¿Cuántas personas quieres agregar? ")) #Indica el número de resultados que quieres obtener.
    for i in range(0, amount): #Bucle de incremento iterable.
        género = ["Hombre", "Mujer"] #Géneros
        g_escogido = género[randint(0, 1)] #Se escoge hombre o mujer.
        if g_escogido == "Hombre": #Si se escoge hombre...
            nombres = ["Santiago", "Mateo", "Sebastián", "Leonardo", "Alejandro", "Matías", "Fernando", "Emiliano", "Diego", "Daniel", "Juan", "Migue", "Ángel", "Alexis", "Victor", "José", "Julio", "Marcos", "Raúl", "Arturo", "Mauricio", "Manuel", "Roberto", "Ricardo", "Leonardo", "Benito", "Jesús", "Pablo", "Emmanuel", "Gabriel", "Valentín", "Jorge", "César", "Aldo", "Federico", "David", "Guillermo", "Gian", "Fabrizio", "Massimo", "Paolo", "Constantino"] #42 nombres masculinos (Puedes agregar más si lo deseas).
            pronombre = "Él" #Pronombre masculino.
        else: #Si se escoge mujer...
            nombres = ["Ángela", "María", "Fernanda", "Jessica", "Karina", "Rosa", "Jaqueline", "Norma", "Margarita", "Sofía", "Valentina", "Ximena", "Andrea", "Valeria", "Victoria", "Renata", "Regina", "Camila", "Estefania", "Olivia", "Diana", "Ámbar", "Iliana", "Ivanna", "Nicole", "Sara", "Ana", "Sandra", "Gabriela", "Alejandra", "Paola", "Rocio", "Jacoba", "Martha", "Eva", "Carmen", "Denisse", "Claudia", "Giselle", "Tizziana", "Lisa", "Fabiola"] #42 nombres femeninos (Puedes agregar más si lo deseas).
            pronombre = "Ella" #Pronombre femenino.
        nombre = nombres[randint(0, len(nombres) - 1)] #Se escoge un nombre dependiendo del género.
        apellidos = ["Ramírez", "Franco", "Fernandez", "González", "Palacios", "Solano", "Jiménez", "García", "Martínez", "López", "Hernández", "Pérez", "Cruz", "Flores", "Gómez", "Sánchez", "Rodríguez", "Haro", "Cabrera", "Cervantes", "Morales", "Guerrero", "Zarate", "Melo", "Quevedo", "Galván", "Soqui", "Peña", "Ortiz", "Vázquez", "Velázquez", "Contreras", "Vargas", "Castro", "Aguilar", "López", "Linares", "Sierra", "Zapata", "Caballero", "Medina", "Mendoza", "Gama", "Artega", "Solis", "Gallegos", "Espinosa", "Olmos", "Lozano", "Cardenas", "Villalobos", "Sanchez", "Garza", "Cortés", "Acevedo", "Suarez", "Rocha", "Arana", "Paredes", "Carbajal", "Ponce", "Ibarra", "Torres", "Duarte", "Díaz", "Beltrán", "Saucedo", "Roldán", "Reyes", "Rosales", "Zacarias", "Sosa", "Peralta", "Valadez", "Raya", "Oria", "Guevara", "Abascal"] #78 apellidos (Puedes agregar más si lo deseas).
        apellido_p = apellidos[randint(0, len(apellidos) - 1)] #Se escoge un apellido paterno.
        apellido_m = apellidos[randint(0, len(apellidos) - 1)] #Se escoge un apellido materno.
        edad = 49 + randint(-31, 31) #Se define la edad.
        estado = ["Aguascalientes", "Baja California", "Baja Californai Sur", "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaola", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"] #Estados de la Republica Mexicana.
        correos = ["@hotmail.com", "@yahoo.com", "@outlook.com", "@gmail.com"] #Correos electronicos más usados.
        x = x + 1 #El valor x va reasignandose cada vez que el bucle se repite (aumenta de uno en uno).
        print("------------------------Persona " + str(x) + "------------------------")
        print(pronombre, "es", nombre, apellido_p, apellido_m) #Nombre completo de la persona.
        print(g_escogido) #Género de la persona.
        print(pronombre, "tiene", edad, "años") #Edad de la persona
        print(pronombre, "nació en", 2021 - edad) #Año de nacimiento de la persona
        print(pronombre, "es de", estado[randint(0, 31)]) #Estado de procedencia de la persona.
        print("Su número de celular es: 222" + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))) #Número de celular de la persona.
        print("Su correo electrónico es: " + nombre.lower() + "." + apellido_p.lower() + correos[randint(0, 3)]) #Correo electónico de la persona
        print("")
        
def Ayuda(): #Función de ayuda.
    print("Bienvenido a Random.py, la funcionalidad de este programa radica en generar variables aleatorias, así que te diré como funciona cada una:") #Muestra el menú de ayuda.
    print("1 - Número aleatorio entre dos números: Esta función proporciona la cantidad que desees de números aleatorios entre un límite de enteros que indiques.")
    print("2 - Baraja aleatoria: De una baraja, podrás obtener cuantas cartas aleatorias quieres de la baraja inglesa. No te quedes con un as bajo la manga.")
    print("3 - Lanzamiento de moneda: Lanza cuantas monedas desees y tendrán dos posibles resultados: Cara o Cruz.")
    print("4 - Lanzamiento de dado: Lanza cuantos dados desees y tenndrás seis posibles resultados dependiendo de las caras de los dados.")
    print("5 - Si o No: Similar a lanzar una moneda, pero con las posibilidades de Si y No. Ideal si eres una persona muy indecisa.")
    print("6 - Letra aleatoria: Brinda cuantas letras quieras obtener del alfabeto inglés.")
    print("7 - Piedra papel o tijera: Lanza solo una desición aleatoria entre Piedra, Papel o Tijera. No, no es tu amigo virtual, solo es un código")
    print("8 - Coordenada geográfica aleatoria: Brinda una ubicación geográfica aleatoria en grados decimales. Sin dudas, el favorito del autor.")
    print("9 - Número binario aleatorio: Genera un número entero entre 0 y una base binaria para mostrar dicho número y el número en binario.")
    print("0 - Lista aleatoria: Genera una lista mediante las entradas de la cantidad de elementos de la lista y sus elementos.")
    print("11 - Contraseña aleatoria: Genera contraseñas aleatorias de 16 caracteres con numeros, letras en mayúscula y minuscula y símbolos.")
    print("12 - Persona aleatoria: Genera los datos de una persona, como su nombre completo, género, edad, estado de procedencia, y otros datos")
    
def Menu(menu): #Función menú (MAIN).
    if menu == 1: #Si el menu es 1...
        NumAleatorio() #Ejecuta la función de número aleatorio.
    if menu == 2: #Si el menu es 2...
        BarajaAleatoria() #Ejecuta la función de baraja aleatoria.
    if menu == 3: #Si el menu es 3...
        LanzamientoMoneda() #Ejecuta la función de lanzamiento de moneda aleatorio.
    if menu == 4: #Si el menu es 4...
        LanzamientoDado() #Ejecuta la función de lanzamiento de dado aleatorio.
    if menu == 5: #Si el menu es 5...
        DecisionAleatoria() #Ejecuta la función de desición aleatoria.
    if menu == 6: #Si el menu es 6...
        LetraAleatoria() #Ejecuta la función de letra aleatoria.
    if menu == 7: #Si el menu es 7...
        PiedraPapelTijera() #Ejecuta la función de pierda, papel o tijera.
    if menu == 8: #Si el menu es 8...
        CoordenadaGeografica() #Ejecuta la función de coordenada geográfica aleatoria.
    if menu == 9: #Si el menu es 9...
        NumBinarioAleatorio() #Ejecuta la función de número binario aleatorio.
    if menu == 0: #Si el menu es 0...
        ListaAleatoria() #Ejecuta la función de lista aleatoria.
    if menu == 11: #Si el menu es 11...
        ContraseñaAleatoria() #Ejecuta la función de contraseña aleatoria.
    if menu == 12: #Si el menu es 12...
        PersonaAleatoria() #Ejecuta la función de persona aleatoria.
    if menu == 99: #Si el menu es 99...
        Ayuda() #Ejecuta la función de ayuda.

#INICIA EL CÓDIGO:
from random import randint, sample, uniform #Modulo de random (randint genera un número entero aleatorio, sample elige aleatoriamente una opción de una lista sin reemplazo, uniform genera un número decimal aleatorio).
print("\n---------------------------------\nBienvenido a Random miscellaneous\n---------------------------------") #Mensaje de bienvenida (solo se muestra la primera vez).
while True: #Repite el programa siempre que lo parámetros se cumplan.
    menu = int(input("\nMENU:\n1 - Número aleatorio entre dos números\n2 - Baraja aleatoria\n3 - Lanzamiento de moneda\n4 - Lanzamiento de dado\n5 - Si o No\n6 - Letra aleatoria\n7 - Piedra papel o tijera\n8 - Coordenada geográfica aleatoria\n9 - Número binario aleatorio\n0 - Lista aleatoria\n11 - Contraseña aleatoria\n12 - Persona aleatoria\n99 - Ayuda\n")) #Menu que pide la primer variable para seguir el programa.
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5 and menu != 6 and menu != 7 and menu != 8 and menu != 9 and menu != 0 and menu != 11 and menu != 12 and menu != 99:
        print("\n-----------------------------------")
        print("Porfavor, ingresa una opción válida") #Mensaje de error.
        print("-----------------------------------")
        menu = int(input("\nMENU:\n1 - Número aleatorio entre dos números\n2 - Baraja aleatoria\n3 - Lanzamiento de moneda\n4 - Lanzamiento de dado\n5 - Si o No\n6 - Letra aleatoria\n7 - Piedra papel o tijera\n8 - Coordenada geográfica aleatoria\n9 - Número binario aleatorio\n0 - Lista aleatoria\n11 - Contraseña aleatoria\n12 - Persona aleatoria\n99 - Ayuda\n")) #Menu que pide la primer variable para seguir el programa.
    else:
        Menu(menu) #Ejecuta la función de menú (MAIN).
