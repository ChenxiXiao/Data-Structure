# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Ordered Doubly-Linked Lists
# Term:       Summer 2018


class Node:    
    def __init__(self, item, next = None, prev = None):
        self.item = item #(e.g. integer)
        self.next = next
        self.prev = prev # references 


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None #refers to a​ Node ​object


    def add(self, item):
        prev = None
        cur = self.head
        if self.head == None and self.tail == None:  
            self.head = self.tail = Node(item, None, None) # first item is the last item
        elif item < cur.item: #smallest
            node = Node(item, cur, None)
            self.head = node
            cur.prev = node
            
        elif cur.next == None:# one item #can only be bigger
            node = Node(item, None, cur)
            cur.next = self.tail = node
        else:
            self.add_assist(item, cur)


    def add_assist(self, item, cur):       
        while True:
            prev = cur
            cur = cur.next   
            if item < cur.item:
                node = Node(item, cur, prev) # node is connected with the current node
            
                prev.next = cur.prev = node# insert in the middle
                break
            elif cur.next == None and item > prev.item: #max number, append last
                self.tail = cur.next = Node(item, None, cur)
                break

                    #self.tail is the item 


    def remove(self, item):
        prev = None
        cur = self.head
        while cur != None:
            if cur.item == item:
                if cur.prev == None:#first
                    if cur.next == None: #only item
                        self.head = self.tail = None                   
                    else:
                        self.head = cur.next #delete the first item
                        self.head.prev = None  #update the head 
                else:
                    prev.next = cur.next
                    if cur.next == None: #last
                        self.tail = prev
                    else:
                        cur.next.prev = prev
                return True
            prev = cur
            cur = cur.next
        return False




    def index(self, item):
        cur = self.head
        index = 0
        while cur != None:
            if cur.item == item:
                return index
            cur = cur.next
            index += 1
        return None



    def pop(self, index):

        if index < 0:
            raise IndexError
        count = 0
        cur = self.head
        while cur != None:
            if index == count and self.remove(cur.item):
                return cur.item
            count += 1
            cur = cur.next
        raise IndexError

    
    def contains(self, item):           
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


    def to_list(self):
        l = []
        cur = self.head
        while cur != None:
            
            l.append(cur.item)
            cur = cur.next
        return l



    def to_reversed_list(self):
        if self.head == None:
            return []
        O = OrderedList()
        O.head = self.head.next
        O.tail = self.tail
        return O.to_reversed_list() + [self.head.item]
##        
##        l = []
##        cur = self.tail
##        while cur != None:
##            
##            l.append(cur.item)
##            cur = cur.prev
##        return l
##    
        
    

