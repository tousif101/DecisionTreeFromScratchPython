class Node(object):
    def __init__(self,attribute,threshold, isLeaf, entropy,classification):
        self.left = None
        self.right = None
        self.attribute = attribute
        self.threshold = threshold
        self.isLeaf = isLeaf
        self.entropy = entropy
        self.classification = classification

    def printtree(self,node):
        if node.left is not None:
            self.printtree(node.left)
        print("--The Classification is " + str(node.classification))
        print("--The Attribute is " + str(node.attribute))
        if node.right is not None:
            self.printtree(node.right)

    # def getLeft(self):
    #     return self.left
    #
    # def setLeft(self,value):
    #     self.left = value
    #
    #
    # def getRight(self):
    #     return self.right
    #
    # def setLeft(self, value):
    #     self.left = value




            # class Tree:
#     def __init__(self):
#         self.root = None
#
#     def getRoot(self):
#         return self.root


## attribute, threshold, leaf or not, class, pointer left or right