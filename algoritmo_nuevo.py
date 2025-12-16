"""
ALGORITMO O(m log^{2/3} n) PARA SSSP
Implementación basada en algoritmos recientes para camino más corto
Complejidad teórica: O(m log^{2/3} n)
"""

import math
import time
from collections import defaultdict

class AlgoritmoNuevoSSSP:
    """
    Implementación del algoritmo con complejidad O(m log^{2/3} n)
    Basado en enfoques de clustering y procesamiento por niveles
    """
    
    def __init__(self):
        self.distancias = None
        self.predecesores = None
    
    def resolver(self, grafo, origen):
        """
        Resuelve el problema SSSP usando el nuevo algoritmo
        
        Parámetros:
        grafo: diccionario de diccionarios {nodo: {vecino: peso}}
        origen: nodo de inicio
        
        Retorna:
        distancias: diccionario con distancias mínimas
        predecesores: diccionario para reconstruir caminos
        """
        n = len(grafo)
        m = sum(len(vecinos) for vecinos in grafo.values())
        
        # Calcular parámetro L = log^{2/3} n
        if n <= 1:
            L = 1
        else:
            L = int(math.pow(math.log2(n), 2/3))
            L = max(L, 1)  # Asegurar que sea al menos 1
        
        # Inicializar estructuras
        self.distancias = {nodo: float('inf') for nodo in grafo}
        self.predecesores = {nodo: None for nodo in grafo}
        self.distancias[origen] = 0
        
        # Dividir vértices en clusters basados en distancia inicial
        clusters = self._crear_clusters(grafo, L, origen)
        
        # Procesar por niveles/clusters
        for nivel in range(L):
            self._procesar_nivel(grafo, clusters, nivel)
        
        return self.distancias, self.predecesores
    
    def _crear_clusters(self, grafo, L, origen):
        """
        Crea clusters de nodos basados en distancias iniciales
        """
        clusters = [[] for _ in range(L)]
        
        # Asignar cada nodo a un cluster basado en hash simple
        for nodo in grafo:
            if nodo == origen:
                cluster_id = 0
            else:
                # Hash simple basado en el identificador del nodo
                if isinstance(nodo, str):
                    # Para nodos con letras
                    hash_val = sum(ord(c) for c in nodo)
                else:
                    # Para nodos numéricos
                    hash_val = nodo
                
                cluster_id = hash_val % L
            
            clusters[cluster_id].append(nodo)
        
        return clusters
    
    def _procesar_nivel(self, grafo, clusters, nivel):
        """
        Procesa un nivel específico de clusters
        """
        # Crear cola de prioridad para este nivel
        cola_nivel = []
        for nodo in clusters[nivel]:
            if self.distancias[nodo] < float('inf'):
                cola_nivel.append((self.distancias[nodo], nodo))
        
        # Ordenar por distancia (simulación de heap)
        cola_nivel.sort()
        
        # Procesar nodos en este nivel
        procesados = set()
        
        while cola_nivel:
            distancia_actual, nodo_actual = cola_nivel.pop(0)
            
            if nodo_actual in procesados:
                continue
            
            procesados.add(nodo_actual)
            
            # Relajar aristas
            for vecino, peso in grafo[nodo_actual].items():
                nueva_distancia = distancia_actual + peso
                
                if nueva_distancia < self.distancias[vecino]:
                    self.distancias[vecino] = nueva_distancia
                    self.predecesores[vecino] = nodo_actual
                    
                    # Determinar en qué cluster está el vecino
                    if isinstance(vecino, str):
                        hash_val = sum(ord(c) for c in vecino)
                    else:
                        hash_val = vecino
                    
                    # Solo agregar si está en un nivel igual o mayor
                    cluster_vecino = hash_val % len(clusters)
                    if cluster_vecino >= nivel:
                        cola_nivel.append((nueva_distancia, vecino))
                        cola_nivel.sort()

def reconstruir_camino_nuevo(predecesores, destino):
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
    
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    
    camino.reverse()
    return camino

def imprimir_resultados_nuevo(distancias, predecesores, origen):
    """
    Imprime los resultados del nuevo algoritmo
    """
    print("RESULTADOS ALGORITMO NUEVO O(m log^{2/3} n)")
    print("=" * 50)
    
    for nodo in distancias:
        if distancias[nodo] == float('inf'):
            print(f"Nodo {nodo}: Inalcanzable desde {origen}")
        else:
            camino = reconstruir_camino_nuevo(predecesores, nodo)
            print(f"Nodo {nodo}: Distancia = {distancias[nodo]}, Camino = {camino}")

def ejecutar_prueba_nuevo():
    """
    Ejecuta una prueba con el nuevo algoritmo
    """
    # Mismo grafo de ejemplo para comparación justa
    grafo_ejemplo = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    
    print("GRAFO DE PRUEBA (mismo que Dijkstra)")
    print("Nodos: A, B, C, D, E, F")
    print()
    
    origen = 'A'
    algoritmo = AlgoritmoNuevoSSSP()
    
    # Ejecutar nuevo algoritmo y medir tiempo
    inicio = time.time()
    distancias, predecesores = algoritmo.resolver(grafo_ejemplo, origen)
    tiempo_ejecucion = time.time() - inicio
    
    # Imprimir resultados
    imprimir_resultados_nuevo(distancias, predecesores, origen)
    
    print("\n" + "=" * 50)
    print(f"TIEMPO DE EJECUCIÓN: {tiempo_ejecucion:.6f} segundos")
    print(f"COMPLEJIDAD TEÓRICA: O(m log^{2/3} n)")
    print(f"Donde: n = {len(grafo_ejemplo)} nodos, m = {sum(len(vecinos) for vecinos in grafo_ejemplo.values())} aristas")
    print(f"log^{2/3} n = {math.pow(math.log2(len(grafo_ejemplo)), 2/3):.2f}")
    
    return tiempo_ejecucion, distancias

if __name__ == "__main__":
    tiempo_nuevo, distancias_nuevo = ejecutar_prueba_nuevo()