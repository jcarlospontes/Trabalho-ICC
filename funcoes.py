def RemoverAgenda():
	clear()
	print("  #########################")
	print(" ### Remover da agenda ###")
	print("#########################\n")
	nomes = []
	numeros = []
	arquivo = open("lista.txt","r")
	i = 0
	texto = arquivo.readlines()
	if texto == []:
		print("\nNenhum contato na agenda!\n")
		voltar = input("Aperte ENTER para voltar ao menu")
		return MenuAgenda()
	for linha in texto:
		i += 1
		nome, numero = linha.strip().split(':')
		print("{}) {} - {}\n".format(i, nome,numero))
		nomes.append(nome)
		numeros.append(numero)
	arquivo.close()
	escolha = input("Digite o contato que deseja Remover: ")
	while escolha.isnumeric() == False:
		return RemoverAgenda()
	escolha = int(escolha)
	while ((escolha < 1) or (escolha > i)):
		return RemoverAgenda()
	clear()
	nomes.pop(escolha-1)
	numeros.pop(escolha-1)
	x = 0
	arquivo = open("lista.txt","w")
	while x < i-1:
		arquivo.write("{}:{}\n".format(nomes[x],numeros[x]))
		x += 1
	arquivo.close()
	print("Contato removido com sucesso!")
	volte = input("Aperte ENTER para voltar ao menu")
	return MenuAgenda()


def EditarAgenda():
	clear()
	print("  ########################")
	print(" ### Editar a agenda ###")
	print("#######################\n")
	nomes = []
	numeros = []
	arquivo = open("lista.txt","r")
	i = 0
	texto = arquivo.readlines()
	if texto == []:
		print("\nNenhum contato na agenda!\n")
		voltar = input("Aperte ENTER para voltar ao menu")
		return MenuAgenda()
	for linha in texto:
		i += 1
		nome, numero = linha.strip().split(':')
		print("{}) {} - {}\n".format(i, nome,numero))
		nomes.append(nome)
		numeros.append(numero)
	arquivo.close()
	escolha = input("Digite o contato que deseja editar: ")
	while escolha.isnumeric() == False:
		return EditarAgenda()
	escolha = int(escolha)
	while ((escolha < 1) or (escolha > i)):
		return EditarAgenda()
	clear()
	nomenovo = input("Digite um novo nome para {}: ".format(nomes[escolha-1]))
	if nomenovo == "":
		pass
	else:
		nomes[escolha-1] = nomenovo
	numeronovo = input("Digite um novo numero para {}: ".format(nomes[escolha-1]))
	while numeronovo.isnumeric() == False:
		print("Apenas números!\n")
		numeronovo = input("Digite um novo numero para {}: ".format(nomes[escolha-1]))
		numeros[escolha-1] = numeronovo
	x = 0
	arquivo = open("lista.txt","w")
	while x < i:
		arquivo.write("{}:{}\n".format(nomes[x],numeros[x]))
		x += 1
	arquivo.close()
	print("\nModificação feita com sucesso!\n")
	volte = input("Aperte ENTER para voltar ao menu")
	return MenuAgenda()
	


def AdicionarAgenda():
	clear()
	print("  ###########################")
	print(" ### Adicionar na agenda ###")
	print("###########################\n")
	arquivo = open("lista.txt","a")
	nome = input("Digite o nome do contato: ")
	while nome.isalpha == False or nome == "" or nome[0] == " ":
		novonome = ""
		x = 0
		for a in nome:
			if (a.isalpha()) == True:
				x += 1
				novonome += a
		if novonome.isalpha() == True:
			break
		else:
			print("Nome inválido!\n")
			nome = input("Digite o nome do contato: ")
	numero = input("Digite o número do {}: ".format(nome))
	while numero.isnumeric() == False or numero == "":
		print("Apenas números!\n")
		numero = input("Digite o número do {}: ".format(nome))
	arquivo.write("{}:{}\n".format(nome,numero))
	arquivo.close()
	print("\nContato {} adicionado com sucesso!\n".format(nome))
	voltar = input("Aperte ENTER para voltar ao menu ")
	return MenuAgenda()

def VisualizarAgenda():
	clear()
	print("  ###########################")
	print(" ### Visualizando Agenda ###")
	print("###########################\n")
	arquivo = open("lista.txt","r")
	i = 0
	texto = arquivo.readlines()
	if texto == []:
		print("\nNenhum contato na agenda!\n")
	for linha in texto:
		i += 1
		nome, numero = linha.strip().split(':')
		print("{}) {} - {}\n".format(i, nome,numero))
	arquivo.close()
	voltar = input("Aperte ENTER para voltar ao menu ")
	return MenuAgenda()

def BuscaAgenda():
	clear()
	print("  #######################")
	print(" ### Busca na Agenda ###")
	print("#######################\n")
	print("")
	arquivo = open("lista.txt","r")
	texto = arquivo.readlines()
	if texto == []:
		print("\nNenhum contato na agenda!\n")
		voltar = input("Pressione ENTER para voltar")
		return MenuAgenda()
	print(" 1) Procurar Nome")
	print(" 2) Procurar Número\n")
	print(" 0) Voltar ao menu\n")
	Q = input("Digite sua escolha: ")
	found = False
	if Q.isnumeric() == True:
		Q = int(Q)
	else:
		return BuscaAgenda()
	if Q == 0:
		arquivo.close()
		return MenuAgenda()
	elif Q == 1:
		nome = input("Digite o nome que deseja procurar: ")
		for linha in texto:
			agendanome, agendanumero = linha.strip().split(':')
			if agendanome.lower() == nome.lower():
				clear()
				print("  ##################")
				print(" ### Encontrado ###")
				print("##################\n")
				print("\nNome encontrado!\n")
				found = True
				print("Nome: {}\nNúmero: {}\n".format(agendanome,agendanumero))
				break
		arquivo.close()
		if found == False:
			clear()
			print("  ######################")
			print(" ### Não Encontrado ###")
			print("######################\n")
			print("\n\n\nNome não encontrado!\n")
	elif Q == 2:
		numero = input("Digite o numero que deseja procurar: ")
		for linha in texto:
			agendanome, agendanumero = linha.strip().split(':')
			if agendanumero == numero:
				clear()
				print("  ##################")
				print(" ### Encontrado ###")
				print("##################\n")
				print("\nNúmero encontrado!\n")
				found = True
				print("Nome: {}\nNúmero: {}\n".format(agendanome,agendanumero))
				break
		arquivo.close()
		if found == False:
			clear()
			print("  ######################")
			print(" ### Não Encontrado ###")
			print("######################\n")
			print("\n\n\nNúmero não encontrado!\n")
	else:
		arquivo.close()
		return BuscaAgenda()

	print(" 1) Nova Busca\n")
	print(" 0) Voltar ao menu\n")
	escolha = input("Digite sua escolha: ")
	if escolha.isnumeric() == True:
		escolha = int(escolha)
	else:
		return NovabuscaAgenda()

	if escolha == 1:
		return BuscaAgenda()
	if escolha == 0:
		return MenuAgenda()
	else:
		return NovabuscaAgenda()
		
def NovabuscaAgenda():
	clear()
	print("  ############################")
	print(" ### Nova busca na Agenda ###")
	print("############################\n")
	print(" 1) Nova Busca\n")
	print(" 0) Voltar ao menu\n")
	print("\nEscolha inválida!\n")
	escolha = input("Digite sua escolha: ")
	if escolha.isnumeric() == True:
		escolha = int(escolha)
	else:
		return NovabuscaAgenda()
	if escolha == 1:
		return BuscaAgenda()
	if escolha == 0:
		return MenuAgenda()
	else:
		return NovabuscaAgenda()

def clear():
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')

def MenuAgenda():
	clear()
	print("  #########################")
	print(" ### Agenda Telefônica ###")
	print("#########################\n")
	print(" 1) Visualizar Agenda")
	print(" 2) Adicionar Contato")
	print(" 3) Editar Contato")
	print(" 4) Excluir Contato")
	print(" 5) Procurar Contato\n")
	print(" 0) Fechar Agenda\n")
	
	R = input("Digite sua escolha: ")
	if R.isnumeric() == True:
		R = int(R)
	else:
		return MenuAgenda()
	print("")

	if (R == 0):
		clear()
		return 0
	if (R == 1):
		return VisualizarAgenda()
	if (R == 2):
	    return AdicionarAgenda()
	if (R == 3):
		return EditarAgenda()
	if (R == 4):
		return RemoverAgenda()
	if (R == 5):
		return BuscaAgenda()
	else:
		return MenuAgenda()
