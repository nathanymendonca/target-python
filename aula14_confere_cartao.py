'''

Manipulando Strings
* String indices
*Fatiamento de strings ( inicio:fim:pass)
*Funções built0in, len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

'''

#Positivos
cartao = input('Digite o número do cartão sem espaço ')

conferencia_cartao_bin = cartao[0:5]

conferencia_cartao_lastfour = cartao[12:16]

print(f' Números do início do cartão "{conferencia_cartao_bin}" - Números do fim do cartão "{conferencia_cartao_lastfour}". O cartão possui {len(cartao)} digitos ao todo.')