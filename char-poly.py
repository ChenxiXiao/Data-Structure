def poly_add2(poly1, poly2):
    poly = []    
      #create a list for sum of the input polynomials 
    x1 = poly1[0] + poly2[0]
    poly.append(x1)
    x2 = poly1[1] + poly2[1]
    poly.append(x2)       
   # poly.append[2]--doesn't mean anything  = poly1[2] + poly2[2]                   
    x3 = poly1[2] + poly2[2]    
    poly.append(x3)   
    return poly 


assert poly_add2([1, 2, 3], [2, 5, 6]) == [3, 7, 9]
assert poly_add2([2, 2, 2], [3, 4, 5]) == [5, 6, 7]
assert poly_add2([3, 4, 5], [5, 4, 3]) == [8, 8, 8]


def poly_mult2(poly1, poly2):
    poly = []
    x1 = poly1[0]*poly2[0]
    poly.append(x1)
    x2 = poly1[1] * poly2[0] + poly1[0] * poly2[1] 
    poly.append(x2)
    x3 = poly1[2] * poly2[1] + poly1[1] * poly2[2] 
    poly.append(x3)
    x4 = poly1[2] * poly2[2] 
    poly.append(x4)
    return poly
assert poly_mult2([1, 0, 3], [1, 1, 1]) == [1, 1, 3, 3]
assert poly_mult2([3, 4, 5], [4, 5, 6]) == [12, 31, 49, 30]
assert poly_mult2([1, 2, 3], [1, 2, 3]) == [1, 4, 12, 9]


def is_lower_101(char):
    return ord(char) in range(ord('a'), ord('z')+1)
    


# if not +1::[x,??] generate numbers up to, but not including this number
#if not RETURN, return NONE
# return string to number --- FALSE 
# ord('a') <= ord(char) <= ord('z')
   # 'a' <= char <='z'
#COMPLICATED:
   # if len(char) == 1:
   # if 'a' <= char <= 'z':
    #    return True
       #incorrect: if char in chr(ord(A..Z)):
    #    if 'A' <= char <= 'Z':
     #        return False
    
print("e is lowercase", is_lower_101('e')) 
assert is_lower_101('e') == True
assert is_lower_101('T') == False 
assert is_lower_101('Z') == False 
# ?? integer has no len: how to len a number --assert is_lower_101(1) == None  
#TRUE : print(is_lower_101('e'))


def char_rot_13(char):
  #  decode = [] #create a list for decoded sentence 
    if char.isalpha():
 # isalpha() is a method of the string class. original.isalpha()
# test if the string is all letters or not
        if char.islower():
            new_char = chr(ord(char) - 13) #what if goes out of range 
            if  new_char < 'a':
                return chr(ord(new_char)+26) 
            return x
      #          decode.append(x) only a single character `
        if char.isupper():
            new_char = chr(ord(char) + 13) #unboundedLocalERROR used before assignment 
            if new_char > 'Z':
                return chr(ord(new_char) -26)
            return y
     #           decode.append(y)
   # return decode 

print('a', char_rot_13('a'))
assert char_rot_13('a') =='n'
assert char_rot_13('N') =='A'
assert char_rot_13('b') =='o'


def str_rot_13(my_str):
    text = []
    time = 0 
    while time < len(my_str):   
        word = my_str[time]
        time += 1
        if ord(word) - 13 < 0: 
       # return chr(ord(my_str) + ord(s))
            x = chr(13-ord(word))
        else:
            x = chr(ord(word) -13)
        text.append(x)
    merge_text = ''.join(text)
    return merge_text
print('xx.?L', str_rot_13("xx.?L"))

assert str_rot_13('x.x') == 'k!k'
assert str_rot_13('<>.') == '/1!'
assert str_rot_13('L0') == '?#'



def str_translate_101(my_str, old, new):
    text = []
    time = 0
    while time < len(my_str):
        x = my_str[time]        
        time += 1
        if old == x:
             x = new 
        text.append(x)
        ##print out seperately 
  #  x = str(old)
   # for x in my_str:
    #    my_str[len(x)] = new
    #str' object does not support item assignment
    y ="".join(text)    
    return y
print('abscdd',str_translate_101("abscdd", "d", "D"))
assert str_translate_101("abcdcba", "a", "x") == "xbcdcbx"
assert str_translate_101("BWTBW", "B", "b") == "bWTbW"
assert str_translate_101("Ass","A", "ble") == "bless" 
