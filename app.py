import streamlit as st
from datetime import datetime, timedelta

# Configuración de la aplicación
st.set_page_config(page_title="Calculadora Días Hábiles CO", page_icon="📅")

st.title("🇨🇴 Calculadora de Días Hábiles")
st.write("Resta 30 días hábiles a una fecha (Colombia 2026).")

# Festivos Colombia 2026 (Ley Emiliani aplicada)
festivos_2026 = [
    "2026-01-01", "2026-01-12", "2026-03-23", "2026-04-02", "2026-04-03",
    "2026-05-01", "2026-05-18", "2026-06-08", "2026-06-15", "2026-06-29",
    "2026-07-20", "2026-08-07", "2026-08-17", "2026-10-12", "2026-11-02",
    "2026-11-16", "2026-12-08", "2026-12-25"
]
# Convertimos a formato de fecha de Python
festivos_dates = [datetime.strptime(f, "%Y-%m-%d").date() for f in festivos_2026]

def calcular_resta_habiles(fecha_inicio, dias_a_restar):
    fecha_actual = fecha_inicio
    contador = 0
    while contador < dias_a_restar:
        fecha_actual -= timedelta(days=1)
        # weekday() < 5 significa Lunes a Viernes (0,1,2,3,4)
        if fecha_actual.weekday() < 5 and fecha_actual not in festivos_dates:
            contador += 1
    return fecha_actual

# Interfaz de usuario para iPad
fecha_ref = st.date_input("Selecciona la fecha de inicio:", value=datetime.now().date())

if st.button("Calcular -30 días hábiles"):
    resultado = calcular_resta_habiles(fecha_ref, 30)
    
    st.divider()
    st.success("Resultado del cálculo:")
    st.header(f"📅 {resultado.strftime('%d / %m / %Y')}")
    st.info(f"Día resultante: {resultado.strftime('%A')}")

st.caption("Nota: El cálculo omite sábados, domingos y los festivos oficiales de Colombia.")
