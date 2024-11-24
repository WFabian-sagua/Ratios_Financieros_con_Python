# Análisis de Ratios Financieros - Proyecto Educativo

¡Hola! Soy **Fabian Sagua**, fundador de **DATA COUNT AI**. Este proyecto tiene un propósito **educacional** y está diseñado para ayudarte a comprender cómo se calculan y analizan los **ratios financieros** de una empresa utilizando datos reales del cierre del periodo 2023.

## Propósito del Proyecto

Este proyecto busca enseñar, de forma práctica, cómo evaluar la salud financiera de una organización utilizando **ratios financieros** clave. El análisis está basado en un conjunto de datos extraídos de la **Superintendencia del Mercado de Valores (SMV)**, específicamente de una empresa al cierre del **31 de diciembre de 2023**.

El objetivo es que, a través de este repositorio, puedas aprender a calcular y entender ratios como:

- **Liquidez Corriente**
- **Liquidez Ácida**
- **Endeudamiento**
- **Rentabilidad sobre el Patrimonio (ROE)**

He preparado dos versiones de este proyecto para que puedas elegir la que mejor se adapte a tus necesidades:

- **Versión de escritorio (Python)**: Una versión más "clásica" que puedes ejecutar localmente en tu máquina.
- **Versión interactiva (Google Colab)**: Si prefieres trabajar directamente desde tu navegador, esta opción te permitirá interactuar con los datos de manera sencilla.

## Fuente de los Datos

Los datos utilizados en este proyecto provienen directamente de la **Superintendencia del Mercado de Valores (SMV)** y corresponden a una empresa al cierre del **31 de diciembre de 2023**. El archivo Excel con la información financiera se encuentra disponible en el repositorio bajo el nombre `ef1.xlsx`.

## Descripción del Proyecto

Este repositorio contiene el código necesario para calcular los ratios financieros más comunes a partir de los datos del estado de situación financiera de la empresa. Los ratios que calculamos son:

- **Liquidez Corriente**: Activos Corrientes / Pasivos Corrientes
- **Liquidez Ácida**: (Activos Corrientes - Inventarios) / Pasivos Corrientes
- **Endeudamiento**: Total Pasivos / Total Patrimonio
- **Rentabilidad sobre el Patrimonio (ROE)**: Resultados Acumulados / Capital Emitido

### Características del Proyecto

- **Lectura y procesamiento de datos**: Utilizamos **pandas** para leer los datos del archivo Excel y procesarlos correctamente.
- **Limpieza de datos**: Implementamos funciones para limpiar y convertir los valores de manera que puedan ser usados para los cálculos.
- **Cálculos financieros**: Realizamos los cálculos de los ratios utilizando fórmulas estándar.
- **Interactividad**: En la versión de **Google Colab**, puedes cargar el archivo y ver los resultados en tiempo real.
- **Resultados claros y directos**: Los resultados de los cálculos se presentan en la consola o en celdas de Google Colab, según la versión que elijas.

## Requisitos

### Para la versión de escritorio (Python)
Asegúrate de tener instalado **Python 3.8.7 en adelante** y las siguientes bibliotecas:

- **pandas**: Para manejar los datos.
- **openpyxl**: Para leer los archivos Excel.

Puedes instalar las dependencias ejecutando:

```bash
pip install pandas openpyxl
