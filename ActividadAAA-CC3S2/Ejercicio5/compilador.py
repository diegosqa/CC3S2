import re

class ErrorLexico(Exception):
    pass

class ErrorSintactico(Exception):
    pass

class Compilador:
    def __init__(self):
        self.tokens = []
    
    def analizar_lexico(self, codigo):
        # Analizador léxico básico utilizando expresiones regulares
        patron = r'print|\d+|\+|\(|\)|\*'
        tokens = re.findall(patron, codigo)
        if len(''.join(tokens)) != len(codigo.replace(" ", "")):
            raise ErrorLexico("Error léxico: Token inválido en el código.")
        self.tokens = tokens

    def analizar_sintactico(self):
        # Analizador sintáctico simple que verifica la estructura
        if self.tokens[0] != 'print' or self.tokens[1] != '(' or self.tokens[-1] != ')':
            raise ErrorSintactico("Error sintáctico: Falta un paréntesis o un operador.")
        if '*' in self.tokens:
            raise ErrorLexico("Error léxico: Uso incorrecto del operador '*'.")
    
    def ejecutar(self):
        # Ejecutar código validado
        if len(self.tokens) == 6 and self.tokens[2].isdigit() and self.tokens[3] == '+' and self.tokens[4].isdigit():
            return int(self.tokens[2]) + int(self.tokens[4])
        raise ErrorSintactico("Error sintáctico: Estructura inválida.")
    
    def compilar_y_ejecutar(self, codigo):
        self.analizar_lexico(codigo)
        self.analizar_sintactico()
        return self.ejecutar()

