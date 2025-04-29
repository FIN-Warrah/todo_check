import sys
import subprocess
import os

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        web_app_path = os.path.join(os.path.dirname(__file__), "web.py")
        subprocess.run(["streamlit", "run", web_app_path, "--"] + sys.argv[2:])
    else:
        from todo_check.cli import main as cli_main
        cli_main()

if __name__ == "__main__":
    main()