#5 Autocomplete with Tries
TrieNode:
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
Time Complexity: The initialization of TrieNode creates a dictionary for children and sets a boolean flag. Both operations take constant time, O(1).
Space Complexity: The space complexity of a TrieNode object is O(1) because it only contains a fixed number of attributes.
    def insert(self, char):
        return self.children[char]
Time Complexity: The insert method of TrieNode accesses or creates a child node in the children dictionary. This operation takes constant time, O(1).
Space Complexity: The space complexity remains O(1) because it doesn't use any additional memory beyond creating a new TrieNode if needed.
    def suffixes(self, suffix=''):
        suffixes_set = set()

        if self.is_word and suffix != '':
            suffixes_set.add(suffix)

        for char, node in self.children.items():
            suffixes_set.update(node.suffixes(suffix + char))
        
        return suffixes_set
Time Complexity: The suffixes method performs a depth-first search (DFS) traversal of the trie, visiting each node exactly once. In the worst case, it traverses through all nodes in the trie, resulting in a time complexity of O(N), where N is the total number of nodes in the trie.
Space Complexity: The space complexity depends on the size of the output set containing all suffixes. In the worst case, if all words in the trie have distinct suffixes, the space complexity would be O(M), where M is the total number of characters in all suffixes.

Trie:
class Trie:
    def __init__(self):
        self.root = TrieNode()
Time Complexity: The initialization of Trie object creates a single root node. This operation takes constant time, O(1).
Space Complexity: The space complexity of a Trie object is O(1) because it only contains a fixed number of attributes.
    def insert(self, word):
        current_node = self.root
        for char in word:
            current_node = current_node.insert(char)
        current_node.is_word = True
Time Complexity: The insert method of Trie performs a sequence of constant-time operations for each character in the word being inserted. In the worst case, where the word is new and none of its characters are shared with existing words in the trie, the time complexity is O(L), where L is the length of the word.
Space Complexity: The space complexity depends on the size of the trie, which grows with the number of distinct words inserted. In the worst case, if each word is distinct and has no shared prefixes, the space complexity would be O(N), where N is the total number of nodes in the trie.
    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

Time Complexity: The find method of Trie performs a sequence of constant-time operations for each character in the prefix being searched. In the worst case, where the prefix is not present in the trie, or it's a prefix of multiple words, the time complexity is O(L), where L is the length of the prefix.
Space Complexity: The space complexity is O(1) because it only uses a fixed amount of extra space regardless of the size of the trie.