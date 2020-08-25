from dataclasses import dataclass
import subprocess
import sys
from subprocess import CompletedProcess
from typing import Callable, Tuple

@dataclass
class ArtifactoryAccess:
    ArtifactRegistry: str
    Username: str
    Password: str

def Process(
    func: Callable[[None], CompletedProcess]
) -> Tuple[subprocess.CompletedProcess, Exception]:
    res = None

    try:
        res = func()
        res.check_returncode()
    except subprocess.CalledProcessError as e:
        return res, e
    except subprocess.SubprocessError as e:
        return res, e

    return res, None
