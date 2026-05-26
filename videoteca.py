titulos = ["Todo Poderoso", "El Padrino", "Forrest Gump", "El Origen", "Matrix", "El Señor de los Anillos", "Gladiador", "El Club de la Pelea", "El Gran Gatsby", "El Rey León", "Titanic", "Avatar", "Jurassic Park", "El Resplandor", "El Silencio de los Corderos"]
años = [2003, 1972, 1994, 2010, 1999, 2001, 2000, 1999, 2013, 1994, 1997, 2009, 1993, 1980, 1991]
calificaciones = [6.8, 9.2, 8.8, 8.8, 8.7, 8.8, 8.5, 8.8, 7.2, 8.5, 7.8, 7.8, 8.1, 8.4, 8.6]
generos = ["Comedia", "Crimen", "Drama", "Ciencia Ficción", "Acción", "Aventura", "Épica", "Thriller", "Romance", "Animación", "Romance", "Ciencia Ficción", "Aventura", "Terror", "Thriller"]
videoteca = [titulos, años, calificaciones, generos]
print("Bienvenido a la videoteca. Aquí tienes las películas disponibles según calificación y año:")
for i in range(len(videoteca[0])):
    if i==0:
        menor=videoteca[2][i]
        mayor=videoteca[2][i]
    else:
        if videoteca[2][i] < menor:
            menor = videoteca[2][i]
        if videoteca[2][i] > mayor:
            mayor = videoteca[2][i]
print("dime la calificacion deseada entre", (menor-1), "y", mayor)
calificacion = float(input())
for i in range(len(videoteca[0])):
    if i==0:
        menor=videoteca[1][i]
        mayor=videoteca[1][i]
    else:
        if videoteca[1][i] < menor:
            menor = videoteca[1][i]
        if videoteca[1][i] > mayor:
            mayor = videoteca[1][i]
print("dime el año deseado entre", (menor-1), "y", mayor)
año = int(input())
print("Películas con calificación cercana a", calificacion, "y año cercano a", año, ":")        
for i in range(len(videoteca[0])):
    if (videoteca[2][i] >= (calificacion - 1.5) and videoteca[2][i] <= (calificacion + 1.5)) and (videoteca[1][i] >= (año)):
        print(videoteca[0][i], "-", videoteca[1][i], "-", videoteca[2][i], "-", videoteca[3][i])