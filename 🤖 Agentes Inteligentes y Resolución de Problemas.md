# 🤖 Agentes Inteligentes y Resolución de Problemas
## Presentación Interactiva para Estudiantes Universitarios

Una presentación completa e interactiva sobre **Agentes Inteligentes** y **Resolución de Problemas** en Inteligencia Artificial, diseñada para estudiantes universitarios. Incluye conceptos teóricos, ejemplos resueltos y ejercicios prácticos interactivos.

---

## 📋 Contenido de la Presentación

### 1. **Agentes Inteligentes y Entornos** (Sección 2.1)
- Conceptos fundamentales de agentes
- Propiedades PEAS (Performance, Environment, Actuators, Sensors)
- Clasificación de entornos (observable, determinista, episódico, estático, discreto, multiagente)

### 2. **Tipos de Agentes y Arquitecturas** (Sección 2.2)
- Agente de Reflejo Simple
- Agente de Reflejo Basado en Modelo
- Agente Basado en Objetivos
- Agente Basado en Utilidad
- Agente de Aprendizaje

### 3. **Modelos de Toma de Decisiones** (Sección 2.3)
- Lógica y Razonamiento
- Teoría de la Decisión
- Modelo BDI (Beliefs, Desires, Intentions)

### 4. **Problemas y Espacios de Búsqueda** (Sección 2.4)
- Definición formal de problemas
- Estado inicial, acciones, test de objetivo, función de costo
- Espacio de estados y árbol de búsqueda

### 5. **Algoritmos de Búsqueda No Informada** (Sección 2.5)
- Búsqueda en Amplitud (BFS)
- Búsqueda en Profundidad (DFS)
- Búsqueda de Costo Uniforme (UCS)
- Búsqueda en Profundidad Iterativa (IDDFS)

### 6. **Ejemplo Resuelto: Agente Aspiradora**
- Implementación de un agente de reflejo simple
- Simulación interactiva del comportamiento del agente
- Visualización del historial de acciones

### 7. **Ejercicio Práctico: Búsqueda de Rutas**
- Problema del viajero en Rumania
- Comparación interactiva de algoritmos de búsqueda
- Análisis de rendimiento (pasos, costo, nodos expandidos)

---

## 🚀 Instalación y Ejecución

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd /home/ubuntu
   ```

2. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación Streamlit**
   ```bash
   streamlit run app.py
   ```

4. **Abrir en el navegador**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre automáticamente, visita la URL manualmente

---

## 📁 Estructura del Proyecto

```
/home/ubuntu/
├── app.py                      # Aplicación principal de Streamlit
├── agente_aspiradora.py        # Implementación del agente aspiradora
├── algoritmos_busqueda.py      # Implementación de algoritmos de búsqueda
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
└── presentacion_agentes_ia.md  # Contenido teórico en Markdown
```

### Descripción de Archivos

- **app.py**: Aplicación Streamlit principal que contiene toda la presentación interactiva
- **agente_aspiradora.py**: Módulo con la implementación del agente aspiradora (ejemplo resuelto)
- **algoritmos_busqueda.py**: Módulo con implementaciones de BFS, DFS, UCS e IDDFS
- **requirements.txt**: Lista de dependencias necesarias
- **presentacion_agentes_ia.md**: Contenido teórico en formato Markdown

---

## 💻 Uso de la Presentación

### Navegación
1. Usa el menú lateral para seleccionar diferentes secciones
2. Lee las explicaciones teóricas en cada sección
3. Interactúa con los ejemplos y ejercicios

### Ejemplo Resuelto: Agente Aspiradora
1. Selecciona el estado inicial de las ubicaciones A y B (Limpio o Sucio)
2. Haz clic en "Ejecutar Simulación"
3. Observa el historial de acciones y el estado final

### Ejercicio Práctico: Búsqueda de Rutas
1. Selecciona una ciudad de origen y destino
2. Elige los algoritmos a comparar (BFS, DFS, UCS, IDDFS)
3. Haz clic en "Buscar Ruta"
4. Observa los resultados y compara el rendimiento de los algoritmos

---

## 🎯 Objetivos de Aprendizaje

Al completar esta presentación, los estudiantes podrán:

✓ Entender qué es un agente inteligente y sus componentes  
✓ Clasificar entornos según sus propiedades  
✓ Identificar y describir diferentes tipos de agentes  
✓ Formalizar problemas de búsqueda  
✓ Implementar algoritmos de búsqueda no informada  
✓ Analizar y comparar el rendimiento de algoritmos  
✓ Resolver problemas reales usando técnicas de IA  

---

## 📚 Temas Cubiertos

### Conceptos Teóricos
- Definición y propiedades de agentes inteligentes
- Clasificación de entornos (PEAS)
- Tipos de agentes y arquitecturas
- Modelos de toma de decisiones
- Formalización de problemas
- Algoritmos de búsqueda

### Implementaciones Prácticas
- Agente aspiradora (ejemplo resuelto)
- Algoritmos de búsqueda (BFS, DFS, UCS, IDDFS)
- Problema del viajero (ejercicio práctico)
- Comparación interactiva de algoritmos

---

## 🔧 Características Técnicas

### Tecnologías Utilizadas
- **Streamlit**: Framework para crear aplicaciones web interactivas
- **Python 3**: Lenguaje de programación
- **Pandas**: Manipulación y visualización de datos
- **Markdown**: Formato para documentación

### Características de la Aplicación
- Interfaz interactiva y amigable
- Visualización de datos en tablas
- Simulaciones ejecutables
- Comparación de algoritmos
- Documentación integrada

---

## 📖 Ejemplos de Uso

### Ejemplo 1: Simular el Agente Aspiradora
```python
from agente_aspiradora import simular_entorno, Estado, Ubicacion

# Definir entorno inicial
entorno_inicial = {
    Ubicacion.A: Estado.SUCIO,
    Ubicacion.B: Estado.LIMPIO
}

# Ejecutar simulación
agente, historial_entornos, historial_acciones = simular_entorno(entorno_inicial)

# Ver resultados
for percepcion, accion in historial_acciones:
    print(f"Ubicación: {percepcion.ubicacion.value}, Estado: {percepcion.estado.value}")
```

### Ejemplo 2: Usar Algoritmos de Búsqueda
```python
from algoritmos_busqueda import ProblemaDeRuta, busqueda_amplitud

# Definir grafo
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Crear problema
problema = ProblemaDeRuta(grafo, 'A', 'D')

# Ejecutar búsqueda
resultado = busqueda_amplitud(problema)

# Ver resultados
print(resultado)
```

---

## 🎓 Para Instructores

Esta presentación es ideal para:
- **Clases de Inteligencia Artificial**: Enseñanza de conceptos fundamentales
- **Laboratorios Prácticos**: Ejercicios interactivos en clase
- **Proyectos de Estudiantes**: Base para proyectos más complejos
- **Autoaprendizaje**: Estudiantes pueden aprender a su propio ritmo

### Sugerencias de Uso en Clase
1. Presenta cada sección teórica usando la presentación
2. Ejecuta los ejemplos resueltos en vivo
3. Pide a los estudiantes que resuelvan los ejercicios prácticos
4. Compara resultados y discute diferencias
5. Propón variaciones y extensiones

---

## 🐛 Solución de Problemas

### La aplicación no inicia
- Verifica que Streamlit esté instalado: `pip install streamlit`
- Verifica que estés en el directorio correcto: `cd /home/ubuntu`

### Error de módulos no encontrados
- Instala las dependencias: `pip install -r requirements.txt`
- Verifica que Python 3 esté instalado: `python3 --version`

### Errores en la simulación
- Verifica que los archivos `agente_aspiradora.py` y `algoritmos_busqueda.py` estén en el mismo directorio que `app.py`
- Revisa la consola para mensajes de error detallados

---

## 📝 Notas Importantes

- La presentación cubre conceptos **fundamentales** de agentes inteligentes
- Los algoritmos implementados son **no informados** (no usan heurísticas)
- Los ejemplos están diseñados para ser **educativos**, no optimizados para producción
- Se recomienda ejecutar la presentación en **navegadores modernos** (Chrome, Firefox, Safari)

---

## 🔗 Referencias

- Russell, S. J., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.)
- Nilsson, N. J. (1998). Artificial Intelligence: A New Synthesis
- Poole, D. L., & Mackworth, A. K. (2010). Artificial Intelligence: Foundations of Computational Agents

---

## 📄 Licencia

Esta presentación educativa está disponible para uso académico y educativo.

---

## 👨‍💻 Autor

Creada como material educativo para estudiantes universitarios de Inteligencia Artificial.

---

## 📞 Soporte

Para preguntas o problemas:
1. Revisa la sección de Solución de Problemas arriba
2. Verifica que todas las dependencias estén instaladas
3. Consulta la documentación de Streamlit: https://docs.streamlit.io

---

**¡Disfruta aprendiendo sobre Agentes Inteligentes! 🤖**
