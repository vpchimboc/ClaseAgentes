# 🚀 Guía Rápida: Agentes Inteligentes y Resolución de Problemas

## Inicio Rápido

### Opción 1: Ejecutar el script (Recomendado)
```bash
cd /home/ubuntu
./run.sh
```

### Opción 2: Comando directo
```bash
cd /home/ubuntu
streamlit run app.py
```

## Navegación de la Presentación

### 📚 Menú Principal
El menú lateral te permite seleccionar entre 8 secciones:

1. **🏠 Inicio** - Introducción y objetivos de aprendizaje
2. **🤖 Agentes Inteligentes y Entornos** - Conceptos fundamentales
3. **🏗️ Tipos de Agentes y Arquitecturas** - Clasificación de agentes
4. **🎯 Modelos de Toma de Decisiones** - Cómo deciden los agentes
5. **🔍 Problemas y Espacios de Búsqueda** - Formalización de problemas
6. **⚙️ Algoritmos de Búsqueda No Informada** - BFS, DFS, UCS, IDDFS
7. **💻 Ejemplo Resuelto: Agente Aspiradora** - Simulación interactiva
8. **🎓 Ejercicio Práctico: Búsqueda de Rutas** - Ejercicio en clase

## Ejercicios Interactivos

### Ejercicio 1: Agente Aspiradora
**Objetivo**: Entender cómo un agente simple puede resolver un problema.

**Pasos**:
1. Ve a la sección "💻 Ejemplo Resuelto: Agente Aspiradora"
2. Selecciona el estado inicial de las ubicaciones A y B
3. Haz clic en "▶️ Ejecutar Simulación"
4. Observa cómo el agente limpia el entorno

**Preguntas para reflexionar**:
- ¿Cuántos pasos tardó el agente en limpiar todo?
- ¿Qué hubiera pasado si el agente tuviera memoria?
- ¿Cómo cambiaría el algoritmo si hubiera 3 ubicaciones?

### Ejercicio 2: Búsqueda de Rutas
**Objetivo**: Comparar diferentes algoritmos de búsqueda.

**Pasos**:
1. Ve a la sección "🎓 Ejercicio Práctico: Búsqueda de Rutas"
2. Selecciona una ciudad de origen (ej: Arad)
3. Selecciona una ciudad de destino (ej: Bucharest)
4. Elige los algoritmos a comparar (BFS, DFS, UCS, IDDFS)
5. Haz clic en "🔍 Buscar Ruta"
6. Analiza los resultados

**Preguntas para reflexionar**:
- ¿Qué algoritmo encontró la ruta más corta?
- ¿Cuál fue el más eficiente (menos nodos expandidos)?
- ¿Por qué algunos algoritmos expandieron más nodos?
- ¿Cuál es la diferencia entre "pasos" y "costo"?

## Conceptos Clave

### Agentes Inteligentes
Un agente es un sistema que:
- **Percibe** su entorno (sensores)
- **Procesa** la información
- **Actúa** sobre el entorno (actuadores)

### Tipos de Entornos (PEAS)
- **P**erformance: Medida de éxito
- **E**nvironment: El mundo del agente
- **A**ctuators: Cómo actúa el agente
- **S**ensors: Cómo percibe el agente

### Algoritmos de Búsqueda

| Algoritmo | Completo | Óptimo | Memoria | Uso |
| :--- | :--- | :--- | :--- | :--- |
| **BFS** | ✓ | ✓ | Alta | Espacios pequeños |
| **DFS** | ✗ | ✗ | Baja | Espacios profundos |
| **UCS** | ✓ | ✓ | Alta | Costos variables |
| **IDDFS** | ✓ | ✓ | Baja | Espacios grandes |

## Tareas Sugeridas en Clase

### Tarea 1: Modificar el Agente Aspiradora
Modifica `agente_aspiradora.py` para:
- Agregar una tercera ubicación (C)
- Cambiar las reglas de decisión
- Agregar un costo a cada acción

### Tarea 2: Crear un Nuevo Problema
Usa `algoritmos_busqueda.py` para:
- Crear un grafo de ciudades de tu país
- Comparar algoritmos en ese grafo
- Analizar qué algoritmo es mejor para tu caso

### Tarea 3: Implementar un Nuevo Algoritmo
Implementa un nuevo algoritmo de búsqueda:
- Búsqueda de profundidad limitada (DLS)
- Búsqueda de costo uniforme mejorada
- Tu propio algoritmo

## Preguntas Frecuentes

**P: ¿Cuál es la diferencia entre BFS y IDDFS?**
R: BFS usa mucha memoria, IDDFS usa poca. Ambos encuentran la solución óptima.

**P: ¿Por qué DFS no siempre encuentra la solución?**
R: DFS puede quedar atrapado en ciclos o caminos muy profundos.

**P: ¿Qué es el "costo de camino"?**
R: Es la suma de los costos de todas las acciones en el camino.

**P: ¿Cómo sé qué algoritmo usar?**
R: Depende del problema:
- Espacio pequeño → BFS
- Espacio profundo → DFS
- Costos variables → UCS
- Espacio grande → IDDFS

## Recursos Adicionales

### Lecturas Recomendadas
- Russell & Norvig: "Artificial Intelligence: A Modern Approach"
- Nilsson: "Artificial Intelligence: A New Synthesis"

### Videos Útiles
- Búsqueda en amplitud (BFS)
- Búsqueda en profundidad (DFS)
- Algoritmos de búsqueda comparados

### Herramientas
- Python: Para implementar algoritmos
- Streamlit: Para crear interfaces interactivas
- Graphviz: Para visualizar grafos

## Consejos para Aprender Mejor

1. **Lee primero la teoría** antes de ejecutar los ejemplos
2. **Ejecuta los ejemplos** y experimenta con diferentes parámetros
3. **Resuelve los ejercicios** en clase
4. **Modifica el código** para entender mejor cómo funciona
5. **Compara resultados** entre diferentes algoritmos
6. **Discute con compañeros** tus hallazgos

## Errores Comunes

❌ **Error**: Pensar que BFS siempre es mejor que DFS
✓ **Corrección**: Cada algoritmo tiene ventajas y desventajas

❌ **Error**: Confundir "pasos" con "costo"
✓ **Corrección**: Pasos = número de acciones, Costo = suma de distancias

❌ **Error**: Pensar que un algoritmo óptimo siempre es mejor
✓ **Corrección**: Óptimo = mejor solución, pero puede ser lento

## Próximos Pasos

Después de completar esta presentación, puedes:
1. Aprender algoritmos de búsqueda **informada** (A*, búsqueda heurística)
2. Estudiar **aprendizaje automático** (machine learning)
3. Explorar **redes neuronales** y deep learning
4. Implementar **sistemas multiagente**

---

**¡Buena suerte en tu aprendizaje! 🚀**
