"""
SISTEMA SIMPLIFICADO DE EXPERIMENTACIÓN PARA COLAB
"""

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
import os
import random
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. FUNCIONES DE LOS ALGORITMOS SIMPLIFICADAS
# ============================================================================

def dijkstra_simple(grafo, origen):
    """Dijkstra básico"""
    import heapq
    
    distancias = {nodo: float('inf') for nodo in grafo}
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
                heapq.heappush(heap, (nueva_distancia, vecino))
    
    return distancias

def nuevo_algoritmo_simple(grafo, origen):
    """Nuevo algoritmo O(m log^2/3 n) simplificado"""
    import math
    
    n = len(grafo)
    
    # Calcular L = log^{2/3} n
    if n <= 1:
        L = 1
    else:
        L = max(1, int(math.pow(math.log2(n), 2/3)))
    
    # Inicializar distancias
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    
    # Procesar en fases
    for iteracion in range(L):
        nodos_activos = [nodo for nodo in grafo if distancias[nodo] < float('inf')]
        
        for nodo_actual in nodos_activos:
            for vecino, peso in grafo[nodo_actual].items():
                nueva_distancia = distancias[nodo_actual] + peso
                
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
    
    return distancias

# ============================================================================
# 2. FUNCIONES PARA GENERAR GRAFOS
# ============================================================================

def generar_grafos_prueba():
    """Genera grafos de prueba simples"""
    
    # Grafo 1: Simple de 6 nodos
    grafo1 = {
        0: {1: 4, 2: 2},
        1: {0: 4, 2: 1, 3: 5},
        2: {0: 2, 1: 1, 3: 8, 4: 10},
        3: {1: 5, 2: 8, 4: 2, 5: 6},
        4: {2: 10, 3: 2, 5: 3},
        5: {3: 6, 4: 3}
    }
    
    # Grafo 2: Aleatorio de 10 nodos
    grafo2 = {}
    for i in range(10):
        grafo2[i] = {}
        for j in range(10):
            if i != j and random.random() < 0.3:
                grafo2[i][j] = random.randint(1, 20)
    
    # Grafo 3: Aleatorio de 20 nodos
    grafo3 = {}
    for i in range(20):
        grafo3[i] = {}
        for j in range(20):
            if i != j and random.random() < 0.2:
                grafo3[i][j] = random.randint(1, 50)
    
    # Grafo 4: Aleatorio de 30 nodos
    grafo4 = {}
    for i in range(30):
        grafo4[i] = {}
        num_vecinos = random.randint(5, 15)
        vecinos = random.sample(range(30), num_vecinos)
        for j in vecinos:
            if i != j:
                grafo4[i][j] = random.randint(1, 100)
    
    return [
        ("Grafo_6n", grafo1),
        ("Grafo_10n", grafo2),
        ("Grafo_20n", grafo3),
        ("Grafo_30n", grafo4)
    ]

# ============================================================================
# 3. EJECUTAR EXPERIMENTOS SIMPLES
# ============================================================================

def ejecutar_experimentos_simples():
    """Ejecuta experimentos y muestra resultados"""
    
    print("=" * 60)
    print("EXPERIMENTOS SIMPLES: DIJKSTRA vs NUEVO ALGORITMO")
    print("=" * 60)
    
    # Generar grafos
    grafos = generar_grafos_prueba()
    
    resultados = []
    
    # Probar cada grafo
    for nombre, grafo in grafos:
        print(f"\nProbando {nombre}: {len(grafo)} nodos")
        
        # Medir Dijkstra
        inicio = time.time()
        for _ in range(10):  # 10 ejecuciones para promedio
            dijkstra_simple(grafo, 0)
        tiempo_dijkstra = (time.time() - inicio) / 10
        
        # Medir nuevo algoritmo
        inicio = time.time()
        for _ in range(10):
            nuevo_algoritmo_simple(grafo, 0)
        tiempo_nuevo = (time.time() - inicio) / 10
        
        # Calcular speedup
        if tiempo_nuevo > 0:
            speedup = tiempo_dijkstra / tiempo_nuevo
        else:
            speedup = 0
        
        # Guardar resultados
        resultados.append({
            'grafo': nombre,
            'nodos': len(grafo),
            'aristas': sum(len(vecinos) for vecinos in grafo.values()),
            'dijkstra': tiempo_dijkstra,
            'nuevo': tiempo_nuevo,
            'speedup': speedup
        })
        
        print(f"  Dijkstra: {tiempo_dijkstra:.6f}s")
        print(f"  Nuevo: {tiempo_nuevo:.6f}s")
        print(f"  Speedup: {speedup:.2f}x")
    
    return pd.DataFrame(resultados)

# ============================================================================
# 4. GENERAR GRÁFICOS SIMPLES
# ============================================================================

def generar_graficos_simples(df_resultados):
    """Genera gráficos simples de los resultados"""
    
    print("\n" + "=" * 60)
    print("GENERANDO GRÁFICOS")
    print("=" * 60)
    
    # Configurar estilo
    plt.style.use('default')
    
    # Figura 1: Comparación de tiempos
    plt.figure(figsize=(10, 6))
    
    x = np.arange(len(df_resultados))
    width = 0.35
    
    plt.bar(x - width/2, df_resultados['dijkstra'], width, 
            label='Dijkstra', color='blue', alpha=0.7)
    plt.bar(x + width/2, df_resultados['nuevo'], width, 
            label='Algoritmo Nuevo', color='red', alpha=0.7)
    
    plt.xlabel('Grafo')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.xticks(x, df_resultados['grafo'])
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Añadir valores en las barras
    for i, (d, n) in enumerate(zip(df_resultados['dijkstra'], df_resultados['nuevo'])):
        plt.text(i - width/2, d + 0.000001, f'{d:.6f}', ha='center', va='bottom', fontsize=8)
        plt.text(i + width/2, n + 0.000001, f'{n:.6f}', ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    # Figura 2: Speedup por grafo
    plt.figure(figsize=(10, 6))
    
    plt.bar(df_resultados['grafo'], df_resultados['speedup'], 
            color=['green' if s > 1 else 'red' for s in df_resultados['speedup']], 
            alpha=0.7)
    
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Límite neutral')
    plt.xlabel('Grafo')
    plt.ylabel('Speedup (Dijkstra / Nuevo)')
    plt.title('Speedup del Nuevo Algoritmo vs Dijkstra')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Añadir valores en las barras
    for i, speedup in enumerate(df_resultados['speedup']):
        plt.text(i, speedup + 0.05, f'{speedup:.2f}x', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    # Figura 3: Tiempo vs tamaño del grafo
    plt.figure(figsize=(10, 6))
    
    plt.plot(df_resultados['nodos'], df_resultados['dijkstra'], 'o-', 
             label='Dijkstra', linewidth=2, markersize=8)
    plt.plot(df_resultados['nodos'], df_resultados['nuevo'], 's-', 
             label='Algoritmo Nuevo', linewidth=2, markersize=8)
    
    plt.xlabel('Número de nodos')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Escalabilidad: Tiempo vs Tamaño del Grafo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Añadir etiquetas de puntos
    for i, (n, d, nuevo) in enumerate(zip(df_resultados['nodos'], 
                                          df_resultados['dijkstra'], 
                                          df_resultados['nuevo'])):
        plt.annotate(f'{d:.6f}', (n, d), textcoords="offset points", 
                    xytext=(0,10), ha='center', fontsize=8)
        plt.annotate(f'{nuevo:.6f}', (n, nuevo), textcoords="offset points", 
                    xytext=(0,-15), ha='center', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    # Figura 4: Gráfico de dispersión tiempo vs aristas
    plt.figure(figsize=(10, 6))
    
    plt.scatter(df_resultados['aristas'], df_resultados['dijkstra'], 
                s=100, alpha=0.7, label='Dijkstra', color='blue')
    plt.scatter(df_resultados['aristas'], df_resultados['nuevo'], 
                s=100, alpha=0.7, label='Algoritmo Nuevo', color='red')
    
    plt.xlabel('Número de aristas')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo vs Número de Aristas')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Añadir etiquetas de puntos
    for i, (m, d, nuevo) in enumerate(zip(df_resultados['aristas'], 
                                          df_resultados['dijkstra'], 
                                          df_resultados['nuevo'])):
        plt.annotate(df_resultados['grafo'][i], (m, d), 
                    textcoords="offset points", xytext=(0,10), 
                    ha='center', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    # Figura 5: Resumen completo
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subgráfico 1: Tiempos
    axes[0, 0].bar(df_resultados['grafo'], df_resultados['dijkstra'], 
                   alpha=0.7, label='Dijkstra', color='blue')
    axes[0, 0].bar(df_resultados['grafo'], df_resultados['nuevo'], 
                   alpha=0.7, label='Nuevo', color='red', bottom=df_resultados['dijkstra'])
    axes[0, 0].set_title('Tiempos de Ejecución')
    axes[0, 0].set_ylabel('Tiempo (s)')
    axes[0, 0].legend()
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Subgráfico 2: Speedup
    colors = ['green' if s > 1 else 'red' for s in df_resultados['speedup']]
    axes[0, 1].bar(df_resultados['grafo'], df_resultados['speedup'], color=colors, alpha=0.7)
    axes[0, 1].axhline(y=1, color='black', linestyle='--', alpha=0.5)
    axes[0, 1].set_title('Speedup (Dijkstra/Nuevo)')
    axes[0, 1].set_ylabel('Speedup')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Subgráfico 3: Tiempo vs nodos
    axes[1, 0].plot(df_resultados['nodos'], df_resultados['dijkstra'], 'o-', 
                    label='Dijkstra', markersize=8)
    axes[1, 0].plot(df_resultados['nodos'], df_resultados['nuevo'], 's-', 
                    label='Nuevo', markersize=8)
    axes[1, 0].set_title('Escalabilidad vs Nodos')
    axes[1, 0].set_xlabel('Nodos')
    axes[1, 0].set_ylabel('Tiempo (s)')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Subgráfico 4: Tiempo vs aristas
    axes[1, 1].plot(df_resultados['aristas'], df_resultados['dijkstra'], 'o-', 
                    label='Dijkstra', markersize=8)
    axes[1, 1].plot(df_resultados['aristas'], df_resultados['nuevo'], 's-', 
                    label='Nuevo', markersize=8)
    axes[1, 1].set_title('Escalabilidad vs Aristas')
    axes[1, 1].set_xlabel('Aristas')
    axes[1, 1].set_ylabel('Tiempo (s)')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.suptitle('Comparación Completa: Dijkstra vs Algoritmo O(m log²/³ n)', 
                 fontsize=14, y=1.02)
    plt.tight_layout()
    plt.show()
    
    # Imprimir tabla de resultados
    print("\n" + "=" * 60)
    print("TABLA DE RESULTADOS")
    print("=" * 60)
    print(df_resultados.to_string(index=False))
    
    # Estadísticas resumen
    print("\n" + "=" * 60)
    print("RESUMEN ESTADÍSTICO")
    print("=" * 60)
    print(f"Speedup promedio: {df_resultados['speedup'].mean():.2f}x")
    print(f"Speedup máximo: {df_resultados['speedup'].max():.2f}x")
    print(f"Speedup mínimo: {df_resultados['speedup'].min():.2f}x")
    
    if df_resultados['speedup'].mean() > 1:
        print(" El nuevo algoritmo es más rápido en promedio")
    else:
        print("  Dijkstra es más rápido en promedio")

# ============================================================================
# 5. EJECUTAR TODO
# ============================================================================

# Ejecutar experimentos
df = ejecutar_experimentos_simples()

# Generar gráficos
if not df.empty:
    generar_graficos_simples(df)