def INPUT_textoClaro(): #<--------- RECEBE E RETORNA O INPUT DO TEXTO CLARO
    while True:
        textoClaro = input('Insira sua mensagem de até 128 caracteres a ser encriptada aqui: ')

        if len(textoClaro) > 128:
            print ('ERRO. A mensagem supera o limite de caracteres.')
        else:
            print('Sua mensagem é:', textoClaro)
            break
    return textoClaro

def INPUT_Chave(textoClaro): #<--------- RECEBE E RETORNA O INPUT DA CHAVE
    while True:
        Chave = input('Insira uma chave do mesmo tamanho ou menor que sua mensagem, {} caracteres, aqui. Quanto mais longa, mais seguros estão seus dados: '.format(len(textoClaro)))
        
        if len(Chave) > len(str(textoClaro)):
            print ('ERRO. A chave supera o limite de caracteres.')
        else:
            print('Sua chave é:', Chave)
            break
    return Chave

def INPUT_textoCifrado():  #<--------- RECEBE E RETORNA O INPUT DO TEXTO CIFRADO
    textoCifrado = input('Insira o texto cifrado a ser decriptado aqui: ')
    print('Sua texto cifrado é:', textoCifrado)
    return textoCifrado

def INPUT_chaveDec(): #<--------- RECEBE E RETORNA O INPUT DA CHAVE
    ChaveDec = input('Insira a chave do texto cifrado: ')
    print('Sua chave é:', ChaveDec)
    return ChaveDec


#-----------------OPERAÇÃO XOR------------------------------------------------------------------------------------------------------------------------------------------
def listText_XOR_listChave (text, chave):  #<--------- REALIZA A OPERAÇÃO XOR ENTRE DUAS LISTAS INT (NO CASO DESSE CODIGO, EM UNICODE)
    xoredLista = []
    for i in range(max(len(text), len(chave))): # Vamos fazer o for de acordo com a quantidade de caracteres da string que for maior
        xored_value = text[i%len(text)] ^ chave[i%len(chave)] #Ord retona um valor numerico que representa o unicode code dos caracteres de uma string
        xoredLista.append(xored_value) # Adicionar o valor desta rodada for a lista xoredLista
    return xoredLista


#-----------------TRANSFORMAÇÕES------------------------------------------------------------------------------------------------------------------------------------------
def STR_to_UnicodeList (str):  #<--------- TRANSFORMA UMA STRING EM UMA LISTA DE UNICODE
    ucLista = [] # Cria uma lista vazia
    for i in range(len(str)): # for é feito de acordo com a quantidade de caracteres da string
        ucValue = ord(str[i%len(str)]) # ord tranforma o caracter em seu unicode correspondente
        ucLista.append(ucValue) # Adiciona o valor desta rodada na lista vazia
    return ucLista

def STRlist_to_UnicodeList (list):  #<--------- TRANSFORMA UMA LISTA DE CARACTERES EM UMA LISTA UNICODE
    ucLista = [] # Cria uma lista vazia
    for i in list: # for é feito de acordo com a quantidade de elementos dentro da lista
        ucValue = ord(i) # ord tranforma o caracter em seu unicode correspondente
        ucLista.append(ucValue)  # Adiciona o valor desta rodada na lista vazia
    return ucLista

def UClist_to_SRTList (list):  #<--------- TRANSFORMA UMA LISTA UNICODE EM UMA LISTA DE CARACTERES
    strLista = [] # Cria uma lista vazia
    for i in list: # for é feito de acordo com a quantidade de elementos dentro da lista
        strValue = chr(i) # chr tranforma o unicode em seu caractere correspondente
        strLista.append(strValue) # Adiciona o valor desta rodada na lista vazia
    return strLista

def UClist_to_HEXlist (list):   #<--------- TRANSFORMA UMA UNICODE EM UMA LISTA HEX
    hexLista = [] # Cria uma lista vazia
    for i in list: # for é feito de acordo com a quantidade de elementos dentro da lista
        hexValue = hex(i)[2:] # hext tranforma o unicode em seu codigo hex correspondente, no python os codigos ex veem com x0 na frentem então retiramos os dois primeiros caracteres do elemento
        if len(hexValue) % 2 != 0: # O python omite quando o primeiro caracter do hex é um 0. Para não atrapalhar a decodificação - que faremos dividindo a cifra de 2 em 2 - checamos se o valor hex tem dois caracteres em não
            hexValue = '0' + hexValue # se não, adicionamos um 0 na frente
        hexLista.append(hexValue) # Adiciona o valor desta rodada na lista vazia
    return hexLista

def listHEX_to_listUC (list):   #<--------- TRANSFORMA UMA LISTA HEX EM UMA LISTA UNICODE
    ucLista = [] # Cria uma lista vazia
    for i in list: # for é feito de acordo com a quantidade de elementos dentro da lista
        ucValue = (int(i, 16)) # dividimos o codigo hex em uka base 16 e o transformamos em um int para encontrar o unicode correspondente
        ucLista.append(ucValue) # Adiciona o valor desta rodada na lista vazia
    return ucLista