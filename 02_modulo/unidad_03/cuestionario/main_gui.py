import tkinter as tk
from tkinter import messagebox
import level
import question as q

actualizar_widget = lambda widget, propiedad, valor: widget.config(**{propiedad: valor})

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("=== QUIZ: FRONTEND ===")
        self.root.geometry("650x450")
        self.root.configure(padx=20, pady=20)

        self.p_level = 2
        self.preguntas_totales = self.p_level * 3
        self.n_pregunta = 1
        self.alternativas_actuales = []

        self.lbl_nivel = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#2563eb")
        self.lbl_nivel.pack(pady=(0, 10))

        self.lbl_enunciado = tk.Label(root, text="", font=("Arial", 11), wraplength=600, justify="center")
        self.lbl_enunciado.pack(pady=(0, 20))

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(fill="x")

        self.botones = []
        for i in range(4):
            btn = tk.Button(self.frame_botones, text="", font=("Arial", 10), cursor="hand2", command=lambda idx=i: self.evaluar_respuesta(idx))
            btn.pack(fill="x", pady=5, ipady=5)
            self.botones.append(btn)

        self.cargar_siguiente_escenario()

    def cargar_siguiente_escenario(self):
        if self.n_pregunta > self.preguntas_totales:
            messagebox.showinfo("¡Felicidades!", "Has respondido todas las preguntas correctamente.")
            self.root.destroy()
            return

        dificultad = level.choose_level(self.n_pregunta, self.p_level)
        texto_nivel = f"Pregunta {self.n_pregunta} de {self.preguntas_totales} | Nivel: {dificultad.upper()}"
        actualizar_widget(self.lbl_nivel, "text", texto_nivel)

        enunciado, self.alternativas_actuales = q.choose_q(dificultad)
        actualizar_widget(self.lbl_enunciado, "text", enunciado)

        for i, alt in enumerate(self.alternativas_actuales):
            actualizar_widget(self.botones[i], "text", f"{chr(65+i)}. {alt[0]}")
            actualizar_widget(self.botones[i], "state", tk.NORMAL)

    def evaluar_respuesta(self, indice_seleccionado):
        es_correcta = self.alternativas_actuales[indice_seleccionado][1] == 1

        if es_correcta:
            messagebox.showinfo("Resultado", "¡Respuesta Correcta! Avanza a la siguiente ronda")
            self.n_pregunta += 1
            self.cargar_siguiente_escenario()
        else:
            messagebox.showerror("Game Over", "Respuesta Incorrecta")
            self.root.destroy()

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    app = AplicacionGUI(ventana_principal)
    ventana_principal.mainloop()