from contratos import EvaluacionBase, IAuditable
from typing import Dict, List

calcular_promedio = lambda valores: sum(valores) / len(valores) if valores else 0.0

# Herencia Simple
class ExamenAlternativas(EvaluacionBase):

    def __init__(self, id_entrega: str, nombre_alumno: str, modulo: str, pauta_oficial: Dict[int, str], respuestas_alumno: Dict[int, str]):
        super().__init__(id_entrega, nombre_alumno, modulo)
        self.pauta_oficial = pauta_oficial
        self.respuestas_alumno = respuestas_alumno
        self.detalle_correccion: List[str] = []

    def corregir_entrega(self) -> float:
        if self.corregida:
            return self.nota_final

        correctas = 0
        for num_pregunta, respuesta_correcta in self.pauta_oficial.items():
            respuesta_dada = self.respuestas_alumno.get(num_pregunta, '')

            if respuesta_dada.upper() == respuesta_correcta.upper():
                correctas += 1
                self.detalle_correccion.append(f"P{num_pregunta}: Correcta")
            else:
                self.detalle_correccion.append(f"P{num_pregunta}: Incorrecta")

        self.nota_final = round((correctas / len(self.pauta_oficial)) * 100, 1)
        self.corregida = True
        return self.nota_final


# Herencia Múltiple
class ProyectoPractico(EvaluacionBase, IAuditable):

    def __init__(self, id_entrega: str, nombre_alumno: str, modulo: str, repo_url: str, rubrica_puntajes: Dict[str, float]):
        super().__init__(id_entrega, nombre_alumno, modulo)
        self.repo_url = repo_url
        self.rubrica_puntajes: Dict[str, float] = rubrica_puntajes

    def corregir_entrega(self) -> float:
        if self.corregida:
            return self.nota_final

        valores_rubrica = list(self.rubrica_puntajes.values())
        self.nota_final = round(calcular_promedio(valores_rubrica), 1)
        self.corregida = True
        return self.nota_final

    def ejecutar_auditoria_codigo(self) -> dict:
        es_valido = "github.com" in self.repo_url.lower()
        observacion = "URL de repositorio válida" if es_valido else "El repositorio no pertenece a GitHub o es inaccesible."

        return {
            "aprobado": es_valido,
            "url_analizada": self.repo_url,
            "observaciones": observacion
        }