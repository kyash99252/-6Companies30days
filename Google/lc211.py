class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
    
    def containsKey(self, key: str) -> bool:
        return self.links[ord(key) - ord('a')] is not None
    
    def put(self, key: str, node) -> None:
        self.links[ord(key) - ord('a')] = node
    
    def get(self, key: str):
        return self.links[ord(key) - ord('a')]
    
    def setFlag(self) -> None:
        self.flag = True
    
    def getFlag(self) -> bool:
        return self.flag

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        n = len(word)
        node = self.root
        for i in range(n):
            if not node.containsKey(word[i]):
                node.put(word[i], Node())
            node = node.get(word[i])
        node.setFlag()

    def search(self, word: str) -> bool:
        return self._searchRecursion(word, self.root)
    
    def _searchRecursion(self, word: str, node: Node) -> bool:
        n = len(word)
        for i in range(n):
            if word[i] == '.':
                for ch in range(26):
                    if node.containsKey(chr(ch + ord('a'))):
                        next_node = node.get(chr(ch + ord('a')))
                        if self._searchRecursion(word[i+1:], next_node):
                            return True
                return False
            else:
                if not node.containsKey(word[i]):
                    return False
                else:
                    node = node.get(word[i])
        return node.getFlag()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)