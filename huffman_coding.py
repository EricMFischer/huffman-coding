'''
In this programming problem and the next you'll code up the greedy algorithm from the lectures on
Huffman coding.

The huffman_coding.txt file describes an instance of the problem. It has the following format:
[number_of_symbols]
[weight of symbol #1]
[weight of symbol #2]
...

For example, the third line of the file is "6852892," indicating that the weight of the second
symbol of the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A
More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set.
What is the maximum length of a codeword in the resulting Huffman code?
'''
import time


# Binary Tree class
class Binary_Tree:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
        else:
            self._insert(val, self)

    def _insert(self, val, root):
        if val < root.val:
            if root.left is None:
                root.left = Binary_Tree(val)
            else:
                self._insert(val, root.left)
        else:
            if root.right is None:
                root.right = Binary_Tree(val)
            else:
                self._insert(val, root.right)

    def contains(self, val):
        if self.val is None:
            return None
        else:
            return self._contains(val, self)

    def _contains(self, val, root):
        if val == root.val:
            return True
        elif val < root.val and root.left is not None:
            return self._contains(val, root.left)
        elif val > root.val and root.right is not None:
            return self._contains(val, root.right)
        else:
            return False

    def get_root(self):
        return self.val

    def print_tree(self, tree):
        if tree is not None:
            self.print_tree(tree.left)
            print(tree.val)
            self.print_tree(tree.right)

    def delete_tree(self):
        self.val = None
        self.left = None
        self.right = None


# input: filename
# output: array of huffman codes
def huffman_coding(filename):
    return None


def main():
    start = time.time()
    result = huffman_coding('huffman_coding.txt')

    # tree = Binary_Tree()
    # tree.insert(3)
    # tree.insert(4)
    # tree.insert(0)
    # tree.insert(8)
    # tree.insert(2)

    print('result: ', result)
    print('elapsed time: ', time.time() - start)


main()
