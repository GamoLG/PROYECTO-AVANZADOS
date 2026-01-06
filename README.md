# PROYECTO-AVANZADOS
Proyecto del curso de Algoritmos Avanzados
# Comparación de Algoritmos de Camino Más Corto

## 📋 Descripción

Este proyecto implementa y compara el rendimiento de dos algoritmos para encontrar el camino más corto en grafos:

1. **Algoritmo de Dijkstra Original** - Implementación clásica con complejidad O(m log n)
2. **Algoritmo Mejorado** - Implementación optimizada con complejidad O(m log²/³ n)

El objetivo es analizar y visualizar las diferencias de rendimiento entre ambos algoritmos en diferentes tipos de grafos.

## 🎯 Características

- Implementación completa del algoritmo de Dijkstra original
- Implementación del algoritmo mejorado con complejidad O(m log²/³ n)
- Generación de grafos de prueba (densos, dispersos, aleatorios, caminos, etc.)
- Comparación exhaustiva de tiempos de ejecución
- Visualizaciones detalladas con matplotlib
- Análisis de escalabilidad
- Verificación de correctitud de los resultados

## 📦 Requisitos

```python
heapq
time
random
matplotlib
pandas
collections
```

## 🚀 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/comparacion-algoritmos.git
cd comparacion-algoritmos
```

2. Instala las dependencias:
```bash
pip install matplotlib pandas
```

## 💻 Uso

### Ejecución en Jupyter Notebook

Abre el archivo `GRUPO1_AVANZADOS_LUICHOQUISPE_COMPARACIONDEALGORITMOS_CODIGO.ipynb` en Jupyter Notebook o Google Colab y ejecuta las celdas secuencialmente.

### Estructura del Notebook

El notebook está organizado en las siguientes secciones:

1. **CÓDIGO 1: Algoritmo de Dijkstra Original**
   - Implementación clásica
   - Función de reconstrucción de caminos
   - Prueba con grafo de ejemplo

2. **CÓDIGO 2: Algoritmo Mejorado O(m log²/³ n)**
   - Implementación optimizada
   - Estructura de datos avanzada
   - Comparación con Dijkstra

3. **CÓDIGO 3: Generador de Grafos de Prueba**
   - Grafos densos
   - Grafos dispersos
   - Grafos aleatorios
   - Grafos en cadena
   - Grafos completos
   - Grafos bipartitos

4. **CÓDIGO 4: Experimentos y Comparación**
   - Ejecución de pruebas
   - Medición de tiempos
   - Generación de visualizaciones

## 📊 Visualizaciones

El proyecto genera múltiples gráficos para analizar el rendimiento:

1. **Comparación de Tiempos**: Gráfico de barras mostrando tiempos de ejecución
2. **Speedup**: Visualización del factor de mejora del algoritmo nuevo
3. **Escalabilidad vs Nodos**: Análisis del crecimiento del tiempo según el tamaño
4. **Escalabilidad vs Aristas**: Relación entre densidad y rendimiento
5. **Resumen Completo**: Dashboard con todas las métricas

## 📈 Resultados Esperados

El análisis compara ambos algoritmos en términos de:

- **Tiempo de ejecución**: Medido en segundos
- **Speedup**: Factor de mejora (Tiempo Dijkstra / Tiempo Nuevo)
- **Escalabilidad**: Comportamiento con grafos de diferentes tamaños
- **Correctitud**: Verificación de que ambos algoritmos producen los mismos resultados

## 🔬 Complejidad Teórica

| Algoritmo | Complejidad Temporal | Estructura de Datos |
|-----------|---------------------|---------------------|
| Dijkstra Original | O(m log n) | Min-Heap binario |
| Algoritmo Mejorado | O(m log²/³ n) | Estructura optimizada |

Donde:
- `n` = número de nodos
- `m` = número de aristas

## 📝 Ejemplo de Uso

```python
# Definir un grafo
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

# Ejecutar Dijkstra
distancias, predecesores = dijkstra_original(grafo, 'A')

# Ejecutar algoritmo mejorado
distancias_nuevo, predecesores_nuevo = algoritmo_nuevo(grafo, 'A')
```

## 👥 Autores

**Grupo 1 - Algoritmos Avanzados**
- RICHARD BRAULIO PUMA CONDORI

- JHOEL ALEX LUICHO QUISPE

- ABELARDO TITO QUISPE

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

**Nota**: Este proyecto fue desarrollado como parte del curso de Algoritmos Avanzados.
