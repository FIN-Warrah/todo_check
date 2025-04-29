import argparse
from todo_check.core import extract_todos_from_directory
from todo_check.utils import build_todo_tree, print_tree

def main():
    parser = argparse.ArgumentParser(description="TODO Comment Checker")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Project directory to scan')

    args = parser.parse_args()

    todos = extract_todos_from_directory(args.directory)

    if todos:
        todo_tree = build_todo_tree(todos)
        print_tree(todo_tree)
    else:
        print("🎉 No TODO/FIXME/BUG comments found.")

if __name__ == "__main__":
    main()