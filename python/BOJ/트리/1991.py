import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data;
        self.left = left;
        self.right = right;


n = int(sys.stdin.readline());
nodeMap = {};
for _ in range(n):
    parent, left, right = sys.stdin.readline().split();
    node = Node(parent, left, right);
    nodeMap[parent] = node;

for nodeData in nodeMap:
    node = nodeMap[nodeData];
    leftData = node.left if node.left != '.' else None;
    rightData = node.right if node.right != '.' else None;
    if leftData: node.left = nodeMap[leftData];
    else: node.left = None;
    if rightData: node.right = nodeMap[rightData];
    else: node.right = None;

def preOrder(root):
    if not root: return;

    print(root.data, end = '');
    preOrder(root.left);
    preOrder(root.right);

def inOrder(root):
    if not root: return;

    inOrder(root.left);
    print(root.data, end='');
    inOrder(root.right);

def postOrder(root):
    if not root: return;

    postOrder(root.left);
    postOrder(root.right);
    print(root.data, end='');

preOrder(nodeMap['A']);
print();
inOrder(nodeMap['A']);
print();
postOrder(nodeMap['A']);