class Usuario:
    def __init__(self, nome, matricula):
        self._nome = nome 
        self._matricula = matricula
        
    def inserir_novo_professor(self, nome, matricula, pote):
        with open("usuarios.txt", 'a', encoding= "utf-8") as arquivo:
            arquivo.write(f"\nNome: {nome} Matricula: {matricula} Pote: {pote}")

    def inserir_novo_aluno(self, nome, matricula, curso):
        with open("usuarios.txt", 'a', encoding= "utf-8") as arquivo:
            arquivo.write(f"\nNome: {nome} Matricula: {matricula}, Curso: {curso}")

    def status_pote(self, nome, matricula, numero ,pote):
        with open("usuarios.txt", 'w', encoding= "utf-8") as arquivo:
            arquivo.write(f"\nNome: {nome} Matricula: {matricula} Numero: {numero} Pote: {pote}")
                


class Aluno(Usuario):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self._curso = curso
        

class Professor(Usuario):
    def __init__(self, nome, matricula, numero, pote=None):
        super().__init__(nome, matricula)
        self._numero_pote = numero
        self._pote = None
    



    
