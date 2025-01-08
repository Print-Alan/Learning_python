#Administrador de recetas
from pathlib import Path,PureWindowsPath


carpeta_recetas = Path(Path.home(),"Desktop","Ilearn-py","Dia6","Recetas")
ruta_windows = PureWindowsPath(carpeta_recetas)

cantidad_recetas = sum(1 for archivo in carpeta_recetas.rglob("*.txt") if archivo.is_file())


print(f"Bienvenido\nEsta es tu ruta de las recetas:   {ruta_windows}\n")
print(f"Actualmente tienes {cantidad_recetas} recetas disponibles.\n")

r = input("""
        [1] - leer receta
        [2] - crear receta
        [3] - crear categoria
        [4] - eliminar receta
        [5] - eliminar categoria
        [6] - finalizar programa
        ¿Qué categoria eliges?: """)

if r == 6:
    print("Programa cerrado")
else:
    print("No se que poner")
    