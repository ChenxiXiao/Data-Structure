# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Queue
# Term:       Summer 2018


class Node:    
    def __init__(self, item, node = None):
        self.item = item
        self.node = node
##    def __repr__(self):
##        return "Node {0}".format(self.item)
        
        
class ListQueue:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.count = 0
    

    def enqueue(self, item): #appending a new node to the rear of the list     
        self.count += 1
        if self.capacity < self.count: #makesure it's not full
            self.count -= 1
            raise ValueError
        if self.head == None:
            self.head = Node(item)         
        else:
            temp = self.head
            while temp.node != None: #last node               
                temp = temp.node
                 #append new node inside the last one
                break
            temp.node = Node(item)   


    def dequeue(self): #dequeuing an item will require removing the front of the list.      
        if self.count == 0:
            raise ValueError       
        temp = self.head
        self.count -= 1
        self.head = self.head.node   
        return temp


class CircularQueue:
#The indices front and rear are incremented as
    #items are added and deleted from the queue
    #All arithmetic modulo the size of the array structure
    #allocated to store the queue.
    #Care must be taken in distinguishing a full from an empty queue.

    
    def __init__(self, capacity):

        self.buf = [None] * capacity
        self.count = 0
        self.capacity = capacity
        
        self.front = 0
        self.rear = capacity - 1
        

    def enqueue(self, item): #append rear
        size = self.size()
        if size == self.capacity:
            raise ValueError #full
        if size == 0 or self.front != 0 and self.rear == self.capacity:
            self.buf[0] = item
             #next pos
            self.rear = 0 
        else:
                
            self.rear = (self.rear + 1) % self.capacity
            self.buf[self.rear] = item           
            # update rear

            
    def dequeue(self): #head 
        if self.size() == 0:
            raise ValueError # empty
        else:
            temp = self.buf[self.front]
            self.buf[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return temp
            
    def size(self):
        num = 0
        for l in self.buf:
            if l != None:
                num += 1
        return num 
    
