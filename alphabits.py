# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Alphabits
# Term:       Summer 2018


def get_char_freq(string):
    ASCII = 256
    res = [0] * ASCII
    for s in string:
        res[ord(s)] += 1
    return res


def comes_before(tree_a, tree_b):
    if tree_a.freq < tree_b.freq:
        return True
    elif tree_a.freq == tree_b.freq and ord(tree_a.char) < ord(tree_b.char):
        return True
    return False

    
class HuffmanNode:
    def __init__(self, char, freq = 0, l_child = None, r_child = None):
        self.char = char
        self.l_child = l_child
        self.r_child = r_child
        self.freq = freq
#    def __repr__(self):
 #       return self.char
    def __eq__(self, other):
        return self.char == other.char and self.freq == other.freq 

        
def create_tree(freq_list):
    #create node #add to sorted_list
    unsorted = []
#    space = 32
#    Del = 127
    for index in range(len(freq_list)):  #freq_list
        if freq_list[index] > 0:
           unsorted.append(HuffmanNode(chr(index), freq_list[index]))
    if len(unsorted) == 0:
        return None
    sorted_list = sort(unsorted)
    #combine nodes until there is only one root left in the sorted list
    while len(sorted_list) != 1:
            #remove 2 lowest and append a new combined node
        low1 = sorted_list[0]
        low2 = sorted_list[1]
        par = min(ord(low1.char), ord(low2.char))#parent char
        freq = low1.freq + low2.freq
        new_node = HuffmanNode(chr(par), freq, low1, low2)
         #append in the beginning
        sorted_list.append(new_node)
        sorted_list.remove(low1)
        sorted_list.remove(low2)
        sorted_list = sort(unsorted) #relocate
    return sorted_list[0]       



def sort(unsorted_list):
    sorted_list = unsorted_list
    for n in range(len(sorted_list)):
        for j in range(n):
            if comes_before(sorted_list[n], sorted_list[j]):
                sorted_list[n], sorted_list[j] = sorted_list[j], sorted_list[n]
    return sorted_list


def create_code(root): #edge: ONLY ONE CHARARCTER?? 
    ASCII = 256
    l = [''] * ASCII
    if root is None:
        return l
    def bit(root, s = '', l = []):
        if root.l_child is not None:
            bit(root.l_child, s + '0')
        if root.r_child is not None:
            bit(root.r_child, s + '1') 
        else:
            l.append([s, root.char])
        return l
    bits = bit(root)
    for i in bits:
        bit_string = i[0]
        char = i[1]
        l[ord(char)] = bit_string
    return l



def encode(string):
    res = ''
    freq = get_char_freq(string)
    root = create_tree(freq)
    l = create_code(root)
    for s in string:
        res += l[ord(s)]
    return res


def decode(bit_string, freq_list):
    res = ''
    acc = ''
    root = create_tree(freq_list)
    l = create_code(root)
    code_guide = []
    for code in range(len(l)):
        if l[code] != '':
            code_guide.append([l[code], chr(code)])
    for bit in bit_string:
        acc += bit
        for code in code_guide:
            if code[0] == acc:
                res += code[1]
                acc = ''
    return res
        
