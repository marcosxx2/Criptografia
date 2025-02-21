from Funcoes import *

print('-'*100)

textoClaro = INPUT_textoClaro() #-- INPUT DO textoClaro

print('-'*100)

Chave = INPUT_Chave(textoClaro) #-- INPUT DA Chave

textoC_Lista_UC = STR_to_UnicodeList(textoClaro) #-- TRANSFORMA O textoClaro EM UMA LISTA EM UNICODE

chave_Lista_UC = STR_to_UnicodeList(Chave) #-- TRANSFORMA A Chave EM UMA LISTA EM UNICODE

xoredLista = listText_XOR_listChave(textoC_Lista_UC, chave_Lista_UC) #-- textoClaro(lista e unicode) XOR Chave(lista e unicode) = textoCifrado(lista e unicode)

for c in range(0, 10):
    substituição = listText_XOR_listChave(textoC_Lista_UC, xoredLista)
    
    xoredLista = listText_XOR_listChave(substituição, chave_Lista_UC )

#strLista1 = ucLIST_to_strList(xoredLista1) #-- TRABSFORMA O textoCifrado(lista e enicode) EM UMA LISTA DE CARACTERES
#textoCifrado = ''.join(strLista1) #-- <<< Problema. Ao juntar os caracteres da lista acima em uma string, ou usar a função .decode no unicode ou hex para conseguir um uma 
                                   #                    string de caracteres, o python associa com as entradas simbolos muito complexos que quebram o terminal depois das
                                   #                    operações "chave XOR texto", impedindo a decifração. Por isso escolhi finalizar com o texto em HEX para legibilidade da cifra.

hexLista = UClist_to_HEXlist(xoredLista) #-- TRANSFORMAD O textoCifrado(lista e unicode) UMA LISTA HEX

textoCifradoHex = ''.join(hexLista) #-- TRANSFORMA O textoCifrado(lista e hext) UMA STRING

print('.\n'*5)

print('Seu texto cifrado é:', textoCifradoHex) #-- OUTPUT