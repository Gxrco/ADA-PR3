from typing import List, Tuple
import itertools

class MTFAnalyzer:
    """Clase para analizar el algoritmo Move to Front y sus variantes."""
    
    def __init__(self):
        self.history = []
    
    def mtf_access(self, config_list: List[int], request: int, step: int) -> Tuple[int, List[int]]:
        """
        Simula un acceso MTF y devuelve el costo y la nueva configuración.
        
        Args:
            config_list: Lista actual de configuración
            request: Elemento solicitado
            step: Número de paso (para logging)
        
        Returns:
            Tupla (costo, nueva_configuración)
        """
        config = config_list.copy()
        
        # Encontrar la posición del elemento (1-indexado)
        if request in config:
            position = config.index(request) + 1
            cost = position
            
            # Mover el elemento al frente
            config.remove(request)
            config.insert(0, request)
            
            # Registrar en historial
            self.history.append({
                'step': step,
                'initial_config': config_list.copy(),
                'request': request,
                'cost': cost,
                'final_config': config.copy()
            })
            
            return cost, config
        else:
            raise ValueError(f"Elemento {request} no encontrado en la lista")
    
    def run_mtf_sequence(self, initial_config: List[int], requests: List[int], 
                        print_steps: bool = True) -> int:
        """
        Ejecuta una secuencia completa de solicitudes MTF.
        
        Args:
            initial_config: Configuración inicial de la lista
            requests: Secuencia de solicitudes
            print_steps: Si imprimir los pasos detallados
        
        Returns:
            Costo total de accesos
        """
        self.history.clear()
        config = initial_config.copy()
        total_cost = 0
        
        if print_steps:
            print(f"Configuración inicial: {config}")
            print("-" * 60)
        
        for i, request in enumerate(requests):
            cost, config = self.mtf_access(config, request, i + 1)
            total_cost += cost
            
            if print_steps:
                print(f"Paso {i+1}: Solicitud {request} | Costo: {cost} | "
                      f"Nueva configuración: {config}")
        
        if print_steps:
            print("-" * 60)
            print(f"Costo total de accesos: {total_cost}")
            print()
        
        return total_cost
    
    def find_best_sequence(self, initial_config: List[int], length: int) -> Tuple[List[int], int]:
        """
        Encuentra la secuencia de solicitudes que minimiza el costo total.
        
        Args:
            initial_config: Configuración inicial
            length: Longitud de la secuencia a generar
        
        Returns:
            Tupla (mejor_secuencia, costo_mínimo)
        """
        elements = initial_config.copy()
        best_sequence = None
        min_cost = float('inf')
        
        # Para secuencias largas, probamos patrones comunes
        if length <= 10:
            # Fuerza bruta para secuencias cortas
            for sequence in itertools.product(elements, repeat=length):
                cost = self.run_mtf_sequence(initial_config, list(sequence), False)
                if cost < min_cost:
                    min_cost = cost
                    best_sequence = list(sequence)
        else:
            # Para secuencias largas, probamos patrones obvios
            # Patrón 1: Solo el primer elemento
            sequence1 = [elements[0]] * length
            cost1 = self.run_mtf_sequence(initial_config, sequence1, False)
            
            # Patrón 2: Secuencia en orden
            sequence2 = (elements * (length // len(elements) + 1))[:length]
            cost2 = self.run_mtf_sequence(initial_config, sequence2, False)
            
            # Patrón 3: Secuencia inversa
            sequence3 = (elements[::-1] * (length // len(elements) + 1))[:length]
            cost3 = self.run_mtf_sequence(initial_config, sequence3, False)
            
            costs = [(cost1, sequence1), (cost2, sequence2), (cost3, sequence3)]
            min_cost, best_sequence = min(costs, key=lambda x: x[0])
        
        return best_sequence, min_cost
    
    def find_worst_sequence(self, initial_config: List[int], length: int) -> Tuple[List[int], int]:
        """
        Encuentra la secuencia de solicitudes que maximiza el costo total.
        
        Args:
            initial_config: Configuración inicial
            length: Longitud de la secuencia a generar
        
        Returns:
            Tupla (peor_secuencia, costo_máximo)
        """
        elements = initial_config.copy()
        worst_sequence = None
        max_cost = 0
        
        if length <= 10:
            # Fuerza bruta para secuencias cortas
            for sequence in itertools.product(elements, repeat=length):
                cost = self.run_mtf_sequence(initial_config, list(sequence), False)
                if cost > max_cost:
                    max_cost = cost
                    worst_sequence = list(sequence)
        else:
            # Para secuencias largas, probamos patrones que generen alto costo
            # Patrón 1: Alternar entre primer y último elemento
            sequence1 = []
            for i in range(length):
                sequence1.append(elements[0] if i % 2 == 0 else elements[-1])
            cost1 = self.run_mtf_sequence(initial_config, sequence1, False)
            
            # Patrón 2: Secuencia que evita beneficios de localidad
            sequence2 = []
            for i in range(length):
                sequence2.append(elements[i % len(elements)])
            cost2 = self.run_mtf_sequence(initial_config, sequence2, False)
            
            # Patrón 3: Acceso siempre al último elemento
            sequence3 = [elements[-1]] * length
            cost3 = self.run_mtf_sequence(initial_config, sequence3, False)
            
            costs = [(cost1, sequence1), (cost2, sequence2), (cost3, sequence3)]
            max_cost, worst_sequence = max(costs, key=lambda x: x[0])
        
        return worst_sequence, max_cost
