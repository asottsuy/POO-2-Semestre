
class Estante:
    def __init__(self):
        self._nichos = {}   
        andares = [100,200,300,400,500,600,700,800]
        for salas in andares:
            for s in range(1,5):
                self._nichos[salas+s] = True
        
        
    
        
    

  
    def pegar_pote(self, numero):
        #self.ler_arquivo()
        if numero in self._nichos.keys(): #verifica se o pote existe como chave no dicionario
            pote_selecionado = self._nichos[numero] #atribui o valor a uma variavel
            if pote_selecionado == True:#verifica se o pote ja nao tinha sido pego antes
                if pote_selecionado: #se o pote foi selecionado
                    self._nichos[numero] = False #muda o valor da chave para False
                    self.atualizar_arquivo()
                    print(f"O pote {numero}, foi pego.")
            else: 
                print(f"O pote {numero}, já foi pego.") #se o pote já foi pego antes
        else:
            print(f"O pote {numero}, não existe.") #se o pote não existir
            

    def guardar_pote(self, numero):
        #self.ler_arquivo()
        if numero in self._nichos.keys(): #verifica se o pote existe como chave no dicionario
            pote_selecionado = self._nichos[numero]
            print(111, pote_selecionado) #atribui o valor a uma variavel
            
            if pote_selecionado == False: #verifica se o pote ja nao tinha sido devolvido antes
                print(222)
                self._nichos[numero] = True #muda o valor da chave para True
                self.atualizar_arquivo()
                print(f"O pote {numero}, foi guardado.")
            else: 
                print(f"O pote {numero}, já foi guardado anteriormente.") #se o pote já foi guardado antes
        else:
            print(f"O pote {numero}, não existe.") #se o pote não existir
        input("::::")

    def atualizar_arquivo(self): #vai limpar o conteudo velho e atualizar pelo novo
        with open("potes.txt", 'w') as arquivo:
            arquivo.write(f"\n{self._nichos}")

    def ler_arquivo(self): #vai apenas ler o arquivo
        with open("potes.txt", 'r') as arquivo:
            texto = arquivo.read()
            














