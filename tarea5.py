"""
Catalina G
Código: 8978486
30 / 09 / 2022
"""


# Punto 1 #


def sumas_acumuladas(arr):
    i = 0
    ans = []
    for y in range(len(arr)):
        i += arr[y]
        ans.append(i)
    return ans


def sumas_acum(arr):
    ans = [0] * len(arr)
    acum = 0
    for i in range(1, len(arr)):
        acum += arr[i]
        ans[i] = acum
    return ans


# Punto 2 #


def leer_imprimir(n):
    i = 0
    while i < n:
        lel = input()
        res = sumas_acumuladas(lel)
        i += 1
        return res


def leer_imprimir2():
    n = int(input())
    output_string = ""
    for i in range(1, n + 1):
        secuencia = input()
        secuencia = secuencia.split(" ")
        secuencia_int = [0] * int(secuencia[0])
        for j in range(int(secuencia[0])):
            secuencia_int[j] = int(secuencia[j + 1])
        secuencia = sumas_acum(secuencia_int)
        secuencia_print = ""
        for j in range(1, len(secuencia)):
            secuencia_print += f"{secuencia[j]}, "
        if secuencia[0] != "0":
            secuencia_print = secuencia_print[0:(len(secuencia_print) - 2)]

        # 3 5 6 7
        # [3, 5, 6, 7] "5, 6, 7"
        output_string += f"Case {i}: {secuencia_print}\n"
        # print(secuencia)
    print(output_string)


def leer_imprimir3():
    archivo_input = open("C:\\Users\\admin\\PycharmProjects\\pythonProject\\datos.txt")
    n = -1
    i = 1
    output_string = ""
    for line in archivo_input:
        # Leer el primer número para obtener la n
        if n == -1:
            n = int(line)
            continue

        # Tomar la secuencia, pasarla a entero para poder pasarla a la función de las sumas acomuladas
        secuencia = line.split(" ")
        secuencia_int = [0] * int(secuencia[0])
        for j in range(int(secuencia[0])):
            secuencia_int[j] = int(secuencia[j + 1])
        secuencia = sumas_acum(secuencia_int)

        # Pasar el arreglo a string para luego guardarlo
        secuencia_print = ""
        for j in range(1, len(secuencia)):
            secuencia_print += f"{secuencia[j]}, "
        if secuencia[0] != "0":
            secuencia_print = secuencia_print[0:(len(secuencia_print) - 2)]

        output_string += f"Case {i}: {secuencia_print}\n"
        i += 1
    archivo_input.close()
    output = open("C:\\Users\\admin\\PycharmProjects\\pythonProject\\datos.out.", "w")
    output.write(output_string)
    output.close()

    # print(archivo_input.readline())


"""
ejemplo = "1 22 2 "
lis = []
numero_actual = ""
for i in range(len(ejemplo)):
    if ejemplo[i] != " ":
        numero_actual += ejemplo[i]
    else:
        lis.append(numero_actual)
        numero_actual = ""
if numero_actual == " ":
    lis.append(numero_actual)


print(lis)
"""

# leer_imprimir2()
leer_imprimir3()


# Punto 3 #


def matriz_por_vector(n, m):
    i, n1, a, p1 = 0, 0, 0, 0
    ans = []
    for n1 in range(len(n)):
        p1 = n[n1]
        for a in range(p1[n1]):
            ans1 = p1[n1] * m[a]
            ans.append(ans1)
            return ans


def matriz_por_vector2(matriz, vector):
    for i in range(len(matriz)):
        for j in range(len(vector)):
            matriz[i][j] *= vector[j]
    return matriz


print(matriz_por_vector2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [2, 3, 4, 5]))


# punto 4 #


def crear_de_lista_de_contenido(Pra1):
    r = 0
    m = 0
    for i in range(len(Pra1)):
        r1 = Pra1[i]
        m = len(Pra1) / 2
        r = i[r1]
        while r != m:
            r = str()
            ans = r * m
            return ans


def crear_de_lista_de_conteo(lPar):
    lista_conteo = []
    for tupla in lPar:
        for _ in range(tupla[1]):
            lista_conteo.append(tupla[0])
    return lista_conteo


print(crear_de_lista_de_conteo([(1, 3), (12, 4), (8, 2), (9, 0), (12, 1)]))


# punto 5#


def es_subcadena(cad1, cad2):
    ans = False
    while cad1 in cad2:
        ans = True
        return ans


def es_subcadena2(cad1, cad2):
    indice = 0
    for letra in cad2:
        if letra == cad1[indice]:
            indice += 1
            if indice == len(cad1):
                return True
        else:
            indice = 0
    return False


print(es_subcadena2("fici", "tuveunproblemadedificilsolucion"))
# punto 6 #

peliculas = [["Erase una vez en Hollywood", "Quentin Tarantino", "Humor Negro", 2016, 90, 374,
              ["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]],
             ["Avengers Endgame", "Hermanos Russo",
              "Accion", 2019, 356, 2800,
              ["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans",
               "Chris Hemsworth", "Scarlett Johansson"]],
             ["The wolf of wall street", "Martin Scorsese",
              "Humor Negro", 2013, 100, 392,
              ["Leonardo Di Caprio", "Margot Robbie", "Jonah Hill"]],
             ["The Ladykillers", "Alexander Mackendrick",
              "Humor Negro", 1955, 2, 10,
              ["Alec Guinness", "Herbert Lom",
               "Peter Sellers", "Cecil Parker"]],
             ["50 First Dates", "Peter Segal",
              "Comedia Romantica", 2004, 75, 120,
              ["Adam Sandler", "Drew Barrymore", "Rob Schneider"]],
             ["Titanic", "James Cameron", "Drama", 1997, 200, 1843,
              ["Leonardo Di Caprio", "Kate Winslet", "Billy Zane",
               "Gloria Stuart"]]]

""" parte a """


def fracaso(peliculas):
    fracasadas = []
    for pelicula in peliculas:
        if pelicula[4] < pelicula[5]:
            fracasadas.append(pelicula[0])
    return fracasadas


print(fracaso(peliculas))
""" Parte b """


def conteo_peliculas_actor(peliculas):
    actores_cantidad = []
    for pelicula in peliculas:
        for actor in pelicula[6]:
            existe = False
            indice = -1
            i = 0
            for actor_cant in actores_cantidad:
                if actor == actor_cant[0]:
                    existe = True
                    indice = i
                    break
                i += 1
            if not existe:
                actores_cantidad.append([actor, 1])
            else:
                actores_cantidad[indice][1] += 1

    return actores_cantidad


print(conteo_peliculas_actor(peliculas))


# punto 7 #

def buscar_equipo(equipo_nombre, equipos):
    i = 0
    for equipo in equipos:
        if equipo_nombre == equipo[0]:
            return i
        i += 1
    return -1


def encontrar_ganadores(equipos):
    ganadores = []
    puntaje_maximo = -1
    for equipo in equipos:
        if equipo[1] > puntaje_maximo:
            ganadores = [equipo]
            puntaje_maximo = equipo[1]
        elif equipo[1] == puntaje_maximo:
            ganadores.append(equipo)
    return ganadores


def determinar_gan(partidos):
    equipos = []
    for partido in partidos:
        if partido[1] > partido[3]:
            indice = buscar_equipo(partido[0], equipos)
            if indice == -1:
                equipos.append([partido[0], 3])
            else:
                equipos[indice][1] += 3

            indice = buscar_equipo(partido[2], equipos)
            if indice == -1:
                equipos.append([partido[2], 0])
        elif partido[1] < partido[3]:
            indice = buscar_equipo(partido[2], equipos)
            if indice == -1:
                equipos.append([partido[2], 3])
            else:
                equipos[indice][1] += 3

            indice = buscar_equipo(partido[0], equipos)
            if indice == -1:
                equipos.append([partido[0], 0])
        else:
            indice = buscar_equipo(partido[0], equipos)
            if indice == -1:
                equipos.append([partido[0], 1])
            else:
                equipos[indice][1] += 1

            indice = buscar_equipo(partido[2], equipos)
            if indice == -1:
                equipos.append([partido[2], 1])
            else:
                equipos[indice][1] += 1
    return encontrar_ganadores(equipos)


print(determinar_gan([["America", 3, "Cali", 0],
                      ["Junior", 2, "America", 3],
                      ["Santafe", 2, "Junior", 1],
                      ["Cali", 2, "Junior", 2],
                      ["America", 1, "Santafe", 1]]))


# Input: matriz n x m
# Descripción: Tomar una matriz n x m y sumar cada uno de sus elementos
# Output: int (suma de todos los elementos de la matriz)
def determinar_ganador(lis):
    n, j = 0, 0
    for i in range(len(lis)):
        f = lis[i]
        for p in range(f):
            k = f[p]
            x = k / 2
            if x == 0 and len(k) == x and len(k) == 1:
                n += k
            elif len(k) != x:
                j = str(k)
            return j, n
