def solution(nodeInfo):
    answer = [[]]
    nodeInfo = [nodeInfo + [i + 1] for i, nodeInfo in enumerate(nodeInfo)];
    print(getPreOrder(nodeInfo));
    return answer


def getPreOrder(nodeInfo):
    if len(nodeInfo) == 0: return [];
    if len(nodeInfo) == 1:
        return [nodeInfo[0][2]];
    nodeInfo.sort(key=lambda x: -x[1]);
    root = nodeInfo[0];
    left = [node for node in nodeInfo if node[0] < root[0]];
    right = [node for node in nodeInfo if node[0] > root[0]];

    leftOrder = getPreOrder(left);
    rightOrder = getPreOrder(right);

    return [root[2]] + leftOrder + rightOrder;

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]);