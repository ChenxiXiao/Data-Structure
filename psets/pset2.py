# Name: Chenxi Xiao        
# Course: CPE 202      
# Instructor: Daniel Kauffman 
# Assignment: Pset2
# Term: Summer 2018


class Stack:


    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError
        self.list = [None] * capacity
        

    def push(self, item):
        if None not in self.list:
            raise ValueError
        for i in range(len(self.list)):
            if self.list[i] == None:
                self.list[i] = item
                break           


    def pop(self):
        if self.list[0] == None:
            raise ValueError
        for i in range(len(self.list))[::-1]:
            if self.list[i] != None:
                temp = self.list[i]
                self.list[i] = None
                break
        return temp

