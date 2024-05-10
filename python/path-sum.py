import collections


def has_path_sum(root, target_sum: int) -> bool:
    if not root:
        return False
    queue = collections.deque([(root, root.val)])
    while queue:
        node, path = queue.popleft()
        if not node.left and not node.right and path == target_sum:
            return True
        if node.left:
            queue.append((node.left, path + node.left.val))
        if node.right:
            queue.append((node.right, path + node.right.val))
    return False


print(has_path_sum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22))
