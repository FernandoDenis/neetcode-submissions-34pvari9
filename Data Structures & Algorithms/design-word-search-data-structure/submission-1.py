# ..r
# a b c
# a a a
# p e a:

# {1:d,b,m,2:a,b,3:a,b,r}
class TrieNode:
    def __init__(self):
        self.childs = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter not in curr.childs:
                curr.childs[letter] = TrieNode()
            curr = curr.childs[letter]
        curr.word = True
        return

    def search(self, word: str) -> bool:
        def dfs(node,position):
            if position == len(word) - 1:
                if word[position] in node.childs:
                    return node.childs[word[position]].word
                elif word[position] == "." and node.childs:
                    for key, value in node.childs.items():
                        if value.word:
                            return True
                    return False
                return False

            if not node.childs:
                return False

            if word[position] == ".":
                for key,value in node.childs.items():
                    if dfs(value, position + 1):
                        return True
                return False
            
            if word[position] in node.childs:
                if dfs(node.childs[word[position]], position + 1):
                    return True
                return False
            else:
                return False

        return dfs(self.trie,0)


        
