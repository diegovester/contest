# Question 1: Recursive — 2 points

# There is a mistake in this problem. Find out what it is and fix it.


def recursive(node):
    """
    Given a node, recursively print out the value of each node in the tree
    :param node: Node
    :return: None
    """
    if node is None:
        recursive(node.left)
        recursive(node.right)
        print(node.value)
    return 
    