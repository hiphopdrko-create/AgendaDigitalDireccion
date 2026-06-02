import tkinter as tk


def abrir_alumnos():
    print("Abrir módulo de alumnos")


def abrir_maestros():
    print("Abrir módulo de maestros")


def abrir_citas():
    print("Abrir módulo de citas")


def abrir_busqueda():
    print("Abrir búsqueda")


# Ventana principal
ventana = tk.Tk()
ventana.title("Agenda Digital de Dirección")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Título
titulo = tk.Label(
    ventana,
    text="Agenda Digital de Dirección",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

# Botones
btn_alumnos = tk.Button(
    ventana,
    text="Alumnos",
    width=20,
    height=2,
    command=abrir_alumnos
)
btn_alumnos.pack(pady=5)

btn_maestros = tk.Button(
    ventana,
    text="Maestros",
    width=20,
    height=2,
    command=abrir_maestros
)
btn_maestros.pack(pady=5)

btn_citas = tk.Button(
    ventana,
    text="Citas",
    width=20,
    height=2,
    command=abrir_citas
)
btn_citas.pack(pady=5)

btn_busqueda = tk.Button(
    ventana,
    text="Buscar",
    width=20,
    height=2,
    command=abrir_busqueda
)
btn_busqueda.pack(pady=5)

btn_salir = tk.Button(
    ventana,
    text="Salir",
    width=20,
    height=2,
    command=ventana.destroy
)
btn_salir.pack(pady=20)

ventana.mainloop()