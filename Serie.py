class Serie:
    # Creamos el constructor
    def __init__(self, titulo="", numTemporadas=3, entregado=False, genero="", creador=""):
        self.titulo = titulo
        self.numTempo = numTemporadas
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    # Creamos el metodo "toString"
    def __str__(self):
        return str(self.titulo + ", " + repr(self.numTempo) + ", " + repr(self.entregado) + ", " + self.genero + ", " + self.creador)

    # Creamos los getter y los setter para cada atributo
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo=titulo

    def get_numeroTemp(self):
        return self.numeroTempo

    def set_numeroTemp(self, numTemp):
        self.numTempo=numTemp

    def get_genero(self):
        return self.genero

    def set_genero(self, gen):
        self.genero=gen

    def get_creador(self):
        return self.creador

    def set_creador(self, crear):
        self.creador = crear