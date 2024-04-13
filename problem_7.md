#7 Request Routing in a Web Server with a Trie
RouteTrie:
class RouteTrie:
    def __init__(self):
        self.children = defaultdict(RouteTrie)
        self.handler = None
Time Complexity: The initialization of a RouteTrie object involves creating a defaultdict for children and setting the handler attribute to None. Both operations take constant time, O(1).
Space Complexity: The RouteTrie object contains two attributes, children and handler, which take constant space. Therefore, the space complexity is O(1).

Route:
class Route:
    def __init__(self, root_handler=""):
        self.root = RouteTrie()
        self.root.handler = root_handler

    def update(self, path, handler):
        node = self.root
        for part in path:
            node = node.children[part]
        node.handler = handler

    def find_path(self, path):
        node = self.root
        for part in path:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler
Time Complexity:
The initialization of a Route object involves creating a RouteTrie object as its root. This operation takes constant time, O(1).
The update method iterates through each part of the path, where the number of iterations is proportional to the length of the path. Therefore, it has a time complexity of O(L), where L is the length of the path.
The find_path method also iterates through each part of the path, with a time complexity of O(L), where L is the length of the path.
Space Complexity:
The Route object contains a RouteTrie object as its root, which takes constant space. Therefore, the space complexity is O(1).

Router:
class Router:
    def __init__(self, root_handler="", not_found_handler=None):
        self.route_trie = Route(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.route_trie.update(path.strip("/").split("/"), handler)

    def looking(self, path):
        handler = self.route_trie.find_path(path.strip("/").split("/"))
        return handler if handler is not None else self.not_found_handler
Time Complexity:
The initialization of a Router object involves creating a Route object as its route_trie. This operation takes constant time, O(1).
The add_handler method and looking method both call methods of the Route object (update and find_path), which have time complexities of O(L), where L is the length of the path.
Space Complexity:
The Router object contains a Route object (route_trie) and possibly a handler (not_found_handler), both of which take constant space. Therefore, the space complexity is O(1).
To summarize:

Time Complexity: The time complexity of the methods in the provided classes is primarily determined by the length of the path involved. The methods have time complexities of O(L), where L is the length of the path.
Space Complexity: The space complexity of the provided classes is O(1) because they only contain a fixed number of attributes regardless of the input.