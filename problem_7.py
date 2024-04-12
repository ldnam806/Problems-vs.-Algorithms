from collections import defaultdict

class RouteTrie:
    def __init__(self):
        self.children = defaultdict(RouteTrie)
        self.handler = None

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

class Router:
    def __init__(self, root_handler="", not_found_handler=None):
        self.route_trie = Route(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.route_trie.update(path.strip("/").split("/"), handler)

    def looking(self, path):
        handler = self.route_trie.find_path(path.strip("/").split("/"))
        return handler if handler is not None else self.not_found_handler

# Testing the code
router = Router("root handler", "not found handler")
router.add_handler("/blog", "blog handler")
router.add_handler("/blog/python", "python blog handler")
router.add_handler("/blog/java", "java blog handler")
router.add_handler("/about", "about handler")

print(router.looking("/"))  # Output: 'root handler'
print(router.looking("/blog"))  # Output: 'blog handler'
print(router.looking("/blog/python"))  # Output: 'python blog handler'
print(router.looking("/blog/java"))  # Output: 'java blog handler'
print(router.looking("/about"))  # Output: 'about handler'
print(router.looking("/home"))  # Output: 'not found handler'
print(router.looking("/blog/java/spring"))  # Output: 'not found handler'
