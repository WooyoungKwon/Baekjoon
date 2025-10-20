import sys

class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
            if node.isEnd:
                return False

        if node.children:
            return False
            
        node.isEnd = True
        return True
        

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    phoneNumber = [input().rstrip() for _ in range(N)]
    trie = Trie()
    answer = "YES"
    for i in range(N):
        if not trie.insert(phoneNumber[i]):
            answer = "NO"
            break
    print(answer)