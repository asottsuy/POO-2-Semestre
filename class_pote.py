class Pote:
    def __init__(self, numero):
        self._numero = numero
        self._chave = True
        self._caneta = True
        self._ctrl_ar = True
        self._ctrl_projetor = True

    def mostrar_conteudo_pote(self):
        print(f"""
        Chave: {self._chave} - Numero: {self._numero}
        Caneta: {self._caneta} - Controle Ar: { self._ctrl_ar} - Controle Projetor: {self._ctrl_projetor}""")
        

    