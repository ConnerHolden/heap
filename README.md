# Table of Contents

[*Introduction*](#introduction)  
[*What is a Min Heap?*](#what-is-a-min-heap?)  
[*Optional Dependencies*](#optional-dependencies)
[*Usage*](#usage)

## Introduction

Simple min heap project. Constructs a min heap from a random or empty array. Items can be added to and extracted from the heap.

## What is a Min Heap?

A min heap is a binary tree data structure. Its defining features are (1) that each node is greater than or equal to its parent node and (2) that the root node is the smallest. The min heap must allow items to be added and extracted. When an operation is performed on the min heap, the heap must be reconstructed to conform to the min-heap property.

## Optional Dependencies

Tree visualization: [`binarytree`](https://pypi.org/project/binarytree/)

## Usage

Output of `python min_heap.py -h` :
```
usage: python min_heap.py [-c | --custom] 
                          [-s <value> | --size <value>] [-r <value> | --range <value>]
                                           
Generates random binary tree and constructs a min heap.

    [-c]    Generates an empty array.
    [-s]    Generates random binary tree with <value> items. (Default = 20)
    [-r]    Generates random binary tree of integer values from 1 to <value>. (Default = 100)
```