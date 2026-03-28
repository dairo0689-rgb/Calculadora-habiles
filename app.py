import streamlit as st

# Configuración de página
st.set_page_config(page_title="Calculadora de Sueldo Pro", page_icon="💰")

st.title("💸 Calculadora de Nómina Editable")
st.markdown("Introduce los valores manualmente para calcular el sueldo neto.")

# --- SECCIÓN DE ENTRADA DE DATOS ---
with st.container():
    st.subheader("📌 Datos Básicos")
    col1, col2 = st.columns(2)
    
    with col1:
        sueldo_base = st.number_input("Sueldo Base ($)", min_value=0.0, value=1300000.0, step=10000.0)
        dias_trabajados = st.number_input("Días Trabajados", min_value=0, max_value=30, value=30)
    
    with col2:
        auxilio_transporte = st.number_input("Auxilio de Transporte ($)", min_value=0.0, value=162000.0)
        otros_bonos = st.number_input("Otros Bonos/Comisiones ($)", min_value=0.0, value=0.0)

st.divider()

# --- SECCIÓN DE DEDUCCIONES ---
with st.container():
    st.subheader("📉 Deducciones de Ley")
    c1, c2 = st.columns(2)
    
    with c1:
        pct_salud = st.slider("Salud (%)", 0.0, 10.0, 4.0)
    with c2:
        pct_pension = st.slider("Pensión (%)", 0.0, 10.0, 4.0)

# --- CÁLCULOS LÓGICOS ---
# Proporcional del sueldo por días trabajados
sueldo_devengado = (sueldo_base / 30) * dias_trabajados

# Base para seguridad social (Sueldo devengado + bonos, usualmente sin auxilio transporte)
base_seguridad_social = sueldo_devengado + otros_bonos

descuento_salud = base_seguridad_social * (pct_salud / 100)
descuento_pension = base_seguridad_social * (pct_pension / 100)

total_deducciones = descuento_salud + descuento_pension
sueldo_neto = sueldo_devengado + auxilio_transporte + otros_bonos - total_deducciones

# --- MOSTRAR RESULTADOS ---
st.divider()
st.subheader("📋 Resumen de Pago")

res1, res2, res3 = st.columns(3)
res1.metric("Total Devengado", f"${(sueldo_devengado + auxilio_transporte + otros_bonos):,.0f}")
res2.metric("Total Deducciones", f"-${total_deducciones:,.0f}", delta_color="inverse")
res3.metric("NETO A RECIBIR", f"${sueldo_neto:,.0f}")

# Tabla detallada para claridad
datos_tabla = {
    "Concepto": ["Sueldo por días", "Auxilio Transporte", "Bonificaciones", "Salud", "Pensión"],
    "Ingresos": [sueldo_devengado, auxilio_transporte, otros_bonos, 0, 0],
    "Egresos": [0, 0, 0, descuento_salud, descuento_pension]
}

st.table(datos_tabla)

if st.button("✅ Confirmar y Guardar"):
    st.balloons()
    st.success(f"Cálculo finalizado: El neto es ${sueldo_neto:,.0f}")
