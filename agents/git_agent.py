import subprocess


class GitAgent:
    def run_git_command(self, git_command: str):
        if not git_command.startswith("git"):
            raise ValueError("Git command must start with 'git'")
        subprocess.run(git_command.split(" "))
