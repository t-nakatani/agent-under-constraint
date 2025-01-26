from agents.student_agent import StudentAgent


def main(feedback_file_path: str) -> str:
    student_agent = StudentAgent(feedback_file_path)
    submission_path = student_agent.run()
    return submission_path


if __name__ == "__main__":
    import sys

    args = sys.argv
    feedback_file_path = args[1]
    main(feedback_file_path)
