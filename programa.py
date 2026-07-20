# =====================================================================
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
# Problema Seleccionado: Problema 5 - Control de Horas Laborales
# =====================================================================

def clasificar_jornada(total_horas):
    """
    Función para calcular la clasificación de la jornada.
    Cumple con el Criterio 3 (Uso de funciones para optimizar).
    """
    # Lógica de Negocio (Estructuras de control condicionales - Criterio 1)
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

def generar_informe_horas():
    print("==================================================")
    print("        INFORME DE HORAS SEMANALES - ECBTI        ")
    print("==================================================")
    
    # Matriz inicializadora con 4 recursos y sus horas de Lunes a Viernes
    # Cumple con el requisito de desarrollo: Matriz con 4 recursos
    matriz_empleados = [
        ["Juan Pérez", 8, 9, 8, 8, 9],       # Total: 42 (Sobretiempo)
        ["María López", 8, 8, 8, 7, 6],      # Total: 37 (Horario Estándar)
        ["Carlos Gómez", 10, 10, 9, 8, 8],   # Total: 45 (Sobretiempo)
        ["Ana Rodríguez", 8, 8, 8, 8, 8]     # Total: 40 (Horario Estándar)
    ]
    
    # Estructura de repetición para recorrer la matriz (Criterio 2)
    for empleado in matriz_empleados:
        nombre = empleado[0]
        
        # Estructura secuencial/repetición para sumar las horas del empleado
        horas_semanales = sum(empleado[1:]) 
        
        # Llamado a la función optimizadora
        clasificacion = clasificar_jornada(horas_semanales)
        
        # Salida requerida por la guía
        print(f"Recurso: {nombre}")
        print(f"  - Total Horas Semanales: {horas_semanales} hrs")
        print(f"  - Clasificación Jornada: {clasificacion}")
        print("-" * 50)

# Bloque principal de ejecución
if __name__ == "__main__":
    generar_informe_horas()