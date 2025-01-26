from agents.supervisor_agent import SupervisorAgent


def main(submission_file_path: str) -> str:
    supervisor_agent = SupervisorAgent(submission_file_path)
    feedback_path = supervisor_agent.run()
    return feedback_path


if __name__ == "__main__":
    import sys

    args = sys.argv
    submission_file_path = args[1]
    main(submission_file_path)
