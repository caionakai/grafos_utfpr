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

def isInt(string):
    for i in string:
        if int(i):
            return int(i)
    return 0

def Combinacao_Dos_Autores(nomes):
    novo_nome=[]
    for linha in nomes:
        for i in range(0 , len(linha)):
            for j in range(i+1 , len(linha)):
                novo_nome.append({linha[i].replace('\n',''),linha[j].replace('\n','')})
    return novo_nome

def TestList(arquivo):
    string=[]
    size=0
    for linha in arquivo:
        token = linha.split(',')
        if size>0:
            string.append(token)
            size = size -1
        else:
            
            size = isInt(token)
        
argc = len(sys.argv)

if argc != 2:
    print 'Uso: python nani.py arquivo_dos_nome_dos_autores '
    sys.exit(0)

aux = sys.argv[1]


arquivo = open(aux).readlines()

TestList(arquivo)
    

