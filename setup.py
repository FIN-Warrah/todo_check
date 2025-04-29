from setuptools import setup, find_packages

setup(
    name="todo-check",
    version="0.1.0",
    description="A simple tool to extract TODO comments from project files",
    packages=find_packages(),
    install_requires=[
        "streamlit",
    ],
    entry_points={
        'console_scripts': [
            'todo-check=todo_check.main:main',
        ],
    },
    python_requires='>=3.7',
)