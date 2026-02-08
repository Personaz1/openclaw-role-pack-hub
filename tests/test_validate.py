import subprocess

def test_validate_all():
    subprocess.check_call(["python3", "-m", "rolepackhub.cli", "--all"])
