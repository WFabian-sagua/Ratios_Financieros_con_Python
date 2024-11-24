# **Análisis de Ratios Financieros - Proyecto Completo**

**Desarrollado por:** Fabian Sagua, Fundador de **DATA COUNT AI**

Este proyecto está diseñado para automatizar el cálculo de **ratios financieros** utilizando datos almacenados en archivos Excel. Los cálculos se realizan a través de dos versiones: una para **entornos de escritorio** y otra basada en **Google Colab**, permitiendo la ejecución en un entorno web interactivo. El propósito es proporcionar una herramienta útil para analizar la situación financiera de una empresa mediante los **ratios financieros** más relevantes, tales como:

- **Liquidez Corriente**
- **Liquidez Ácida**
- **Endeudamiento**
- **Rentabilidad sobre el Patrimonio (ROE)**

## **Descripción del Proyecto**

Este repositorio incluye dos versiones del mismo análisis de ratios financieros:

1. **Versión de Escritorio**: Implementada en Python utilizando bibliotecas como **pandas** y **openpyxl** para leer y procesar los datos de un archivo Excel local. Los cálculos y resultados se visualizan en la consola.
2. **Versión de Google Colab**: Una versión interactiva donde puedes cargar el archivo Excel desde Google Drive, realizar los cálculos de los ratios financieros y visualizar los resultados directamente en el entorno web de Google Colab.

Ambas versiones permiten a los usuarios calcular de manera eficiente y sencilla los principales ratios financieros, mejorando el análisis y la toma de decisiones.

## **Objetivos Principales**

- **Automatizar el Cálculo de Ratios Financieros**: Calculando la **Liquidez Corriente**, **Liquidez Ácida**, **Endeudamiento** y **Rentabilidad sobre el Patrimonio (ROE)** utilizando los datos de un archivo Excel.
- **Interactividad**: Ofrecer dos formas de ejecución, una en **Google Colab** para aquellos que prefieren trabajar en la web y otra en **escritorio** para usuarios locales con Python.
- **Facilidad de Uso**: Diseñado para que los usuarios puedan copiar, pegar y ejecutar el código fácilmente, garantizando que comprendan el proceso detrás de los cálculos.

## **Características y Funcionalidades**

- **Conexión y Lectura de Datos**: Ambos métodos permiten la carga de datos financieros desde archivos Excel, utilizando bibliotecas como **pandas** y **openpyxl**.
- **Cálculos de Ratios Financieros**: Implementación de los siguientes ratios:
  - **Liquidez Corriente**: Activos Corrientes / Pasivos Corrientes
  - **Liquidez Ácida**: (Activos Corrientes - Inventarios) / Pasivos Corrientes
  - **Endeudamiento**: Total Pasivos / Total Patrimonio
  - **Rentabilidad sobre el Patrimonio (ROE)**: Resultados Acumulados / Capital Emitido
- **Validación de Datos**: Limpieza y conversión de datos para asegurar que se utilicen valores numéricos válidos para los cálculos.
- **Visualización de Resultados**: Los resultados se muestran de manera clara en la consola para la versión de escritorio y en celdas interactivas en Google Colab.

## **Requisitos**

### **Versión de Escritorio (Python)**
Para ejecutar la versión de escritorio, asegúrate de tener instaladas las siguientes librerías:

- **Python 3.x**
- **Librerías necesarias**:
  - pandas
  - openpyxl

Para instalar las librerías, puedes usar el siguiente comando en tu terminal o consola:

```bash
pip install pandas openpyxl
