info = dict()
def search(startNode):
    if len(info[startNode]) == 0:
        return 2
    currNode = startNode
    while True:
        if len(info[currNode]) == 0:
            return 2
        elif len(info[currNode]) >= 2:
            return 3
        elif info[currNode][0] == startNode:
            return 1
        currNode = info[currNode][0]
        
def solution(edges):
    global info
    answer = [0, 0, 0, 0]
    keys = set()
    for u, v in edges:
        keys.add(u)
        keys.add(v)
    N = len(keys)
    info = {key: [] for key in keys}
    inputEdge = {key: 0 for key in keys}
    
    for edge in edges:
        info[edge[0]].append(edge[1])
        inputEdge[edge[1]] += 1

    centerNode = 0
    for i in info.keys():
        if inputEdge[i] == 0 and len(info[i]) >= 2:
            centerNode = i
            break
            
    for i in info[centerNode]:
        answer[search(i)] += 1
    answer[0] = centerNode
    return answer