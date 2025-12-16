"""
ALGORITMO DE DIJKSTRA ORIGINAL
Implementación clásica para el problema de camino más corto desde un origen (SSSP)
Complejidad: O(m log n) usando heap binario, donde:
- n = número de vértices
- m = número de aristas
"""

import heapq
import time

def dijkstra_original(grafo, origen):
    """
    Implementación del algoritmo de Dijkstra original usando min-heap
    
    Parámetros:
    grafo: diccionario de diccionarios {nodo: {vecino: peso}}
    origen: nodo de inicio
    
    Retorna:
    distancias: diccionario con la distancia mínima desde origen a cada nodo
    predecesores: diccionario para reconstruir los caminos
    """
    
    # Inicializar estructuras
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[origen] = 0
    
    # Heap para nodos no procesados (distancia, nodo)
    heap = [(0, origen)]
    
    # Conjunto para nodos ya procesados
    procesados = set()
    
    while heap:
        # Extraer el nodo con menor distancia
        distancia_actual, nodo_actual = heapq.heappop(heap)
        
        # Si ya procesamos este nodo, continuar
        if nodo_actual in procesados:
            continue
        
        # Marcar nodo como procesado
        procesados.add(nodo_actual)
        
        # Relajar todas las aristas del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            if vecino in procesados:
                continue
            
            nueva_distancia = distancia_actual + peso
            
            # Si encontramos un camino más corto
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))
    
    return distancias, predecesores

def reconstruir_camino(predecesores, destino):
    """
    Reconstruye el camino desde el origen hasta el destino
    
    Parámetros:
    predecesores: diccionario de predecesores
    destino: nodo final
    
    Retorna:
    Lista con el camino desde origen hasta destino
    """
    camino = []
    nodo_actual = destino
    
    # Retroceder desde el destino hasta el origen
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    
    # Invertir el camino para que vaya de origen a destino
    camino.reverse()
    return camino

def imprimir_resultados(distancias, predecesores, origen):
    """
    Imprime los resultados del algoritmo de Dijkstra
    """
    print("RESULTADOS DIJKSTRA ORIGINAL")
    print("=" * 50)
    
    for nodo in distancias:
        if distancias[nodo] == float('inf'):
            print(f"Nodo {nodo}: Inalcanzable desde {origen}")
        else:
            camino = reconstruir_camino(predecesores, nodo)
            print(f"Nodo {nodo}: Distancia = {distancias[nodo]}, Camino = {camino}")

def ejecutar_prueba():
    """
    Ejecuta una prueba con un grafo de ejemplo
    """
    # Grafo de ejemplo (mismo que usaremos en todas las comparaciones)
    grafo_ejemplo = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    
    print("GRAFO DE PRUEBA")
    print("Nodos: A, B, C, D, E, F")
    print("Aristas con pesos:")
    for nodo in grafo_ejemplo:
        for vecino, peso in grafo_ejemplo[nodo].items():
            print(f"  {nodo} -> {vecino} : {peso}")
    print()
    
    origen = 'A'
    
    # Ejecutar Dijkstra y medir tiempo
    inicio = time.time()
    distancias, predecesores = dijkstra_original(grafo_ejemplo, origen)
    tiempo_ejecucion = time.time() - inicio
    
    # Imprimir resultados
    imprimir_resultados(distancias, predecesores, origen)
    
    print("\n" + "=" * 50)
    print(f"TIEMPO DE EJECUCIÓN: {tiempo_ejecucion:.6f} segundos")
    print(f"COMPLEJIDAD TEÓRICA: O(m log n)")
    print(f"Donde: n = {len(grafo_ejemplo)} nodos, m = {sum(len(vecinos) for vecinos in grafo_ejemplo.values())} aristas")
    
    return tiempo_ejecucion, distancias

if __name__ == "__main__":
    tiempo_dijkstra, distancias_dijkstra = ejecutar_prueba()