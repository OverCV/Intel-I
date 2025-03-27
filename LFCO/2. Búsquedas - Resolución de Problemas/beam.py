def beam_search(grafo, nodo_inicial, nodo_destino, heuristica, beam_width=2):
    # Nivel actual: [(heurística, nodo, camino)]
    nivel_actual = [(heuristica[nodo_inicial], nodo_inicial, [nodo_inicial])]
    visitados = set([nodo_inicial])

    while nivel_actual:
        siguiente_nivel = []

        for _, actual, camino in nivel_actual:
            if actual == nodo_destino:
                return camino

            print(f"> actual: {actual}")

            # Expandir nodo actual
            for hijo, _ in grafo[actual]:
                if hijo not in visitados:
                    visitados.add(hijo)
                    nuevo_camino = camino + [hijo]
                    siguiente_nivel.append((heuristica[hijo], hijo, nuevo_camino))
                    print(f"  > candidato: {hijo}, h(n): {heuristica[hijo]}")

        # Quedarse solo con los beam_width mejores nodos
        siguiente_nivel.sort()  # Ordenar por heurística (menor primero)
        nivel_actual = siguiente_nivel[:beam_width]
        print(
            f"Nodos seleccionados para siguiente nivel: {[n for _, n, _ in nivel_actual]}"
        )

    return None  # No hay camino
