import sys

# abcd
# abcd

string = sys.stdin.readline().strip();
n = int(sys.stdin.readline());
focus = len(string) - 1;

class LinkedList:
    def __init__(self):
        self.head = Node(-1);
        self.current = self.head;

    def add(self, node):
        self.current.next = node;
        node.prev = self.current;
        self.current = node;
        if not self.head.next:
            self.head.next = node;

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;

lList = LinkedList();
for char in string:
    lList.add(Node(char));

# abcd
# abczd

for i in range(n):
    command = sys.stdin.readline().split();
    if len(command) == 1:
        if command[0] == 'L':
            if lList.current.data != -1:
                lList.current = lList.current.prev;
        elif command[0] == 'D':
            if lList.current.next:
                lList.current = lList.current.next;
        else:
            if lList.current.data != -1:
                if not lList.current.next:
                    lList.current.prev.next = None;
                    lList.current = lList.current.prev;
                else:
                    lList.current.prev.next = lList.current.next;
                    lList.current.next.prev = lList.current.prev;
                    lList.current = lList.current.prev;
    else:
        char = command[1];
        node = Node(char);
        if not lList.current.next:
            lList.add(node);
        else:
            node.prev = lList.current;
            node.next = lList.current.next;
            lList.current.next.prev = node;
            lList.current.next = node;
            lList.current = node;

cur = lList.head.next;

while cur:
    print(cur.data, end = '');
    cur = cur.next;



