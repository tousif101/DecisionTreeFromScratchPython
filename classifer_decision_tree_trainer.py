"""
@Author: Tousif Chowdhury
"""

import csv
import math
from binarytree import Node


"""
Read in file and assign to seperate arrays for each row
"""
my_file = csv.reader(open("DecTree_Training__v200.csv"))

attr1 = []
attr2 = []
attr3 = []
attr4 = []
classification = []

for row in my_file:
    attr1.append(row[0])
    attr2.append(row[1])
    attr3.append(row[2])
    attr4.append(row[3])
    classification.append(row[4])

attr1.pop(0)
attr2.pop(0)
attr3.pop(0)
attr4.pop(0)
classification.pop(0)

attr1float = [float(i) for i in attr1]
attr2float = [float(i) for i in attr2]
attr3float = [float(i) for i in attr3]
attr4float = [float(i) for i in attr4]

"""
Get the approiate thresholds
"""
thresholds = []
for i in range(1,100):
    thresholds.append(i/10)


"""
Make a list of tuples from the information read in the file to throw
into our classifer.
"""
listValues = []
for i in range(0,len(attr1float)):
    valueTuple = (attr1float[i],attr2float[i],attr3float[i],attr4float[i], classification[i])
    listValues.append(valueTuple)


"""
Takes in the attributes values, the classifcation data, and the threshold
Does all the math to find the entropy.
Return weighted entropy
"""
def calculationEntropy(attribute,yesorno, threshold):

    classLessThreshold = 0
    notclassLessThreshold = 0
    classGreaterThreshold = 0
    notClassGreaterThreshold = 0

    for i in range(0, len(attribute)):
        if yesorno[i] == '1' and attribute[i] <= threshold:
            classLessThreshold += 1
        if yesorno[i] == '1' and attribute[i] > threshold:
            classGreaterThreshold += 1
        if yesorno[i] == '0' and attribute[i] <= threshold:
            notclassLessThreshold += 1
        if yesorno[i] == '0' and attribute[i] > threshold:
            notClassGreaterThreshold += 1

    totalGreaterThan = 0
    totalLessThan = 0
    for item in attribute:
        if item <= threshold:
            totalLessThan += 1
        if item > threshold:
            totalGreaterThan += 1


    if classLessThreshold == 0:
        entropyClassLess = 0
    else:
        entropyClassLess = (classLessThreshold / totalLessThan) * math.log((classLessThreshold / totalLessThan), 2)

    if notclassLessThreshold == 0:
        entropyNotClassLess = 0
    else:
        entropyNotClassLess = (notclassLessThreshold / totalLessThan) * math.log((notclassLessThreshold / totalLessThan), 2)

    if classGreaterThreshold == 0:
        entropyClassGreater = 0
    else:
        entropyClassGreater = (classGreaterThreshold / totalGreaterThan) * math.log((classGreaterThreshold / totalGreaterThan), 2)

    if notClassGreaterThreshold == 0:
        entropyNotClassGreater = 0
    else:
        entropyNotClassGreater = (notClassGreaterThreshold / totalGreaterThan) * math.log((notClassGreaterThreshold / totalGreaterThan), 2)

    entropyLesserAttribute = -entropyClassLess - entropyNotClassLess


    entropyGreaterAttribute = -entropyClassGreater - entropyNotClassGreater


    weightedEntropy = (totalGreaterThan * entropyGreaterAttribute + totalLessThan * entropyLesserAttribute) / len(attribute)

    return weightedEntropy


"""
Decision algorithm. Takes in a list of values, a node and the depth of
the tree.
"""
def decisionTree(node,listValues,depth):
    #Get all possible thresholds.
    thresholds = []
    for i in range(1, 100):
        thresholds.append(i / 10)

    #Break into new arrays, so its easier to put into entropy function
    newAttributeOne = []
    newAttributeTwo = []
    newAttributeThree = []
    newAttributeFour = []
    newClassification = []
    for val in listValues:
        newAttributeOne.append(val[0])
        newAttributeTwo.append(val[1])
        newAttributeThree.append(val[2])
        newAttributeFour.append(val[3])
        newClassification.append(val[4])
    attributes = [newAttributeOne,newAttributeTwo,newAttributeThree,newAttributeFour]

    #get the most classified value
    zeroCounter = 0
    oneCounter = 0
    mostClassfied = None
    for val in newClassification:
        if val == "0":
            zeroCounter += 1
        if val == "1":
            oneCounter += 1

        if zeroCounter > oneCounter:
            nodeChildLeft = Node(None,None,True,None,0)
            node.left = nodeChildLeft
            mostClassfied = "0"
        else:
            nodeChildRight = Node(None, None, True, None, 1)
            node.right = nodeChildRight
            mostClassfied = "1"

    #base case is reached. Return the tree.
    if depth >= 4:
        return node

    else:
        #for each attributes look at all possible thresholds
        #for each threshold, go through all data in 1 attribute
        # now I split. Find best split. threhold and entropy.
        bestEntropyValue = 10000
        bestThreshold = 1000
        counter = 0
        bestAttribute = 0
        for attribute in attributes:
            counter +=1
            for threshold in thresholds:
                entropy = calculationEntropy(attribute,classification,threshold)
                if entropy < bestEntropyValue:
                    bestEntropyValue = entropy
                    bestThreshold = threshold
                    bestAttribute = counter

        #split the data based on the best attribute and threshold found.
        #Add to tree
        leftSplit = []
        rightSplit = []
        for val in listValues:
            if val[bestAttribute-1] <= bestThreshold:
                leftSplit.append(val)
            if val[bestAttribute-1] >= bestThreshold:
                rightSplit.append(val)

        #create node and add to tree.
        node.entropy = bestEntropyValue
        node.threshold = bestThreshold
        node.attribute = bestAttribute
        node.isLeaf = False

        nodeLeft = Node(None, None, None,None,None)
        nodeRight = Node(None, None, None,None,None)

        node.left = nodeLeft
        node.right = nodeRight

        #recurse on both halfs
        decisionTree(nodeLeft,leftSplit, depth+1)
        decisionTree(nodeRight,rightSplit, depth+1)


#node that the function returns

"""
Code to write to the file.
Could not finish. Did not fully understand how to use
the trainer tree and write to a python file with the right
code.
"""

node = Node(None,None,None)
node = decisionTree(node)


#print begining, imports
#open the csv
# do function declation classify(node)

#seperate function that recurses on itself


"""
Work on implenting using the generated decision tree to classify data.
"""
def start():
    open("HW_5B_Chowdhury_Tousif.py", "w")

def write():
    stringToWrite = "import sys" \
                    "file = sys.argv[1]" \
                    ""



