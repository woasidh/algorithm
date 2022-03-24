tree = []
count = 0
while count <= 10000:
    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1

def preToPost(nums):
    if len(nums) <= 1:
        return nums;
    root = nums[0];
    left = [];
    right = [];
    for i in range(1, len(nums)):
        if nums[i] < root:
            left.append(nums[i]);
        else:
            right.append(nums[i]);

    return preToPost(left) + preToPost(right) + [root];

print(preToPost(tree));
