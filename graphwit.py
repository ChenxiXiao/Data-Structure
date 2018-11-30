# Name:       Chenxi Xiao
# Course:     CPE 202
# Instructor: Daniel Kauffman
# Assignment: graphwit
# Term:       Summer 2018

import re


def get_patterns():
    regexp = [(re.compile(r'[\{\[\(].*?[\)\]\}]'), 'remove'), 
             (re.compile(r'(?:\-){3,}|(?:\=){3,}'), 'remove'),
             (re.compile(r'[^-=\<\>A-Z\d]'), 'remove'),
             (re.compile(r'(?P<weight1>\d?)(?P<direction>(<(?:-+|=+)>)|(<(?:=+|-+))|((?:=+|-+)>))(?P<weight2>\d?)'), 'search'),
             (re.compile(r'(?P<vertex>[A-Z]{1}).*(?P<neighbor>[A-Z]{1})'), 'search')]
  
    return regexp


def parse_edges(pattern, strings):
    graph_dict = {}
    for string in strings:
        res = pattern[0][0].sub('', string)
        res = pattern[2][0].sub('', res)
        res = pattern[1][0].sub('', res)
        data = get_data(pattern, res)
        if data:
 #           vertex = data[1]  neighbor = data[2]
            if '<' in data[0]:  #direction
                weight = int(data[1 + 2])
                if graph_dict.get(data[2]):
                    graph_dict[data[2]].append((data[1], weight)) #weight <
                else:
                    graph_dict[data[2]] = [(data[1], weight)]
            if '>' in data[0]:
                weight = int(data[2 + 2])
                if graph_dict.get(data[1]):
                    graph_dict[data[1]].append((data[2], weight)) #weight > 
                else:
                    graph_dict[data[1]] = [(data[2], weight)]
    return graph_dict

        # match?? then sub//search??
   


def get_data(pattern, res): # res - last result from removal
    alphab = 4
    vertexes = pattern[alphab][0].search(res)
    if not vertexes or not vertexes.group('vertex') or not vertexes.group('neighbor'):
        return None
    vertex = vertexes.group('vertex') 
    neighbor = vertexes.group('neighbor')
    res = pattern[alphab - 1][0].search(res)
    if not res:
        direction = '<->'  # not matching the format
    else:
        direction = res.group('direction')
        weight1 = res.group('weight1')
        weight2 = res.group('weight2')
   #     direction = res['direction']
   #     weight1 = res['weight1']
   #     weight2 = res['weight2']
    if not res or not weight1:
        weight1 = '1'
    if not res or not weight2:
        weight2 = '1'
    return (direction, vertex, neighbor, weight1, weight2)
 

def order_bfs(adj_list, start_vertex):
    visited = []
    visited.append(start_vertex)
    path = []
    if adj_list == [] or start_vertex not in adj_list.keys():
        return []
    for adj in adj_list[start_vertex]:
        path.append(adj[0])
    while path:
        second_path = []
        for i in path:
            if i in adj_list.keys(): 
                for adj in adj_list[i]:
                    vertex = adj[0]
                    if vertex not in visited:
                        second_path.append(vertex)
            if i not in visited: # two vertex direct to one vertex                                 
                visited.append(i)
        path = second_path
    return visited       


def order_dfs(adj_list, start_vertex):
    visiting = [start_vertex]
    visited = []
    if adj_list == [] or start_vertex not in adj_list.keys():
        return []
    while visiting:
        vertex = visiting.pop()
        if vertex not in visited: 
            visited.append(vertex) # end 
         #keep searching
        if vertex in adj_list.keys():
            for adj in adj_list[vertex][::-1]:
                if adj[0] not in visited:
                    visiting.append(adj[0])
    return visited

