# --- 1. Definición de la Función ---
# El programa "aprende" que existe esta función,
# pero NO ejecuta este código todavía.
def mi_funcion_saludo():
    print("      -> 2. ¡Estoy DENTRO de la función!")
    print("      -> 3. La función está terminando... Vuelvo...")

# --- Programa Principal ---
# La ejecución SIEMPRE comienza aquí, fuera de las funciones.

print("1. Estoy ANTES de la llamada a la función.")

# --- 2. La Llamada (Invocación) ---
# Esta línea le dice al programa:
# "¡PAUSA aquí y SALTA al código de 'mi_funcion_saludo'!"
mi_funcion_saludo()

# --- 3. El Retorno ---
# El programa REGRESA a este punto exacto
# y continúa con la siguiente línea.
print("4. Estoy DESPUÉS de la llamada a la función.")
print("5. El programa ha terminado.")
