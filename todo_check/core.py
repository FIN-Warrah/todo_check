import os
import re

def is_code_file(filename):
    extensions = ['.py', '.java', '.cpp', '.c', '.js', '.ts', '.go', '.rb']
    return any(filename.endswith(ext) for ext in extensions)

def extract_todos_from_file(filepath):
    todos = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        inside_block_comment = False

        for lineno, line in enumerate(lines, 1):
            line_strip = line.strip()

            # Python 和 C/JS/Java 单行注释标识
            comment_index_hash = line.find('#')
            comment_index_slash = line.find('//')
            comment_index_block_start = line.find('/*')
            comment_index_block_end = line.find('*/')

            if inside_block_comment:
                # 多行注释中
                comment_content = line_strip
                if re.search(r'TODO|FIXME|BUG', comment_content, re.IGNORECASE):
                    todos.append({'file': filepath, 'line': lineno, 'content': comment_content})
                if comment_index_block_end != -1:
                    inside_block_comment = False

            elif comment_index_hash != -1:
                # Python单行或Python代码后注释
                comment_content = line[comment_index_hash:]
                if re.search(r'TODO|FIXME|BUG', comment_content, re.IGNORECASE):
                    todos.append({'file': filepath, 'line': lineno, 'content': comment_content.strip()})

            elif comment_index_slash != -1:
                # C/JS/Java 单行注释或代码后注释
                comment_content = line[comment_index_slash:]
                if re.search(r'TODO|FIXME|BUG', comment_content, re.IGNORECASE):
                    todos.append({'file': filepath, 'line': lineno, 'content': comment_content.strip()})

            elif comment_index_block_start != -1:
                # 多行注释开始
                inside_block_comment = True
                comment_content = line[comment_index_block_start:]
                if re.search(r'TODO|FIXME|BUG', comment_content, re.IGNORECASE):
                    todos.append({'file': filepath, 'line': lineno, 'content': comment_content.strip()})

            # 其他正常代码，跳过

    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

    return todos

def extract_todos_from_directory(root_dir):
    all_todos = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if is_code_file(filename):
                filepath = os.path.join(dirpath, filename)
                todos = extract_todos_from_file(filepath)
                if todos:
                    all_todos.extend(todos)

    return all_todos