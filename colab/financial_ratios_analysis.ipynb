import gspread
from google.colab import auth
import pandas as pd

# Autenticarse en Google Colab
auth.authenticate_user()

# Autorizar gspread usando las credenciales predeterminadas de Google Colab
from google.auth.transport.requests import Request
from google.auth import default

creds, _ = default()
gc = gspread.authorize(creds)

# URL de la hoja de Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/1WUVRLy-wPcOP-no2fJL8pCcOK1NxMMiXg4ak3GJBdec/edit?usp=sharing"

# Obtener el ID del documento
sheet_id = sheet_url.split("/d/")[1].split("/")[0]

# Abrir la hoja usando su ID
spreadsheet = gc.open_by_key(sheet_id)

# Seleccionar la primera hoja (Hoja1)
worksheet = spreadsheet.get_worksheet(0)

# Obtener todos los registros y convertirlos en un DataFrame de pandas
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Mostrar las primeras filas del DataFrame para verificar los datos
#print(df.head())

# Función para convertir los valores a numéricos (eliminando comas y otros caracteres)
def convertir_a_numero(valor):
    try:
        return pd.to_numeric(valor.replace(',', '').replace('$', '').replace(' ', ''), errors='coerce')
    except AttributeError:
        return pd.to_numeric(valor, errors='coerce')

# Extraer los valores necesarios para los cálculos de ratios financieros
efectivo_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Efectivo y Equivalentes al Efectivo', '31 de Diciembre del 2023'].values[0])
cuentas_por_cobrar_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Cuentas por Cobrar Comerciales y Otras Cuentas por Cobrar', '31 de Diciembre del 2023'].values[0])
inventarios_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Inventarios', '31 de Diciembre del 2023'].values[0])
total_activos_corrientes_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Total Activos Corrientes', '31 de Diciembre del 2023'].values[0])
pasivos_corrientes_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Total Pasivos Corrientes', '31 de Diciembre del 2023'].values[0])
capital_emitido_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Capital Emitido', '31 de Diciembre del 2023'].values[0])
total_pasivos_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Total Pasivos', '31 de Diciembre del 2023'].values[0])
total_patrimonio_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Total Patrimonio', '31 de Diciembre del 2023'].values[0])

# Ejemplo de cálculo de ratios financieros:

# 1. **Ratio de Liquidez Corriente**: Activos Corrientes / Pasivos Corrientes
liquidez_corriente = total_activos_corrientes_2023 / pasivos_corrientes_2023

# 2. **Ratio de Liquidez Ácida**: (Activos Corrientes - Inventarios) / Pasivos Corrientes
liquidez_acida = (total_activos_corrientes_2023 - inventarios_2023) / pasivos_corrientes_2023

# 3. **Ratio de Endeudamiento**: Total Pasivos / Total Patrimonio
endeudamiento = total_pasivos_2023 / total_patrimonio_2023

# 4. **Ratio de Rentabilidad sobre el Patrimonio (ROE)**: Resultados Acumulados / Capital Emitido
resultados_acumulados_2023 = convertir_a_numero(df.loc[df['Cuenta'] == 'Resultados Acumulados', '31 de Diciembre del 2023'].values[0])
roe = resultados_acumulados_2023 / capital_emitido_2023

# Mostrar los resultados
print(f"Ratio de Liquidez Corriente: {liquidez_corriente:.2f}")
print(f"Ratio de Liquidez Ácida: {liquidez_acida:.2f}")
print(f"Ratio de Endeudamiento: {endeudamiento:.2f}")
print(f"Ratio de Rentabilidad sobre el Patrimonio (ROE): {roe:.2f}")
