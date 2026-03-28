import streamlit as st

# Configuración de la interfaz
st.set_page_config(page_title="Calculadora Manual", layout="centered")

st.title("💰 Calculadora de Nómina")
st.markdown("Ajusta los valores directamente. **No se requiere subir ningún Excel.**")

# --- ENTRADA DE DATOS EDITABLE ---
st.subheader("📌 Datos del Empleado")

col1, col2 = st.columns(2)

with col1:
    # Estos campos reemplazan las celdas de tu Excel
    sueldo_base = st.number_input("Sueldo Base ($)", value=1300000, step=10000)
    dias_trabajados = st.slider("Días Trabajados", 0, 30, 30)
    auxilio_transporte = st.number_input("Auxilio de Transporte ($)", value=162000)

with col2:
    bonificaciones = st.number_input("Otros Ingresos / Bonos ($)", value=0)
    pct_salud = st.number_input("Descuento Salud (%)", value=4.0, step=0.1)
    pct_pension = st.number_input("Descuento Pensión (%)", value=4.0, step=0.1)

st.divider()

# --- LÓGICA DE CÁLCULO ---
# Sueldo proporcional a los días
sueldo_devengado = (sueldo_base / 30) * dias_trabajados

# Base para seguridad social (Sueldo + Bonos)
base_calculo = sueldo_devengado + bonificaciones

# Deducciones
valor_salud = base_calculo * (pct_salud / 100)
valor_pension = base_calculo * (pct_pension / 100)

# TOTAL NETO
total_ingresos = sueldo_devengado + auxilio_transporte + bonificaciones
total_egresos = valor_salud + valor_pension
neto_final = total_ingresos - total_egresos

# --- RESULTADOS ---
st.subheader("💵 Resultado del Cálculo")

c1, c2, c3 = st.columns(3)
c1.metric("Ingresos", f"${total_ingresos:,.0f}")
c2.metric("Deducciones", f"-${total_egresos:,.0f}", delta_color="inverse")
c3.metric("Neto a Pagar", f"${neto_final:,.0f}")

# Tabla resumen para mayor claridad
st.table({
    "Concepto": ["Sueldo Devengado", "Auxilio Transporte", "Bonos", "Salud", "Pensión", "TOTAL NETO"],
    "Valor": [
        f"${sueldo_devengado:,.0f}", 
        f"${auxilio_transporte:,.0f}", 
        f"${bonificaciones:,.0f}", 
        f"-${valor_salud:,.0f}", 
        f"-${valor_pension:,.0f}", 
        f"${neto_final:,.0f}"
    ]
})
