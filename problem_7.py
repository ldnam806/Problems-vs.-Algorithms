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

# Test cases
# Create a new Router with a default handler for non-existent paths
router = Router(not_found_handler="not_found_handler")

# Test Case 1: General Case
router.add_handler("/home", "home_handler")
router.add_handler("/about", "about_handler")
router.add_handler("/contact", "contact_handler")

print(router.looking("/about"))  # Expected output: "about_handler"

# Test Case 2: Edge Case - Empty Path
router.add_handler("", "empty_path_handler")
print(router.looking(""))        # Expected output: "empty_path_handler"

# Test Case 3: Edge Case - Non-existent Path
router.add_handler("/products", "products_handler")
router.add_handler("/services", "services_handler")
print(router.looking("/blog"))   # Expected output: "not_found_handler"

