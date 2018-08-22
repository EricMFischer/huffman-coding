## Synopsis
In this programming problem and the next you'll code up the greedy algorithm from the lectures on
Huffman coding. The huffman_coding.txt file describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the weight of the second
symbol of the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A
More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set.
What is the maximum length of a codeword in the resulting Huffman code?

## Motivation

This greedy algorithm shows how a simple binary tree can be used to generate the best binary prefix-free encoding for a given set of characters. The binary tree returned by the algorithm minimizes the average encoding length by giving the symbols that are more frequent, which can be represented by node weights, shorter encodings. As such, the goal is to generate variable-length encodings in which no code is a prefix of another (i.e. "prefix-free"). Huffman coding is a fundamental type of lossless compression (e.g. mp3)

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
