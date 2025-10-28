# AGENTES INTELIGENTES Y RESOLUCIÓN DE PROBLEMAS

## 2.1. Agentes inteligentes y entornos

### Conceptos Fundamentales
*   **Agente Inteligente (AI):** Un sistema que percibe su entorno a través de sensores y actúa sobre ese entorno a través de actuadores.
*   **Función del Agente:** La función que mapea una secuencia de percepciones a una acción. $f: P^* \to A$.
*   **Programa del Agente:** La implementación concreta de la función del agente.
*   **Entorno:** El mundo exterior con el que interactúa el agente.

### Propiedades de los Entornos (PEAS)
*   **P**erformance (Medida de rendimiento)
*   **E**nvironment (Entorno)
*   **A**ctuators (Actuadores)
*   **S**ensors (Sensores)

### Tipos de Entornos (Clasificación)
| Propiedad | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **Totalmente vs. Parcialmente Observable** | ¿Los sensores del agente pueden acceder al estado completo del entorno? | Ajedrez (Totalmente) vs. Conducción (Parcialmente) |
| **Determinista vs. Estocástico** | ¿El estado siguiente del entorno está completamente determinado por el estado actual y la acción del agente? | Ajedrez (Determinista) vs. Conducción (Estocástico) |
| **Episódico vs. Secuencial** | ¿La experiencia del agente se divide en episodios atómicos (cada episodio no afecta al siguiente)? | Clasificación de piezas (Episódico) vs. Ajedrez (Secuencial) |
| **Estático vs. Dinámico** | ¿El entorno puede cambiar mientras el agente está pensando? | Crucigrama (Estático) vs. Conducción (Dinámico) |
| **Discreto vs. Continuo** | ¿El número de estados, percepciones y acciones es finito o infinito? | Ajedrez (Discreto) vs. Conducción (Continuo) |
| **Un solo agente vs. Multiagente** | ¿Hay otros agentes en el entorno? | Solitario (Un solo agente) vs. Ajedrez (Multiagente) |

---

## 2.2. Tipos de agentes y arquitecturas

### Tipos de Agentes
1.  **Agente de Reflejo Simple:** Actúa basado únicamente en la percepción actual, ignorando el historial de percepciones. (Condición-Acción)
2.  **Agente de Reflejo Basado en Modelo:** Mantiene un estado interno (modelo) que le ayuda a rastrear partes del mundo que no son observables.
3.  **Agente Basado en Objetivos:** Utiliza el conocimiento de un objetivo (meta) para decidir qué acciones tomar.
4.  **Agente Basado en Utilidad:** Utiliza una función de utilidad para medir qué tan deseable es un estado, buscando la acción que maximice la utilidad esperada.
5.  **Agente de Aprendizaje:** Capaz de aprender de su experiencia, mejorando su rendimiento con el tiempo.

### Arquitecturas
*   **Arquitectura de Agente:** La forma en que se conectan los componentes del agente (sensores, actuadores, programa del agente).
*   **Componentes Clave:** Sensores, Actuadores, Módulo de Percepción, Módulo de Decisión, Base de Conocimiento.

---

## 2.3. Modelos de toma de decisiones en agentes inteligentes

### Modelos Clave
*   **Lógica y Razonamiento:** Uso de lógica formal (proposicional o de primer orden) para inferir conclusiones y tomar decisiones.
*   **Modelos Basados en Utilidad/Teoría de la Decisión:** El agente elige la acción que maximiza la utilidad esperada. Fundamental en entornos estocásticos.
*   **Modelo BDI (Beliefs, Desires, Intentions):** Un modelo popular que utiliza:
    *   **Creencias (Beliefs):** Lo que el agente cree que es verdad sobre el entorno.
    *   **Deseos (Desires):** Los estados que el agente quiere alcanzar (posibles objetivos).
    *   **Intenciones (Intentions):** Los deseos que el agente se ha comprometido a perseguir.

---

## 2.4. Problemas y espacios de búsqueda

### Definición de Problema
Un problema se define formalmente mediante cuatro componentes:
1.  **Estado Inicial:** El estado en el que comienza el agente.
2.  **Acciones (Función de Transición):** Una descripción de las acciones disponibles para el agente y el estado resultante de cada acción.
3.  **Test de Objetivo:** La condición que determina si un estado es un estado objetivo.
4.  **Función de Costo del Camino:** Asigna un costo numérico a cada camino (secuencia de acciones).

### Espacio de Búsqueda
*   **Espacio de Estados:** El conjunto de todos los estados alcanzables desde el estado inicial.
*   **Árbol de Búsqueda:** Una estructura de datos que representa el proceso de búsqueda, donde los nodos son estados y las ramas son acciones.

---

## 2.5. Algoritmos de búsqueda no informada

Los algoritmos de búsqueda no informada (o "ciega") solo utilizan la información de la definición del problema (estado inicial, acciones, test de objetivo), sin conocimiento adicional sobre la distancia o el costo restante para alcanzar el objetivo.

### Algoritmos Principales
1.  **Búsqueda en Amplitud (Breadth-First Search - BFS):**
    *   Expande el nodo menos profundo en el árbol de búsqueda.
    *   Garantiza encontrar la solución más corta (óptima) si el costo de cada paso es uniforme.
    *   **Estructura de datos:** Cola (FIFO).
2.  **Búsqueda en Costo Uniforme (Uniform-Cost Search - UCS):**
    *   Expande el nodo con el costo de camino más bajo ($g(n)$).
    *   Garantiza encontrar la solución de menor costo.
    *   **Estructura de datos:** Cola de prioridad.
3.  **Búsqueda en Profundidad (Depth-First Search - DFS):**
    *   Expande el nodo más profundo en la frontera de búsqueda.
    *   No garantiza la optimalidad ni la completitud (puede quedar atrapado en un camino infinito).
    *   **Estructura de datos:** Pila (LIFO).
4.  **Búsqueda en Profundidad Limitada (Depth-Limited Search - DLS):**
    *   DFS con un límite de profundidad predefinido ($l$).
5.  **Búsqueda en Profundidad Iterativa (Iterative Deepening Depth-First Search - IDDFS):**
    *   Realiza DLS con límites de profundidad crecientes ($l=0, 1, 2, \dots$).
    *   Combina la completitud y optimalidad de BFS con la eficiencia de espacio de DFS.

---

# Ejemplos Resueltos y Casos Prácticos (Python/Streamlit)

## Ejemplo Resuelto: Agente de Reflejo Simple (Aspiradora)

### Descripción
Un agente aspiradora opera en un entorno de dos estados (A y B), donde cada estado puede estar Limpio (L) o Sucio (S). El agente solo percibe su ubicación y si la celda está sucia.

### Programa del Agente (Reglas Condición-Acción)
| Percepción (Ubicación, Suciedad) | Acción |
| :--- | :--- |
| (A, Sucio) | Aspirar |
| (B, Sucio) | Aspirar |
| (A, Limpio) | Mover a B |
| (B, Limpio) | Mover a A |
| (A, Limpio) y (B, Limpio) | Detenerse |

### Implementación en Python (Pendiente de codificación)
*   Se creará una clase `AgenteAspiradora` y una función `simular_entorno`.

## Caso Práctico (Ejercicio para Clase): Búsqueda en Amplitud (BFS)

### Problema: El Problema del Viajero (Rutas Aéreas Simplificadas)
*   **Objetivo:** Encontrar la ruta más corta (mínimo número de escalas) entre dos ciudades en un mapa simplificado.
*   **Espacio de Estados:** Ciudades (nodos).
*   **Acciones:** Vuelos directos (aristas).
*   **Ejercicio:** Implementar BFS para encontrar el camino de la ciudad 'Origen' a la ciudad 'Destino' en un grafo dado.

### Estructura de la Solución (Pendiente de codificación en Streamlit)
*   Un script `app_bfs.py` que:
    1.  Define el grafo de ciudades.
    2.  Implementa la función `bfs`.
    3.  Usa `streamlit` para permitir al usuario ingresar el Origen y Destino y visualizar el resultado.

---

## Estructura de Archivos (Para la siguiente fase)
*   `app.py`: El archivo principal de Streamlit que contendrá el contenido teórico (`presentacion_agentes_ia.md`) y enlazará a los ejemplos.
*   `agente_aspiradora.py`: Implementación del ejemplo resuelto.
*   `ejercicio_viajero.py`: Implementación del ejercicio práctico de BFS.
*   `requirements.txt`: Para instalar `streamlit`.
