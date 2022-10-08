"""
Catalina G
Código: 8978486
30 / 09 / 2022
"""

# Punto 1 #


def sumas_acumuladas(lel):
    i = 0
    ans = []
    for y in range(len(lel)):
        i += lel[y]
        ans.append(i)
    return ans

# Punto 2 #


def leer_imprimir(n):
    i = 0
    while i < n:
        lel = input()
        res = sumas_acumuladas(lel)
        i += 1
        return res


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


# punto 5#


def es_subcadena(cad1, cad2):
    ans = False
    while cad1 in cad2:
        ans = True
        return ans



# punto 6 #

""" parte a """


def fracaso(p):
    c = 0
    r = 0
    k = ""
    for i in range(len(p)):
        if c == p[5] and r == p[6] and c < r:
            k = "fracaso"
        return k

""" Parte b """


def conteo_peliculas_actor(pelis):
    p = 0
    for i in range(len(pelis)):
        t = pelis[i]
        if t == pelis[5]:
            p += 1
    for l in range(len(pelis)):
        k = pelis[l]
        return k, p



# punto 7 #


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


