# dog
""" {
    d:{
        o:{
            gW: {

            }
        }
    }
}
"""
# ^
class TrieNode:
    def __init__(self, value = None):
        self.childs = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.childs:
                curr.childs[letter] = TrieNode()
            curr = curr.childs[letter]
        curr.word = True
        return

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.childs:
                return False
            curr = curr.childs[letter]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.childs:
                return False
            curr = curr.childs[letter]
        return True
        
        