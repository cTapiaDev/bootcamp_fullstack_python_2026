from contratos import EvaluacionBase, IAuditable
from typing import List

class GestorEvaluaciones:

    def __init__(self):
        self.entregas_registradas: List[EvaluacionBase] = []

    def registrar_nueva_entrega(self, evaluacion: EvaluacionBase) -> None:
        self.entregas_registradas.append(evaluacion)
        print(f"Entrega {evaluacion.id_entrega} registrado con éxito.")

    def corregir_todas_las_entregas(self) -> None:
        if not self.entregas_registradas:
            print("No hay entregas registradas.")
            return

        print("\n---INICIANDO PROCESO DE CORRECCIÓN MASIVA---")
        for entrega in self.entregas_registradas:
            if not entrega.corregida:
                nota = entrega.corregir_entrega()
                print(f"Terminado: {entrega.nombre_alumno} | Módulo: {entrega.modulo} | Nota: {nota}")

        print("-" * 20)

    def auditar_proyectos(self) -> None:
        print("\n---INICIANDO AUDITORÍA DE CÓDIGO---")
        auditorias_realizadas = 0

        for entrega in self.entregas_registradas:
            if isinstance(entrega, IAuditable):
                auditorias_realizadas += 1
                resultado = entrega.ejecutar_auditoria_codigo()

                estado = "APROBADO" if resultado["aprobado"] else "REPROBADO"
                print(f"{estado} | Alumno: {entrega.nombre_alumno} | Obs: {resultado["observaciones"]}")

        if auditorias_realizadas == 0:
            print("No existen proyectos prácticos auditables en el registro.")
        print("-" * 20)

    def listar_boletin_general(self) -> None:
        print("\n---BOLETÍN DE NOTAS---")
        for entrega in self.entregas_registradas:
            nota_str = f"{entrega.nota_final}/100" if entrega.corregida else "Pendiente..."
            print(f"{entrega.obtener_resumen()} | Calificación: {nota_str}")
