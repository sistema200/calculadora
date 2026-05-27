import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("-->| El Chino |<--")
        self.geometry("300x500")
        self.resizable(False, False)

        # Variable que almacena lo que se muestra en la pantalla
        self.expresion = tk.StringVar()

        # Pantalla de la calculadora
        pantalla = tk.Entry(self, textvariable=self.expresion,
                            font=("Arial", 30), bd=20, relief=tk.RIDGE,
                            justify="right")
        pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

        # Definir los botones
        botones = [
            ("/", 1, 0), ("*", 1, 1), ("C", 1, 2), ("←", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("%", 4, 3),
            ("0", 5, 0,), ("00", 5, 1), (".", 5, 2), ("=", 5, 3),
            ("El Chino", 6, 0, 4)
        ]

        for (texto, fila, columna, *colspan) in botones:
            ancho = 5
            comando = lambda t=texto: self._presionar(t)
            btn = tk.Button(self, text=texto, width=ancho, height=2,
                            font=("Arial", 18), command=comando)
            if colspan:
                btn.grid(row=fila, column=columna, columnspan=colspan[0],
                         padx=5, pady=5, sticky="nsew")
            else:
                btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

        # Ajustar pesos de filas y columnas para que los botones se expandan uniformemente
        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def _presionar(self, tecla):
        """Maneja la lógica de cada botón."""
        if tecla == "C":
            self.expresion.set("")
        elif tecla == "El Chino":
            self.expresion.set("")
        elif tecla == "←":
            actual = self.expresion.get()
            self.expresion.set(actual[:-1])   # elimina el último carácter
        elif tecla == "=":
            # Evaluar la expresión
            try:
                resultado = eval(self.expresion.get())
                self.expresion.set(str(resultado))
            except Exception:
                self.expresion.set("Error")
        else:
            # Añadir el carácter pulsado a la expresión
            actual = self.expresion.get()
            self.expresion.set(actual + tecla)


if __name__ == "__main__":
    app = Calculadora ()
    app.mainloop()
