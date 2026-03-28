import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calculadora de Nómina", layout="centered")

st.title("💰 Procesador de Sueldos y Nómina")
st.write("Sube el archivo `Calculadora Sueldo.xlsx` para calcular el neto a pagar.")

uploaded_file = st.file_uploader("Cargar archivo Excel", type=["csv", "xlsx"])

if uploaded_file:
    # Leemos el archivo. Si es CSV usamos read_csv, si es Excel read_excel
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # --- EXTRACCIÓN DE DATOS SEGÚN TU EXCEL ---
        # Basado en la estructura del archivo subido:
        # Columna 0 suele ser la etiqueta, Columna 1 el valor.
        
        sueldo_base = df.iloc[0, 1]  # Fila 1, Columna B
        dias_trabajados = df.iloc[1, 1] 
        auxilio_transporte = df.iloc[2, 1]
        
        st.subheader("Datos de Entrada")
        col1, col2 = st.columns(2)
        col1.metric("Sueldo Base", f"${sueldo_base:,.0f}")
        col2.metric("Días", int(dias_trabajados))

        if st.button("🧮 Calcular Nómina"):
            # --- FÓRMULAS INTEGRADAS ---
            # 1. Proporcional de sueldo
            sueldo_devengado = (sueldo_base / 30) * dias_trabajados
            
            # 2. Descuentos de Ley (Ejemplo: 4% Salud, 4% Pensión)
            salud = sueldo_devengado * 0.04
            pension = sueldo_devengado * 0.04
            
            # 3. Total Neto
            total_neto = sueldo_devengado + auxilio_transporte - (salud + pension)

            # --- MOSTRAR RESULTADOS ---
            st.divider()
            st.success(f"### Neto a Pagar: ${total_neto:,.0f}")
            
            resultados = {
                "Concepto": ["Sueldo Devengado", "Auxilio Transporte", "Salud (4%)", "Pensión (4%)", "TOTAL NETO"],
                "Valor": [sueldo_devengado, auxilio_transporte, -salud, -pension, total_neto]
            }
            
            df_res = pd.DataFrame(resultados)
            st.table(df_res.style.format({"Valor": "${:,.0f}"}))

            # Opción para descargar el resultado en el iPad
            csv_data = df_res.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Descargar Reporte", csv_data, "nomina_calculada.csv", "text/csv")

    except Exception as e:
        st.error(f"Error al leer las celdas: Asegúrate de que el formato sea el correcto. {e}")

else:
    st.info("💡 Consejo: Asegúrate de que el nombre de las filas coincida con el orden de tu Excel original.")

