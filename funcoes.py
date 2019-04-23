def Visualizarlista():
	arquivo = open("lista.txt","r")
	i = 0
	texto = arquivo.readlines()
	for linha in texto:
		i += 1
		print("{}) {}\n".format(i, linha))
	arquivo.close()
	voltar = input("Aperte ENTER para voltar ")
	if voltar == "":
		return Menulista()

def Buscalista():
	print("\nVocê deseja procurar por\n")
	print(" 1) Nome")
	print(" 2) Número\n")
	print(" 0) Voltar\n")
	escolha = int(input("Digite sua escolha: "))
	while escolha < 0 or escolha > 2:
		print("Opção inválida!")
		escolha = int(input("Digite sua escolha: "))
	if escolha == 1:
		print("")
		nome = str(input("Digite o nome que você deseja procurar: "))
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
	if (R == 5):
		return Buscalista()
