from enum import Enum

from routes.endpoints import feedback, submission


class CommandType(Enum):
    FEEDBACK = "feedback"
    SUBMIT = "submit"


def dispatch(command_type: CommandType, file_path: str):
    if command_type == CommandType.FEEDBACK:
        feedback(file_path)
    elif command_type == CommandType.SUBMIT:
        submission(file_path)


if __name__ == "__main__":
    import sys

    args = sys.argv
    command_type = CommandType(args[1])
    file_path = args[2]
    dispatch(command_type, file_path)
