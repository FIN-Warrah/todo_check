import streamlit as st
from todo_check.core import extract_todos_from_directory
import os

def main():
    st.title("📝 TODO Comment Viewer")

    # 输入路径，但**不自动触发检测**
    root_dir = st.text_input("Enter project directory path (input only, no auto scan):", "")

    # 页面一开始就显示Scan按钮
    scan_button = st.button("🔍 Scan for TODOs")

    # 只有点击按钮，才开始真正执行检测
    if scan_button:
        if root_dir and os.path.isdir(root_dir):
            todos = extract_todos_from_directory(root_dir)

            if todos:
                st.success(f"✅ Found {len(todos)} TODO/FIXME/BUG comments!")

                grouped = {}
                for todo in todos:
                    grouped.setdefault(todo['file'], []).append(todo)

                for file, file_todos in grouped.items():
                    with st.expander(f"📄 {os.path.relpath(file)}", expanded=True):
                        for todo in file_todos:
                            st.markdown(f"> **Line {todo['line']}**: {todo['content']}")
            else:
                st.info("🎉 No TODO/FIXME/BUG comments found.")
        else:
            st.warning("⚠️ Please enter a valid and existing directory path before scanning.")

if __name__ == "__main__":
    main()