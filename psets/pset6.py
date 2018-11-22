# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Max Heap 
# Term:       Summer 2018


class TreeNode:
    def __init__(self, priority):
        self.priority = priority 
        self.parent = None
        self.l_child = None
        self.r_child = None
    def __eq__(self, other):
        return self.priority == other.priority     


class MaxHeap:

    def __init__(self, ints):
        self.ints = self.heapify(ints) 
        
    def get_heap(self):
        return self.ints

   

    def sieve_down(self, ints, pos = 0):         
        l = pos * 2 + 1
        r = pos * 2 + 2
        maximum = pos
 #       if r == len(ints) and ints[pos] < ints[l]:
            #one left child
        #    ints[l], ints[pos] = ints[pos], ints[l]
        
        if r >= len(ints):
            if l == len(ints)-1 and ints[pos] < ints[l]:
                ints[l], ints[pos] = ints[pos], ints[l]
            return ints #base 
        if ints[l] > ints[pos]:
            maximum = l
            pos = l
        if ints[r] > ints[maximum]:
            maximum = r
            pos = r
        if maximum != pos:
            ints[maximum], ints[pos] = ints[pos], ints[maximum]
           # return self.sieve_down(ints, maximum)
            return self.sieve_down(ints, pos + 1)
        return ints
 

    def heapify(self, ints):
        #shape + heap
        if ints == []:
            return []
        start = (len(ints) - 1) // 2
        while start >= 0:
            ints = self.sieve_down(ints, start)
            start -= 1
##        for pos in range(len(ints), -1, -1):
##            ints = self.sieve_down(ints, pos)
        return ints 


    def insert(self, new_int):
        self.ints += [new_int]
        pos = len(self.ints) - 1 
        pr = (pos - 1) // 2 # parent
        while pos > 0 and pr >= 0: #-1 if list empty
            if self.ints[pos] > self.ints[pr]:
                 self.ints[pos], self.ints[pr] = self.ints[pr], self.ints[pos]
            pos = pr
            pr = (pos - 1) // 2
                        

    def delete(self):
        #empty 
        if self.ints == []:
            return None
        #swap
        deleted = self.ints[0]
        self.ints[0] = self.ints[-1]
        self.ints = self.ints[:-1]
        #sift down the root
        self.ints = self.sieve_down(self.ints) 
        return deleted
                

    def sort_heap(self):
        #Return a sorted list of this heap's integers using heap sort.
 
        sort = []
        l = self.ints[:]
#        m = MaxHeap(self.ints)
        for i in range(len(self.ints)):           
            root = l.delete()
            sort.append(root)
        self.ints = [i for i in l]
        return sort[::-1]



    def create_tree(self):
        #empty
        if self.ints == []:
            return None
        if len(self.ints) == 1:
            return TreeNode(self.ints[0])
        nodelist = [TreeNode(i) for i in self.ints]
        root = nodelist[0]
        for pos in range(len(nodelist)):
            l = pos * 2 + 1
            r = pos * 2 + 2
            parent = (pos - 1) // 2
            if l < len(nodelist):
                nodelist[pos].l_child = nodelist[l]
            if r < len(nodelist):
                nodelist[pos].r_child = nodelist[r]
            if parent >= 0:
                nodelist[pos].parent = nodelist[parent]
        return root

 
