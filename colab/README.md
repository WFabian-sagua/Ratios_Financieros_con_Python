# **RATIOS FINANCIEROS**  
### Presentado por: Fabian Sagua, Fundador de **DATA COUNT AI**  

Este proyecto automatiza el cálculo de ratios financieros utilizando datos almacenados en una hoja de cálculo de Google Sheets.  
Se conecta directamente a la hoja de Google Sheets mediante la API de Google, extrae información financiera y calcula indicadores clave como:  
**Liquidez Corriente**, **Liquidez Ácida**, **Ratio de Endeudamiento** y **Rentabilidad sobre el Patrimonio (ROE)**.  

### Funciones principales:  
1. **Conexión a Google Sheets**: Utiliza las credenciales predeterminadas de Google Colab para acceder y descargar datos de una hoja específica.  
2. **Procesamiento de datos**: Convierte valores de texto en datos numéricos válidos y realiza validaciones para garantizar integridad.  
3. **Cálculo de ratios financieros**:  
   - **Liquidez Corriente**: Relación entre activos corrientes y pasivos corrientes.  
   - **Liquidez Ácida**: Relación entre activos corrientes (sin inventarios) y pasivos corrientes.  
   - **Endeudamiento**: Relación entre total de pasivos y total del patrimonio.  
   - **Rentabilidad sobre el Patrimonio (ROE)**: Relación entre resultados acumulados y capital emitido.  
4. **Visualización de resultados**: Presenta los cálculos en la consola para un análisis inmediato.  

### Librerías utilizadas:  
- **gspread**: Para interactuar con Google Sheets.  
- **oauth2client**: Para autenticación con la API de Google.  
- **pandas**: Para procesar y analizar datos. 

### Nota Importante:  
Si eres nuevo usuario de Google Colab, debes instalar las librerías mencionadas con el siguiente comando:

```bash
pip install pandas gspread oauth2client

```

### Contacto:  
📞 **931555720**  
📧 **info@datacountai.digital**  
🌐 [www.datacountai.digital](https://www.datacountai.digital)  
