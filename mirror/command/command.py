from ..process import Process, ArtifactoryAccess
import subprocess
import sys


def DockerLogin(a: ArtifactoryAccess) -> Exception:
    _, err = Process(
        lambda: subprocess.run(
            ["docker", "login", "-u", a.Username, "-p", a.Password, a.ArtifactRegistry],
            stderr=sys.stderr,
            stdout=sys.stdout,
            stdin=subprocess.DEVNULL,
        )
    )


def DockerTag(fromImage: str, toImage: str) -> Exception:
    _, err = Process(
        lambda: subprocess.run(
            ["docker", "tag", fromImage, toImage],
            stderr=sys.stderr,
            stdout=sys.stdout,
            stdin=subprocess.DEVNULL,
        )
    )

    return err


def DockerPull(image: str) -> Exception:
    _, err = Process(
        lambda: subprocess.run(
            ["docker", "pull", image],
            stderr=sys.stderr,
            stdout=sys.stdout,
            stdin=subprocess.DEVNULL,
        )
    )

    return err


def DockerPush(image: str) -> Exception:
    _, err = Process(
        lambda: subprocess.run(
            ["docker", "push", image],
            stderr=sys.stderr,
            stdout=sys.stdout,
            stdin=subprocess.DEVNULL,
        )
    )

    return err


def DockerMirror(fromImage: str, toImage: str) -> Exception:
    err = DockerPull(fromImage)
    if err != None:
        return err

    err = DockerTag(fromImage, toImage)
    if err != None:
        return err

    err = DockerPush(toImage)
    if err != None:
        return err

    return None
