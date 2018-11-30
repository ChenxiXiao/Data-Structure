# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Post Fix It
# Term:       Summer 2018

def main():
    pass


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
        temp = None
        popped = False
        for i in range(len(self.list))[::-1]:
            if self.list[i] != None:
                temp = self.list[i]
                self.list[i] = None
                popped = True
                break 

        if not popped and self.list[0] == None:
            raise ValueError
        return temp


def add_parentheses(s):
    if '(' in s or ')' in s or len(s) == 0:
        return s       
    else:
        operator = '^*/-+'
        l = s.split() # list form
        for op in operator:
            while op in l:
                 l = merge(l, op) #return a new string       
        res = " ".join(list(l[0])) #l = ['(1+((2*5)/6))']
    return res 
            

def merge(s, op):
    if '^' == op:       
        loc = s[::-1].index(op) #find the last ^
        loc = (loc * -1) - 1 + len(s) # true loc
    else:
        loc = s.index(op)   
    merge = ['(' + ''.join(s[loc - 1: loc + 2]) + ')']
    s[loc - 1: loc + 2], merge = merge, s[loc - 1: loc + 2]
    return s 


def infix_to_postfix(input_str):
    input_str = add_parentheses(input_str)
    capacity = 30
    num_stack = Stack(capacity)
    op_stack = Stack(capacity)
    for char in input_str:
        if char.isdigit():
            num_stack.push(char)
        elif char in '^*/-+':
            op_stack.push(char)                     
        elif ')' == char:
            op = op_stack.pop()
            num_stack.push(op)
    
    output_str = ''
    while True:
        try:
            output_str = num_stack.pop() + output_str
        except ValueError:
            break
    output_str = ' '.join(list(output_str))
    return output_str
            

def postfix_valid(input_str):
    capacity = 30
    num_stack = Stack(capacity)
    if len(list(input_str.lstrip('-'))) == 1:
        return True
    if input_str == '': # prevent empty input
        return False
    for char in list(input_str.split(' ')):
        if char.isdigit() or char.lstrip('-').replace('.', '').isdigit():
            num_stack.push(char)
        #if char in '^*/-+':
        else:
            try:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
            except:
                return False
            num_stack.push(num1)
    return num_stack.list[1] == None and num_stack.list[0] != None


def pop_num(char, num_stack):
    num1 = num_stack.pop()
    num2 = num_stack.pop()
    if char == '^':
        num_stack.push(num2 ** num1)
    elif char == '*':
        num_stack.push(num2 * num1)
    elif char == '/':
        if num1 == 0:
            raise ValueError
        num_stack.push(num2 / num1)
    elif char == '-':
        num_stack.push(num2 - num1)
   # elif char == '+':
    else:
        num_stack.push(num1 + num2)
    return num_stack.list[0]


def postfix_eval(input_str):
    capacity = 30
    num_stack = Stack(capacity)
    if postfix_valid(input_str):
        l = list(input_str.split(' '))
        if len(l) == 1:
            return float(input_str)
        for char in l:
            ispos = char.replace('.', '').isdigit() 
            isneg = char[1:].replace('.', '').isdigit()
            if ispos or isneg:
                num_stack.push(float(char))
            #elif char in '^*/-+':
            else:
                res = pop_num(char, num_stack)
        return res





if __name__ == "__main__":
    main()

