from Videojuego import Videojuego
from Serie import Serie

# Creamos las listas donde iran guardados los objetos
series = list()
juegos = list()

# Creamos los objetos y los insertamos en su correspondiente lista
series.insert(-1, Serie(titulo="Breaking Bad", numTemporadas=5, entregado=True, genero="Drama Criminal", creador="Netflix"))
series.insert(-1, Serie(titulo="Squid Game", numTemporadas=1, entregado=False, genero="Drama", creador="Netflix"))
series.insert(-1, Serie(titulo="Stars Wars: The Bad Batch", numTemporadas=1, entregado=True, genero="Ciencia ficción", creador="Dave Filoni"))
series.insert(-1, Serie(titulo="Loki", numTemporadas=1, entregado=False, genero="Crimen; Ciencia ficción; Superhéroes; Comedia", creador="Marvel"))
series.insert(-1, Serie(titulo="Attack On Titan", numTemporadas=3, entregado=True, genero="Accion-Ficcion", creador="Hajime Isayama"))

juegos.insert(-1, Videojuego(titulo="League Of Legends", horasEstimadas=25, entregado=False, genero="MOBA", comp="Riot Games"))
juegos.insert(-1, Videojuego(titulo="Minecraft", horasEstimadas=80, entregado=True, genero="Free Roam", comp="Mojang"))
juegos.insert(-1, Videojuego(titulo="Grand Theft Auto V", horasEstimadas=120, entregado=False, genero="Free Roam", comp="Rockstar Games"))
juegos.insert(-1, Videojuego(titulo="Counter Strike : Global Offesive", horasEstimadas=500, entregado=True, genero="Shooter", comp="Valve"))
juegos.insert(-1, Videojuego(titulo="Shadow Of The Colossus", horasEstimadas=24, entregado=False, genero="Acción", comp="Sony Computer Entertainment"))

# Creamos la variable para cada tipo de objeto donde se guardaran los valores mas altos de cada una
serieMasAlta = Serie()
juegoMasAlto = Videojuego()

# Mostramos solo si estan entregados y cogemos la serie con mas temporadas, ademas de mostrarlas por pantalla
for i in series:
    if i.entregado:
        print(i)
        if i.numTempo > serieMasAlta.numTempo:
            serieMasAlta = i

# Hacemos el mismo proceso con los videojuegos
for i in juegos:
    if i.entregado:
        print(i)
        if i.horasEstimadas > juegoMasAlto.horasEstimadas:
            juegoMasAlto=i

# Mostramos por pantalla los valores mas altos de cada tipo de objeto
print("\nSerie con más temporadas: " + str(serieMasAlta))
print("Juego con más horas: " + str(juegoMasAlto))