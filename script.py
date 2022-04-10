# import packages

import pandas as pd
from sklearn.model_selection import train_test_split

def getData(): # prepares dataframes

    f1 = open("abstracts.txt", 'r', encoding="utf-8") # read abstracts

    abstracts = [line.rstrip().split("|--|") for line in f1] # seperate abstracts into list

    f2 = open("edgelist.txt", 'r') # read edgelist
    
    edges = [line.rstrip().split(",") for line in f2] # seperate edgelists into list

    f3 = open("authors.txt", 'r', encoding="utf-8") # read authors

    authors = [line.rstrip().split("|--|") for line in f3] # seperate authors into list

    for paper in authors: # seperate author names into list
        paper[1] = paper[1].split(",")

    for edge in edges: # add abstracts and authors to edge list
        edge.append(abstracts[int(edge[0])][1])
        edge.append(abstracts[int(edge[1])][1])
        edge.append(authors[int(edge[0])][1])
        edge.append(authors[int(edge[1])][1])

    df = pd.DataFrame(edges, columns = ['A_Id', 'B_Id', 'A_Abstract', 'B_Abstract', 'A_Authors', 'B_Authors']) # create dataframe 

    """
    Each row of df represents an edge
    A and B are the two connected Papers

    id: dataframe row id
    A_Id/B_Id: Ids of the A and B
    A_Abstract/B_Abstract: Abstracts of the A and B
    A_Authors/B_Authors: Lists Authors of the A and B
    """

    train, test = train_test_split(df, test_size=0.2) # seperate dataframe into train/test dataframes

getData()