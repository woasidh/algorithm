import sys

n = int(sys.stdin.readline());

inOrder = list(map(int, sys.stdin.readline().split()));
postOrder = list(map(int, sys.stdin.readline().split()));

indexArr = [-1 for _ in range(n + 1)];
for i in range(n):
    indexArr[inOrder[i]] = i;

# 왼 중 오
# 왼 오 중
# 중 왼 오

def printRoot(in_start, in_end, post_start, post_end):
    global inOrder, postOrder;
    root = postOrder[post_end];
    rootIdx = indexArr[root];
    leftLen = rootIdx;
    rightLen = in_end - rootIdx;
    print(root, end = ' ');
    if leftLen > 0: printRoot(in_start, rootIdx - 1, post_start, post_start + rootIdx - 1);
    if rightLen > 0: printRoot(rootIdx + 1, in_end, post_start + rootIdx + 1, post_end - 1);

printRoot(0, n - 1, 0, n - 1);