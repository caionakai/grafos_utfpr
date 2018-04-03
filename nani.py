#GET ORDER
import networkx as nx
import sys



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
                novo_nome.append({0:linha[i].replace('\n',''),1:linha[j].replace('\n','')})
    return novo_nome

def Inicializacao(arquivo):
    
    G = nx.Graph()
    string=[]
    size=0
    teste=0
    for linha in arquivo:
        token = linha.split(',')
        if size>0:
            string.append(token)
            size = size -1
        else:
            ##Inicializar iteracao
            for i in Combinacao_Dos_Autores(string):
                G.add_node(i[0],cor='branco',tempo = 0)
                G.add_node(i[1],cor='branco',tempo = 0)
                G.add_edge(i[0], i[1])
            if G.number_of_nodes()> 0:
                teste=teste+1
                print("Teste ",teste)
                for node in G.nodes:
                    DFS_Visit(G,node)
            ##Limpando para proxima iteracao
            G.clear()
            del string[:]
            size = isInt(token)
        
argc = len(sys.argv)

if argc != 2:
    print 'Uso: python nani.py arquivo_dos_nome_dos_autores '
    sys.exit(0)

aux = sys.argv[1]


arquivo = open(aux).readlines()

Inicializacao(arquivo)



