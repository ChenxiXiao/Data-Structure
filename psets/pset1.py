# Name: Chenxi Xiao        
# Course: CPE 202      
# Instructor: Daniel Kauffman 
# Assignment: Practice Set
# Term: Summer 2018

def permute(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    else:
        l = []
        for i in s:
            record = [x for x in s if x != i]
            for j in permute(record):
                l.append(i + "".join(j))
        return l
    
        
        
def is_reachable(n):
    goal = 42
    if n == goal:
        return True
    if n < goal:
        return False
    if n % 2 == 0:
        if is_reachable(int(n / 2)):
            return True     
    if n % 3 == 0 or n % 4 == 0:
        req2 = int(str(n)[-1 * 2])
        req1 = int(str(n)[-1])  
        sub_12 = n - int(str(n)[-1]) * int(str(n)[-1 * 2])
        if req1 != 0 and req2 != 0 and is_reachable(sub_12):
            return True
#Runtime Error when substitute is_reachable with a variable 

    if n % 5 == 0:
        if is_reachable(n - goal):
            return True
    return False
       
