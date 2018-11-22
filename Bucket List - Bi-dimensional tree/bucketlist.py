# Name:       Chenxi Xiao
# Course:     CPE 202   
# Instructor: Daniel Kauffman  
# Assignment: Bucket List
# Term:       Summer 2018


import math



def main():
   f = open("cities.csv", 'r')
   lines = f.readlines()
   table = create_table(lines[1:])
   ap = open("airports.csv", 'r')
   lines = ap.readlines()
   updated_table = update_table(table, lines[1:])
 
 #   pass
    

def create_table(lines, city_total = 257):
    table = CountryTable(city_total)
    for line in lines:
        
        lst = line.strip().split(',')
        #0 city 1 country 2 lat 3 lon
 #       print(lst[0], lst[1], lst[2], lst[3])
        country = lst[1].strip()
        if len(country) == 2:
            table.put_node(lst[0], country, float(lst[2]), float(lst[1 + 2]))
    return table



def update_table(table, lines):
    for line in lines:
        line = line.strip().split(',')
        ap = line[0]
      #  code = line[1].strip()
       # if code == '' or len(code) != 2:
        #    continue
        lat = float(line[2])
        lon =  float(line[1 + 2])
        closest_node = table.get_node(lat, lon)
        closest_node.airport = ap
        lat_x = closest_node.lat
        lon_x = closest_node.lon
        closest_node.distance = get_distance(lat_x, lon_x, lat, lon)
     

def find_travel_distance(table, lat_x, lon_x, lat_y, lon_y):
    A = table.get_node(lat_x, lon_x)
    a = A.distance
    if a is None:
        a = 0
    B = table.get_node(lat_y, lon_y)
    b = B.distance
    if b is None:
        b = 0
    ab = get_distance(A.lat, A.lon, B.lat, B.lon)
    distance = a + b + ab
    return distance




class CityNode:
    def __init__(self, city_name, country_code, latitude, longitude):
        self.name = city_name
        self.country = country_code #2-character string
        self.lat = latitude # type: float
        self.lon = longitude
        self.airport = None #3/4-character string
        self.distance = None # type: float
        self.children = {"ne": None, "nw": None, "se": None, "sw": None}
##        for k, v in self.children.items():
##            self.k = v

    def __eq__(self, other):
        con = False
        if self.lat == other.lat and self.lon == other.lon:
            con = True
        return con and self.name == other.name


    def __repr__(self):
        return '{0} , {1}'.format(self.name, self.country)
 

    def add_city(self, node, root = None):
        #add root -- put node
        # node will be appended to self
        ans = self.find_direction(node)        
        if self.children[ans]:
            self.children[ans].add_city(node)
#            root = self.update_tree(self, ans)
        else:
            #append to the tree
            self.children[ans] = node
            root = self.update_tree(self, ans)
        return root
#    def add_city(self, node):
        #add root -- put node
        # node will be appended to self
#        ans = self.find_direction(node)        
#        if self.children[ans]:
 #           self.children[ans].add_city(node)
 #           node = self.update_tree(self, ans)
#        else:
            #append to the tree
#            self.children[ans] = node
        #return node #root node
        # balance tree from the root -- self.children; direction = ans
#        return node #root 
              
         
    def find_direction(self, node):
        # node is _ans_ to the self
        s = ''
        if self.lat - node.lat >= 0: # =
            s += 's' #node should be appended on the south 
        else:
            s += 'n'
        if self.lon - node.lon >= 0:
            s += 'w'
        else:
            s += 'e'
        # detect
        return s
                   
    def update_tree(self, node, direction):
        factor = balance_factor(node, direction)
        if factor not in [-1, 0, 1]: #unbalance 
            reverse = {'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}
            rev = reverse[direction]
            if factor > 1: # >=1 #left heavy #right rotate
                node = rotate(node, direction)
            elif factor < -1: #opposite direction is heavy 
                node = rotate(node, rev)
        return node #parent node
         #root
            

def preorder(node, lchild, res = []):
    reverse = {'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}
    r_child = reverse[lchild]
    res += [node.name]
    if node.children[lchild]:
        preorder(node.children[lchild], lchild, res)
    
    if node.children[r_child]:
        preorder(node.children[r_child], lchild, res)
    s = '{0} : {1} , {2}'.format(lchild, r_child, res)
    return s


def rotate(node, direction):
    reverse = {'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}
    rev = reverse[direction]
    stored_root = node
    L_node = node.children[direction]
    R_node = node.children[rev]
    if balance_factor(L_node, direction) < 0: # zigzag
        #left rotate
        temp = L_node
        L_node = L_node.children[rev]
        stored = L_node.children[direction] 
        temp.children[rev] = stored
        L_node.children[direction] = temp
    temp = L_node.children[rev] #could be None
    node = L_node
    stored_root.children[direction] = temp # append the branch 
    node.children[rev] = stored_root # available for sure               
    return node #parent                  
            
    
def get_height(node, direction):
    reverse = {'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}
    rev = reverse[direction]
    # base will not be None
    if node is None:
        return 0
    if node.children[direction] is None and node.children[rev] is None:
        #self is the last node
        return 1
    dirc = get_height(node.children[direction], direction)
    oppo = get_height(node.children[rev], direction)
    return max(dirc, oppo) + 1


def balance_factor(node, direction):
    reverse = {'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}
    rev = reverse[direction]
    L = get_height(node.children[direction], direction) # return a height int
    R = get_height(node.children[rev], direction)
    return L - R #[-1, 0, 1] == balance
##        # positive number means input direction is heavy 


def get_distance(lat_x, lon_x, lat_y, lon_y):
    r = 6371
    lat_x = math.radians(lat_x)
    lat_y = math.radians(lat_y)
    lon_x = math.radians(lon_x)
    lon_y = math.radians(lon_y)
    df_lat = lat_x - lat_y
    df_lon = lon_x - lon_y
    equation = math.cos(lat_x) * math.cos(lat_y) *  (math.sin(df_lon / 2) ** 2) 
    under_root = (math.sin(df_lat / 2)) ** 2 + equation
    res = 2 * r * math.asin(math.sqrt(under_root))
    return res
   

class CountryTable:
    
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def get_bucket_list(self):
        return self.table

    def get_load_factor(self):
        bucket = 0
        for i in self.table:
            if i:
                bucket += 1
        if bucket == 0:
            return 0
        return bucket / self.size


    def resize(self):
        self.size = (self.size * 2) + 1
        temp = self.table[:]
        self.table = [None] * self.size
        for i in temp:
            if i: 
                key = self.hash(i.country) #rehash
                while key < self.size:
                    if self.table[key] is None:
                        # append a new country
                        self.table[key] = i
                        break
                    key += 1
                    if key == self.size:
                        key = 0


    def put_node(self, city_name, country_code, latitude, longitude):
        factor = 0.75
        city = CityNode(city_name, country_code, latitude, longitude)
        #Add a city to the table
        #hashing to the proper bucket
        res = self.hash(country_code)
        while res < self.size:
            if self.table[res] is None:
                # append a new country
                self.table[res] = city
                break
            elif self.table[res].country == country_code:
                #found an emty slot for node
                root = self.table[res]
                root = root.add_city(city, root)
                self.table[res] = root
                break
            res += 1
            if res == self.size:
                res = 0 
        if self.get_load_factor() > factor:
            self.resize()

        
    def get_node(self, lat, lon, country_code = None):
        #d keep track of the closest city found as it searches the
        #height of the tree and must complete in logarithmic time.
        #r = 6371
        min_node = []
        min_dis = []
        if country_code:
            hashed_res = self.hash(country_code)
            for i in self.table[hashed_res:]:
                if i and country_code == i.country:
                    min_node = self.find_closest_node(lat, lon, i)
                    return min_node[0] #linear probing found country_code
                hashed_res += 1
            for i in self.table[:hashed_res]:
                if i and country_code == i.country:
                    min_node = self.find_closest_node(lat, lon, i)
                    return min_node[0] #linear probing found country_code
                hashed_res += 1             
        for country in self.table:
            if country:
                node = self.find_closest_node(lat, lon, country)
                min_node.append(node[0])
                min_dis.append(node[1])
        return min_node[min_dis.index(min(min_dis))] 


    def find_closest_node(self, latitude, longitude, root):
##        min_node = []
##        min_df = []
##        axis1 = self.collect_distance(latitude, longitude, 'nw', root, [], [])
##        axis2 = self.collect_distance(latitude, longitude, 'ne', root, [], [])
##        min_node += axis1[0]
##        min_node += axis2[0]
##        min_df += axis1[1]
##        min_df += axis2[1]
        min_ = self.collect_distance(latitude, longitude, 'nw', root, [], [])
        min_df = min_[1]
        min_node = min_[0]
        loc = min_df.index(min(min_df))
        return (min_node[loc], min(min_df))


    def collect_distance(self, lat, lon, l, root, min_df = [], min_node = []):
        reverse = {'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}
        axis = {'ne': 'se', 'nw': 'sw', 'se': 'ne', 'sw': 'nw'}
        r = reverse[l]
        root_dis = abs(get_distance(root.lat, root.lon, lat, lon))
        
        min_df += [root_dis]
        min_node += [root]
        if root.children[l]:
            L = root.children[l]
            self.collect_distance(lat, lon, l, L, min_df, min_node)
        if root.children[r]:
            R = root.children[r]
            self.collect_distance(lat, lon, l, R, min_df, min_node)
        if root.children[axis[l]]:
            L = root.children[axis[l]]
            self.collect_distance(lat, lon, l, L, min_df, min_node)
        if root.children[axis[r]]:
            R = root.children[axis[r]]
            self.collect_distance(lat, lon, l, R, min_df, min_node)
        return [min_node, min_df]
    

    def hash(self, country_code):
        reduce = 55
        num = ''
        if country_code == '':
            return 0
        for s in country_code:
            num += str(ord(s) - reduce) #65-90
        return int(num) % self.size



#if __name__ == "__main__":
#    main() 
