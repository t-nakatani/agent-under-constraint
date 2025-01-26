from abc import ABC, abstractmethod

# from enum import Enum
# class CommandType(Enum):


class ISupervisorAgent(ABC):
    def feedback_to_student(self):
        submission = self._read_submission(self.submission_file_path)
        self._think(submission)
        submission_path = self._write_feedback(submission)
        return submission_path

    @abstractmethod
    def _read_submission(self, file_path: str):
        """
        read agent submission from file
        file is written by student agent in previous round
        """
        pass

    @abstractmethod
    def _think(self, submission: str):
        """
        think about how to improve submission
        """
        pass

    @abstractmethod
    def _write_feedback(self, submission: str):
        """
        write feedback to file
        file is read by student agent in next round
        """
        pass


class SupervisorAgent(ISupervisorAgent):
    def __init__(self, submission_file_path: str):
        self.submission_file_path = submission_file_path

    def _read_submission(self, file_path: str):
        with open(file_path, "r") as file:
            return file.read()

    def _think(self, submission: str):
        print(submission)

    def _write_feedback(self, submission: str):
        with open(self.submission_file_path, "w") as file:
            file.write(submission)
