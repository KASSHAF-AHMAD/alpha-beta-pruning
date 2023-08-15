
import numpy as np
import math


file = open("input.txt", 'r')
data = file.read()
sentences = data.splitlines()
no_of_turn = int(sentences[0])
dep = no_of_turn;
bran = int(sentences[1])
number_of_notes = pow(bran, dep)

min = int(sentences[2].split()[0])
max = int(sentences[2].split()[1])


print ("Depth: ", math.pow(2,dep))
print ("Branch: ", bran)
print ("Terminal States (Leaf Nodes): ", math.pow(bran,dep+1))

one = np.random.randint(low=min, high=max, size=bran)
one = one.tolist()
two = np.random.randint(low=min, high=max, size=bran)
two = two.tolist()
three = np.random.randint(low=min, high=max, size=bran)
three = three.tolist()

tree = [[one, two], [three]]
print(tree)

root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global tree
    global root
    global pruned
    i = 0
    for child in branch:
        if type(child) is list:
            (nalpha, nbeta) = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:
                beta = nalpha if nalpha < beta else beta
            else:
                alpha = nbeta if nbeta > alpha else alpha
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
            if alpha >= beta:
                pruned += 1
                break
    if depth == root:
        tree = alpha if root == 0 else beta
    return (alpha, beta)

def alphabeta(in_tree=tree, start=root, upper=max, lower=min):
    global tree
    global pruned
    global root

    (alpha, beta) = children(tree, start, upper, lower)
    
    if __name__ == "__main__":
        #print ("(alpha, beta): ", alpha, beta)
        #print ("Result: ", tree)
        print ("Maximum amount: ", pruned)
        print ("Comparisons: ", math.pow(bran,dep+1))
        z = math.pow(bran,dep+1)
        z = z - pruned
        z = z + 1
        print ("Comparisons: ", z)

    return (alpha, beta, tree, pruned)

if __name__ == "__main__":
    alphabeta(None)