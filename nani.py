#GET ORDER
import networkx as nx
import sys


G = nx.Graph()

cor = "branco"
tempo = 0
'''
G.add_node("v1",cor='azul')
G.add_node("v2",cor='perto')



G.nodes["v1"]['cor'] = 'amarelo'
print (G.nodes.data())

'''

def removeBreakLine(name):
    if name[len(name)-1] == '.':
       name = name[:-1]

            
argc = len(sys.argv)

if argc != 3:
    print 'Uso: python nani.py numero_de_artigos arquivo_dos_nome_dos_autores '
    sys.exit(0)

numero_de_artigos = sys.argv[1]
aux = sys.argv[2]

if 1 > numero_de_artigos > 100:
    print 'Entrada Incorreta'

arquivo = open(aux).readlines()

for linha in arquivo:
    token = linha.split(',')
    for i in token:
        if i != "0\n":
            G.add_node(i, cor='Branca', tempo = 0)
