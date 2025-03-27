from collections import deque
import heapq
import itertools
import os
import random
from matplotlib import pyplot as plt
from networkx import MultiDiGraph
import osmnx as ox


def dijkstra_min_fuel_consumption(orig, dest, vehicle_fuel_efficiency, plot=False):
    visited = set()  # Conjunto de nodos visitados
    total_fuel_consumed = 0  # Total de combustible consumido
    for node in G.nodes:
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
        G.nodes[node]["g_score"] = float("inf")
    for edge in G.edges(keys=True):
        style_unvisited_edge(edge)
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    G.nodes[orig]["g_score"] = 0
    pq = [(0, orig)]
    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            if plot:
                print("Iteraciones:", step)
                plot_graph()
            return reconstruct_path(
                orig, dest, plot=plot, algorithm="dijkstra_min_fuel_consumption"
            ), total_fuel_consumed
        if node in visited:
            continue
        visited.add(node)
        for edge in G.out_edges(node, keys=True):
            style_visited_edge((edge[0], edge[1], edge[2]))
            neighbor = edge[1]
            edge_length = G.edges[edge]["length"]
            max_speed = G.edges[edge]["maxspeed"]
            fuel_consumption = edge_length / (max_speed * vehicle_fuel_efficiency)
            total_fuel_consumed += fuel_consumption
            tentative_g_score = G.nodes[node]["g_score"] + fuel_consumption
            if tentative_g_score < G.nodes[neighbor]["g_score"]:
                G.nodes[neighbor]["previous"] = node
                G.nodes[neighbor]["g_score"] = tentative_g_score
                heapq.heappush(pq, (G.nodes[neighbor]["g_score"], neighbor))
                for edge2 in G.out_edges(neighbor, keys=True):
                    style_active_edge((edge2[0], edge2[1], edge2[2]))
                fuel_used = fuel_consumption * vehicle_fuel_efficiency
                print(f"Used {fuel_used:.2f} gallons of fuel for edge {edge}")
                step += 1
        print(f"total = {total_fuel_consumed:.2f} gallons")


def a_star_traffic_lights(orig, dest, plot=False):
    for node in G.nodes:
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
        G.nodes[node]["g_score"] = float("inf")
        G.nodes[node]["f_score"] = float("inf")
    for edge in G.edges:
        style_unvisited_edge(edge)
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    G.nodes[orig]["g_score"] = 0
    G.nodes[orig]["f_score"] = distance(orig, dest)
    pq = [(G.nodes[orig]["f_score"], orig)]
    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            if plot:
                print("Iteraciones:", step)
                plot_graph()
            return reconstruct_path(
                orig, dest, plot=plot, algorithm="a_star_traffic_lights"
            )
        for edge in G.out_edges(node):
            style_visited_edge((edge[0], edge[1], 0))
            neighbor = edge[1]
            tentative_g_score = G.nodes[node]["g_score"] + distance(node, neighbor)
            travel_time = G.edges[
                (node, neighbor, 0)
            ][
                "weight"
            ]  # considera el tiempo de viaje en función de la distancia y la velocidad máxima
            # Añade el tiempo de espera en semáforos al tiempo de viaje
            travel_time += G.edges[(node, neighbor, 0)].get("traffic_light_wait", 0)
            tentative_g_score += G.edges[(node, neighbor, 0)].get(
                "traffic_light_wait", 0
            )
            if tentative_g_score < G.nodes[neighbor]["g_score"]:
                G.nodes[neighbor]["previous"] = node
                G.nodes[neighbor]["g_score"] = tentative_g_score
                G.nodes[neighbor]["f_score"] = tentative_g_score + distance(
                    neighbor, dest
                )
                heapq.heappush(pq, (G.nodes[neighbor]["f_score"], neighbor))
                for edge2 in G.out_edges(neighbor):
                    style_active_edge((edge2[0], edge2[1], 0))
        step += 1


def add_node_sizes(default_size=10):
    """
    Agrega el atributo 'size' a todos los nodos con un valor predeterminado.
    """
    for node in G.nodes:
        if "size" not in G.nodes[node]:
            G.nodes[node]["size"] = default_size


def style_traffic_lights(default_color="green", default_linewidth=1):
    """
    Modifica el color de los nodos que representan semáforos y agrega el atributo 'color', 'alpha' y 'linewidth' a los bordes.
    """
    for node, data in G.nodes(data=True):
        #! Editar estilos originales.

        if random.random() < 0.15:
            G.nodes[node]["semaforo_rojo"] = True
            G.nodes[node]["tiempo"] = 10
            G.nodes[node]["node_color"] = default_color

        if random.random() < 0.0125:
            G.nodes[node]["es_turistico"] = True
            G.nodes[node]["node_color"] = "#FA0AFA"

        # if 'traffic_light' in G.nodes[node]:
        #     print(G.nodes[node])

        # if G.nodes[node]['semaforo']:  # Verifica si el nodo tiene el atributo 'semaforo'
        # semaforo = data['semaforo']
        # if isinstance(semaforo, dict) and 'color' in semaforo:
        # G.nodes[node]['node_color'] = default_color  # Cambia el color del nodo según el atributo 'color' del semáforo

    for edge in G.edges:
        if "color" not in G.edges[edge]:
            G.edges[edge]["color"] = (
                "#d36206"  # Define un color predeterminado para los bordes
            )
        if "alpha" not in G.edges[edge]:
            G.edges[edge]["alpha"] = (
                1  # Define un valor predeterminado para la transparencia de los bordes
            )
        if "linewidth" not in G.edges[edge]:
            G.edges[edge]["linewidth"] = (
                default_linewidth  # Define un ancho de línea predeterminado para los bordes
            )


def bfs_turisticos(G, origen):
    visitados = set()  # Conjunto de nodos visitados
    turisticos = set()  # Conjunto de nodos turísticos

    # Se añaden al conjunto de turisticos las claves de los nodos que son turisticos
    if any("es_turistico" in data for _, data in G.nodes(data=True)):
        for node, data in G.nodes(data=True):
            if "es_turistico" in data:
                print(node, data)
                turisticos.add(node)
    # y Verificar si no hay nodos turísticos en el grafo
    else:
        print("No hay nodos turísticos en el grafo.")
        return None

    # Creamos una cola para el BFS
    cola = deque([(origen, [origen])])

    while cola:
        nodo, camino = cola.popleft()
        visitados.add(nodo)

        # Si el nodo actual es un sitio turístico y aún no lo hemos visitado, lo agregamos al camino
        if nodo in turisticos and nodo not in camino:
            camino.append(nodo)

        # Si hemos visitado todos los sitios turísticos, detenemos el BFS
        if turisticos.issubset(set(camino)):
            return camino

        # Exploramos los vecinos del nodo actual
        for vecino in G.neighbors(nodo):
            if vecino not in visitados:
                cola.append((vecino, camino + [vecino]))

    return None  # Si no se puede encontrar un camino que pase por todos los sitios turísticos.


def turistic_tsp(self, origen: int, destino: int):
    for node in self._G.nodes:
        self._G.nodes[node]["previous"] = None

    # Marcar nodos turísticos y establecer colores y tamaños iniciales
    for node in self._G.nodes:
        if random.random() < 0.0125:
            self._G.nodes[node]["es_turistico"] = True
            self._G.nodes[node]["color"] = BLUE_NODE
        else:
            self._G.nodes[node]["color"] = BLACK_NODE
        self._G.nodes[node]["size"] = 10

    self._G.nodes[origen]["size"] = 50
    self._G.nodes[origen]["color"] = WHITE_NODE

    # Inicializar variables
    camino = [origen]
    nodos_turisticos = {
        node for node, data in self._G.nodes(data=True) if "es_turistico" in data
    }
    nodos_visitados = set(camino)

    # Algoritmo del vecino más cercano
    while nodos_turisticos:
        nodo_actual = camino[-1]
        nodo_mas_cercano = None
        distancia_minima = float("inf")
        for vecino in self._G.neighbors(nodo_actual):
            if vecino not in nodos_visitados:
                d = self._G.edges[(nodo_actual, vecino, 0)]["weight"]
                if d < distancia_minima:
                    distancia_minima = d
                    nodo_mas_cercano = vecino
        if nodo_mas_cercano is None:  # Si no se encontró vecino turístico, salir
            break
        self.style_path_edge((nodo_actual, nodo_mas_cercano, 0))
        camino.append(nodo_mas_cercano)
        nodos_visitados.add(nodo_mas_cercano)
        if nodo_mas_cercano in nodos_turisticos:
            nodos_turisticos.remove(nodo_mas_cercano)

import networkx as nx
import matplotlib.pyplot as plt

for node in G.nodes:
    if ('x' in G.nodes[node]) and ('y' in G.nodes[node]):
        G.nodes[node]['pos'] = (G.nodes[node]['x'], G.nodes[node]['y'])

# Función para manejar eventos de clic
def on_click(event):
    if event.button == 1 and event.inaxes is not None:
        x, y = event.xdata, event.ydata
        # Buscar el nodo más cercano a la posición clickeada
        min_dist = float('inf')
        selected_node = None
        for node, (nx, ny) in nx.get_node_attributes(G, 'pos').items():
            dist = (x - nx) ** 2 + (y - ny) ** 2
            if dist < min_dist:
                min_dist = dist
                selected_node = node
        if selected_node is not None:
            print(f"Nodo seleccionado: {selected_node}")

# Dibujar el grafo con detalles mínimos
plt.figure(figsize=(8, 6))
pos = nx.get_node_attributes(G, 'pos')
nx.draw_networkx_nodes(G, pos=pos, node_size=50, node_color='skyblue', edgecolors='black', linewidths=0.5)
nx.draw_networkx_edges(G, pos=pos, width=0.5, edge_color='gray', arrows=False)
plt.title("Grafo de ejemplo")

# Registrar el manejador de eventos de clic
plt.gcf().canvas.mpl_connect('button_press_event', on_click)

plt.show()