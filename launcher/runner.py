from behave.__main__ import main as run_test_case
from pathlib import Path

project_path = Path(__file__).parent.parent.parent

feature = f"{project_path}/_weeloDemoQA/bdd/features/CreateStudentInDemoQAPage.feature"
scenario = "Create Student in Demo_QA page"
run_test_case([feature, '-n', scenario])
