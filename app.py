"""
Institto Tecnológico Superior del Azuay con Condición de Universitario
Asignatura: Inteligencia Artificial
Unidad 2: Agentes Inteligentes y Resolución de Problemas
Mgtr. Verónica Chimbo

"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Agregar directorio actual al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent))

from agente_aspiradora import (
    AgenteAspiradora, Ubicacion, Estado, Accion, simular_entorno, obtener_descripcion_accion
)
from algoritmos_busqueda import (
    ProblemaDeRuta, busqueda_amplitud, busqueda_profundidad,
    busqueda_costo_uniforme, busqueda_profundidad_iterativa
)

# Configuración de la página
st.set_page_config(
    page_title="Agentes Inteligentes y Resolución de Problemas",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .section-title {
        color: #2ca02c;
        border-bottom: 2px solid #2ca02c;
        padding-bottom: 10px;
    }
    .example-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
    }
    .exercise-box {
        background-color: #fff8dc;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #ff7f0e;
    }
    </style>
""", unsafe_allow_html=True)

# Navegación principal
st.sidebar.title("📚 Contenido")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "🏠 Inicio",
        "🤖 Agentes Inteligentes y Entornos",
        "🏗️ Tipos de Agentes y Arquitecturas",
        "🎯 Modelos de Toma de Decisiones",
        "🔍 Problemas y Espacios de Búsqueda",
        "⚙️ Algoritmos de Búsqueda No Informada",
        "💻 Ejemplo Resuelto: Agente Aspiradora",
        "🎓 Ejercicio Práctico: Búsqueda de Rutas"
    ]
)

# ============================================================================
# SECCIÓN: INICIO
# ============================================================================
if seccion == "🏠 Inicio":
    st.markdown("""
    <h1 class="main-title">🤖 Agentes Inteligentes y Resolución de Problemas</h1>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Bienvenido a la Presentación Interactiva
        
        Esta presentación está diseñada para estudiantes universitarios que desean comprender
        los conceptos fundamentales de **Agentes Inteligentes** y **Resolución de Problemas**
        en el campo de la Inteligencia Artificial.
        
        ### Contenido de la Presentación
        
        La presentación cubre los siguientes temas:
        
        1. **Agentes Inteligentes y Entornos** - Conceptos básicos, propiedades PEAS y tipos de entornos
        2. **Tipos de Agentes y Arquitecturas** - Diferentes tipos de agentes y cómo se estructuran
        3. **Modelos de Toma de Decisiones** - Cómo los agentes toman decisiones
        4. **Problemas y Espacios de Búsqueda** - Formalización de problemas y espacios de estados
        5. **Algoritmos de Búsqueda No Informada** - BFS, DFS, UCS, IDDFS
        
        ### Características Especiales
        
        - 📖 **Explicaciones Teóricas**: Conceptos fundamentales explicados de manera clara
        - 💡 **Ejemplos Resueltos**: Implementaciones prácticas de conceptos teóricos
        - 🎯 **Ejercicios Interactivos**: Casos prácticos para resolver en clase
        - 🐍 **Código Python**: Implementaciones completas y ejecutables
        """)
    
    with col2:
        st.info("""
        ### 🎯 Objetivos de Aprendizaje
        
        Al completar esta presentación, podrás:
        
        ✓ Entender qué es un agente inteligente
        ✓ Clasificar entornos según sus propiedades
        ✓ Identificar tipos de agentes
        ✓ Formalizar problemas de búsqueda
        ✓ Implementar algoritmos de búsqueda
        ✓ Resolver problemas reales con IA
        """)
    
    st.divider()
    
    st.markdown("""
    ### 📖 Cómo Usar Esta Presentación
    
    1. **Navega por las secciones** usando el menú lateral
    2. **Lee las explicaciones teóricas** en cada sección
    3. **Ejecuta los ejemplos resueltos** para ver cómo funcionan
    4. **Resuelve los ejercicios prácticos** en clase
    5. **Experimenta con los parámetros** para entender mejor los conceptos
    
    ¡Comencemos! Selecciona una sección del menú lateral para empezar.
    """)

# ============================================================================
# SECCIÓN: AGENTES INTELIGENTES Y ENTORNOS
# ============================================================================
elif seccion == "🤖 Agentes Inteligentes y Entornos":
    st.markdown("""
    <h2 class="section-title">🤖 Agentes Inteligentes y Entornos</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 2.1.1 Conceptos Fundamentales
    
    Un **agente inteligente** es un sistema que:
    - Percibe su entorno a través de sensores
    - Procesa esa información
    - Actúa sobre el entorno a través de actuadores
    
    La función del agente mapea una secuencia de percepciones a una acción: **f: P* → A**
    
    #### Componentes Clave
    
    | Componente | Descripción |
    | :--- | :--- |
    | **Sensores** | Dispositivos que permiten al agente percibir el entorno |
    | **Actuadores** | Dispositivos que permiten al agente actuar sobre el entorno |
    | **Función del Agente** | Mapea percepciones a acciones |
    | **Programa del Agente** | Implementación concreta de la función del agente |
    
    ### 2.1.2 Propiedades PEAS
    
    Para describir un entorno, utilizamos el marco PEAS:
    
    - **P**erformance (Medida de rendimiento)
    - **E**nvironment (Entorno)
    - **A**ctuators (Actuadores)
    - **S**ensors (Sensores)
    
    #### Ejemplo: Agente Taxi Autónomo
    
    | Componente | Descripción |
    | :--- | :--- |
    | **Performance** | Pasajeros seguros, destino rápido, combustible económico |
    | **Environment** | Carreteras, tráfico, peatones, otros vehículos |
    | **Actuators** | Volante, acelerador, frenos, cambios |
    | **Sensors** | Cámara, radar, GPS, velocímetro, sensores de proximidad |
    """)
    
    st.divider()
    
    st.markdown("""
    ### 2.1.3 Tipos de Entornos
    
    Los entornos se clasifican según varias dimensiones:
    """)
    
    # Tabla interactiva de tipos de entornos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Observabilidad
        - **Totalmente Observable**: Los sensores acceden al estado completo
        - **Parcialmente Observable**: Los sensores solo ven parte del estado
        
        #### Determinismo
        - **Determinista**: El siguiente estado está completamente determinado
        - **Estocástico**: Hay incertidumbre en el siguiente estado
        """)
    
    with col2:
        st.markdown("""
        #### Episódico vs. Secuencial
        - **Episódico**: Cada episodio es independiente
        - **Secuencial**: Las acciones afectan estados futuros
        
        #### Estático vs. Dinámico
        - **Estático**: El entorno no cambia mientras el agente piensa
        - **Dinámico**: El entorno puede cambiar
        """)
    
    st.divider()
    
    st.markdown("""
    ### Matriz de Clasificación de Entornos
    """)
    
    clasificacion = {
        "Entorno": ["Ajedrez", "Conducción", "Crucigrama", "Diagnóstico Médico"],
        "Observable": ["Total", "Parcial", "Total", "Parcial"],
        "Determinista": ["Sí", "No", "Sí", "No"],
        "Episódico": ["No", "No", "Sí", "Sí"],
        "Estático": ["Sí", "No", "Sí", "Sí"],
        "Discreto": ["Sí", "No", "Sí", "Sí"]
    }
    

    df = pd.DataFrame(clasificacion)
    st.dataframe(df, use_container_width=True)

# ============================================================================
# SECCIÓN: TIPOS DE AGENTES Y ARQUITECTURAS
# ============================================================================
elif seccion == "🏗️ Tipos de Agentes y Arquitecturas":
    st.markdown("""
    <h2 class="section-title">🏗️ Tipos de Agentes y Arquitecturas</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 2.2.1 Tipos de Agentes
    
    Existen varios tipos de agentes, clasificados por su complejidad y capacidades:
    """)
    
    # Tabs para cada tipo de agente
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Reflejo Simple",
        "Reflejo + Modelo",
        "Basado en Objetivos",
        "Basado en Utilidad",
        "Aprendizaje"
    ])
    
    with tab1:
        st.markdown("""
        #### Agente de Reflejo Simple
        
        **Descripción**: Actúa basado únicamente en la percepción actual, sin memoria.
        
        **Características**:
        - Usa reglas condición-acción
        - No mantiene estado interno
        - Muy eficiente pero limitado
        
        **Pseudocódigo**:
        ```
        función AgenteReflejo(percepción):
            estado ← InterpretarEntrada(percepción)
            regla ← SeleccionarRegla(estado)
            acción ← ReglaAcción(regla)
            retornar acción
        ```
        
        **Ejemplo**: Agente aspiradora simple, termostato
        """)
    
    with tab2:
        st.markdown("""
        #### Agente de Reflejo Basado en Modelo
        
        **Descripción**: Mantiene un estado interno (modelo) del mundo.
        
        **Características**:
        - Mantiene un modelo del entorno
        - Actualiza el estado con cada percepción
        - Puede manejar entornos parcialmente observables
        
        **Pseudocódigo**:
        ```
        función AgenteReflejo(percepción):
            estado ← ActualizarEstado(estado, acción, percepción)
            regla ← SeleccionarRegla(estado)
            acción ← ReglaAcción(regla)
            retornar acción
        ```
        
        **Ejemplo**: Robot de navegación, agente de conducción
        """)
    
    with tab3:
        st.markdown("""
        #### Agente Basado en Objetivos
        
        **Descripción**: Utiliza un objetivo (meta) para decidir qué hacer.
        
        **Características**:
        - Tiene un objetivo explícito
        - Busca secuencias de acciones que alcanzan el objetivo
        - Más flexible que los agentes de reflejo
        
        **Pseudocódigo**:
        ```
        función AgenteBasadoEnObjetivos(percepción):
            estado ← ActualizarEstado(estado, acción, percepción)
            objetivo ← ObtenerObjetivo()
            acción ← BuscarAcción(estado, objetivo)
            retornar acción
        ```
        
        **Ejemplo**: Agente de planificación, robot de tareas
        """)
    
    with tab4:
        st.markdown("""
        #### Agente Basado en Utilidad
        
        **Descripción**: Maximiza una función de utilidad que mide qué tan deseable es un estado.
        
        **Características**:
        - Usa una función de utilidad
        - Elige acciones que maximizan la utilidad esperada
        - Maneja preferencias y trade-offs
        
        **Pseudocódigo**:
        ```
        función AgenteBasadoEnUtilidad(percepción):
            estado ← ActualizarEstado(estado, acción, percepción)
            acción ← ArgMax(acciones, Utilidad(estado))
            retornar acción
        ```
        
        **Ejemplo**: Agente de trading, sistema de recomendación
        """)
    
    with tab5:
        st.markdown("""
        #### Agente de Aprendizaje
        
        **Descripción**: Capaz de aprender de su experiencia y mejorar su rendimiento.
        
        **Características**:
        - Aprende de la experiencia
        - Mejora su rendimiento con el tiempo
        - Puede adaptarse a entornos cambiantes
        
        **Componentes**:
        1. **Elemento de Aprendizaje**: Mejora el agente
        2. **Crítico**: Proporciona retroalimentación
        3. **Generador de Problemas**: Sugiere acciones exploratorias
        4. **Elemento de Ejecución**: El agente actual
        
        **Ejemplo**: Agente de aprendizaje por refuerzo, red neuronal
        """)

# ============================================================================
# SECCIÓN: MODELOS DE TOMA DE DECISIONES
# ============================================================================
elif seccion == "🎯 Modelos de Toma de Decisiones":
    st.markdown("""
    <h2 class="section-title">🎯 Modelos de Toma de Decisiones en Agentes Inteligentes</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 2.3.1 Modelos Principales
    
    Los agentes inteligentes utilizan diferentes modelos para tomar decisiones:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Lógica y Razonamiento
        
        **Descripción**: Uso de lógica formal para inferir conclusiones.
        
        **Ventajas**:
        - Razonamiento transparente
        - Fácil de verificar
        
        **Desventajas**:
        - Requiere conocimiento completo
        - Lento en entornos grandes
        
        **Ejemplo**:
        ```
        Si lluvia → llevar paraguas
        Si frío → abrigarse
        ```
        """)
    
    with col2:
        st.markdown("""
        #### Teoría de la Decisión
        
        **Descripción**: Elige acciones que maximizan la utilidad esperada.
        
        **Fórmula**:
        ```
        Acción Óptima = ArgMax(a) E[Utilidad(a)]
        ```
        
        **Ventajas**:
        - Maneja incertidumbre
        - Maneja preferencias
        
        **Desventajas**:
        - Requiere probabilidades
        - Computacionalmente costoso
        """)
    
    st.divider()
    
    st.markdown("""
    ### 2.3.2 Modelo BDI (Beliefs, Desires, Intentions)
    
    Un modelo popular que utiliza tres componentes:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        ### 🧠 Creencias (Beliefs)
        
        Lo que el agente cree que es verdad sobre el entorno.
        
        **Ejemplo**:
        - "Llueve"
        - "Estoy en casa"
        - "Tengo dinero"
        """)
    
    with col2:
        st.info("""
        ### 🎯 Deseos (Desires)
        
        Los estados que el agente quiere alcanzar.
        
        **Ejemplo**:
        - "Quiero estar seco"
        - "Quiero ir al trabajo"
        - "Quiero comprar comida"
        """)
    
    with col3:
        st.info("""
        ### 💪 Intenciones (Intentions)
        
        Los deseos que el agente se ha comprometido a perseguir.
        
        **Ejemplo**:
        - "Voy a llevar paraguas"
        - "Voy a tomar el autobús"
        - "Voy a ir al supermercado"
        """)
    
    st.divider()
    
    st.markdown("""
    ### Ciclo de Decisión BDI
    
    ```
    1. Percibir el entorno
    2. Actualizar creencias
    3. Generar deseos (opciones)
    4. Filtrar deseos (intenciones)
    5. Seleccionar acciones
    6. Ejecutar acciones
    7. Repetir
    ```
    """)

# ============================================================================
# SECCIÓN: PROBLEMAS Y ESPACIOS DE BÚSQUEDA
# ============================================================================
elif seccion == "🔍 Problemas y Espacios de Búsqueda":
    st.markdown("""
    <h2 class="section-title">🔍 Problemas y Espacios de Búsqueda</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 2.4.1 Definición Formal de un Problema
    
    Un problema se define mediante cuatro componentes:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 1. Estado Inicial
        
        El estado en el que comienza el agente.
        
        **Ejemplo**: En el problema del puzzle 8, el estado inicial es la configuración inicial de las fichas.
        """)
    
    with col2:
        st.markdown("""
        #### 2. Función de Transición (Acciones)
        
        Describe las acciones disponibles y el estado resultante.
        
        **Ejemplo**: En ajedrez, las acciones son movimientos legales.
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 3. Test de Objetivo
        
        La condición que determina si un estado es un objetivo.
        
        **Ejemplo**: En el puzzle 8, el objetivo es que las fichas estén en orden.
        """)
    
    with col2:
        st.markdown("""
        #### 4. Función de Costo
        
        Asigna un costo numérico a cada acción o camino.
        
        **Ejemplo**: En navegación, el costo es la distancia recorrida.
        """)
    
    st.divider()
    
    st.markdown("""
    ### 2.4.2 Espacio de Estados
    
    El **espacio de estados** es el conjunto de todos los estados alcanzables desde el estado inicial.
    
    **Tamaño del espacio**:
    - Puzzle 8: 9! / 2 ≈ 181,000 estados
    - Ajedrez: ≈ 10^43 estados
    - Mundo real: Infinito o muy grande
    
    ### 2.4.3 Árbol de Búsqueda
    
    Una estructura de datos que representa el proceso de búsqueda:
    - **Nodos**: Representan estados
    - **Ramas**: Representan acciones
    - **Raíz**: El estado inicial
    - **Hojas**: Estados sin sucesores expandidos
    
    **Diferencia importante**: El árbol de búsqueda puede ser mucho más grande que el espacio de estados,
    ya que el mismo estado puede alcanzarse por diferentes caminos.
    """)
    
    st.info("""
    **Ejemplo**: En el juego de 8 reinas, el espacio de estados tiene 8^8 = 16,777,216 estados,
    pero el árbol de búsqueda puede ser mucho más grande si no evitamos estados repetidos.
    """)

# ============================================================================
# SECCIÓN: ALGORITMOS DE BÚSQUEDA NO INFORMADA
# ============================================================================
elif seccion == "⚙️ Algoritmos de Búsqueda No Informada":
    st.markdown("""
    <h2 class="section-title">⚙️ Algoritmos de Búsqueda No Informada</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Los algoritmos de búsqueda no informada (o "ciega") solo utilizan la información de la definición
    del problema, sin conocimiento adicional sobre la distancia o el costo restante para alcanzar el objetivo.
    """)
    
    # Tabs para cada algoritmo
    tab1, tab2, tab3, tab4 = st.tabs(["BFS", "DFS", "UCS", "IDDFS"])
    
    with tab1:
        st.markdown("""
        #### Búsqueda en Amplitud (BFS - Breadth-First Search)
        
        **Estrategia**: Expande el nodo menos profundo en la frontera de búsqueda.
        
        **Estructura de datos**: Cola (FIFO - First In, First Out)
        
        **Pseudocódigo**:
        ```
        función BFS(problema):
            frontera ← Cola([NodoRaíz(problema.estadoInicial)])
            explorados ← conjunto vacío
            
            mientras frontera no está vacía:
                nodo ← frontera.sacar()
                si nodo.estado en explorados:
                    continuar
                
                si problema.esObjetivo(nodo.estado):
                    retornar nodo
                
                explorados.agregar(nodo.estado)
                
                para cada sucesor en problema.sucesores(nodo):
                    si sucesor.estado no en explorados:
                        frontera.agregar(sucesor)
            
            retornar fallo
        ```
        
        **Propiedades**:
        | Propiedad | Valor |
        | :--- | :--- |
        | **Completo** | Sí (si existe solución) |
        | **Óptimo** | Sí (si costos uniformes) |
        | **Complejidad Temporal** | O(b^d) |
        | **Complejidad Espacial** | O(b^d) |
        
        Donde b = factor de ramificación, d = profundidad de la solución
        
        **Ventajas**:
        - Garantiza encontrar la solución más corta
        - Completo
        
        **Desventajas**:
        - Alto consumo de memoria
        - Lento en espacios grandes
        """)
    
    with tab2:
        st.markdown("""
        #### Búsqueda en Profundidad (DFS - Depth-First Search)
        
        **Estrategia**: Expande el nodo más profundo en la frontera de búsqueda.
        
        **Estructura de datos**: Pila (LIFO - Last In, First Out)
        
        **Pseudocódigo**:
        ```
        función DFS(problema):
            frontera ← Pila([NodoRaíz(problema.estadoInicial)])
            explorados ← conjunto vacío
            
            mientras frontera no está vacía:
                nodo ← frontera.sacar()
                
                si nodo.estado en explorados:
                    continuar
                
                si problema.esObjetivo(nodo.estado):
                    retornar nodo
                
                explorados.agregar(nodo.estado)
                
                para cada sucesor en problema.sucesores(nodo):
                    si sucesor.estado no en explorados:
                        frontera.agregar(sucesor)
            
            retornar fallo
        ```
        
        **Propiedades**:
        | Propiedad | Valor |
        | :--- | :--- |
        | **Completo** | No (puede quedar atrapado) |
        | **Óptimo** | No |
        | **Complejidad Temporal** | O(b^m) |
        | **Complejidad Espacial** | O(bm) |
        
        Donde b = factor de ramificación, m = profundidad máxima
        
        **Ventajas**:
        - Bajo consumo de memoria
        - Rápido en algunos casos
        
        **Desventajas**:
        - No completo
        - No óptimo
        - Puede explorar caminos muy largos
        """)
    
    with tab3:
        st.markdown("""
        #### Búsqueda de Costo Uniforme (UCS - Uniform-Cost Search)
        
        **Estrategia**: Expande el nodo con el costo de camino más bajo (g(n)).
        
        **Estructura de datos**: Cola de prioridad
        
        **Pseudocódigo**:
        ```
        función UCS(problema):
            frontera ← ColaPrioridad([NodoRaíz(problema.estadoInicial)])
            explorados ← conjunto vacío
            
            mientras frontera no está vacía:
                nodo ← frontera.sacar()
                
                si nodo.estado en explorados:
                    continuar
                
                si problema.esObjetivo(nodo.estado):
                    retornar nodo
                
                explorados.agregar(nodo.estado)
                
                para cada sucesor en problema.sucesores(nodo):
                    si sucesor.estado no en explorados:
                        frontera.agregar(sucesor)
            
            retornar fallo
        ```
        
        **Propiedades**:
        | Propiedad | Valor |
        | :--- | :--- |
        | **Completo** | Sí |
        | **Óptimo** | Sí |
        | **Complejidad Temporal** | O(b^(1+⌊C*/ε⌋)) |
        | **Complejidad Espacial** | O(b^(1+⌊C*/ε⌋)) |
        
        Donde C* = costo de la solución óptima, ε = costo mínimo de una acción
        
        **Ventajas**:
        - Garantiza encontrar la solución de menor costo
        - Óptimo
        
        **Desventajas**:
        - Alto consumo de memoria
        - Lento
        """)
    
    with tab4:
        st.markdown("""
        #### Búsqueda en Profundidad Iterativa (IDDFS - Iterative Deepening DFS)
        
        **Estrategia**: Realiza DLS con límites de profundidad crecientes (0, 1, 2, ...).
        
        **Pseudocódigo**:
        ```
        función IDDFS(problema, límiteMax):
            para profundidad = 0 hasta límiteMax:
                resultado ← DLS(problema, profundidad)
                si resultado ≠ fallo:
                    retornar resultado
            retornar fallo
        ```
        
        **Propiedades**:
        | Propiedad | Valor |
        | :--- | :--- |
        | **Completo** | Sí |
        | **Óptimo** | Sí (si costos uniformes) |
        | **Complejidad Temporal** | O(b^d) |
        | **Complejidad Espacial** | O(bd) |
        
        **Ventajas**:
        - Completo y óptimo como BFS
        - Bajo consumo de memoria como DFS
        - Mejor que BFS en la mayoría de casos
        
        **Desventajas**:
        - Repite trabajo (expande nodos múltiples veces)
        - Más lento que BFS en algunos casos
        """)
    
    st.divider()
    
    st.markdown("""
    ### Comparación de Algoritmos
    """)
    
    comparacion = {
        "Algoritmo": ["BFS", "DFS", "DLS", "UCS", "IDDFS"],
        "Completo": ["Sí", "No", "No*", "Sí", "Sí"],
        "Óptimo": ["Sí*", "No", "No", "Sí", "Sí*"],
        "Tiempo": ["O(b^d)", "O(b^m)", "O(b^l)", "O(b^(1+⌊C*/ε⌋))", "O(b^d)"],
        "Espacio": ["O(b^d)", "O(bm)", "O(bl)", "O(b^(1+⌊C*/ε⌋))", "O(bd)"]
    }
    
    df_comp = pd.DataFrame(comparacion)
    st.dataframe(df_comp, use_container_width=True)
    
    st.caption("*Sí si los costos de las acciones son uniformes")

# ============================================================================
# SECCIÓN: EJEMPLO RESUELTO - AGENTE ASPIRADORA
# ============================================================================
elif seccion == "💻 Ejemplo Resuelto: Agente Aspiradora":
    st.markdown("""
    <h2 class="section-title">💻 Ejemplo Resuelto: Agente Aspiradora</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    <h3>Descripción del Problema</h3>
    <p>Un agente aspiradora opera en un entorno de dos ubicaciones (A y B). Cada ubicación puede estar
    Limpia (L) o Sucia (S). El agente percibe su ubicación actual y si la celda está sucia, y debe
    limpiar todo el entorno.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Reglas del Agente (Condición-Acción)
    
    | Percepción | Acción |
    | :--- | :--- |
    | (A, Sucio) | Aspirar |
    | (B, Sucio) | Aspirar |
    | (A, Limpio) | Mover a B |
    | (B, Limpio) | Mover a A |
    """)
    
    st.divider()
    
    st.markdown("### Simulación Interactiva")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Configuración Inicial")
        
        # Seleccionar estado inicial
        estado_a = st.selectbox("Estado de A:", ["Limpio", "Sucio"], key="estado_a")
        estado_b = st.selectbox("Estado de B:", ["Limpio", "Sucio"], key="estado_b")
        
        # Convertir a enums
        estado_a_enum = Estado.LIMPIO if estado_a == "Limpio" else Estado.SUCIO
        estado_b_enum = Estado.LIMPIO if estado_b == "Limpio" else Estado.SUCIO
        
        entorno_inicial = {
            Ubicacion.A: estado_a_enum,
            Ubicacion.B: estado_b_enum
        }
        
        if st.button("▶️ Ejecutar Simulación", use_container_width=True):
            st.session_state.ejecutar_simulacion = True
    
    with col2:
        st.markdown("#### Estado Inicial")
        col_a, col_b = st.columns(2)
        
        with col_a:
            color_a = "🟢" if entorno_inicial[Ubicacion.A] == Estado.LIMPIO else "🔴"
            st.metric("Ubicación A", entorno_inicial[Ubicacion.A].value, delta=color_a)
        
        with col_b:
            color_b = "🟢" if entorno_inicial[Ubicacion.B] == Estado.LIMPIO else "🔴"
            st.metric("Ubicación B", entorno_inicial[Ubicacion.B].value, delta=color_b)
    
    # Ejecutar simulación
    if st.session_state.get("ejecutar_simulacion", False):
        st.divider()
        
        agente, historial_entornos, historial_acciones = simular_entorno(entorno_inicial)
        
        st.markdown("### Historial de Ejecución")
        
        # Crear tabla con historial
        historial_tabla = []
        ubicacion = Ubicacion.A
        
        for i, (percepcion, accion) in enumerate(historial_acciones, 1):
            desc_accion = obtener_descripcion_accion(accion, percepcion.ubicacion)
            
            historial_tabla.append({
                "Paso": i,
                "Ubicación": percepcion.ubicacion.value,
                "Estado": percepcion.estado.value,
                "Acción": desc_accion
            })
            
            if accion == Accion.MOVER_A:
                ubicacion = Ubicacion.B if ubicacion == Ubicacion.A else Ubicacion.A
        
        df_historial = pd.DataFrame(historial_tabla)
        st.dataframe(df_historial, use_container_width=True, hide_index=True)
        
        # Mostrar estado final
        st.markdown("### Estado Final")
        col_a, col_b = st.columns(2)
        
        with col_a:
            color_a = "🟢" if historial_entornos[-1][Ubicacion.A] == Estado.LIMPIO else "🔴"
            st.metric("Ubicación A", historial_entornos[-1][Ubicacion.A].value, delta=color_a)
        
        with col_b:
            color_b = "🟢" if historial_entornos[-1][Ubicacion.B] == Estado.LIMPIO else "🔴"
            st.metric("Ubicación B", historial_entornos[-1][Ubicacion.B].value, delta=color_b)
        
        st.success(f"✓ Simulación completada en {agente.pasos} pasos")

# ============================================================================
# SECCIÓN: EJERCICIO PRÁCTICO - BÚSQUEDA DE RUTAS
# ============================================================================
elif seccion == "🎓 Ejercicio Práctico: Búsqueda de Rutas":
    st.markdown("""
    <h2 class="section-title">🎓 Ejercicio Práctico: Búsqueda de Rutas</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="exercise-box">
    <h3>Descripción del Ejercicio</h3>
    <p>En este ejercicio, implementaremos y compararemos diferentes algoritmos de búsqueda no informada
    para encontrar la ruta más corta entre dos ciudades en un mapa de Rumania.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Definir el grafo de Rumania
    grafo_rumania = {
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Zerind': [('Oradea', 71), ('Sibiu', 99), ('Arad', 75)],
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Timisoara': [('Arad', 118), ('Lugoj', 111)],
        'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
        'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
        'Drobeta': [('Mehadia', 75)],
        'Sibiu': [('Oradea', 151), ('Zerind', 99), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
        'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138), ('Drobeta', 120)],
        'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
        'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
        'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
        'Giurgiu': [('Bucharest', 90)],
        'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
        'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
        'Eforie': [('Hirsova', 86)],
        'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
        'Iasi': [('Vaslui', 92), ('Neamt', 87)],
        'Neamt': [('Iasi', 87)]
    }
    
    st.markdown("### Mapa de Rumania (Simplificado)")
    st.info("""
    El grafo contiene 20 ciudades conectadas por carreteras. Los números en las aristas
    representan la distancia en kilómetros entre ciudades.
    """)
    
    st.markdown("### Configuración del Ejercicio")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ciudades = sorted(list(grafo_rumania.keys()))
        ciudad_origen = st.selectbox("Ciudad de Origen:", ciudades, index=ciudades.index("Arad"))
    
    with col2:
        ciudad_destino = st.selectbox("Ciudad de Destino:", ciudades, index=ciudades.index("Bucharest"))
    
    with col3:
        algoritmos = st.multiselect(
            "Algoritmos a Comparar:",
            ["BFS", "DFS", "UCS", "IDDFS"],
            default=["BFS", "UCS"]
        )
    
    if st.button("🔍 Buscar Ruta", use_container_width=True):
        if ciudad_origen == ciudad_destino:
            st.error("❌ La ciudad de origen y destino deben ser diferentes")
        else:
            problema = ProblemaDeRuta(grafo_rumania, ciudad_origen, ciudad_destino)
            
            st.divider()
            st.markdown("### Resultados de la Búsqueda")
            
            resultados = {}
            
            if "BFS" in algoritmos:
                resultados["BFS"] = busqueda_amplitud(problema)
            
            if "DFS" in algoritmos:
                resultados["DFS"] = busqueda_profundidad(problema)
            
            if "UCS" in algoritmos:
                resultados["UCS"] = busqueda_costo_uniforme(problema)
            
            if "IDDFS" in algoritmos:
                resultados["IDDFS"] = busqueda_profundidad_iterativa(problema)
            
            # Mostrar resultados en tabs
            tabs = st.tabs(list(resultados.keys()))
            
            for tab, (nombre_algo, resultado) in zip(tabs, resultados.items()):
                with tab:
                    if resultado.encontrado:
                        st.success("✓ Solución encontrada")
                        
                        # Mostrar camino
                        camino_str = " → ".join([estado for estado, _ in resultado.camino])
                        st.markdown(f"**Camino**: {camino_str}")
                        
                        # Mostrar estadísticas
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Pasos", len(resultado.camino) - 1)
                        
                        with col2:
                            st.metric("Costo Total", f"{resultado.costo_total:.0f} km")
                        
                        with col3:
                            st.metric("Nodos Expandidos", resultado.nodos_expandidos)
                        
                        # Mostrar detalles del camino
                        st.markdown("**Detalles del Camino**:")
                        
                        detalles = []
                        for i, (estado, accion) in enumerate(resultado.camino):
                            detalles.append({
                                "Paso": i,
                                "Ciudad": estado,
                                "Acción": accion if accion != "Inicio" else "Inicio"
                            })
                        
                        df_detalles = pd.DataFrame(detalles)
                        st.dataframe(df_detalles, use_container_width=True, hide_index=True)
                    
                    else:
                        st.error("❌ No se encontró solución")
            
            # Comparación de algoritmos
            if len(resultados) > 1:
                st.divider()
                st.markdown("### Comparación de Algoritmos")
                
                comparacion_datos = []
                for nombre_algo, resultado in resultados.items():
                    comparacion_datos.append({
                        "Algoritmo": nombre_algo,
                        "Encontrado": "✓" if resultado.encontrado else "✗",
                        "Pasos": len(resultado.camino) - 1 if resultado.encontrado else "-",
                        "Costo": f"{resultado.costo_total:.0f}" if resultado.encontrado else "-",
                        "Nodos Expandidos": resultado.nodos_expandidos
                    })
                
                df_comparacion = pd.DataFrame(comparacion_datos)
                st.dataframe(df_comparacion, use_container_width=True, hide_index=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px; margin-top: 30px;">
    <p>Presentación Interactiva: Agentes Inteligentes y Resolución de Problemas</p>
    <p>Asignatura: Inteligencia Artificial | TDS</p>
</div>
""", unsafe_allow_html=True)
