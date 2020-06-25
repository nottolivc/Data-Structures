# create the node class
class BST:

    def __init__(self,rootValue):
        self.value = rootValue
        self.left  = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    def addValue(self,newValue):
        if newValue == self.value: 
            return self
        if newValue < self.value:
            if self.left : return self.left.addValue(newValue)
            self.left = BST(newValue)
            return self.left
        if self.right : return self.right.addValue(newValue)
        self.right = BST(newValue)
        return self.right

    def printTree(self):
        print(self, lambda n:(str(n.value),n.left,n.right))      

root = BST(80)

root.addValue(50)
root.addValue(90)
root.addValue(10)
root.addValue(60)
root.addValue(30)
root.addValue(70)
root.addValue(55)
root.addValue(5)
root.addValue(35)
root.addValue(85)

root.printTree()