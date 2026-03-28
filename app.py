<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Días Hábiles Colombia</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; padding: 20px; background-color: #f4f7f6; }
        .card { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 400px; width: 100%; }
        h2 { color: #2c3e50; margin-top: 0; font-size: 1.5rem; }
        label { display: block; margin-bottom: 8px; font-weight: bold; color: #555; }
        input { width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; font-size: 1rem; }
        button { width: 100%; padding: 12px; background-color: #007bff; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 1rem; transition: background 0.3s; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; padding: 15px; border-radius: 6px; background-color: #e9ecef; display: none; }
        .result span { display: block; font-size: 1.1rem; color: #333; }
        .date-out { font-weight: bold; color: #d9534f; }
    </style>
</head>
<body>

<div class="card">
    <h2>Calculadora (Colombia)</h2>
    <p>Resta 30 días hábiles a una fecha:</p>
    
    <label for="fechaInicial">Selecciona la fecha:</label>
    <input type="date" id="fechaInicial">
    
    <button onclick="calcular()">Calcular Fecha</button>

    <div id="resultado" class="result">
        <span>La fecha resultante es:</span>
        <span id="fechaFinal" class="date-out"></span>
    </div>
</div>

<script>
    // Festivos Colombia 2026 (Ejemplo simplificado de fechas fijas y móviles)
    const festivos2026 = [
        "2026-01-01", "2026-01-12", "2026-03-23", "2026-04-02", "2026-04-03",
        "2026-05-01", "2026-05-18", "2026-06-08", "2026-06-15", "2026-06-29",
        "2026-07-20", "2026-08-07", "2026-08-17", "2026-10-12", "2026-11-02",
        "2026-11-16", "2026-12-08", "2026-12-25"
    ];

    function esFestivo(fecha) {
        const f = fecha.toISOString().split('T')[0];
        return festivos2026.includes(f);
    }

    function calcular() {
        let fechaInput = document.getElementById('fechaInicial').value;
        if (!fechaInput) {
            alert("Por favor selecciona una fecha");
            return;
        }

        let fecha = new Date(fechaInput + "T00:00:00");
        let diasARestar = 30;

        while (diasARestar > 0) {
            fecha.setDate(fecha.getDate() - 1);
            let diaSemana = fecha.getDay(); // 0 es Domingo, 6 es Sábado

            // Si no es sábado (6), ni domingo (0), ni festivo
            if (diaSemana !== 0 && diaSemana !== 6 && !esFestivo(fecha)) {
                diasARestar--;
            }
        }

        const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        document.getElementById('fechaFinal').innerText = fecha.toLocaleDateString('es-CO', opciones);
        document.getElementById('resultado').style.display = 'block';
    }
</script>

</body>
</html>
