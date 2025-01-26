from agents.student_agent import StudentAgent
from agents.supervisor_agent import SupervisorAgent


def submission(submission_file_path: str) -> str:
    student_agent = StudentAgent(submission_file_path)
    submission_path = student_agent.submit_output_to_supervisor()
    return submission_path


def feedback(submission_file_path: str) -> str:
    supervisor_agent = SupervisorAgent(submission_file_path)
    feedback_path = supervisor_agent.feedback_to_student()
    return feedback_path
