from dunamai import (
    Version,
)
import pytest
from pathlib import Path

@pytest.fixture
# Create dummy git repo with one tag
def create_git_repo_with_tag(tmp_path: Path) -> Path:
    import os
    import subprocess

    repo_dir = Path("test_repo")
    os.makedirs(repo_dir, exist_ok=True)
    os.chdir(repo_dir)
    subprocess.run(["git", "init"], check=True)
    with open("README.md", "w") as f:
        f.write("# Test Repo\n")
    subprocess.run(["git", "add", "README.md"], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    subprocess.run(["git", "tag", "v1.0.0"], check=True)
    return repo_dir

def test_from_vcs():
    # Test with a valid git repository
    version = Version.from_vcs(Vcs.Any)
    assert version == Version("1.0.0")

    os.environ["GIT_TRACE"] = "1"
    
    version = Version.from_vcs(Vcs.Any)