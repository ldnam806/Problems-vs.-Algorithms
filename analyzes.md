#1 Square Root of an Integer
Initialization (Lines 2-4):
- We check if the input number is 0 or 1. If it is, we return the number itself as their square roots are the same. This initialization step takes constant time, O(1).
- We initialize two pointers, left and right, which define the search range for the square root. This step also takes constant time, O(1).
- Additionally, we initialize the result variable to store a temporary result, which also takes constant time, O(1).

Binary Search Loop (Lines 6-11):
- This loop is where the main work happens. It implements a binary search algorithm to find the square root of the input number.
- In each iteration, we calculate the midpoint (mid) of the current search range and check if mid * mid equals the input number. If it does, we return mid.
- Otherwise, based on whether mid * mid is less than or greater than the input number, we adjust the search range by updating left or right.
- Since the search space is halved in each iteration, this loop has a time complexity of O(log n), where n is the value of the input number.

Return (Line 13):
- After the loop, we return the result variable, which holds the nearest square root found. This operation takes constant time, O(1).

In summary, the time complexity of the sqrt function is dominated by the binary search loop, which has a time complexity of O(log n), where n is the value of the input number. Therefore, the overall time complexity of the function is O(log n).

#2 Search in a Rotated Sorted Array
Initialization (Lines 6-7):
- We initialize two pointers, left and right, which represent the indices of the first and last elements in the array. This step takes constant time, O(1).

Binary Search Loop (Lines 9-24):
- This loop implements the binary search algorithm to find the target number in the rotated sorted array.
- In each iteration, we calculate the middle index mid and compare the middle element with the target number.
- Depending on the comparison, we update the left or right pointer to narrow down the search range.
- Since the search space is halved in each iteration, this loop has a time complexity of O(log n), where n is the number of elements in the array.

Return (Line 26):
- After the loop, if the target number is found, we return its index. Otherwise, we return -1. This operation takes constant time, O(1).

In summary, the overall time complexity of the rotated_array_search function is dominated by the binary search loop, which has a time complexity of O(log n), where n is the number of elements in the input array.

Therefore, the time complexity of the rotated_array_search function is O(log n). This indicates that the algorithm's runtime grows logarithmically with the size of the input array, making it efficient for large datasets.

#3 Rearrange Array Digits
Find Maximum and Minimum Elements (Lines 6-14):
- We iterate through the input list once to find the maximum and minimum elements. This operation has a linear time complexity of O(n), where n is the number of elements in the input list.

Count Digit Frequencies (Lines 18-20):
- We iterate through the input list again to count the frequency of each digit. This operation also has a linear time complexity of O(n).

Construct Numbers (Lines 23-35):

We iterate through the frequency array, which has a constant size of 10 (since there are only 10 digits). This operation has a constant time complexity of O(1).
Overall, the time complexity of the rearrange_digits_max_sum function is dominated by the linear scans of the input list to find the maximum and minimum elements and count digit frequencies. Therefore, the overall time complexity is O(n), where n is the number of elements in the input list.

In summary, the function has a linear time complexity, making it efficient for large input lists while meeting the requirement of O(n log n) time complexity stated in the problem.

#4 Dutch National Flag Problem
Initialization (Line 3):
- We initialize three pointers low, mid, and high. This operation takes constant time, O(1).

Traverse the Array (Lines 5-11):
- We traverse the array once using the mid pointer until it meets the high pointer.
- Inside the loop, we perform constant-time operations such as comparisons and swapping elements.
- As the array is traversed only once, the time complexity of this operation is O(n), where n is the number of elements in the input array.

Return (Line 13):
- After the traversal, we return the sorted array. This operation takes constant time, O(1).

Overall, the time complexity of the `sort_array` function is O(n), where n is the number of elements in the input array.

The function efficiently sorts the input array consisting of only 0s, 1s, and 2s in a single traversal, meeting the requirements of the problem statement. Additionally, the provided test cases ensure the correctness of the implementation.

#5 Autocomplete with Tries
Insertion (TrieNode.insert and Trie.insert):
- Inserting a word of length m into the trie involves traversing through m levels of the trie. Each level requires a constant time operation to insert a character into a node's children dictionary. Therefore, the time complexity for insertion is O(m), where m is the length of the word being inserted.

Finding Prefix (Trie.find):
- Finding a prefix of length n also involves traversing through n levels of the trie. Each level requires a constant time operation to check if the character exists in the node's children dictionary. Therefore, the time complexity for finding a prefix is O(n), where n is the length of the prefix being searched.

Finding Suffixes (TrieNode.suffixes):
- The suffixes function is recursive and explores all paths below the current node to collect suffixes of complete words. In the worst case scenario, where there are no shared prefixes among words, each node in the trie may have k children (where k is the size of the alphabet). Therefore, the function may recursively traverse through all k children of each node until it reaches the leaf nodes, resulting in a time complexity of O(k^d), where d is the depth of the trie (the maximum length of the words) and k is the size of the alphabet.

Overall, the time complexity of trie operations depends on the length of the words being inserted or searched for, and the size of the alphabet. In practice, trie operations often have time complexity proportional to the length of the input, making them efficient for many use cases.

#6 Unsorted Integer Array

The function initializes min_val and max_val with the first element of the input array. This operation runs in constant time, O(1).

Traversal: The function iterates through the input array once, starting from the second element. This traversal has a time complexity of O(n), where n is the number of elements in the input array.

Comparison and Updates: For each element in the array (except the first one), the function performs two comparisons and, if necessary, updates both min_val and max_val. These comparisons and updates are constant time operations and occur for each element in the array, resulting in a total time complexity of O(n).

Return: After the traversal, the function returns a tuple containing the minimum and maximum values. This operation runs in constant time, O(1).

Overall, the time complexity of the `get_min_max_value` function is O(n), where n is the number of elements in the input array. This is because the function iterates through the array once and performs constant time operations for each element. Thus, the function meets the requirement of running in O(n) time.

#7 Request Routing in a Web Server with a Trie
`RouteTrie`: Represents a single node in the Trie. It contains the children nodes and the handler associated with the path represented by this node.
`Route`: Represents the Trie itself, containing the root node and methods to update paths and find handlers.
`Router`: Represents the HTTP router, which uses the RouteTrie to handle requests. It provides methods to add handlers for specific paths and to look up handlers for incoming requests.

Now let's analyze the time complexity of the methods in these classes:

RouteTrie:
- __init__: This method initializes a RouteTrie object. It uses a defaultdict to initialize the children dictionary, which has a time complexity of O(1) for each access. Thus, the overall time complexity is O(1).

Route:
- __init__: This method initializes a Route object by creating a root node. It has a time complexity of O(1).
- `update`: This method inserts a path and its corresponding handler into the Trie. It iterates over each part of the path, accessing or creating nodes in the Trie. The time complexity is O(k), where k is the length of the path.
- `find_path`: This method finds the handler associated with a given path in the Trie. It iterates over each part of the path, accessing nodes in the Trie. The time complexity is O(k), where k is the length of the path.

Router:
- __init__: This method initializes a Router object by creating a RouteTrie instance. It has a time complexity of O(1).
- `add_handler`: This method adds a handler for a specific path in the router. It calls the update method of the Route class. The time complexity is O(k), where k is the length of the path.
- `looking`: This method looks up the handler for a given path in the router. It calls the find method of the Route class. The time complexity is O(k), where k is the length of the path.
- `split_path_parts`: This method splits a path into its individual parts. It has a time complexity of O(n), where n is the length of the path.

Overall, the time complexity of inserting a path or finding a handler in the router is O(k), where k is the length of the path. The initialization of the router and Trie has a time complexity of O(1).