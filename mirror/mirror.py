from dataclasses import dataclass
from typing import List, Tuple
import fire
import pathlib
import json
import io
from .command import *
import logging

# setup logger
logging.basicConfig(level=logging.DEBUG)

@dataclass
class MirrorUnit:
    FromImage: str
    ToImage: str

def MirrorTargetCollector(path: str) -> Tuple[List[MirrorUnit], Exception]:
    mirrorInfo = None

    with io.open(path) as f:
        mirrorInfo = json.load(f)
    
    mirrorList = mirrorInfo.get("mirror", [])

    rst = []

    for m in mirrorList:
        rst.append(MirrorUnit(m["from"], m["to"]))
    
    return rst, None

def Mirror(path: str) -> None:
    mirrorList, err = MirrorTargetCollector(path)
    if err != None:
        logging.error(err)
        return

    for m in mirrorList:
        err = DockerMirror(m.FromImage, m.ToImage)    
        if err != None:
            logging.error(err)
            return
    return

def main():
    fire.Fire(Mirror)

if __name__ == "__main__":
    main()