import numpy as np
import time


def func_activacion(x: float):
    return 1 if x >= 0 else 0


def entrenar_neurona(
    X: np.ndarray,
    Y: np.ndarray,
    epocas=100,
    tasa_aprendizaje=0.1,
):
    num_caracs = X.shape[1]
    pesos = np.zeros(num_caracs)
    bias = 0

    for epoca in range(epocas):
        print(f"epoca {epoca}")

        nuevos_pesos = False

        for i in range(X.shape[0]):
            z = np.dot(X[i], pesos) + bias
            pred_y = func_activacion(z)
            error = y[i] - pred_y

            if error != 0:
                pesos += error * tasa_aprendizaje * X[i]
                bias += error * tasa_aprendizaje
                nuevos_pesos = True

            time.sleep(0.01)

        if not nuevos_pesos:
            print(f"convergencia en {epoca}")
            break
    return pesos, bias


X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([0, 0, 0, 1])


def predecir(input_uno, input_dos, pesos, bias):
    X_input = np.array([input_uno, input_dos])
    z = np.dot(X_input, pesos) + bias
    return func_activacion(z)


# entrenar la neurona
pesos_entrenados, bias_entrenados = entrenar_neurona(X, y)

# realizar predicciones
valor_in_uno = 0
valor_in_dos = 0

prediccion = predecir(
    valor_in_uno,
    valor_in_dos,
    pesos_entrenados,
    bias_entrenados,
)
print(f"la prediccion es {valor_in_uno}, {valor_in_dos} = {prediccion}")
