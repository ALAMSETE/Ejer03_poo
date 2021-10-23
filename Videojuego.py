class Videojuego:
    # Creamos el constructor
    def __init__(self, titulo="", horasEstimadas=10, entregado=False, genero="", comp=""):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.comp = comp

    # Creamos el metodo "toString"
    def __str__(self):
        return str(self.titulo + ", " + repr(self.horasEstimadas) + ", " +  repr(self.entregado) + ", " + self.genero + ", " + self.comp)

    # Creamos los getter y los setter para cada atributo
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titu):
        self.titulo=titu

    def get_horasEstimadas(self):
        return self.horasEstimadas

    def set_horasEstimadas(self, horas):
        self.horasEstimadas=horas

    def get_genero(self):
        return self.genero

    def set_genero(self, gen):
        self.genero = gen

    def get_compania(self):
        return self.comp

    def set_compania(self, compa):
        self.comp=compa