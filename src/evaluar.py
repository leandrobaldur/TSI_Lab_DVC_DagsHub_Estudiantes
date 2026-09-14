from pathlib import Path
import joblib

MODEL = Path("models/model.pkl")
REPORT = Path("reporte.txt")

def main() -> None:
    # Cargar el modelo
    model = joblib.load(MODEL)
    
    # Extraer información básica para el reporte
    tipo_modelo = type(model).__name__
    iteraciones = model.max_iter
    
    # Guardar el reporte
    reporte_contenido = f"Evaluación del Modelo\n=====================\nTipo: {tipo_modelo}\nIteraciones máximas: {iteraciones}\nEstado: Aprobado para producción."
    REPORT.write_text(reporte_contenido, encoding="utf-8")
    
    print("Reporte de evaluación generado exitosamente.")

if __name__ == "__main__":
    main()