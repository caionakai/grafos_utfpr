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
def DFS(G):
    array=[]
    array.append("P. Erdos")
    DFS_Visit(G,array)
    G.remove_node("P. Erdos")

def DFS_Visit(G, array):
    if len(array)==0:
        return
    u=array[0]
    array.remove(u)
    
    for v,b in G.adj[u].items():	#v significa number_of_node_adj
        if G.nodes[v]['cor'] == "branco":
            G.nodes[v]['predecessor'] = u
            G.nodes[v]['cor'] = "cinza"
            G.nodes[v]['finalizacao'] = G.nodes[u]['finalizacao']+1
            array.append(v)
    G.nodes[u]['cor'] = "preto"
    DFS_Visit(G, array)
    
    
    
def Inicializacao(arquivo):
    global tempo
    G = nx.Graph()
    string=[]
    size=0
    teste=0
    for linha in arquivo:
        token = linha.split(", ")
        if size>0:
            string.append(token)
            size = size -1
        else:
            ##Inicializar iteracao
            if G.number_of_nodes()== 0:
                for i in Combinacao_Dos_Autores(string):
                    G.add_node(i[0],cor='branco',finalizacao=0)
                    G.add_node(i[1],cor='branco',finalizacao=0)
                    G.add_edge(i[0], i[1])
                if teste>0:    
                    print("\nTeste ",teste,'\n')
                    DFS(G)
                    for node in G.nodes.data():
                        print(node[0],":",node[1]['finalizacao'] if node[1]['finalizacao']!=0 else "infinito" )
                    exit()
            ##Limpando para proxima iteracao
            teste=teste+1
            G.clear()
            G = nx.Graph()
            del string[:]
            size = isInt(token)
            if size==0:
                break
        
argc = len(sys.argv)

if argc != 2:
    print ('Uso: python nani.py arquivo_dos_nome_dos_autores ')
    sys.exit(0)

aux = sys.argv[1]
arquivo = open(aux).readlines()

Inicializacao(arquivo)



