"""
Módulo: Algoritmos de Búsqueda No Informada
Descripción: Implementación de BFS, DFS, UCS y IDDFS para resolver problemas de búsqueda.
"""

from collections import deque
import heapq
from typing import Dict, List, Tuple, Optional, Set, Callable


class Nodo:
    """Representa un nodo en el árbol de búsqueda."""
    
    def __init__(
        self,
        estado: str,
        padre: Optional['Nodo'] = None,
        accion: Optional[str] = None,
        costo_camino: float = 0
    ):
        """
        Inicializa un nodo.
        
        Args:
            estado: El estado representado por este nodo
            padre: El nodo padre (None si es el nodo raíz)
            accion: La acción que llevó a este nodo desde el padre
            costo_camino: El costo acumulado desde el estado inicial hasta este nodo
        """
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo_camino = costo_camino
        self.profundidad = 0 if padre is None else padre.profundidad + 1
    
    def obtener_camino(self) -> List[Tuple[str, str]]:
        """
        Obtiene el camino desde el estado inicial hasta este nodo.
        
        Returns:
            List[Tuple[str, str]]: Lista de (estado, acción) que forma el camino
        """
        camino = []
        nodo_actual = self
        
        while nodo_actual.padre is not None:
            camino.append((nodo_actual.estado, nodo_actual.accion))
            nodo_actual = nodo_actual.padre
        
        camino.append((nodo_actual.estado, "Inicio"))
        return list(reversed(camino))
    
    def __lt__(self, otro):
        """Comparación para la cola de prioridad (UCS)."""
        return self.costo_camino < otro.costo_camino


class ProblemaDeRuta:
    """Define un problema de búsqueda de ruta en un grafo."""
    
    def __init__(
        self,
        grafo: Dict[str, List[Tuple[str, float]]],
        estado_inicial: str,
        estado_objetivo: str
    ):
        """
        Inicializa el problema.
        
        Args:
            grafo: Diccionario {nodo: [(vecino, costo), ...]}
            estado_inicial: El estado inicial
            estado_objetivo: El estado objetivo
        """
        self.grafo = grafo
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
    
    def es_objetivo(self, estado: str) -> bool:
        """Verifica si un estado es el objetivo."""
        return estado == self.estado_objetivo
    
    def obtener_sucesores(self, estado: str) -> List[Tuple[str, str, float]]:
        """
        Obtiene los sucesores de un estado.
        
        Returns:
            List[Tuple[str, str, float]]: Lista de (estado_sucesor, acción, costo)
        """
        if estado not in self.grafo:
            return []
        
        sucesores = []
        for vecino, costo in self.grafo[estado]:
            accion = f"{estado} → {vecino}"
            sucesores.append((vecino, accion, costo))
        
        return sucesores


class ResultadoBusqueda:
    """Almacena los resultados de una búsqueda."""
    
    def __init__(
        self,
        encontrado: bool,
        camino: Optional[List[Tuple[str, str]]] = None,
        costo_total: float = 0,
        nodos_expandidos: int = 0,
        nodos_frontera: int = 0
    ):
        """
        Inicializa los resultados.
        
        Args:
            encontrado: Si se encontró una solución
            camino: El camino solución (lista de (estado, acción))
            costo_total: El costo total del camino
            nodos_expandidos: Número de nodos expandidos
            nodos_frontera: Número de nodos en la frontera al final
        """
        self.encontrado = encontrado
        self.camino = camino or []
        self.costo_total = costo_total
        self.nodos_expandidos = nodos_expandidos
        self.nodos_frontera = nodos_frontera
    
    def __str__(self) -> str:
        """Representación en string del resultado."""
        if not self.encontrado:
            return "No se encontró solución"
        
        resultado = f"✓ Solución encontrada\n"
        resultado += f"Camino: {' → '.join([estado for estado, _ in self.camino])}\n"
        resultado += f"Pasos: {len(self.camino) - 1}\n"
        resultado += f"Costo total: {self.costo_total:.2f}\n"
        resultado += f"Nodos expandidos: {self.nodos_expandidos}\n"
        resultado += f"Nodos en frontera: {self.nodos_frontera}"
        
        return resultado


def busqueda_amplitud(problema: ProblemaDeRuta) -> ResultadoBusqueda:
    """
    Búsqueda en Amplitud (BFS).
    
    Expande el nodo menos profundo en la frontera de búsqueda.
    Garantiza encontrar la solución más corta (óptima en términos de número de pasos).
    
    Args:
        problema: El problema a resolver
    
    Returns:
        ResultadoBusqueda: Los resultados de la búsqueda
    """
    nodo_inicial = Nodo(problema.estado_inicial)
    
    if problema.es_objetivo(nodo_inicial.estado):
        return ResultadoBusqueda(
            encontrado=True,
            camino=nodo_inicial.obtener_camino(),
            costo_total=0,
            nodos_expandidos=1
        )
    
    frontera = deque([nodo_inicial])
    explorados = set()
    nodos_expandidos = 0
    
    while frontera:
        nodo_actual = frontera.popleft()
        explorados.add(nodo_actual.estado)
        nodos_expandidos += 1
        
        for estado_sucesor, accion, costo in problema.obtener_sucesores(nodo_actual.estado):
            if estado_sucesor not in explorados and estado_sucesor not in [n.estado for n in frontera]:
                nodo_sucesor = Nodo(
                    estado=estado_sucesor,
                    padre=nodo_actual,
                    accion=accion,
                    costo_camino=nodo_actual.costo_camino + costo
                )
                
                if problema.es_objetivo(nodo_sucesor.estado):
                    return ResultadoBusqueda(
                        encontrado=True,
                        camino=nodo_sucesor.obtener_camino(),
                        costo_total=nodo_sucesor.costo_camino,
                        nodos_expandidos=nodos_expandidos,
                        nodos_frontera=len(frontera)
                    )
                
                frontera.append(nodo_sucesor)
    
    return ResultadoBusqueda(encontrado=False, nodos_expandidos=nodos_expandidos)


def busqueda_profundidad(problema: ProblemaDeRuta, limite: Optional[int] = None) -> ResultadoBusqueda:
    """
    Búsqueda en Profundidad (DFS) o Búsqueda en Profundidad Limitada (DLS).
    
    Expande el nodo más profundo en la frontera de búsqueda.
    
    Args:
        problema: El problema a resolver
        limite: Límite de profundidad (None para DFS sin límite)
    
    Returns:
        ResultadoBusqueda: Los resultados de la búsqueda
    """
    nodo_inicial = Nodo(problema.estado_inicial)
    
    if problema.es_objetivo(nodo_inicial.estado):
        return ResultadoBusqueda(
            encontrado=True,
            camino=nodo_inicial.obtener_camino(),
            costo_total=0,
            nodos_expandidos=1
        )
    
    frontera = [nodo_inicial]
    explorados = set()
    nodos_expandidos = 0
    
    while frontera:
        nodo_actual = frontera.pop()
        
        if nodo_actual.estado in explorados:
            continue
        
        explorados.add(nodo_actual.estado)
        nodos_expandidos += 1
        
        # Verificar límite de profundidad
        if limite is not None and nodo_actual.profundidad >= limite:
            continue
        
        for estado_sucesor, accion, costo in problema.obtener_sucesores(nodo_actual.estado):
            if estado_sucesor not in explorados:
                nodo_sucesor = Nodo(
                    estado=estado_sucesor,
                    padre=nodo_actual,
                    accion=accion,
                    costo_camino=nodo_actual.costo_camino + costo
                )
                
                if problema.es_objetivo(nodo_sucesor.estado):
                    return ResultadoBusqueda(
                        encontrado=True,
                        camino=nodo_sucesor.obtener_camino(),
                        costo_total=nodo_sucesor.costo_camino,
                        nodos_expandidos=nodos_expandidos,
                        nodos_frontera=len(frontera)
                    )
                
                frontera.append(nodo_sucesor)
    
    return ResultadoBusqueda(encontrado=False, nodos_expandidos=nodos_expandidos)


def busqueda_costo_uniforme(problema: ProblemaDeRuta) -> ResultadoBusqueda:
    """
    Búsqueda de Costo Uniforme (UCS).
    
    Expande el nodo con el costo de camino más bajo.
    Garantiza encontrar la solución de menor costo.
    
    Args:
        problema: El problema a resolver
    
    Returns:
        ResultadoBusqueda: Los resultados de la búsqueda
    """
    nodo_inicial = Nodo(problema.estado_inicial)
    
    if problema.es_objetivo(nodo_inicial.estado):
        return ResultadoBusqueda(
            encontrado=True,
            camino=nodo_inicial.obtener_camino(),
            costo_total=0,
            nodos_expandidos=1
        )
    
    frontera = [nodo_inicial]
    explorados = set()
    nodos_expandidos = 0
    
    while frontera:
        nodo_actual = heapq.heappop(frontera)
        
        if nodo_actual.estado in explorados:
            continue
        
        explorados.add(nodo_actual.estado)
        nodos_expandidos += 1
        
        for estado_sucesor, accion, costo in problema.obtener_sucesores(nodo_actual.estado):
            if estado_sucesor not in explorados:
                nodo_sucesor = Nodo(
                    estado=estado_sucesor,
                    padre=nodo_actual,
                    accion=accion,
                    costo_camino=nodo_actual.costo_camino + costo
                )
                
                if problema.es_objetivo(nodo_sucesor.estado):
                    return ResultadoBusqueda(
                        encontrado=True,
                        camino=nodo_sucesor.obtener_camino(),
                        costo_total=nodo_sucesor.costo_camino,
                        nodos_expandidos=nodos_expandidos,
                        nodos_frontera=len(frontera)
                    )
                
                heapq.heappush(frontera, nodo_sucesor)
    
    return ResultadoBusqueda(encontrado=False, nodos_expandidos=nodos_expandidos)


def busqueda_profundidad_iterativa(problema: ProblemaDeRuta, limite_maximo: int = 20) -> ResultadoBusqueda:
    """
    Búsqueda en Profundidad Iterativa (IDDFS).
    
    Realiza DLS con límites de profundidad crecientes.
    Combina la completitud y optimalidad de BFS con la eficiencia de espacio de DFS.
    
    Args:
        problema: El problema a resolver
        limite_maximo: Límite máximo de profundidad a explorar
    
    Returns:
        ResultadoBusqueda: Los resultados de la búsqueda
    """
    nodos_expandidos_total = 0
    
    for profundidad in range(limite_maximo + 1):
        resultado = busqueda_profundidad(problema, limite=profundidad)
        nodos_expandidos_total += resultado.nodos_expandidos
        
        if resultado.encontrado:
            resultado.nodos_expandidos = nodos_expandidos_total
            return resultado
    
    return ResultadoBusqueda(encontrado=False, nodos_expandidos=nodos_expandidos_total)


# Ejemplo de uso
if __name__ == "__main__":
    # Definir un grafo de ejemplo (Rumania)
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
    
    # Crear un problema: ir de Arad a Bucharest
    problema = ProblemaDeRuta(grafo_rumania, 'Arad', 'Bucharest')
    
    print("=== Comparación de Algoritmos de Búsqueda ===\n")
    
    # BFS
    print("1. Búsqueda en Amplitud (BFS)")
    resultado_bfs = busqueda_amplitud(problema)
    print(resultado_bfs)
    print()
    
    # DFS
    print("2. Búsqueda en Profundidad (DFS)")
    resultado_dfs = busqueda_profundidad(problema)
    print(resultado_dfs)
    print()
    
    # UCS
    print("3. Búsqueda de Costo Uniforme (UCS)")
    resultado_ucs = busqueda_costo_uniforme(problema)
    print(resultado_ucs)
    print()
    
    # IDDFS
    print("4. Búsqueda en Profundidad Iterativa (IDDFS)")
    resultado_iddfs = busqueda_profundidad_iterativa(problema)
    print(resultado_iddfs)
