"""
Proyecto 3 - Análisis y Diseño de Algoritmos
Implementación de algoritmos MTF (Move to Front) e IMTF (Improved MTF)
Análisis Amortizado y Competitivo
Autor: Gerson Ramírez
"""

import copy
from mtf_analyzer import MTFAnalyzer
from imtf_analyzer import IMTFAnalyzer

def main():
    
    print("=" * 80)
    print("PROYECTO 3 - ALGORITMOS MTF E IMTF")
    print("Análisis Amortizado y Competitivo")
    print("=" * 80)
    print()
    
    mtf = MTFAnalyzer()
    imtf = IMTFAnalyzer()
    initial_config = [0, 1, 2, 3, 4]
    
    # 1. Primera secuencia MTF
    print("1. ALGORITMO MTF - PRIMERA SECUENCIA")
    print("=" * 50)
    sequence1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    cost1 = mtf.run_mtf_sequence(initial_config, sequence1)
    
    # 2. Segunda secuencia MTF
    print("2. ALGORITMO MTF - SEGUNDA SECUENCIA")
    print("=" * 50)
    sequence2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    cost2 = mtf.run_mtf_sequence(initial_config, sequence2)
    
    # 3. Mejor caso (mínimo costo)
    print("3. MEJOR CASO - MÍNIMO COSTO (20 solicitudes)")
    print("=" * 50)
    best_seq, min_cost = mtf.find_best_sequence(initial_config, 20)
    print(f"Mejor secuencia: {best_seq}")
    print(f"Costo mínimo: {min_cost}")
    print()
    
    # 4. Peor caso (máximo costo)
    print("4. PEOR CASO - MÁXIMO COSTO (20 solicitudes)")
    print("=" * 50)
    worst_seq, max_cost = mtf.find_worst_sequence(initial_config, 20)
    print(f"Peor secuencia: {worst_seq}")
    print(f"Costo máximo: {max_cost}")
    print()
    
    # 5. Patrones de repetición
    print("5. PATRONES DE REPETICIÓN")
    print("=" * 50)
    seq_2s = [2] * 20
    cost_2s = mtf.run_mtf_sequence(initial_config, seq_2s)
    
    seq_3s = [3] * 20
    cost_3s = mtf.run_mtf_sequence(initial_config, seq_3s, False)
    print(f"Secuencia de 20 elementos '3': Costo total = {cost_3s}")
    print()
    
    print("ANÁLISIS DE PATRONES:")
    print(f"- Repetición del elemento 2: Costo = {cost_2s}")
    print(f"- Repetición del elemento 3: Costo = {cost_3s}")
    print("PATRÓN OBSERVADO: Cuando se repite un elemento, después del primer")
    print("acceso, todos los accesos subsecuentes tienen costo 1, ya que el")
    print("elemento se mantiene en la posición frontal.")
    print()
    
    # 6. Algoritmo IMTF
    print("6. ALGORITMO IMTF (IMPROVED MTF)")
    print("=" * 50)
    
    print("6.1. IMTF aplicado al MEJOR CASO de MTF:")
    print("-" * 40)
    imtf_best_cost = imtf.run_imtf_sequence(initial_config, best_seq)
    
    print("6.2. IMTF aplicado al PEOR CASO de MTF:")
    print("-" * 40)
    imtf_worst_cost = imtf.run_imtf_sequence(initial_config, worst_seq)
    
    # Resumen final
    print("=" * 80)
    print("RESUMEN DE RESULTADOS")
    print("=" * 80)
    print(f"1. Secuencia 1 (MTF): {cost1}")
    print(f"2. Secuencia 2 (MTF): {cost2}")
    print(f"3. Mejor caso (MTF): {min_cost}")
    print(f"4. Peor caso (MTF): {max_cost}")
    print(f"5. Repetición elemento 2: {cost_2s}")
    print(f"   Repetición elemento 3: {cost_3s}")
    print(f"6. IMTF mejor caso: {imtf_best_cost}")
    print(f"   IMTF peor caso: {imtf_worst_cost}")
    print()
    print("ANÁLISIS COMPETITIVO:")
    print(f"- Ratio IMTF/MTF (mejor caso): {imtf_best_cost/min_cost:.2f}")
    print(f"- Ratio IMTF/MTF (peor caso): {imtf_worst_cost/max_cost:.2f}")

if __name__ == "__main__":
    main()