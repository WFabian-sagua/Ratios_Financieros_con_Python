# Autor: Fabian Sagua
import pandas as pd

# Cargar el archivo de Excel
file_path = 'ef1.xlsx'
df = pd.read_excel(file_path, sheet_name=None)

# Accedemos a la hoja de "Hoja1"
estado_situacion = df['Hoja1']

# Función para convertir los valores a numéricos (eliminando comas y otros caracteres)
def convertir_a_numero(valor):
    try:
        return pd.to_numeric(valor.replace(',', '').replace('$', '').replace(' ', ''), errors='coerce')
    except AttributeError:
        return pd.to_numeric(valor, errors='coerce')

# Extraer los valores necesarios para los cálculos de ratios financieros
efectivo_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Efectivo y Equivalentes al Efectivo', '31 de Diciembre del 2023'].values[0])
cuentas_por_cobrar_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Cuentas por Cobrar Comerciales y Otras Cuentas por Cobrar', '31 de Diciembre del 2023'].values[0])
inventarios_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Inventarios', '31 de Diciembre del 2023'].values[0])
total_activos_corrientes_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Total Activos Corrientes', '31 de Diciembre del 2023'].values[0])
pasivos_corrientes_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Total Pasivos Corrientes', '31 de Diciembre del 2023'].values[0])
capital_emitido_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Capital Emitido', '31 de Diciembre del 2023'].values[0])
total_pasivos_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Total Pasivos', '31 de Diciembre del 2023'].values[0])
total_patrimonio_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Total Patrimonio', '31 de Diciembre del 2023'].values[0])

# Ejemplo de cálculo de ratios financieros:

# 1. **Ratio de Liquidez Corriente**: Activos Corrientes / Pasivos Corrientes
liquidez_corriente = total_activos_corrientes_2023 / pasivos_corrientes_2023

# 2. **Ratio de Liquidez Ácida**: (Activos Corrientes - Inventarios) / Pasivos Corrientes
liquidez_acida = (total_activos_corrientes_2023 - inventarios_2023) / pasivos_corrientes_2023

# 3. **Ratio de Endeudamiento**: Total Pasivos / Total Patrimonio
endeudamiento = total_pasivos_2023 / total_patrimonio_2023

# 4. **Ratio de Rentabilidad sobre el Patrimonio (ROE)**: Resultados Acumulados / Capital Emitido
resultados_acumulados_2023 = convertir_a_numero(estado_situacion.loc[estado_situacion['Cuenta'] == 'Resultados Acumulados', '31 de Diciembre del 2023'].values[0])
roe = resultados_acumulados_2023 / capital_emitido_2023

# Mostrar los resultados
print(f"Ratio de Liquidez Corriente: {liquidez_corriente:.2f}")
print(f"Ratio de Liquidez Ácida: {liquidez_acida:.2f}")
print(f"Ratio de Endeudamiento: {endeudamiento:.2f}")
print(f"Ratio de Rentabilidad sobre el Patrimonio (ROE): {roe:.2f}")
