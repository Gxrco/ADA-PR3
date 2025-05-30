# Proyecto 3 - Análisis de Algoritmos MTF e IMTF

## Descripción

Este proyecto implementa y analiza los algoritmos **Move to Front (MTF)** e **Improved Move to Front (IMTF)**. El objetivo es realizar un análisis amortizado y competitivo de estos algoritmos de gestión de listas auto-organizables.

**Autor:** Gerson Ramírez

## Algoritmos Implementados

### Move to Front (MTF)
Cuando se accede a un elemento de la lista, este se mueve al frente de la lista. El costo de acceso es la posición del elemento antes de moverlo.

### Improved Move to Front (IMTF)
Es una variante de MTF que utiliza una estrategia de *look-ahead*. Cuando se accede a un elemento en la posición `i`, se verifica si este elemento aparece nuevamente dentro de las próximas `i-1` solicitudes futuras.
- Si el elemento **aparece** en las próximas `i-1` solicitudes, se mueve al frente.
- Si el elemento **no aparece**, se deja en su posición actual.
El objetivo es evitar mover elementos al frente innecesariamente si no van a ser accedidos pronto.

## Estructura del Proyecto

-   `analysis.py`: Script principal que ejecuta las simulaciones y análisis de los algoritmos MTF e IMTF.
-   `mtf_analyzer.py`: Contiene la clase `MTFAnalyzer` con la lógica para el algoritmo MTF y funciones para encontrar secuencias de mejor y peor caso.
-   `imtf_analyzer.py`: Contiene la clase `IMTFAnalyzer` (que hereda de `MTFAnalyzer`) con la lógica para el algoritmo IMTF.

## Análisis Realizado

El script `analysis.py` realiza las siguientes pruebas y análisis:

1.  **MTF - Primera Secuencia:** Ejecuta el algoritmo MTF con la secuencia `[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]`.
2.  **MTF - Segunda Secuencia:** Ejecuta el algoritmo MTF con la secuencia `[4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]`.
3.  **MTF - Mejor Caso:** Encuentra y ejecuta la secuencia de 20 solicitudes que produce el mínimo costo para MTF.
4.  **MTF - Peor Caso:** Encuentra y ejecuta la secuencia de 20 solicitudes que produce el máximo costo para MTF.
5.  **MTF - Patrones de Repetición:** Analiza el costo de MTF para secuencias donde un mismo elemento se repite 20 veces (e.g., `[2]*20` y `[3]*20`).
6.  **IMTF - Aplicación a Casos de MTF:**
    *   Aplica IMTF a la secuencia de mejor caso encontrada para MTF.
    *   Aplica IMTF a la secuencia de peor caso encontrada para MTF.
7.  **Resumen y Análisis Competitivo:**
    *   Muestra un resumen de los costos obtenidos en todas las pruebas.
    *   Calcula el ratio competitivo de IMTF respecto a MTF para los escenarios de mejor y peor caso.

## Cómo Ejecutar

1.  Asegúrate de tener Python 3 instalado.
2.  Clona este repositorio o descarga los archivos.
3.  Navega al directorio del proyecto en tu terminal.
4.  Ejecuta el script de análisis:
    ```bash
    python analysis.py
    ```
5.  Los resultados del análisis se imprimirán en la consola.