# ***Kaggle Competition AUEB 2021-2022***

### This is a repo where we store our solution prediction for a Link Citation Prediction Problem


##### Problem Description

```
Link prediction is the problem of predicting the existence of a link between two entities in a network.

The problem of link prediction has recently attracted a lot of attention in many domains. For instance, in social networks, one may be interested in predicting friendship links among users, while in biology, predicting interactions between genes and proteins is of paramount importance.

In this challenge, you will deal with the problem of predicting whether a research paper cites another research paper. You are given a citation network consisting of several thousands of research papers, along with their abstracts and their list of authors. The pipeline that is typically followed to deal with the problem is similar to the one applied in any classification problem; the goal is to use edge information to learn the parameters of a classifier and then to use the classifier to predict whether two nodes are linked by an edge or not.

Next, we also provide a simple approach, on which you can work. The key component is how we create our training and test data. For training, you may first create a numpy array of zeros with 2m rows and n columns (where m is the number of edges in the edgelist file, and n the number of desired features). We then need to populate this array to create the training features. A way to do that is to iterate over all edges in the edgelist file, and if we want to have 3 features: we get the degree of the first node of the edge as the 1st column, the degree of the 2nd node of the edge as the 2nd column and their sum as the 3rd column. For the remaining m rows, we select randomly nodes and get their degrees and sum as features as well. Now we have our matrix for training. We also need to create the y classes. We create a vector of zeros with size 2m. The first m elements represent the edges that are present in the edgelist. Thus we make them 1. The remaining need to be 0, as they represent non-existing edges. We are now ready to give the features and classes to a scikitlearn classifier via the 'fit' method. Afterwards, we only need to create a similar feature matrix for the test file. We then need the probabilities of our predictions. Remember to get the probabilities only for the positive class. Please, check the 'submissionsrandom' file to check if the format matches your output. The 1st column in the submissions file represents an id integer of the edges in test file. 0 points to the first edge of the test file and so on. You are now ready to submit! 

```





