import streamlit as st

# Eliminamos cualquier rastro de subida de archivos
st.set_page_config(page_title="Calculadora Manual", layout="centered")

st.title("✅ Calculadora 100% Manual")
st.write("Esta versión NO usa Excel. Introduce los datos abajo:")

# Entradas manuales
sueldo = st.number_input("Sueldo Base ($)", value=1300000)
transporte = st.number_input("Auxilio Transporte ($)", value=162000)
dias = st.slider("Días Trabajados", 1, 30, 30)

# Cálculos directos
pago_dias = (sueldo / 30) * dias
total = pago_dias + transporte

st.divider()

# Resultados grandes para ver en iPad
st.metric("PAGO TOTAL NETO", f"${total:,.0f}")

st.write(f"Detalle: ${pago_dias:,.0f} de sueldo + ${transporte:,.0f} de transporte.")
