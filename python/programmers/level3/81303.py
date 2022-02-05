# 다시 풀기 linked list로
# class 알기
# linkedlist 문제 풀어보기

def solution(n, k, cmds):
    table = LinkedList();
    startNode = None;
    for i in range(n):
        node = Node(i);
        table.append(node);
        if i == k: startNode = node;

    table.current = startNode;
    for cmd in cmds:
        cmdArr = cmd.split();
        if cmdArr[0] == 'D':
            table.down(int(cmdArr[1]));
        elif cmdArr[0] == 'U':
            table.up(int(cmdArr[1]));
        elif cmdArr[0] == 'C':
            table.deleteCurrent();
        else:
            table.undo();
    result = ['X' for i in range(n)];
    node = table.root;
    while node:
        result[node.num] = 'O';
        node = node.next;

    return ''.join(result);


class Node:
    def __init__(self, num):
        self.prev = None;
        self.next = None;
        self.num = num;


class LinkedList:
    def __init__(self):
        self.current = None;
        self.root = None;
        self.stack = [];

    def append(self, node):
        if not self.root:
            self.root = node;
            self.current = node;
        else:
            self.current.next = node;
            node.prev = self.current;
            self.current = node;

    def down(self, n):
        for i in range(n):
            self.current = self.current.next;

    def up(self, n):
        for i in range(n):
            self.current = self.current.prev;

    def deleteCurrent(self):
        deleteNode = self.current;
        if deleteNode == self.root:
            self.root = deleteNode.next;
            self.root.prev = None;
            self.current = self.root;
        elif not deleteNode.next:
            deleteNode.prev.next = None;
            self.current = deleteNode.prev;
        else:
            deleteNode.prev.next = deleteNode.next;
            deleteNode.next.prev = deleteNode.prev;
            self.current = deleteNode.next;
        self.stack.append(deleteNode);

    def undo(self):
        recoverNode = self.stack.pop();
        if not recoverNode.prev:
            recoverNode.next.prev = recoverNode;
            self.root = recoverNode;
        elif not recoverNode.next:
            recoverNode.prev.next = recoverNode;
        else:
            recoverNode.prev.next = recoverNode;
            recoverNode.next.prev = recoverNode;