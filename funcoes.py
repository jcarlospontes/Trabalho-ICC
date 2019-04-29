import time  #Para importar a função sleep.

def InicioAgenda():
	clear()
	print(bcolors.WARNING + "	                       _              " + bcolors.ENDC)
	print(bcolors.WARNING + "     /\                       | |             " + bcolors.ENDC)
	print(bcolors.WARNING + "    /  \   __ _  ___ _ __   __| | __ _        " + bcolors.ENDC)
	print(bcolors.WARNING + "   / /\ \ / _` |/ _ | '_ \ / _` |/ _` |       " + bcolors.ENDC)
	print(bcolors.WARNING + "  / ____ | (_| |  __| | | | (_| | (_| |       " + bcolors.ENDC)
	print(bcolors.WARNING + " /_/    \_\__, |\___|_| |_|\__,_|\__,_|       " + bcolors.ENDC)
	print(bcolors.WARNING + "           __/ |                              " + bcolors.ENDC)
	print(bcolors.WARNING + "  _______ |___/     __ //\        _           " + bcolors.ENDC)
	print(bcolors.WARNING + " |__   __| | |     / _|/ \|      (_)          " + bcolors.ENDC)
	print(bcolors.WARNING + "    | | ___| | ___| |_ ___  _ __  _  ___ __ _ " + bcolors.ENDC)
	print(bcolors.WARNING + "    | |/ _ | |/ _ |  _/ _ \| '_ \| |/ __/ _` |" + bcolors.ENDC)
	print(bcolors.WARNING + "    | |  __| |  __| || (_) | | | | | (_| (_| |" + bcolors.ENDC)
	print(bcolors.WARNING + "    |_|\___|_|\___|_| \___/|_| |_|_|\___\__,_|" + bcolors.ENDC)
	print("\n\n				Trabalho de IC\n")
	print("					Alunos")
	print("					 Nome1")
	print("					 Nome2")
	print("					 Nome3")
	print("					 Nome4")
	time.sleep(5)						#Tempo que a função ficará na tela.
	return MenuAgenda()

def RemoverAgenda():
	clear()
	print("  #########################")
	print(" ### Remover Da Agenda ###")
	print("#########################\n")
	nomes = []				#Lista para armazenar os nomes do arquivo.
	numeros = []				#Lista para armazenar os numeros do arquivo.
	arquivo = open("lista.txt","r")		#Arquivo aberto no modo 'leitura'.
	i = 0					#Contador de posição na lista.
	texto = arquivo.readlines()		#'texto' será o arquivo completo dividido em linhas para leitura.
	if texto == []:				#Verifica se a lista é vazia.
		print(bcolors.FAIL + "\nNenhum contato na agenda!\n" + bcolors.ENDC)
		voltar = input("Aperte ENTER para voltar ao menu")
		return MenuAgenda()
	for linha in texto:			#Lê cada linha, separando em 'nome' e 'numero' dentro das listas 'nomes' e 'numeros.
		i += 1
		nome, numero = linha.strip().split(':')
		print("{}) {} - {}\n".format(i, nome,numero))
		nomes.append(nome)
		numeros.append(numero)
	arquivo.close()								#Sempre que aberto o arquivo deverá ser fechado.
	escolha = input("Digite o contato que deseja Remover: ")		#Digita o contato listado por 'i' para remoção.
	while escolha.isnumeric() == False:					#Verifica se 'escolha' é numérico.
		return RemoverAgenda()
	escolha = int(escolha)
	while ((escolha < 1) or (escolha > i)):					#Verifica se 'escolha' está no alcance das opções.
		return RemoverAgenda()
	clear()
	nomes.pop(escolha-1)					#Exclui a escolha na posição na lista -1 pois a lista começa do número 0.
	numeros.pop(escolha-1)					#Exclui a escolha na lista 'numeros'.
	x = 0							#'x' é usado para o laço percorrer toda a lista.
	arquivo = open("lista.txt","w")				#Arquivo abre em modo 'escrita' para escrever a lista modificada.
	while x < i-1:
		arquivo.write("{}:{}\n".format(nomes[x],numeros[x]))
		x += 1
	arquivo.close()
	print(bcolors.WARNING + "Contato removido com sucesso!" + bcolors.ENDC)
	volte = input("Aperte ENTER para voltar ao menu")
	return MenuAgenda()


def EditarAgenda():
	clear()
	print("  #####################")
	print(" ### Editar Agenda ###")
	print("#####################\n")
	nomes = []
	numeros = []
	arquivo = open("lista.txt","r")
	i = 0
	j = 0					#Contador para verificação de nome repetido na lista.
	verif = False				#Verificador de nome repetido.
	texto = arquivo.readlines()
	if texto == []:
		print(bcolors.FAIL + "\nNenhum contato na agenda!\n" + bcolors.ENDC)
		voltar = input("Aperte ENTER para voltar ao menu")
		arquivo.close()
		return MenuAgenda()
	for linha in texto:
		i += 1
		nome, numero = linha.strip().split(':')
		print("{}) {} - {}\n".format(i, nome,numero))			#Mostra na tela a lista com nomes, números e posição.
		nomes.append(nome)							#Guarda cada nome na lista 'nomes'.
		numeros.append(numero)							#Guarda cada número na lista 'numeros'.
	arquivo.close()
	escolha = input("Digite o contato que deseja editar: ")				#Seleciona o contato para modificar.
	while escolha.isnumeric() == False:
		return EditarAgenda()
	escolha = int(escolha)				#Aqui a 'escolha' é transformada em inteiro depois de verificada de ser numérica.
	while ((escolha < 1) or (escolha > i)):						#Verifica se a 'escolha' é do tamanho da lista.
		return EditarAgenda()
	clear()
	nomenovo = input("Digite um novo nome para {}: ".format(nomes[escolha-1]))	#Escreve o novo nome para tomar lugar do nome na lista.
	while nomenovo.isalpha() == False or nomenovo == "" or nomenovo[0] == " " or verif == False:	#Verifica se o nome novo contem somente letras, se é vazio ou se começa com 'espaço'.
		prov = ""						#É criado uma variavel 'provisória' para abrigar o novo nome.
		verif = True
		j = 0
		while j < len(nomes):				#Verifica elemento por elemento da lista se é repetido.
			if j == escolha-1:			#Se for a posição original não tem problema repetir.
				j += 1
				continue
			if nomenovo.lower() == nomes[j].lower():
				verif = False
			j += 1
		for a in nomenovo:
			if (a.isalpha()) == True:		#Joga na variavel 'prov' somente letras, caractere por caractere da variavel 'nomenovo'.
				prov += a
		if prov != "" and verif == True and prov != " ":		#Verifica se a variavel 'prov' é não é vazia e se não é repetida na lista.
			break
		else:
			clear()
			print(bcolors.FAIL + "Nome inválido!\n" + bcolors.ENDC)
			nomenovo = input("Digite o nome do contato: ")
	nomes[escolha-1] = nomenovo				#O elemento na lista é agora o nome novo inserido na variavel 'nomenovo'.
	numeronovo = input("Digite um novo numero para {}: ".format(nomes[escolha-1]))	#O usuário digita o novo número.
	verif = False
	while numeronovo.isnumeric() == False or verif == False or numeronovo == "" or numeronovo[0] == " ":		#Verifica se o novo número é numérico, se é repetido, se é vazio ou começa com 'espaço'.
		clear()
		verif = True
		j = 0
		while j < len(numeros):
			if j == escolha-1:
				j += 1
				continue
			if numeronovo == numeros[j]:
				verif = False
			j += 1
		if numeronovo.isnumeric() == False or verif == False or numeronovo == "" or numeronovo[0] == " ":	#Segunda verificação depois da verificação de repetido.
			verif = False
		if verif == False:
			print(bcolors.FAIL + "Número inválido!\n" + bcolors.ENDC)
			numeronovo = input("Digite um novo numero para {}: ".format(nomes[escolha-1]))
			continue
		if (verif == True and numeronovo.isnumeric() == True and numeronovo != "" and numeronovo != " "):
			break
	numeros[escolha-1] = numeronovo							#transforma o elemento da lista no novo número inserido na variavel 'numeronovo'.
	x = 0											#limitador do laço while.
	arquivo = open("lista.txt","w")								#Abre arquivo em modo escrever.
	while x < i:
		arquivo.write("{}:{}\n".format(nomes[x],numeros[x]))				#Coloca a nova lista modificada.
		x += 1
	arquivo.close()
	print(bcolors.WARNING + "\nModificação feita com sucesso!\n" + bcolors.ENDC)
	volte = input("Aperte ENTER para voltar ao menu")
	return MenuAgenda()
	


def AdicionarAgenda():
	clear()
	print("  ###########################")
	print(" ### Adicionar Na Agenda ###")
	print("###########################\n")
	x = 0
	i = 0
	verif = False
	nomes = []
	numeros = []
	arquivo = open("lista.txt","r")
	texto = arquivo.readlines()
	for linha in texto:
		nome, numero = linha.strip().split(':')
		nomes.append(nome)
		numeros.append(numero)
	arquivo.close()
	nome = input("Digite o nome do contato: ")				#Inserindo o nome do novo contato.
	while x < len(nomes):
		if nome.lower() == nomes[x].lower():
			print(bcolors.FAIL + "\nEsse nome já existe na lista, escolha outro!\n" + bcolors.ENDC)
			volt = input("Aperte ENTER para voltar")
			return AdicionarAgenda()
		x += 1
	x = 0
	while nome.isalpha() == False or nome == "" or nome[0] == " ":		#Verificando se o nome só tem letras, se é vazio ou se a primeira letra é 'espaço'.
		novonome = ""
		for a in nome:
			if (a.isalpha()) == True:
				novonome += a
		if nome == "":
			print(bcolors.FAIL + "Nome inválido!\n" + bcolors.ENDC)
			press = input("Aperte ENTER para voltar")
			return AdicionarAgenda()
		if nome.isnumeric() == True:
			print(bcolors.FAIL + "Nome inválido!\n" + bcolors.ENDC)
			press = input("Aperte ENTER para voltar")
			return AdicionarAgenda()
		if nome[0] == " ":
			print(bcolors.FAIL + "Nome inválido!\n" + bcolors.ENDC)
			press = input("Aperte ENTER para voltar")
			return AdicionarAgenda()
		if nome[len(nome)-1] == " ":
			print(bcolors.FAIL + "Nome inválido!\n" + bcolors.ENDC)
			press = input("Aperte ENTER para voltar")
			return AdicionarAgenda()
		if novonome.isalpha() == True and novonome != "" or novonome[0] != " ":
			break
		else:
			print(bcolors.FAIL + "Nome inválido!\n" + bcolors.ENDC)
			press = input("Aperte ENTER para voltar")
			return AdicionarAgenda()




	while verif == False:
		clear()
		print("  ###########################")
		print(" ### Adicionar Na Agenda ###")
		print("###########################\n")
		numero = input("Digite o número do {}: ".format(nome))		#Inserindo o número do novo contato.
		while numero.isnumeric() == False or numero == "":		#Verificando se o número só tem números ou se é vazio.
			clear()
			print(bcolors.FAIL + "Apenas números!\n" + bcolors.ENDC)
			numero = input("Digite o número do {}: ".format(nome))
		verif = True
		while x < len(nomes):
			if numero == numeros[x]:
				print(bcolors.FAIL + "\nEsse número já existe na lista, escolha outro!\n" + bcolors.ENDC)
				ret = input("Aperte ENTER para continuar ")
				verif = False
			x += 1
		x = 0

	arquivo = open("lista.txt","a")						#Abrindo lista de nomes e números no modo adição.
	arquivo.write("{}:{}\n".format(nome,numero))				#Adicionando numero e nome novos.
	arquivo.close()
	print(bcolors.WARNING + "\nContato {} adicionado com sucesso!\n".format(nome) + bcolors.ENDC)
	print(" Nome: {}".format(nome))
	print(" Número: {}\n".format(numero))
	print("1) Adicionar outro contato\n")
	print("0) Voltar ao menu\n")
	voltar = input("Digite sua escolha: ")					#Escolha entre voltar ao menu e adicionar novo contato.
	while voltar == "":
		return NovaAdicaoAgenda()
	while voltar.isnumeric() == False:
		return NovaAdicaoAgenda()
	voltar = int(voltar)
	while voltar < 0 or voltar > 1:
		return NovaAdicaoAgenda()
	if voltar == 1:
		return AdicionarAgenda()
	if voltar == 0:
		return MenuAgenda()

def NovaAdicaoAgenda():
	clear()
	print("  ###########################")
	print(" ### Adicionar Na Agenda ###")
	print("###########################\n")
	print("1) Adicionar outro contato\n")
	print("0) Voltar ao menu\n")
	voltar = input("Digite sua escolha: ")				#Escolha entre adicionar novo contato e voltar ao menu.
	while voltar == "":
		return NovaAdicaoAgenda()
	while voltar.isnumeric() == False:
		return NovaAdicaoAgenda()
	voltar = int(voltar)
	while voltar < 0 or voltar > 1:
		return NovaAdicaoAgenda()
	if voltar == 1:
		return AdicionarAgenda()
	if voltar == 0:
		return MenuAgenda()

def VisualizarAgenda():
	clear()
	print("  ###########################")
	print(" ### Visualizando Agenda ###")
	print("###########################\n")
	arquivo = open("lista.txt","r")							#Abre a lista de nome e numeros no modo leitura.
	i = 0										#'i' conta a posição na lista.
	texto = arquivo.readlines()
	if texto == []:									#Verifica se a lista está vazia.
		print(bcolors.FAIL + "\nNenhum contato na agenda!\n" + bcolors.ENDC)
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
	print(" ### Busca Na Agenda ###")
	print("#######################\n")
	print("")
	i = 0										#'i' é usado para contar a posição na lista.
	arquivo = open("lista.txt","r")							#Abre arquivo em modo leitura.
	texto = arquivo.readlines()
	if texto == []:									#Verifica se a lista está vazia.
		print(bcolors.FAIL + "\nNenhum contato na agenda!\n" + bcolors.ENDC)
		voltar = input("Pressione ENTER para voltar")
		return MenuAgenda()
	print(" 1) Procurar Nome")
	print(" 2) Procurar Número\n")
	print(" 0) Voltar ao menu\n")
	Q = input("Digite sua escolha: ")						#Escolha entre procurar nome, número e voltar ao menu.
	found = False		#'found' é usado para verificar se o nome existe na lista ou não.
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
			i += 1
			agendanome, agendanumero = linha.strip().split(':')
			if agendanome.lower() == nome.lower():
				clear()
				print("  ##################")
				print(" ### Encontrado ###")
				print("##################\n")
				print(bcolors.WARNING + "\nNome encontrado!\n" + bcolors.ENDC)
				found = True
				print("Contato {}\nNome: {}\nNúmero: {}\n".format(i,agendanome,agendanumero))
				i = 0
				break
		arquivo.close()
		if found == False:
			clear()
			print("  ######################")
			print(" ### Não Encontrado ###")
			print("######################\n")
			print(bcolors.FAIL + "\n\n\nNome não encontrado!\n" + bcolors.ENDC)
	elif Q == 2:
		numero = input("Digite o numero que deseja procurar: ")
		for linha in texto:
			i += 1
			agendanome, agendanumero = linha.strip().split(':')
			if agendanumero == numero:
				clear()
				print("  ##################")
				print(" ### Encontrado ###")
				print("##################\n")
				print(bcolors.WARNING + "\nNúmero encontrado!\n" + bcolors.ENDC)
				found = True
				print("Contato {}\nNome: {}\nNúmero: {}\n".format(i,agendanome,agendanumero))
				i = 0
				break
		arquivo.close()
		if found == False:
			clear()
			print("  ######################")
			print(" ### Não Encontrado ###")
			print("######################\n")
			print(bcolors.FAIL + "\n\n\nNúmero não encontrado!\n" + bcolors.ENDC)
	else:
		arquivo.close()
		return BuscaAgenda()

	print(" 1) Nova Busca\n")
	print(" 0) Voltar ao menu\n")
	escolha = input("Digite sua escolha: ")	#Escolha entre uma nova busca e voltar ao menu.
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
	
def NovabuscaAgenda():				#Caso o usuário digite uma escolha diferente das opções.
	clear()
	print("  ############################")
	print(" ### Nova Busca Na Agenda ###")
	print("############################\n")
	print(" 1) Nova Busca\n")
	print(" 0) Voltar ao menu\n")
	print(bcolors.FAIL + "Escolha inválida!\n" + bcolors.ENDC)
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

def clear():					#Limpa a tela;
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')

class bcolors:					#Modificadores de cor.
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
