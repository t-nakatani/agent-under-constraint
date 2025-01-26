import logging
from abc import ABC, abstractmethod


class IStudentAgent(ABC):
    def run(self):
        feedback = self._read_feedback(self.feedback_file_path)
        self._think(feedback)
        feedback_path = self._write_submission(feedback)
        return feedback_path

    @abstractmethod
    def _read_feedback(self, file_path: str) -> str:
        """
        read feedback from file
        file is written by supervisor agent in previous round
        """
        pass

    @abstractmethod
    def _think(self, feedback: str) -> None:
        """
        think about how to improve based on feedback
        """
        pass

    @abstractmethod
    def _write_submission(self, feedback: str) -> None:
        """
        write submission to file
        file is read by supervisor agent in next round
        """
        pass


class StudentAgent(IStudentAgent):
    def __init__(self, feedback_file_path: str):
        self.feedback_file_path = feedback_file_path
        self.logger = logging.getLogger(__name__)

    def _read_feedback(self, file_path: str):
        with open(file_path, "r") as file:
            return file.read()

    def _think(self, feedback: str):
        print(feedback)

    def _write_submission(self, feedback: str):
        with open(self.feedback_file_path, "w") as file:
            file.write(feedback)
