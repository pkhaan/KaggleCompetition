#this is a test

import numpy as np
import pandas as pd
import io 

def readAbstracts():
    f = open("C:\\Users\\peter\\Desktop\\abstracts.txt", 'r')
    
    data = []

    i = 0
    #we read lines until we reach line 10
    for line in f:
        if(i==10):
            break
        
        data.append(line.split("|--|"))

        i+=1
    
    abstracts = pd.DataFrame(data, columns = ['id', 'abstract'])
    print(abstracts)

def readEdges():
    f = open("C:\\Users\\peter\\Desktop\\edgelist.txt", 'r')

    data = []

    i = 0
    #we read lines until we reach line 10
    for line in f:
        if(i==8):
            break
        
        data.append(line.split(","))
        data[-1][1] = data[-1][1].replace("\n", "")
        i+=1    
    
    edges = pd.DataFrame(data, columns = ['first_paper', 'second_paper',])
    print(edges)

def getData():

    #we read abstract file and we split it with the sequence of symbols |--|
    f1 = open("C:\\Users\\peter\\Desktop\\abstracts.txt", 'r', encoding="utf-8")

    abstracts = [line.rstrip().split("|--|") for line in f1]

    #we read edgelist file and we split it via its id.
    f2 = open("C:\\Users\\peter\\Desktop\\edgelist.txt", 'r')
    edges = [line.rstrip().split(",") for line in f2]

    for edge in edges:
        print(edge)

        edge.append(abstracts[edge[0]][1])
        edge.append(abstracts[edge[1]][1])

    df = pd.DataFrame(edges, columns = ['A_id', 'B_id', 'A_abstract', 'B_abstract'])
    print(df)
        
getData()