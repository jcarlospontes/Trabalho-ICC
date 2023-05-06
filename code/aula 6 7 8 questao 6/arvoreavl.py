
class No:
    def __init__(self, valor):
        self.valor = int(valor)
        self.fdir = None
        self.fesq = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def vazia(self):
        if(self.raiz == None):
            print("A árvore está vazia!")
            return True
        else:
            return False
        

    def preordem(self):
        def preordemrec(noatual):
            if(noatual == None):
                return
            else:
                print(noatual.valor, end = ' ')
                preordemrec(noatual.fesq)
                preordemrec(noatual.fdir)
        preordemrec(self.raiz)
        print("")
    

    def inordem(self):
        def inordemrec(noatual=self.raiz):
            if(noatual == None):
                return
            else:
                inordemrec(noatual.fesq)
                print(noatual.valor, end = ' ')
                inordemrec(noatual.fdir)
        inordemrec(self.raiz)
        print("")

    def posordem(self):
        def posordemrec(noatual=self.raiz):
            if(noatual == None):
                return
            else:
                posordemrec(noatual.fesq)
                posordemrec(noatual.fdir)
                print(noatual.valor, end = ' ')
        posordemrec(self.raiz)
        print("")

    def insere(self, valor):
            self.raiz = self._insere_recursivo(self.raiz, valor)
    
    def _insere_recursivo(self, noatual, valor):
        if noatual is None:
            return No(valor)

        if valor < noatual.valor:
            noatual.fesq = self._insere_recursivo(noatual.fesq, valor)
        elif valor > noatual.valor:
            noatual.fdir = self._insere_recursivo(noatual.fdir, valor)

        noatual.altura = max(self.altura(noatual.fdir), self.altura(noatual.fesq)) + 1

        fatorbalanco = self.fator_balanco(noatual)

        
        if fatorbalanco > 1 and valor < noatual.fesq.valor:
            return self.rotdireita(noatual)

        
        if fatorbalanco < -1 and valor > noatual.fdir.valor:
            return self.rotesquerda(noatual)

        
        if fatorbalanco > 1 and valor > noatual.fesq.valor:
            noatual.fesq = self.rotesquerda(noatual.fesq)
            return self.rotdireita(noatual)

        
        if fatorbalanco < -1 and valor < noatual.fdir.valor:
            noatual.fdir = self.rotdireita(noatual.fdir)
            return self.rotesquerda(noatual)

        return noatual
    
    def fator_balanco(self, no):
        if no is None:
            return 0
        return self.altura(no.fesq) - self.altura(no.fdir)
    
    def altura(self, no):
        if no is None:
            return 0
        return no.altura
    
    
    def rotdireita(self, noZ):
        noY = noZ.fesq
        if noY is not None:
            temp = noY.fdir
            noY.fdir = noZ
            noZ.fesq = temp
            noZ.altura = max(self.altura(noZ.fesq), self.altura(noZ.fdir)) + 1
            noY.altura = max(self.altura(noY.fesq), self.altura(noY.fdir)) + 1
            return noY
        else:
            return noZ

    def rotesquerda(self, noZ):
        noY = noZ.fdir
        if noY is not None:
            temp = noY.fesq
            noY.fesq = noZ
            noZ.fdir = temp
            noZ.altura = max(self.altura(noZ.fesq), self.altura(noZ.fdir)) + 1
            noY.altura = max(self.altura(noY.fesq), self.altura(noY.fdir)) + 1
            return noY
        else:
            return noZ
    
    def retornaRaiz(self):
        return self.raiz
    
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
    

arvore = ArvoreAVL()

arvore.insere(35)
arvore.insere(39)
arvore.insere(51)
arvore.insere(20)
arvore.insere(13)
arvore.insere(28)
arvore.insere(22)
arvore.insere(32)
arvore.insere(25)
arvore.insere(33)

print("pre")
arvore.preordem()
print("in")
arvore.inordem()
print("pos")
arvore.posordem()


print(arvore.altura(arvore.raiz.fesq))


