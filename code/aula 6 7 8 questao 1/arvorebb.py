
class No:
    def __init__(self, valor):
        self.valor = int(valor)
        self.fdir = None
        self.fesq = None

class ArvoreBB:
    def __init__(self):
        self.raiz = None

    def vazia(self):
        if(self.raiz == None):
            print("A árvore está vazia!")
            return True
        else:
            return False
        
    #item b
    def preordem(self):
        def preordemrec(noatual):
            if(noatual == None):
                return 0
            else:
                print(noatual.valor, end = ' ')
                preordemrec(noatual.fesq)
                preordemrec(noatual.fdir)
        preordemrec(self.raiz)
        print("")
    
    #item b
    def inordem(self):
        def inordemrec(noatual=self.raiz):
            if(noatual == None):
                return 0
            else:
                inordemrec(noatual.fesq)
                print(noatual.valor, end = ' ')
                inordemrec(noatual.fdir)
        inordemrec(self.raiz)
        print("")

    #item b
    def posordem(self):
        def posordemrec(noatual=self.raiz):
            if(noatual == None):
                return 0
            else:
                posordemrec(noatual.fesq)
                posordemrec(noatual.fdir)
                print(noatual.valor, end = ' ')
        posordemrec(self.raiz)
        print("")

    #item a
    def insere(self, valor):
        noNovo = No(valor)
        if self.vazia():
            self.raiz = noNovo
        else:
            noatual = self.raiz
            while(True):
                if(noatual.valor > valor):
                    if(noatual.fesq == None):
                        noatual.fesq = No(valor)
                        break
                    else:
                        noatual = noatual.fesq
                else:
                    if(noatual.fdir == None):
                        noatual.fdir = No(valor)
                        break
                    else:
                        noatual = noatual.fdir
    
    def retornaRaiz(self):
        return self.raiz
    
    #item c
    def procura(self, valor):
        noatual = self.raiz
        if(self.vazia()):
            return 0
        while(True):
            if(noatual.valor == valor):
                print("Valor "+str(valor)+" encontrado na árvore!")
                break
            else:
                if(noatual.valor > valor):
                    if(noatual.fesq == None):
                        print("Valor "+str(valor)+ " não encontrado na árvore!")
                        break
                    else:
                        noatual = noatual.fesq
                else:
                    if(noatual.fdir == None):
                        print("Valor "+str(valor)+ " não encontrado na árvore!")
                        break
                    else:
                        noatual = noatual.fdir
    
    #item d
    def retornamaior(self):
        noatual = self.raiz
        if(self.vazia()):
            return 0
        while(True):
            if(noatual.fdir == None):
                print("Maior valor encontrado: "+str(noatual.valor))
                break
            else:
                noatual = noatual.fdir

    #item d
    def retornamenor(self):
        noatual = self.raiz
        if(self.vazia()):
            return 0
        while(True):
            if(noatual.fesq == None):
                print("Menor valor encontrado: "+str(noatual.valor))
                break
            else:
                noatual = noatual.fesq

    #item e
    def retornamedia(self):
        varelementos = []
        def mediarec(noatual=self.raiz, elementos = varelementos):
            if(noatual == None):
                return 0
            else:
                elementos.append(noatual.valor)
                mediarec(noatual.fesq, elementos)
                mediarec(noatual.fdir, elementos)
        mediarec(self.raiz, varelementos)
        print("A media encontrada foi: "+str(sum(varelementos)/len(varelementos)))

    #item f
    def retornanulls(self):
        varelementosnull = []
        def nullsrec(noatual=self.raiz, elementos = varelementosnull):
            if(noatual == None):
                varelementosnull.append(1)
                return 0
            else:
                nullsrec(noatual.fesq, elementos)
                nullsrec(noatual.fdir, elementos)
        nullsrec(self.raiz, varelementosnull)
        print("A quantidade de NULLs da arvore é: "+str(len(varelementosnull)))

    #item g
    def retornasoma(self):
        varelementos = []
        def somarec(noatual=self.raiz, elementos = varelementos):
            if(noatual == None):
                return 0
            else:
                elementos.append(noatual.valor)
                somarec(noatual.fesq, elementos)
                somarec(noatual.fdir, elementos)
        somarec(self.raiz, varelementos)
        print("A soma encontrada foi: "+str(sum(varelementos)))

    #item h
    def retornamultiplo(self):
        varelementosmult = []
        def multiplorec(noatual=self.raiz, elementos = varelementosmult):
            if(noatual == None):
                return 0
            else:
                if(noatual.valor % 3 == 0):
                    elementos.append(1)
                multiplorec(noatual.fesq, elementos)
                multiplorec(noatual.fdir, elementos)
        multiplorec(self.raiz, varelementosmult)
        print("O numero de multiplos de 3 encontrado foi: "+str(sum(varelementosmult)))

    #item i
    def retornaquantno(self):
        varelementosquant = []
        def quantnorec(noatual=self.raiz, elementos = varelementosquant):
            if(noatual == None):
                return 0
            else:
                elementos.append(1)
                quantnorec(noatual.fesq, elementos)
                quantnorec(noatual.fdir, elementos)
        quantnorec(self.raiz, varelementosquant)
        print("O numero de elementos encontrado foi: "+str(sum(varelementosquant)))

    #item j
    def retornaquantfolha(self):
        varfolhasquant = []
        def quantfolharec(noatual=self.raiz, folhas = varfolhasquant):
            if(noatual == None):
                return 0
            else:
                if(noatual.fdir == None and noatual.fesq == None):
                    folhas.append(1)
                quantfolharec(noatual.fesq, folhas)
                quantfolharec(noatual.fdir, folhas)
        quantfolharec(self.raiz, varfolhasquant)
        print("O numero de folhas encontrado foi: "+str(sum(varfolhasquant)))

    #item k
    def retornaaltura(self):
        alturas = []
        atual = 0
        def alturarec(noatual=self.raiz, alturas = alturas, atual= atual):
            if(noatual == None):
                alturas.append(atual)
                return 0
            else:
                atual = atual + 1
                alturarec(noatual.fesq, alturas, atual)
                alturarec(noatual.fdir, alturas, atual)
        alturarec(self.raiz, alturas, atual)
        print("A altura da árvore é: "+str(max(alturas)))

    #item l
    def retornaestritbin(self):
        verifica = []
        def quantfolharec(noatual=self.raiz, verifica = verifica):
            if(noatual == None):
                return 0
            else:
                if((noatual.fdir == None and noatual.fesq != None)):
                    verifica.append(1)
                elif((noatual.fdir != None and noatual.fesq == None)):
                    verifica.append(1)
                quantfolharec(noatual.fesq, verifica)
                quantfolharec(noatual.fdir, verifica)
        quantfolharec(self.raiz)
        if(len(verifica) < 1):
            print("A árvore é estritamente binária!")
        else:
            print("A árvore não é estritamente binária!")



#exemplo utilizado na qestao 5
arvore = ArvoreBB()
arvore.insere(77)
arvore.insere(70)
arvore.insere(83)
arvore.insere(68)
arvore.insere(74)
arvore.insere(80)
arvore.insere(85)
arvore.insere(65)
arvore.insere(69)
arvore.insere(72)
arvore.insere(81)
arvore.insere(84)
arvore.insere(87)
arvore.insere(75)
print("pre")
arvore.preordem()
print("in")
arvore.inordem()
print("pos")
arvore.posordem()

arvore.procura(77)

arvore.retornamaior()
arvore.retornamenor()
arvore.retornamedia()
arvore.retornanulls()
arvore.retornasoma()
arvore.retornamultiplo()
arvore.retornaquantno()
arvore.retornaquantfolha()
arvore.retornaestritbin()
arvore.retornaaltura()


