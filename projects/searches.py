# Diseño de proceso de búsqueda por anchura o profundidad de forma manual

# Representación de los datos, se puede diseñar a nivel básico una matriz de conexiones entre los elementos de dos conjuntos de datos


class mat:
    def __init__(self, mat):
        self.data = mat

    def at(self, x, y):
        return self.data[x][y]


datos = mat(
    [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
)


def recorrido(
    origen: tuple[int, int]=(0,0),
    matriz: mat,
):
    inicio_conocido = (0, 1)
    print(f"{matriz.at(*inicio_conocido)=}")

    


recorrido(datos)
