def Adicionarlista():
    arquivo = open("lista.txt","a")
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o número do {}: ".format(nome))
    arquivo.write("{}:{}\n".format(nome,numero))
    arquivo.close()
    print("\nContato {} Adicionado com sucesso!\n".format(nome))
    voltar = input("Aperte ENTER para voltar")
    return Menulista()

def Visualizarlista():
	arquivo = open("lista.txt","r")
	i = 0
	texto = arquivo.readlines()
	for linha in texto:
		i += 1
		linha.split(":")
		print("{}) {} - {}".format(i, linha[0],linha[1]))
	arquivo.close()
	voltar = input("Aperte ENTER para voltar ")
	if voltar == "":
		return Menulista()

def Buscalista():
	print("\nBusca na lista\n")
	nome = input("Digite o nome que deseja procurar: ")
	print("")
	nome = nome.lower()
	arquivo = open("lista.txt","r")
	texto = arquivo.readlines()
	i = 0
	for linha in texto:
	    i += 1
	    linha.split(":")
	    nomelista = linha[0]
	    if nomelista.lower == nome:
	        print(" {}) {}\n".format(i,linha))
	        break
	arquivo.close()
	print(" 1) Nova Busca\n")
	print(" 0) Voltar\n")
	escolha = int(input("Digite sua escolha: "))
	while escolha < 0 or escolha > 1:
		print("Opção inválida!")
		escolha = int(input("Digite sua escolha: "))
	if escolha == 1:
		return Buscalista()
	if escolha == 0:
		return Menulista()
		
def Menulista():
	print("########################")
	print("### Lista Telefonica ###")
	print("########################\n")
	print(" 1) Visualizar Lista")
	print(" 2) Adicionar Contato")
	print(" 3) Editar Contato")
	print(" 4) Excluir Contato")
	print(" 5) Procurar Contato\n")
	print(" 0) Fechar Lista\n")
	
	R = int(input("Digite sua escolha: "))
	print("")
	while(R > 5) or (R < 0):
		print("########################")
		print("### Lista Telefonica ###")
		print("########################\n")
		print(" 1) Vizualizar Lista")
		print(" 2) Adicionar Contato")
		print(" 3) Editar Contato")
		print(" 4) Excluir Contato")
		print(" 5) Procurar Contato\n")
		print(" 0) Fechar Lista\n")
		print(" Opção Inválida.\n")
		R = int(input("Digite sua escolha: "))
		print("")
	
	
	if (R == 0):
		return 0
	if (R == 1):
		return Visualizarlista()
	if (R == 2):
	    return Adicionarlista()
	if (R == 5):
		return Buscalista()
