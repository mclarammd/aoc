class Node:
    def __init__(self, name, val, parent, children):
        self.name = name
        self.parent = parent
        self.val = val
        self.children = children

root = Node("/", 0, None, {})
curr_node = root
i = 0
while True:
    try:
        line = input().split()
        if i == 0:
            i += 1
            continue

        if line[0] == "dir":
            curr_node.children[line[1]] = Node(line[1], 0, curr_node, {})

        elif line[0] == "$":
            if line[1] == "ls":
                continue

            else:
                if line[2] == "..":
                    curr_node = curr_node.parent

                else:
                    curr_node = curr_node.children[line[2]]

        else:
            curr_node.val += int(line[0])

    except:
        break

# print(root.children["gnpd"].children, root.val)
visited = set()
# total = 0
curr_min = float("inf")
def dfs(node):
    visited.add(node)
    for child_k in node.children:
        child = node.children[child_k]
        if child not in visited:
            node.val += dfs(child)

    # if node.val <= 100000:
    #     global total
    #     total += node.val
    if node.val >= 8381165:
        global curr_min
        curr_min = min(curr_min, node.val)

    return node.val

dfs(root)
print(curr_min)
