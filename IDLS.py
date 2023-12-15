from RMP import dict_gn

def DLS(graph, node, goal_node, depth_limit, path):
    if node == goal_node:
        path.append(node)
        return True
    
    if depth_limit == 0:
        return False
    
    for eachNeighbour in graph[node]:
        if DLS(graph, eachNeighbour, goal_node, depth_limit - 1, path):
            path.append(node)
            return True

    return False

def IDLS(graph, start_node, goal_node, max_depth):
    for i in range(max_depth + 1):
        print(str(i) + "st iteration : ")
        path = []
        if DLS(graph, start_node, goal_node, i, path):
            path.reverse()  # Reverse the path to print it in the correct order
            print(" -> ".join(path))
            print("Goal Found !")
            return
        else:
            print("Goal Not Found for depth limit", i)

IDLS(dict_gn, "Arad", "Bucharest", 9)
