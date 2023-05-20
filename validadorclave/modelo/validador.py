# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod
from errores import ValidadorError, NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self.longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def validar_longitud(self, clave):
        if len(clave) <= self.longitud_esperada:
            raise Exception("La clave debe tener una longitud mayor a {}".format(self.longitud_esperada))

    def contiene_mayuscula(self, clave):
        if not any(caracter.isupper() for caracter in clave):
            raise Exception("La clave debe contener al menos una letra mayúscula")

    def contiene_minuscula(self, clave):
        if not any(caracter.islower() for caracter in clave):
            raise Exception("La clave debe contener al menos una letra minúscula")

    def contiene_numero(self, clave):
        if not any(caracter.isdigit() for caracter in clave):
            raise Exception("La clave debe contener al menos un número")


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def es_valida(self, clave):
        super().es_valida(clave)
        self.contiene_caracter_especial(clave)

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        if not any(caracter in caracteres_especiales for caracter in clave):
            raise Exception("La clave debe contener al menos un carácter especial")


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def es_valida(self, clave):
        super().es_valida(clave)
        self.contiene_calisto(clave)

    def contiene_calisto(self, clave):
        if 'Calisto' not in clave.lower():
            raise Exception("La clave debe contener la palabra 'Calisto' con al menos dos letras mayúsculas")


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        try:
            self.regla.es_valida(clave)
            return True
        except Exception as e:
            print(str(e))
            return False
