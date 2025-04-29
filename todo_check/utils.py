import os

def build_todo_tree(todos):
    tree = {}

    for todo in todos:
        filepath = os.path.relpath(todo['file'])  # 相对路径
        parts = filepath.split(os.sep)
        current = tree

        for part in parts[:-1]:  # 目录
            current = current.setdefault(part, {})

        current.setdefault(parts[-1], []).append(todo)

    return tree

def print_tree(tree, indent=0):
    for key, value in tree.items():
        print('    ' * indent + f"- {key}")
        if isinstance(value, dict):
            print_tree(value, indent + 1)
        else:
            for todo in value:
                print('    ' * (indent + 1) + f"[Line {todo['line']}] {todo['content']}")