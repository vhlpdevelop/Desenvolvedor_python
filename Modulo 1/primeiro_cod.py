nome = 'victor'
print('Olá ',nome,' seja bem-vindo')

#Declaração de variaveis de python
#variavel = valor
pessoa = 'string'
#matriz = [] nao existe em python, da pra usar biblioteca numpy


vetor = []
vetor.append(1)
inteiro = 1
flat = 0.1

print('pessoa =>',pessoa)
print('vetor =>', vetor)
print('inteiro =>',inteiro)
print('float',flat)


#Tipos de dados em python
#int, float, bool, str
# comando type(variavel) retorna o tipo => <class 'type'>
#tipo none ou null seria variavel = none

print(type(inteiro))

#fatiamento se chama slice, exemplo
#vetor[3:6] acessa nesse vetor 3,4,5 funciona bem com vetor de strings.
#concatenar é basico, string + string, simples
#filiação ou pertencimento exemplo:
#s1 = 'consolação'
#s2 = 'sola'
#print (s1 in s2) pode-se ate utilizar operador logico como not. -> print (s1 not in s2)

#metodos string
#.upper() todas as letras maiusculas
#.lower() todas as letras minusculas
#.title() primeira letra de cada palavra em maiusculo
#.replace('1','2') substitui 1 por 2
# .startswith('palavra') verifica se a string começa com palavra
# .endswith('palavra') verifica se a string acaba com palavra
# .find('palavra') retorna o indice da primeira ocorrencia da palavra
# .split() particiona a string em outras, que são separadas por um espaço
# .split(',') particiona a string em outras que sao separadas por ','
# .strip() remove os espaços extras no inicio e fim da string


#conversão
#str(algum tipo) vira string
#int() bool() str() podem virar outros também dependendo no que se insere
#exemplo int(9.9999) vira float
#bool(-1) vira inteiro
#str(True) vira booleana
# A conversão é dinamica

#conversão f-string
#
#print (f'eu tenho {ano_atual - nascimento} anos')