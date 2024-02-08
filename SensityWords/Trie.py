from constants import *


class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.createNode()

    def createNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if character is not present
            if not node.children[index]:
                node.children[index] = self.createNode()
            node = node.children[index]
        # mark last node as leaf
        node.isEndOfWord = True

    def search(self, searchStr):
        # Search key in the trie
        node = self.root
        length = len(searchStr)
        for level in range(length):
            indexSearchStr = self._charToIndex(searchStr[level])
            if not node.children[indexSearchStr]:
                return False
            node = node.children[indexSearchStr]

        return node.isEndOfWord

    def _charToIndex(self, char):
        # private function
        # Converts current character into index
        # use only 'a' through 'z' and lower case
        # 97 = a, 98 = b, 99 c
        return ord(char) - ord("a")


# Init object
tree = Trie()

# Construct trie
for word in bannedWords:
    tree.insert(word)

result = tree.search("haha")
print('result: ', result)
