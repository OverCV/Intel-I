# Intel-One: Visualización de Algoritmos en Sistemas Inteligentes

Este repositorio contiene código para la visualización y simulación de algoritmos en el contexto de Sistemas Inteligentes. Diseñado como herramienta de apoyo para el curso, permite visualizar y entender conceptos clave a través de animaciones interactivas.

## Contenidos

El proyecto cubre los siguientes temas del curso:

1. **Presentación del Curso**
   - Introducción a la inteligencia artificial
   - Historia y evolución de los sistemas inteligentes

2. **Búsquedas - Resolución de Problemas**
   - Algoritmos de búsqueda informada y no informada (BFS, DFS, A*, etc.)
   - Visualización de recorridos en laberintos
   - Problemas clásicos (jarras de agua, 8-puzzle, etc.)

3. **Teoría de Juegos**
   - Algoritmos minimax
   - Poda alfa-beta
   - Simulación de juegos adversarios

4. **Representación del Conocimiento**
   - Sistemas basados en reglas
   - Lógica de predicados
   - Razonamiento simbólico

5. **Agentes y Sistemas Multi-Agente**
   - Arquitectura de agentes
   - Comunicación entre agentes
   - Comportamientos emergentes

6. **Razonamiento Bajo Incertidumbre**
   - Redes bayesianas
   - Teoría de la decisión
   - Modelos probabilísticos

## Requisitos

- Python >= 3.8
- Bibliotecas: numpy, matplotlib, networkx, jupyter/ipython

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/intel-one.git
   cd intel-one
   ```

2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Unix/MacOS:
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -e .
   ```

## Uso

### Visualización de algoritmos de búsqueda

```python
from intel_one.laberinto import GeneradorLaberinto, bfs_laberinto_con_estados, crear_animacion_laberinto

# Crear un laberinto
generador = GeneradorLaberinto(ancho=21, alto=21)
generador.crear_lineas_horizontales(num_lineas=5)
laberinto = generador.crear_lineas_verticales(num_lineas=5)

# Definir puntos de inicio y fin
inicio = (0, 0)
final = (20, 20)

# Ejecutar BFS y visualizar
camino, estados = bfs_laberinto_con_estados(laberinto, inicio, final)
animacion = crear_animacion_laberinto(laberinto, inicio, final, estados)
display(animacion)  # En Jupyter Notebook
```

### Resolución del problema de las jarras

```python
from intel_one.jarras import resolver_jarras, visualizar_solucion

# Configurar el problema (jarras de 4 y 3 litros, objetivo: 2 litros)
estados, camino = resolver_jarras(4, 3, 2)
visualizar_solucion(camino)
```

## Estructura del Proyecto

```
intel-one/
├── README.md
├── pyproject.toml
├── intel_one/
│   ├── __init__.py
│   ├── laberinto.py         # Algoritmos de búsqueda en laberintos
│   ├── jarras.py            # Problema de las jarras de agua
│   ├── juegos/              # Implementaciones de teoría de juegos
│   ├── agentes/             # Sistemas multi-agente
│   └── incertidumbre/       # Algoritmos para razonamiento probabilístico
└── notebooks/
    ├── 01_introduccion.ipynb
    ├── 02_busquedas.ipynb
    ├── 03_juegos.ipynb
    └── ...
```

## Contribuciones

Este es un proyecto académico. Si deseas contribuir con mejoras o correcciones, por favor:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Empuja a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está disponible bajo la licencia MIT. Ver el archivo LICENSE para más detalles.