class Potencia:
    def __init__(self,potencia:object):
        self._potencia=2 if potencia is SumaDeCuadrados else 3 if potencia is SumaDeCubos else 0

    def resultado(self):
        pass
class SumaDeCuadrados(Potencia):

    def __init__(self,numero:int):
        super().__init__(SumaDeCuadrados)
        self._resultado = sum([int(i) ** self._potencia for i in str(numero)])

    def resultado(self):
        return self._resultado

class SumaDeCubos(Potencia):

    def __init__(self, numero:int):

        super().__init__(SumaDeCubos)
        self._resultado = sum([int(i) ** self._potencia for i in str(numero)])

    def resultado(self):
        return self._resultado







