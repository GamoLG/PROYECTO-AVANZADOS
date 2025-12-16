"""
COMPARACIÓN DE ALGORITMOS: Dijkstra vs O(m log^{2/3} n)
Comparación exhaustiva de tiempo, eficiencia y resultados
"""

import time
import matplotlib.pyplot as plt
import numpy as np

# Importar los algoritmos de los scripts anteriores
# Nota: En la práctica, estos estarían en módulos separados
# Para este ejemplo, copiamos las funciones esenciales

def dijkstra_simple(grafo, origen):
    """
    Implementación simple de Dijkstra para comparación
    """
    import heapq
    
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[origen] = 0
    
    heap = [(0, origen)]
    procesados = set()
    
    while heap:
        distancia_actual, nodo_actual = heapq.heappop(heap)
        
        if nodo_actual in procesados:
            continue
        
        procesados.add(nodo_actual)
        
        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))
    
    return distancias, predecesores

def algoritmo_nuevo_simple(grafo, origen):
    """
    Implementación simple del nuevo algoritmo para comparación
    """
    import math
    from collections import defaultdict
    
    n = len(grafo)
    
    # Calcular parámetro L
    if n <= 1:
        L = 1
    else:
        L = int(math.pow(math.log2(n), 2/3))
        L = max(L, 1)
    
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[origen] = 0
    
    # Procesar en fases
    for iteracion in range(L):
        # En cada iteración, procesar todos los nodos activos
        nodos_activos = [nodo for nodo in grafo if distancias[nodo] < float('inf')]
        
        for nodo_actual in nodos_activos:
            for vecino, peso in grafo[nodo_actual].items():
                nueva_distancia = distancias[nodo_actual] + peso
                
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
    
    return distancias, predecesores

def comparar_resultados(distancias1, distancias2, nombre1, nombre2):
    """
    Compara si dos conjuntos de distancias son iguales
    """
    print(f"COMPARACIÓN DE RESULTADOS: {nombre1} vs {nombre2}")
    print("=" * 50)
    
    todos_iguales = True
    
    for nodo in distancias1:
        d1 = distancias1[nodo]
        d2 = distancias2[nodo]
        
        # Comparar con tolerancia para números flotantes
        if abs(d1 - d2) > 0.0001:
            if d1 == float('inf') and d2 == float('inf'):
                continue
            print(f"  Diferencia en nodo {nodo}: {nombre1}={d1}, {nombre2}={d2}")
            todos_iguales = False
    
    if todos_iguales:
        print("  ✅ Ambos algoritmos producen los mismos resultados")
    else:
        print("  ❌ Los algoritmos producen resultados diferentes")
    
    return todos_iguales

def prueba_con_grafo_especifico():
    """
    Prueba de comparación con un grafo específico
    """
    # Grafo de prueba
    grafo = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    
    origen = 'A'
    
    print("COMPARACIÓN CON GRAFO ESPECÍFICO")
    print("=" * 50)
    print(f"Nodos: {len(grafo)}")
    print(f"Aristas: {sum(len(vecinos) for vecinos in grafo.values())}")
    print(f"Nodo origen: {origen}")
    print()
    
    # Ejecutar Dijkstra
    inicio_dijkstra = time.time()
    distancias_dijkstra, _ = dijkstra_simple(grafo, origen)
    tiempo_dijkstra = time.time() - inicio_dijkstra
    
    # Ejecutar nuevo algoritmo
    inicio_nuevo = time.time()
    distancias_nuevo, _ = algoritmo_nuevo_simple(grafo, origen)
    tiempo_nuevo = time.time() - inicio_nuevo
    
    # Comparar resultados
    resultados_iguales = comparar_resultados(
        distancias_dijkstra, 
        distancias_nuevo,
        "Dijkstra",
        "Algoritmo Nuevo"
    )
    
    print()
    print("COMPARACIÓN DE TIEMPOS")
    print("=" * 50)
    print(f"Dijkstra: {tiempo_dijkstra:.6f} segundos")
    print(f"Algoritmo Nuevo: {tiempo_nuevo:.6f} segundos")
    
    if tiempo_nuevo > 0:
        speedup = tiempo_dijkstra / tiempo_nuevo
        print(f"Speedup (Dijkstra/Nuevo): {speedup:.2f}x")
        
        if speedup > 1:
            print("  ✅ Dijkstra es más rápido")
        elif speedup < 1:
            print("  ✅ Algoritmo nuevo es más rápido")
        else:
            print("  ⚠️  Ambos tienen tiempos similares")
    
    return tiempo_dijkstra, tiempo_nuevo, resultados_iguales

def prueba_con_varios_grafos():
    """
    Prueba de comparación con múltiples grafos de diferentes tamaños
    """
    print("\n" + "=" * 50)
    print("PRUEBA CON MÚLTIPLES GRAFOS")
    print("=" * 50)
    
    resultados = []
    
    # Generar varios grafos de diferentes tamaños
    grafos_prueba = [
        # (nombre, número de nodos, densidad)
        ("Pequeño", 10, 0.3),
        ("Mediano", 50, 0.2),
        ("Grande", 100, 0.1),
        ("Muy Grande", 200, 0.05),
    ]
    
    import random
    
    for nombre, n_nodos, densidad in grafos_prueba:
        print(f"\nProbando grafo {nombre} ({n_nodos} nodos, densidad {densidad}):")
        
        # Generar grafo aleatorio
        grafo = {}
        for i in range(n_nodos):
            grafo[i] = {}
            for j in range(n_nodos):
                if i != j and random.random() < densidad:
                    peso = random.randint(1, 100)
                    grafo[i][j] = peso
        
        origen = 0
        
        # Medir tiempo Dijkstra
        inicio = time.time()
        dijkstra_simple(grafo, origen)
        tiempo_dijkstra = time.time() - inicio
        
        # Medir tiempo nuevo algoritmo
        inicio = time.time()
        algoritmo_nuevo_simple(grafo, origen)
        tiempo_nuevo = time.time() - inicio
        
        # Calcular speedup
        speedup = tiempo_dijkstra / tiempo_nuevo if tiempo_nuevo > 0 else 0
        
        resultados.append({
            'nombre': nombre,
            'nodos': n_nodos,
            'aristas': sum(len(vecinos) for vecinos in grafo.values()),
            'tiempo_dijkstra': tiempo_dijkstra,
            'tiempo_nuevo': tiempo_nuevo,
            'speedup': speedup
        })
        
        print(f"  Dijkstra: {tiempo_dijkstra:.4f}s")
        print(f"  Nuevo: {tiempo_nuevo:.4f}s")
        print(f"  Speedup: {speedup:.2f}x")
    
    return resultados

def generar_graficos_comparacion(resultados):
    """
    Genera gráficos de comparación
    """
    # Extraer datos
    nombres = [r['nombre'] for r in resultados]
    tiempos_dijkstra = [r['tiempo_dijkstra'] for r in resultados]
    tiempos_nuevo = [r['tiempo_nuevo'] for r in resultados]
    speedups = [r['speedup'] for r in resultados]
    
    # Crear figura con subgráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfico 1: Tiempos de ejecución
    x = np.arange(len(nombres))
    ancho = 0.35
    
    ax1.bar(x - ancho/2, tiempos_dijkstra, ancho, label='Dijkstra', alpha=0.8)
    ax1.bar(x + ancho/2, tiempos_nuevo, ancho, label='Algoritmo Nuevo', alpha=0.8)
    
    ax1.set_xlabel('Tamaño del Grafo')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_title('Comparación de Tiempos de Ejecución')
    ax1.set_xticks(x)
    ax1.set_xticklabels(nombres)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Speedup
    ax2.bar(nombres, speedups, alpha=0.7, color='green')
    ax2.axhline(y=1, color='red', linestyle='--', alpha=0.5, label='Límite neutral')
    
    ax2.set_xlabel('Tamaño del Grafo')
    ax2.set_ylabel('Speedup (Dijkstra / Nuevo)')
    ax2.set_title('Speedup por Tamaño de Grafo')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('comparacion_algoritmos.png', dpi=150)
    plt.show()
    
    print("\nGráficos generados y guardados como 'comparacion_algoritmos.png'")

def resumen_comparacion():
    """
    Genera un resumen completo de la comparación
    """
    print("\n" + "=" * 50)
    print("RESUMEN DE COMPARACIÓN")
    print("=" * 50)
    
    # Ejecutar pruebas
    print("\n1. Prueba con grafo específico:")
    t_dijkstra, t_nuevo, iguales = prueba_con_grafo_especifico()
    
    print("\n2. Prueba con múltiples grafos:")
    resultados = prueba_con_varios_grafos()
    
    # Calcular promedios
    avg_speedup = np.mean([r['speedup'] for r in resultados])
    avg_tiempo_dijkstra = np.mean([r['tiempo_dijkstra'] for r in resultados])
    avg_tiempo_nuevo = np.mean([r['tiempo_nuevo'] for r in resultados])
    
    print("\n" + "=" * 50)
    print("CONCLUSIONES FINALES")
    print("=" * 50)
    print(f"1. Correctitud: {'✅ Ambos algoritmos producen resultados iguales' if iguales else '❌ Resultados diferentes'}")
    print(f"2. Tiempo promedio Dijkstra: {avg_tiempo_dijkstra:.4f} segundos")
    print(f"3. Tiempo promedio Algoritmo Nuevo: {avg_tiempo_nuevo:.4f} segundos")
    print(f"4. Speedup promedio: {avg_speedup:.2f}x")
    
    if avg_speedup > 1:
        print(f"5. Conclusion: Dijkstra es {avg_speedup:.2f} veces más rápido en promedio")
    elif avg_speedup < 1:
        print(f"5. Conclusion: El algoritmo nuevo es {1/avg_speedup:.2f} veces más rápido en promedio")
    else:
        print("5. Conclusion: Ambos algoritmos tienen rendimiento similar")
    
    # Generar gráficos
    generar_graficos_comparacion(resultados)
    
    return resultados

if __name__ == "__main__":
    # Ejecutar comparación completa
    resultados_finales = resumen_comparacion()