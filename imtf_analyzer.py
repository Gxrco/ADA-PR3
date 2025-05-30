from mtf_analyzer import MTFAnalyzer
from typing import List, Tuple

class IMTFAnalyzer(MTFAnalyzer):
    """Clase para el algoritmo IMTF (Improved Move to Front) con look-ahead."""
    
    def imtf_access(self, config_list: List[int], request: int, step: int, 
                   remaining_requests: List[int]) -> Tuple[int, List[int]]:
        """
        Simula un acceso IMTF con look-ahead.
        
        Args:
            config_list: Lista actual de configuración
            request: Elemento solicitado
            step: Número de paso
            remaining_requests: Solicitudes restantes en la secuencia
        
        Returns:
            Tupla (costo, nueva_configuración)
        """
        config = config_list.copy()
        
        if request in config:
            position = config.index(request) + 1
            cost = position
            
            # Look-ahead: verificar si el elemento aparece en los próximos i-1 elementos
            look_ahead_count = position - 1
            should_move = False
            
            if look_ahead_count > 0 and len(remaining_requests) > 0:
                next_elements = remaining_requests[:min(look_ahead_count, len(remaining_requests))]
                should_move = request in next_elements
            elif look_ahead_count == 0:
                # Si está en posición 1, siempre se mantiene al frente
                should_move = True
            
            # Mover al frente solo si cumple la condición
            if should_move:
                config.remove(request)
                config.insert(0, request)
            
            # Registrar en historial
            self.history.append({
                'step': step,
                'initial_config': config_list.copy(),
                'request': request,
                'cost': cost,
                'moved': should_move,
                'look_ahead_count': look_ahead_count,
                'final_config': config.copy()
            })
            
            return cost, config
        else:
            raise ValueError(f"Elemento {request} no encontrado en la lista")
    
    def run_imtf_sequence(self, initial_config: List[int], requests: List[int], 
                         print_steps: bool = True) -> int:
        """
        Ejecuta una secuencia completa de solicitudes IMTF.
        
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
            print("-" * 80)
        
        for i, request in enumerate(requests):
            remaining = requests[i+1:]
            cost, config = self.imtf_access(config, request, i + 1, remaining)
            total_cost += cost
            
            if print_steps:
                move_status = "MOVIDO" if self.history[-1]['moved'] else "NO MOVIDO"
                print(f"Paso {i+1}: Solicitud {request} | Costo: {cost} | "
                      f"{move_status} | Nueva configuración: {config}")
        
        if print_steps:
            print("-" * 80)
            print(f"Costo total de accesos: {total_cost}")
            print()
        
        return total_cost
