import streamlit as st

# Configuración de la aplicación
st.set_page_config(page_title="Calculadora Manual Pro", layout="centered")

st.title("💰 Calculadora de Nómina Directa")
st.write("Introduce los valores manualmente. Esta app no requiere archivos externos.")

# --- FORMULARIO DE DATOS ---
with st.form("calculadora_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        sueldo_base = st.number_input("Sueldo Base Mensual", value=1300000)
        dias = st.slider("Días Trabajados", 1, 30, 30)
        auxilio = st.number_input("Auxilio Transporte", value=162000)
        
    with col2:
        bonos = st.number_input("Otros Ingresos", value=0)
        salud_pct = st.number_input("% Salud", value=4.0)
        pension_pct = st.number_input("% Pensión", value=4.0)
    
    # Botón para ejecutar el cálculo
    calcular = st.form_submit_button("Calcular Ahora")

# --- LÓGICA DE CÁLCULO ---
sueldo_dia = sueldo_base / 30
devengado = sueldo_dia * dias
base_seguridad_social = devengado + bonos

desc_salud = base_seguridad_social * (salud_pct / 100)
desc_pension = base_seguridad_social * (pension_pct / 100)

neto = devengado + auxilio + bonos - (desc_salud + desc_pension)

# --- MOSTRAR RESULTADOS ---
if calcular or dias:
    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("TOTAL INGRESOS", f"${(devengado + auxilio + bonos):,.0f}")
    c2.metric("NETO A RECIBIR", f"${neto:,.0f}")
    
    st.info(f"Cálculo basado en {dias} días laborados.")

