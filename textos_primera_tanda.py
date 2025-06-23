class PrimeraTanda():
    def __init__(self, texto):
        self.texto = texto

    def domingo(self):
        return ""
    def lunes(self):
        return ""
    def martes(self):
        return ""
    def miercoles(self):
        return ""
    def jueves(self):
        return ""
    def viernes(self):
        return ""
    def sabado(self):
        return ""
    
    def procesar(self):
        # Aquí se pueden agregar más métodos para procesar el texto
        return self.texto.upper()  # Ejemplo de procesamiento: convertir a mayúsculas

    def __str__(self):
        return f"Texto procesado: {self.procesar()}"