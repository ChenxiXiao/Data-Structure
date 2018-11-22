# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Separate Chaining
# Term:       Summer 2018



class ChainHashTable:


    def __init__(self, size):
        self.size = size
        self.key = [[] * i for i in range(size)]
        self.value = [[] * i for i in range(size)]
        self.collision = 0
        if self.size <= 0:
            raise ValueError
        

    def hash(self, key):
        return key % self.size


    def get_load_factor(self):
        count = 0
        for i in self.value:
            for j in i:
                count += 1
        if count == 0:
            return 0
        res = count / self.size
        return res


    def get(self, key):
        hashed_res = self.hash(key)
        for i in range(len(self.key[hashed_res])):
            if key == self.key[hashed_res][i]:
                return self.value[hashed_res][i]
        raise LookupError


    def put(self, key, value):
        maximum = 1.5
        if key < 0:
            raise ValueError 
        hashed_res = self.hash(key)
        if key in self.key[hashed_res]: 
            loc = self.key[hashed_res].index(key)
            del self.value[hashed_res][loc]
            self.value[hashed_res].append(value) 
        else:
            if self.key[hashed_res] != []: # not empty-- collision happens
                self.collision += 1
            self.key[hashed_res].append(key)
            self.value[hashed_res].append(value)
        if self.get_load_factor() > maximum:
            temp = self.size
            self.size = (self.size * 2) + 1
            self.value = self.value + [[] * i for i in range(self.size - temp)]
            self.key = self.key + [[] * i for i in range(self.size - temp)]

            
        #After creating the new hash table,
            #all key-value pairs are rehashed into it.
            self.rehashed(temp)
        
    
    def rehashed(self, temp):
##        key_table = [[]] * size
##        value_table = [[]] * size
        for i in range(temp):
            for j in range(len(self.key[i]))[::-1]:
                new_key = self.key[i][j]
                hashed_res = self.hash(new_key)
                value = self.value[i][j]
                if hashed_res != i: # move to the end
                    if self.key[hashed_res] != []: # not empty-- collision happens
                           self.collision += 1
                    self.key[hashed_res].append(new_key)
                    self.value[hashed_res].append(value)
                    #remove(self.key[i].remove(self.key[i][j]))
                    del self.key[i][j] # index
                    del self.value[i][j]
        #don't need to consider repetitive key

        
    def delete(self, key):
        for i in range(len(self.key)):
            for j in range(len(self.key[i])):
                if key == self.key[i][j]: # move to the end 
                    stored_value = self.value[i][j]
                    #remove(self.key[i].remove(self.key[i][j]))
                    del self.key[i][j] # index
                    del self.value[i][j]
                    return (key, stored_value)
        raise LookupError


    def get_collisions(self):
        return self.collision
