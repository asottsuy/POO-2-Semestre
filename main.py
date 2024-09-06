from class_estante import Estante
from class_pote import Pote
from class_usuario import Usuario, Aluno, Professor

class Funcoes():

    def erro():
        print("Erro! Digite um valor válido")
    

"""
r -> ler algo
w -> escrever algo
r+ ->ler e escrever algo
a -> acrescentar algo

"""
estante = Estante()
professor = Professor("Felipe", 123, None, None)

while True:
    menu = input((f"""
    ╔═.✵.═══════════════════════════════╗
     𝙀𝙨𝙩𝙖𝙣𝙩𝙚 𝙙𝙚 𝙥𝙤𝙩𝙚𝙨 𝙙𝙖𝙨 𝙨𝙖𝙡𝙖𝙨 𝙙𝙤 𝙎𝙚𝙣𝙖𝙘
    ╚═══════════════════════════════.✵.═╝
    1- Adicionar Usuário
    2- Listar Usuários
    3- Pegar Pote
    4- Guardar Pote
    5- Listar Potes
    6- Localizar Pote
    7- Sair
    """))

    if menu == "1":
        print("Adicionando usuários")
        usuario = input("Aluno ou Professor?\nDigite '1' para Aluno\nDigite '2' para Professor\nvalor: ")
        if usuario == "1":
            nome = input("Qual o seu nome?")
            matricula = input("Qual a sua matrícula?")
            curso = input("Qual o seu curso?")
            aluno = Aluno(nome, matricula, curso)
            aluno.inserir_novo_aluno(nome, matricula, curso)
            print(f"Bem vindo {nome}!" )        
            continue
        elif usuario == "2":
            nome = input("Qual o seu nome: ")
            matricula = input("Qual a sua matrícula: ")
            professor.inserir_novo_professor(nome, matricula, False)
            print(f"Bem vindo {nome}!" )      
            continue
        else:
            Funcoes.erro()
            continue
    


    elif menu == "2":
         with open("usuarios.txt", 'r', encoding= "utf-8") as arquivo:
            lista_usuario = arquivo.read()
            print(lista_usuario)
        
        
    elif menu == "3":
        usuario = input("Aluno ou Professor?\nDigite '1' para Aluno\nDigite '2' para Professor\nvalor: ")
        if usuario == "1":
            print("Alunos não tem acesso ao Estante!!")
        elif usuario == "2":
            nome = input("Digite o seu nome: ")
            matricula = input("Digite sua matrícula: ")
            

            with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
                lista_usuario = arquivo.readlines()
                encontrado = False
                for linha in lista_usuario:
                    if nome in linha and matricula in linha:
                        print(f"Bem vindo profesor {nome}!")
                        encontrado = True
                        pote_escolhido = int(input("Qual pote você quer pegar?"))
                        estante.pegar_pote(pote_escolhido)
                        professor.status_pote(nome, matricula, pote_escolhido ,True)#quero q o professor esteja com o pote, portanto True
            
                if encontrado == False:
                    print("Professor não encontrado, tente novamente.")
                    continue
        else:
            Funcoes.erro()
            break

    elif menu == "4": #guardar pote
        usuario = input("Aluno ou Professor?\nDigite '1' para Aluno\nDigite '2' para Professor\nvalor: ")
        if usuario == "1":
            print("Alunos não tem acesso ao Estante!!")
        elif usuario == "2":
            nome = input("Digite o seu nome: ")
            matricula = input("Digite sua matrícula: ")
            
            with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
                lista_usuario = arquivo.readlines()
                encontrado = False
                for linha in lista_usuario:
                    if nome in linha and matricula in linha:
                        print(f"Bem vindo profesor {nome}!")
                        encontrado = True
                        pote_escolhido = int(input("Qual pote você quer guardar?"))
                        professor.status_pote(nome, matricula, None, False) #quero que o professor nao esteja mais com o pote, portanto ele sera false
                        estante.guardar_pote(pote_escolhido) #o pote pego sempre some depois de reiniciar
                        
                if encontrado == False:
                    print("Professor não encontrado, tente novamente.")
                    continue
        else:
            Funcoes.erro()
            break
        
    elif menu == "5": #listar potes
        with open("potes.txt", 'r') as arquivo:
            texto = arquivo.read()
            print("True: Disponível \nFalse: Indisponível")
            print(texto)

    elif menu == "6": #localizar potes a partir do numero do pote escolhido   // Vou precisar especificar o numero do pote a qual o professor pegou
        
        pote_escolhido = input("Qual pote deseja encontrar?")
        with open("potes.txt", 'r') as arquivo:
            usuarios = arquivo.read()
            
    
    elif menu == 7: #encerrar programa
        print("Encerrando Programa.")
        break
    else:
        Funcoes.erro()
        break
        
#o arquivo txt nao salva completamente os dados.








