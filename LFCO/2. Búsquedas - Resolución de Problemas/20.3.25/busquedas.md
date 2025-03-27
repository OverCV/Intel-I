Busquedas no informadas (que no tienen la heurísticaa) como:

- Anchura (Por niveles)
- Profundidad
  - iterativa: Llega a un nivel k y se detiene para no seguir bajando
- Bidireccional: Que va desde el inicio y el final al mismo tiempo

Búsquedas informadas (que tienen la heurística) como: Estas permiten saber qué tan cerca está de la solución (estimación a lo que le falta):

Tiene características como que debe ser positiva (no negativa porque el coste se incrementa, si fuera negativo es que se devuelve y habrían mismos puntos, es como si no hubiera biyectividad).
También debe tender a 0 el h(n), la estimación a la solución real debe ser muy cercana (no puede estar sobre-estimada pues eso da problemas en el sistema).

Hill climbing: Toma el más prometedor según la heurística, pero no es muy eficiente porque se queda en un máximo local y no llega al global.

Bean search.
---
Bueno, el primer parcial va hasta esos temas.

--- 

# Agente
Entidad que pensaba el entorno, tenía sensores.
"Razonamiento" -> Planificación
"Actuadores" Efectores

Todo lo de POO estaba en las clases y por el otro los agentes
> Clase:
> - Herencia
> - Polimorfismo
> - Encapsulamiento (Objeto)
> - Abstracción (Clase Interfaz )

Antes los objetos instancian y ejecutan métodos, que estaban los ACLs (Agent Communication Language) que permiten la comunicación entre agentes.


Las 4 R's de la IA:
Recuperación
Reutilizar
Revisión
Retención

---


Beam Search

Este algoritmo se aplica en dos contextos:

Algoritmo informado que aplica al costo del camino o lo que le falta, pero no combina ambas (costo y heurística).

Este enfoque dice haz de luz porque la busqueda se basa en el ancho del haz de luz, cuántos nodos se expanden en cada nivel. Adicional de la info por el coste y heuristica tiene el ancho del haz.

Los algoritmos de BFS DFS manejan dos listas (conjunto abiertos y cerrados), los sucesores están en abiertos y cerrados son para evitar ciclos, aplica la lista de sucesores abiertos.
El chiste es que el haz de luz tiene la restricción que es el foco, cuántos puede ver, qué tan amplia puede hacer la búsqueda

Costo uniforme es por el g(n) (ordena por el de menor coste).
El chiste es que no solo es la dirección sino también el haz de luz, no se expande mucho y es más direccionado.

CUando no hayan sucesores toma el nivel que no se haya procesado.


ESte algoritmo se aplica sobre el procesamiento del lenguaje natural.

El corupues es un conjunto de documentos en un dominio específico.

## Work Embeddings

<!-- // MCP -  -->

<!-- 
"⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬜
⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬜
⬜⬜⬜⬜⬜"
 -->