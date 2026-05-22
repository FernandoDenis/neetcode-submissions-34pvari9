class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class TrieNode:
            def __init__(self):
                self.childs = {}
                self.isWord = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self,word):
                curr = self.root
                for letter in word:
                    if letter not in curr.childs:
                        curr.childs[letter] = TrieNode()
                    curr = curr.childs[letter]
                curr.isWord = True
                return

        ROW, COL = len(board), len(board[0])

        visited = set()
        res = set()

        def dfs(r,c,node,word):

            if r < 0 or r >= ROW or c < 0 or c >= COL or board[r][c] not in node.childs or (r,c) in visited:
                return

            visited.add((r,c))
            node = node.childs[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r, c + 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r - 1, c, node, word)

            visited.remove((r,c))


        wordsTrie = Trie()

        for word in words:
            wordsTrie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,wordsTrie.root, "")

        return list(res)

        

        
        