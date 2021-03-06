# -*- coding: utf-8 -*-
###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 07 = Algoritmo Conjugação Verbal Afirmativo
#
###############################################################################

def conjugacao_verbal_afirmativo(pronome, palavra):

    terceira_pessoa_singular = ['He','She','It']
    terminos_es = ['o', 'z', 'x','ss', 'ch', 'sh']
    vogais = ['a','e','i','o','u']

    if(pronome in terceira_pessoa_singular):
        if(palavra[-1] in terminos_es or palavra[-2:] in terminos_es):
            return pronome+' '+palavra+"es"
        elif(palavra[-1] == "y" and palavra[-2] not in vogais):
            return pronome+' '+palavra[:-1]+"ies"
        elif(palavra[-1] == "y" and palavra[-2] in vogais):
            return pronome+' '+palavra+"s"
        elif(palavra == "have"):
            return pronome+' has'
        else:
            return pronome+' '+palavra+"s"
    else:
        return pronome+' '+palavra
    
verbos = ['watch','say','study','have']
pronomes = ['I','You','He','She','It','You','We','They']

for verbo in verbos:
    for pronome in pronomes:
        print(conjugacao_verbal_afirmativo(pronome,verbo))
