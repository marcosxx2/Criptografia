from Funcoes import *

print('-'*100)

textoCifrado_Hex = INPUT_textoCifrado() #-- INPUT DO textoCifrado

print('-'*100)

Chave = INPUT_chaveDec()  #-- INPUT DA Chave

cifra_listaHex = [textoCifrado_Hex [i:i + 2] for i in range(0, len(textoCifrado_Hex), 2)] #-- DIVIDE O textoCifrado(hex) EM UMA LISTA COM DOIS CARACTERES EM CADA INDICE, CADA DUPLA REPRESENTANDO UM CARACTER COMUM

cifra_listaUc = listHEX_to_listUC(cifra_listaHex) #-- TRANSFORMA O textoCifrado(Hex, lista) EM UMA LISTA EM UNICODE

chave_listaUC = STR_to_UnicodeList(Chave) #-- TRANSFORMA A Chave EM UMA LISTA EM UNICODE

xoredLista = listText_XOR_listChave(cifra_listaUc, chave_listaUC) #-- textoCifrado(unicode, lista) XOR Chave(unicode, lista) = textoClaro(unicode, lista)

for c in range(0, 10):
    substituição = listText_XOR_listChave(cifra_listaUc, xoredLista)
    xoredLista = listText_XOR_listChave(substituição, chave_listaUC)
    # permutação
    

textoC_Lista = UClist_to_SRTList(xoredLista) #-- TRANSFORMA o textoClaro(unicode, lista) EM UMA LISTA DE CARACTERES

textoC_Str = ''.join(textoC_Lista) #-- TRANSFORMAÇÃO A LISTA DE CARACTERES EM UMA STRING

print('.\n'*5)

print('Seu texto claro é:', textoC_Str)