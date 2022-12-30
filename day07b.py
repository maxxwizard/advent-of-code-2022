# build an in-memory tree representation
# each node can have files and directories
from abc import ABC
import sys
from typing import Optional

class Node(ABC):
    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        if parent == None or parent.path == "":
            self.path = name
        else:
            if parent.path == "/":
                self.path = "/" + name
            else:
                self.path = parent.path + "/" + name

class Directory(Node):
    def __init__(self, parent: Optional[Node], name: str) -> None:
        super().__init__(parent, name)
        self.children: set[Node] = set()

class File(Node):
    def __init__(self, parent: Node, name: str, filesize: int) -> None:
        super().__init__(parent, name)
        self.filesize = filesize

# adds a node to the hierarchy
def parse_ls_line(line: str):
    tokens = line.split(' ')
    name = tokens[1]
    if tokens[0] == "dir":
        ptr.children.add(Directory(ptr, name))
    else:
        filesize = int(tokens[0])
        ptr.children.add(File(ptr, name, filesize))

root = Directory(parent = None, name = "")
ptr = root # our current dir as we traverse the hierarchy

with open('input.txt') as reader:
    lines = reader.readlines()

lines = list(map(lambda l: l.strip(), lines))

# line starts with $ = command
# line starts with number = file
# line starts with dir = directory
i = 0
while i < len(lines):
    line = lines[i]
    print(line)
    print("ptr =", ptr.path)
    tokens = line.split(' ')
    assert tokens[0] == "$"
    cmd = tokens[1]
    match cmd:
        case "ls":
            i += 1
            while i < len(lines):
                print("ls_process:", lines[i])
                if lines[i].startswith("$"):
                    i -= 1
                    break
                parse_ls_line(lines[i])
                i += 1
        case "cd":
            param = tokens[2]
            if param == "..":
                ptr = ptr.parent
            else:
                subdir = Directory(ptr, param)
                # if subdir does not exist, create it
                if subdir not in ptr.children:
                    print("creating subdir", subdir.path)
                    ptr.children.add(subdir)
                # move to subdir
                ptr = subdir
        case _:
            raise Exception()
    i += 1
     

# DFS the tree
global_max = 0

def dfs(root, min_sum = sys.maxsize) -> int:
    global global_max, global_min, dir_to_delete
    if root == None:
        return 0

    if isinstance(root, File):
        return root.filesize

    sum = 0
    for d in root.children:
        sum += dfs(d, min_sum)

    global_max = max(sum, global_max)

    if sum >= min_sum and sum < global_min:
        global_min = sum
        dir_to_delete = root.path
    
    #print("dfs", root.path, "{:,}".format(sum))
    return sum

dfs(root)
total_size = 70000000
unused_space = total_size - global_max
space_required = 30000000 - unused_space

global_min = sys.maxsize
dir_to_delete = ""
dfs(root, space_required)

print("total size", total_size)
print("used space", global_max)
print("unused space", unused_space)
print("space_required", space_required)
print("dir_to_delete", dir_to_delete, "size", global_min)