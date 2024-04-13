#1 Square Root of an Integer
def sqrt(number):
This line defines the beginning of the function sqrt which takes one argument, number.
    if number == 0 or number == 1:
        return number
This conditional check takes constant time O(1) because it only involves comparing number with 0 and 1.
    start = 1
    end = number
    result = 0
These three lines initialize three variables (start, end, and result) which require constant space O(1) because they are not dependent on the size of the input.
    while start <= end:
The while loop runs until the start becomes greater than end. The number of iterations depends on the size of the input number, but it's logarithmic due to the binary search. Therefore, the time complexity contribution from this line is O(log N), where N is the given number.
        mid = (start + end) // 2
Calculating the midpoint mid takes constant time O(1) because it's a simple arithmetic operation.
        if mid * mid == number:
            return mid
This conditional check also takes constant time O(1) because it only involves multiplying mid with itself and comparing with the given number.
        elif mid * mid < number:
            start = mid + 1
            result = mid
Updating start and result variables takes constant time O(1) because it involves simple arithmetic operations and variable assignments.
        else:
            end = mid - 1
Similarly, updating the end variable takes constant time O(1).
    return result
Finally, returning the result variable takes constant time O(1).

To summarize:

Time Complexity: The overall time complexity of the function is dominated by the while loop, which performs binary search and runs in O(log N) time, where N is the given number.
Space Complexity: The function only uses a fixed number of variables (start, end, result, and mid), so the space complexity is constant O(1), regardless of the size of the input.

#2 Search in a Rotated Sorted Array
`rotated_array_search`:
def rotated_array_search(input_list, number):
    left, right = 0, len(input_list) - 1
These two lines initialize two variables (left and right) which require constant space O(1) because they are not dependent on the size of the input.
    while left <= right:
The while loop runs until left becomes greater than right. The number of iterations depends on the size of the input list, but it's logarithmic due to binary search. Therefore, the time complexity contribution from this line is O(log N), where N is the number of elements in the input list.
        mid = (left + right) // 2
Calculating the midpoint mid takes constant time O(1) because it's a simple arithmetic operation.
        if input_list[mid] == number:
            return mid
This conditional check also takes constant time O(1) because it only involves comparing input_list[mid] with the given number.
        if input_list[left] <= input_list[mid]:
Another conditional check takes constant time O(1) as it involves comparing two elements of the input list.
            if input_list[left] <= number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
These lines update the left and right pointers based on whether the target number is in the sorted left half or not. Each operation here takes constant time O(1).
        else:
This else statement handles the case when the right half is sorted.
            if input_list[mid] < number <= input_list[right]:
                left = mid + 1
            else:
                right = mid - 1
Similarly, these lines update the left and right pointers based on whether the target number is in the sorted right half. Each operation here takes constant time O(1).
    return -1
Finally, returning -1 takes constant time O(1).

`linear_search`:
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
The for loop runs through each element of the input list. The number of iterations depends on the size of the input list, making the time complexity O(N), where N is the number of elements in the list.
        if element == number:
            return index
This conditional check takes constant time O(1) because it only involves comparing element with the given number.
    return -1
Finally, returning -1 takes constant time O(1).

Overall
Time Complexity:
For rotated_array_search, it's O(log N), where N is the number of elements in the input list.
For linear_search, it's O(N), where N is the number of elements in the input list.
Space Complexity: Both functions have a space complexity of O(1) since they only use a fixed amount of extra space regardless of the size of the input list.

#3 Rearrange Array Digits
`rearrange_digits_max_sum`:
def rearrange_digits_max_sum(input_list):
This line defines the beginning of the function rearrange_digits_max_sum, which takes one argument, input_list.
    if len(input_list) <= 1:
        return input_list
This conditional check takes constant time O(1) because it only involves checking the length of the input list.
    def find_max_min(arr):
        max_num, min_num = float('-inf'), float('inf')
        for num in arr:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        return max_num, min_num
The find_max_min function iterates through the input list to find the maximum and minimum elements. It iterates through each element once, resulting in linear time complexity O(N), where N is the length of the input list.
    max_num, min_num = find_max_min(input_list)
Calling the find_max_min function takes linear time O(N) because it iterates through the input list once.
    frequency = [0] * 10
    for num in input_list:
        frequency[num] += 1
These lines initialize a frequency array and iterate through the input list to count the frequency of each digit. It iterates through each element once, resulting in linear time complexity O(N), where N is the length of the input list.
    num1, num2 = 0, 0
    is_first_num = True
Initializing two variables num1 and num2 takes constant time O(1).
    for digit in range(9, -1, -1):
        while frequency[digit] > 0:
            if is_first_num:
                num1 = num1 * 10 + digit
            else:
                num2 = num2 * 10 + digit
            frequency[digit] -= 1
            is_first_num = not is_first_num
These lines construct the two numbers based on their frequencies. The outer loop runs 10 times, and the inner loop runs at most N times (the length of the input list). Therefore, the time complexity of these lines is O(N) because the dominant factor is the inner loop.
    return [num1, num2]
Finally, returning the two numbers takes constant time O(1).

Overall:
Time Complexity: The overall time complexity of the rearrange_digits_max_sum function is O(N), where N is the length of the input list.
Space Complexity: The space complexity of the function is O(1) because it only uses a fixed amount of extra space regardless of the size of the input list.

#4 Dutch National Flag Problem
`sort_array` function:
def sort_array(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1
These lines initialize three pointers low, mid, and high. Each pointer assignment operation takes constant time O(1).
    while mid <= high:
This while loop runs until the mid pointer surpasses the high pointer. The number of iterations depends on the size of the input list, but it's linear since each iteration increments at least one pointer (mid or high). Therefore, the time complexity contribution from this line is O(N), where N is the length of the input list.
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
If the element at the mid pointer is 0, it swaps the element at mid with the element at low, then increments both low and mid pointers. Each operation here takes constant time O(1).
        elif input_list[mid] == 1:
            mid += 1
If the element at the mid pointer is 1, it only increments the mid pointer. This operation also takes constant time O(1).
        else:  # input_list[mid] == 2
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
If the element at the mid pointer is 2, it swaps the element at mid with the element at high, then decrements the high pointer. Each operation here takes constant time O(1).
    return input_list
Finally, returning the sorted list takes constant time O(1).

Overall:
Time Complexity: The overall time complexity of the sort_array function is O(N), where N is the length of the input list.
Space Complexity: The space complexity of the function is O(1) because it only uses a fixed amount of extra space regardless of the size of the input list.

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

#6 Unsorted Integer Array
`get_min_max_value` function:
def get_min_max_value(ints):
    if not ints:
        return None
Time Complexity: This line contains a simple conditional check to see if the input list ints is empty. Checking the length of the list takes constant time, O(1).
Space Complexity: This line doesn't use any additional space beyond the input list itself. Therefore, it has constant space complexity, O(1).
    min_value = max_value = ints[0]
Time Complexity: This line initializes two variables min_value and max_value to the first element of the input list ints. Assigning values to variables takes constant time, O(1).
Space Complexity: This line doesn't use any additional space. It only assigns values to existing variables, so it has constant space complexity, O(1).
    for num in ints[1:]:
Time Complexity: This line starts a loop that iterates through the elements of the input list ints, starting from the second element (index 1) to the last element. The loop iterates N-1 times, where N is the length of the input list ints. Therefore, the time complexity of this line is O(N), where N is the length of the input list.
Space Complexity: The loop variable num takes constant space, and no additional space is used. Therefore, the space complexity is O(1).
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
Time Complexity: Inside the loop, there are two conditional statements that compare each element num with the current minimum and maximum values. These comparisons take constant time, O(1), for each iteration of the loop. Since the loop iterates N-1 times, the overall time complexity for these comparisons is O(N).
Space Complexity: These conditional statements don't use any additional space beyond the existing variables. Therefore, the space complexity is O(1).
    return (min_value, max_value)
Time Complexity: This line returns a tuple containing the minimum and maximum values. Creating and returning the tuple takes constant time, O(1).
Space Complexity: This line doesn't use any additional space beyond the tuple itself, so it has constant space complexity, O(1).

To summarize:
Time Complexity: The overall time complexity of the get_min_max_value function is O(N), where N is the length of the input list ints.
Space Complexity: The space complexity of the function is O(1) because it only uses a fixed amount of extra space regardless of the size of the input list.

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





