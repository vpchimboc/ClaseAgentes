"""
Módulo: Agente Aspiradora - Ejemplo Resuelto
Descripción: Implementación de un agente de reflejo simple que limpia un entorno de dos ubicaciones.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple


class Ubicacion(Enum):
    """Ubicaciones disponibles en el entorno."""
    A = "A"
    B = "B"


class Estado(Enum):
    """Estados de limpieza de una ubicación."""
    LIMPIO = "Limpio"
    SUCIO = "Sucio"


class Accion(Enum):
    """Acciones que puede realizar el agente."""
    ASPIRAR = "Aspirar"
    MOVER_A = "Mover a "
    DETENER = "Detener"


@dataclass
class Percepcion:
    """Representa la percepción del agente en un momento dado."""
    ubicacion: Ubicacion
    estado: Estado


class AgenteAspiradora:
    """
    Agente de reflejo simple que aspira un entorno de dos ubicaciones.
    
    El agente sigue reglas condición-acción simples:
    - Si está en A y sucio: aspirar
    - Si está en B y sucio: aspirar
    - Si está en A y limpio: mover a B
    - Si está en B y limpio: mover a A
    """
    
    def __init__(self):
        """Inicializa el agente."""
        self.ubicacion_actual = Ubicacion.A
        self.historial_acciones: List[Tuple[Percepcion, Accion]] = []
        self.pasos = 0
    
    def percibir(self, entorno: dict) -> Percepcion:
        """
        El agente percibe su ubicación actual y el estado de la celda.
        
        Args:
            entorno: Diccionario con estados de las ubicaciones {Ubicacion: Estado}
        
        Returns:
            Percepcion: La percepción actual del agente
        """
        estado_actual = entorno[self.ubicacion_actual]
        return Percepcion(ubicacion=self.ubicacion_actual, estado=estado_actual)
    
    def decidir(self, percepcion: Percepcion) -> Accion:
        """
        Decide la acción a realizar basada en la percepción (reglas condición-acción).
        
        Args:
            percepcion: La percepción actual del agente
        
        Returns:
            Accion: La acción a realizar
        """
        # Reglas condición-acción
        if percepcion.estado == Estado.SUCIO:
            return Accion.ASPIRAR
        elif percepcion.ubicacion == Ubicacion.A:
            return Accion.MOVER_A
        else:  # ubicacion == B
            return Accion.MOVER_A
    
    def actuar(self, accion: Accion, entorno: dict) -> dict:
        """
        Ejecuta la acción y modifica el entorno.
        
        Args:
            accion: La acción a ejecutar
            entorno: El estado actual del entorno
        
        Returns:
            dict: El entorno modificado después de la acción
        """
        entorno_nuevo = entorno.copy()
        
        if accion == Accion.ASPIRAR:
            # Limpiar la ubicación actual
            entorno_nuevo[self.ubicacion_actual] = Estado.LIMPIO
        elif accion == Accion.MOVER_A:
            # Mover a la otra ubicación
            self.ubicacion_actual = (
                Ubicacion.B if self.ubicacion_actual == Ubicacion.A else Ubicacion.A
            )
        
        return entorno_nuevo
    
    def ejecutar_ciclo(self, entorno: dict) -> Tuple[dict, Accion]:
        """
        Ejecuta un ciclo completo: percibir, decidir, actuar.
        
        Args:
            entorno: El estado actual del entorno
        
        Returns:
            Tuple[dict, Accion]: El entorno modificado y la acción ejecutada
        """
        percepcion = self.percibir(entorno)
        accion = self.decidir(percepcion)
        entorno_nuevo = self.actuar(accion, entorno)
        
        self.historial_acciones.append((percepcion, accion))
        self.pasos += 1
        
        return entorno_nuevo, accion


def simular_entorno(
    entorno_inicial: dict,
    max_pasos: int = 10
) -> Tuple[AgenteAspiradora, List[dict], List[Tuple[Percepcion, Accion]]]:
    """
    Simula la ejecución del agente aspiradora en el entorno.
    
    Args:
        entorno_inicial: Estado inicial del entorno {Ubicacion: Estado}
        max_pasos: Número máximo de pasos a simular
    
    Returns:
        Tuple: (agente, historial_entornos, historial_acciones)
    """
    agente = AgenteAspiradora()
    entorno_actual = entorno_inicial.copy()
    historial_entornos = [entorno_actual.copy()]
    
    for _ in range(max_pasos):
        # Verificar si el entorno está completamente limpio
        if all(estado == Estado.LIMPIO for estado in entorno_actual.values()):
            break
        
        entorno_actual, accion = agente.ejecutar_ciclo(entorno_actual)
        historial_entornos.append(entorno_actual.copy())
    
    return agente, historial_entornos, agente.historial_acciones


def obtener_descripcion_accion(accion: Accion, ubicacion_actual: Ubicacion) -> str:
    """
    Obtiene una descripción legible de la acción.
    
    Args:
        accion: La acción a describir
        ubicacion_actual: La ubicación actual del agente
    
    Returns:
        str: Descripción de la acción
    """
    if accion == Accion.ASPIRAR:
        return "Aspirar"
    elif accion == Accion.MOVER_A:
        destino = Ubicacion.B if ubicacion_actual == Ubicacion.A else Ubicacion.A
        return f"Mover a {destino.value}"
    else:
        return "Detener"


# Ejemplo de uso
if __name__ == "__main__":
    # Entorno inicial: A sucio, B limpio
    entorno_inicial = {
        Ubicacion.A: Estado.SUCIO,
        Ubicacion.B: Estado.LIMPIO
    }
    
    print("=== Simulación del Agente Aspiradora ===\n")
    print(f"Entorno inicial: A={entorno_inicial[Ubicacion.A].value}, B={entorno_inicial[Ubicacion.B].value}\n")
    
    agente, historial_entornos, historial_acciones = simular_entorno(entorno_inicial)
    
    print("Historial de acciones:")
    ubicacion = Ubicacion.A
    for i, (percepcion, accion) in enumerate(historial_acciones, 1):
        desc_accion = obtener_descripcion_accion(accion, percepcion.ubicacion)
        print(f"Paso {i}: Ubicación={percepcion.ubicacion.value}, Estado={percepcion.estado.value} → {desc_accion}")
        if accion == Accion.MOVER_A:
            ubicacion = Ubicacion.B if ubicacion == Ubicacion.A else Ubicacion.A
    
    print(f"\nEntorno final: A={historial_entornos[-1][Ubicacion.A].value}, B={historial_entornos[-1][Ubicacion.B].value}")
    print(f"Pasos realizados: {agente.pasos}")
