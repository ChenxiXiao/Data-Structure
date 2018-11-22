# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Sorting 
# Term:       Summer 2018

import random
import sys
import time


def main():
    limit = 1000
    if len(sys.argv) != 2:
        print("usage: python3 sorting.py SIZE")
        sys.exit()
    else:
        try:
            n_int = int(sys.argv[1])
        except ValueError:
            print("SIZE must be an integer")
            sys.exit()
    unsorted = [random.randint(0, limit) for i in range(n_int)]
    goal = sorted(unsorted)
    fmt_str = ("{0:<14}: {1:>4} | {2:7.3f} Seconds | " +
               "{3:11,d} Comparisons | {4:11,d} Swaps")
    fun_dict = {"[1] Bubble": bubble_sort, "[2] Selection": selection_sort,
                "[3] Insertion": insertion_sort, "[4] Merge": merge_sort,
                "[5] Quick": quick_sort}
    for name, function in sorted(fun_dict.items(), key = lambda t: t[0]):
        list_copy = list(unsorted)
        start = time.time()
        n_comp, n_swap = function(list_copy)
        duration = time.time() - start
        status = "OK" if list_copy == goal else "FAIL"
        print(fmt_str.format(name, status, duration, n_comp, n_swap))



def bubble_sort(ints):
    comp = 0#comparison
    swap = 0
    for i in range(len(ints) - 1, 0, -1):
        for j in range(i):
            comp += 1
            if ints[j] > ints[j + 1]:
                ints[j], ints[j + 1] = ints[j + 1], ints[j]
                swap += 1
    return (comp, swap)


def selection_sort(ints):
    comp = 0#comparison
    swap = 0
    for i in range(len(ints)):
        minimum = i
        for j in range(i, len(ints)):
            comp += 1
            if ints[minimum] > ints[j]:
                minimum = j
        ints[minimum], ints[i] = ints[i], ints[minimum]
        swap += 1          
    return (comp, swap)


def insertion_sort(ints):
    # start from pos = 1
    #compare with range(pos)
    comp = 0
    swap = 0
    for i in range(1, len(ints)):
        for j in range(i, -1, -1):
            val = ints[j]
            while ints[j] < ints[j - 1] and j - 1 >= 0:
                ints[j] = ints[j - 1]
                j -= 1
                comp += 1
                swap += 1
            ints[j] = val
    return (comp, swap) 


def merge_sort(ints):
    res = get_res(ints)
    new_ints = res[0]
    for i in range(len(new_ints)):
        ints[i] = new_ints[i]
    return res[1]

        
def get_res(ints):
    if len(ints) < 2:
        return [ints[:], (0, 0)]
    mid = len(ints) // 2 # has to be an int
    l = get_res(ints[:mid]) 
    r = get_res(ints[mid:])
    comp = l[1][0] + r[1][0]
    swap = l[1][1] + r[1][1]
    res = merge(l[0], r[0], comp, swap)
    return [res[0], (res[1][0], res[1][1])]

    
def merge(l, r, comp = 0, swap = 0): 
    new_list = []
    if r == [] or l == []:
        new_list = new_list + l + r
    while l != [] and r != []:
        comp += 1
        if l[0] < r[0]:
            new_list.append(l[0])           
            del l[0]
        else:
            new_list.append(r[0])
            del r[0]
            swap += 1
        if r == [] or l == []:
            new_list = new_list + l + r
            break
    return [new_list, [comp, swap]]
       

def median(ints):
    l = []
    #pivot = median of left-most rightmost and center
    left = 0
    l.append(ints[left])
    center = len(ints) // 2
    l.append(ints[center])
    right = len(ints) - 1
    l.append(ints[right])
    l.remove(max(l))
    l.remove(min(l))
    if l[0] == ints[center]:  # left < center < right??? s
        pivot = [center, ints[center]]
    elif l[0] == ints[left]:
        pivot = [left, ints[left]]
    else:
        pivot = [right, ints[right]] #(index, value)
    return pivot



def update_pivot(ints):
    comp = swap = 0
   # L = ints[:len(ints) - 1]
#    R = []  #return
    pivot = median(ints)
    # set the median
    #pivot index = pivot[0] 
    ints[pivot[0]], ints[len(ints) - 1] = ints[len(ints) - 1], ints[pivot[0]]
    #swap with the last element 
    LIndex = 0 # start from beginning 
    RIndex = len(ints) - 2 # start from left of the pivot
    while LIndex < RIndex: #break when ==
        while ints[LIndex] < pivot[1] and RIndex != LIndex: #move  to the right until a bigger num found
            LIndex += 1
            # pivot unchange
        while ints[RIndex] >= pivot[1] and RIndex != LIndex: #finid a smaller
            RIndex -= 1
        comp += 2
        if RIndex == LIndex:
            break
        #if LIndex < RIndex:  
        swap += 1
        ints[LIndex], ints[RIndex] = ints[RIndex], ints[LIndex]
        LIndex += 1
    #if RIndex == LIndex:
    ints[LIndex], ints[-1] = ints[-1], ints[LIndex]
    # pivot[0] = RIndex #position don't matter
    #pivot [1] is the value
    return [ints[:RIndex], pivot[1], ints[RIndex + 1:], comp, swap]




def sort(ints, comp = 0, swap = 0):
    if len(ints) <= 2:
        if len(ints) == 2 and ints[0] > ints[1]:
            swap += 1
            ints[0], ints[1] = ints[1], ints[0]
        return (ints, comp, swap)
    res = update_pivot(ints)
    #pivot = res[1]
    comp += res[2 + 1]
    swap += res[2 + 2]
    l = sort(res[0], comp, swap)  
    r = sort(res[2], comp = 0, swap = 0)
    if len(l) == 2 + 1:
        comp = l[1]
        swap = l[2]
        l = l[0] # extract the list from [list, comp, swap]
    if len(r) == 2 + 1:
        comp += r[1]
        swap += r[2]
        r = r[0] # extract list  
    return [l + [res[1]] + r, comp, swap]


def quick_sort(ints):
    sorted_res = sort(ints)
    ints_list = sorted_res[0]
    comp = sorted_res[1]
    swap = sorted_res[2]
    for i in range(len(ints_list)):
        ints[i] = ints_list[i]
    return (comp, swap)



if __name__ == "__main__":
    main()

