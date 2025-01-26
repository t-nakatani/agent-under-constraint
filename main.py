from endpoints.feedback import main as feedback_main
from endpoints.submit import main as submit_main


def main(type: str, file_path: str):
    if type == "feedback":
        feedback_main(file_path)
    elif type == "submit":
        submit_main(file_path)


if __name__ == "__main__":
    import sys

    args = sys.argv
    type = args[1]
    file_path = args[2]
    main(type, file_path)
