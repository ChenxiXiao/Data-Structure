# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Binary Search Tree 
# Term:       Summer 2018

class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = None
        self.l_child = None
        self.r_child = None
##    def __repr__(self):
##        return "{0} : {1}".format(self.key, self.val)            
    def is_occuppied(self):
        return self.l_child != None and self.r_child != None


class BinarySearchTree:        
    def __init__(self):
        self.root = None
        
    def insert(self, key, val):
        root = self.root
        if root == None:
            self.root = TreeNode(key, val) 
        elif key > root.key:
            if root.r_child is None:
                root.r_child = TreeNode(key, val)
                root.r_child.parent = root
            else:
                BST = BinarySearchTree()
                BST.root = root.r_child 
                BST.insert(key, val)
        else: #key < root.key:
            if root.l_child is None:
                root.l_child = TreeNode(key, val)

                root.l_child.parent = root
            else:
 
                BST = BinarySearchTree()
                BST.root = root.l_child
                BST.insert(key, val)
                   


    def delete_leaf(self, key, temp = None):
        if temp == None:
            temp = self.root
        if key > temp.key:
            temp = temp.r_child 
            return self.delete_leaf(key, temp)
        elif key < temp.key:
            temp = temp.l_child
            return self.delete_leaf(key, temp)
        #if key == root.key: #item found
        elif key == temp.key:
            if temp.is_occuppied() or temp.parent == None:
                return temp
            else: #delete a leave
            
                if key < temp.parent.key:
                
                    temp.parent.l_child = None
                else:
                    temp.parent.r_child = None
                return -1#leaf deleted 


    def delete_root(self, key, temp):
        if temp.l_child == None and temp.r_child == None: #only one node in the tree
            self.root = None
        elif temp.l_child: #there is a left child
            bst = BinarySearchTree()
            bst.root = temp.l_child
            l_max = bst.find_max() #method
            if l_max == temp.key: #no max value//no right child
                if temp.r_child != None:
                    temp.l_child.r_child = temp.r_child
                self.root = temp.l_child
                self.root.parent == None
              #left child becomes the root of the tree
            else:
                rm_leave = self.delete_leaf(l_max, temp)
                temp.key = l_max
            #substitue the root with the last node
        else: # there is no left child but a right child
            self.root = temp.r_child
            self.root.parent = None
            
            

    def sieveup(key, temp):
        #sieve up when there is no interior child
        sieved = temp.l_child.r_child = temp.r_child
        if temp.key < temp.parent.key: #parents l_child
            temp.parent.l_child = sieved
            sieved.parent = temp.parent
        else:
            temp.parent.r_child = sieved
            sieved.parent = temp.parent # parents r_child 
        

    def delete_interior(self, key, temp):
        bst = BinarySearchTree()
        bst.root = temp.l_child
        l_max = bst.find_max()
        bst = BinarySearchTree()
        bst.root = temp.r_child
        r_min = bst.find_min()
        if l_max == temp.key: # left node doesn't have max
            if temp.r_child.l_child is None: 
                sieveup(key, temp)                                                         
            else:
                rm_leave = self.delete_leaf(r_min, temp)
                temp.key = r_min                            
        else:
            self.delete(l_max, temp)
            temp.key = l_max


    def delete(self, key, temp = None):
        temp = self.delete_leaf(key, temp)
        if temp != -1:
           # node
            if temp.parent == None: #root
                self.delete_root(key, temp)
            else: #interior node
                self.delete_interior(key, temp)


 
    def find_min(self):
        l = self.root
        if l == None:
            return None
        while l.l_child != None:
            l = l.l_child

        return l.key

    def find_max(self):
        r = self.root
        if r == None:
            return None
        while r.r_child != None:
            r = r.r_child

        return r.key

    def contains(self, key):
    #Efficiently traverse the BST
        #to find the TreeNode ​containing the given key​.
        #If found, return True​, otherwise return​ False​.
        root = self.root
        if self.root:
            if key == root.key:
                return True
            if key > root.key:
                BST = BinarySearchTree()               
                BST.root = root.r_child               
                return BST.contains(key)
            else: 
                BST = BinarySearchTree()
                BST.root = root.l_child
                return BST.contains(key)
        else:
            return False


    def inorder_list(self):
        res = []
        if self.root == None:
            return []
        if self.root.l_child:
            BST  = BinarySearchTree()
            BST.root = self.root.l_child
            res += BST.inorder_list()
        res += [self.root.key]
        
        if self.root.r_child:
            BST  = BinarySearchTree()
            BST.root = self.root.r_child
            res += BST.inorder_list()
        return res

    def preorder_list(self): #need to initiate l as [] when calling or the previous l will be carried in
        res = []
        if self.root == None:
            return []
        res += [self.root.key]
        if self.root.l_child:
            BST  = BinarySearchTree()
            BST.root = self.root.l_child           
            res += BST.preorder_list()
        if self.root.r_child:
            BST  = BinarySearchTree()
            BST.root = self.root.r_child
            res += BST.preorder_list()
        return res
       

    
    def postorder_list(self):
        res = []
        if self.root == None:
            return []
        if self.root.l_child:
            BST  = BinarySearchTree()
            BST.root = self.root.l_child           
            res += BST.postorder_list() 
        if self.root.r_child:
            BST  = BinarySearchTree()
            BST.root = self.root.r_child
            res += BST.postorder_list()
        res += [self.root.key]
        return res






