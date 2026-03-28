import streamlit as st

# Configuración optimizada para visualización en iPad
st.set_page_config(page_title="Calculadora de Nómina Directa", layout="centered")

# Estilo personalizado para botones y métricas
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_style=True)

st.title("📊 Calculadora de Sueldo Automática")
st.info("Ajusta los valores abajo para ver el cálculo neto al instante.")

# --- ENTRADA DE DATOS (CAMPOS EDITABLES) ---
st.subheader("📝 Parámetros de la Nómina")

# Usamos columnas para aprovechar el ancho de la pantalla del iPad
col1, col2 = st.columns(2)

with col1:
    sueldo_base = st.number_input("Sueldo Base Mensual ($)", value=1300000, step=50000)
    dias_trabajados = st.slider("Días Laborados", 0, 30, 30)
    otros_ingresos = st.number_input("Bonificaciones / Otros ($)", value=0, step=10000)

with col2:
    auxilio_transporte = st.number_input("Auxilio de Transporte ($)", value=162000)
    pct_salud = st.number_input("Descuento Salud (%)", value=4.0, step=0.5)
    pct_pension = st.number_input("Descuento Pensión (%)", value=4.0, step=0.5)

st.divider()

# --- LÓGICA DE CÁLCULO (Síncrona) ---
# Cálculo del básico según días
sueldo_proporcional = (sueldo_base / 30) * dias_trabajados

# Base para descuentos (Sueldo proporcional + bonos)
ibc = sueldo_proporcional + otros_ingresos

descuento_salud = ibc * (pct_salud / 100)
descuento_pension = ibc * (pct_pension / 100)
total_deducciones = descuento_salud + descuento_pension

# Resultado Final
neto_pagar = sueldo_proporcional + auxilio_transporte + otros_ingresos - total_deducciones

# --- VISUALIZACIÓN DE RESULTADOS ---
st.subheader("💰 Resumen del Pago")

# Métricas grandes y claras
m1, m2, m3 = st.columns(3)
m1.metric("Ingresos Totales", f"${(sueldo_proporcional + auxilio_transporte + otros_ingresos):,.0f}")
m2.metric("Deducciones", f"-${total_deducciones:,.0f}", delta_color="inverse")
m3.metric("NETO A PAGAR", f"${neto_pagar:,.0f}")

# Desglose detallado
with st.expander("Ver detalle de la liquidación"):
    st.write(f"**Sueldo por {dias_trabajados} días:** ${sueldo_proportional:,.0f}")
    st.write(f"**Auxilio de Transporte:** ${auxilio_transporte:,.0f}")
    st.write(f"**Descuento Salud ({pct_salud}%):** -${descuento_salud:,.0f}")
    st.write(f"**Descuento Pensión ({pct_pension}%):** -${descuento_pension:,.0f}")

# Botón para simular guardado o impresión
if st.button("💾 Generar Comprobante"):
    st.balloons()
    st.success("Cálculo listo para registro.")
