from dataclasses import dataclass

from utils import IVec3d

MAX_HEIGHT = 256
MIN_HEIGHT = 0

SEGMENT_SIZE = 16


@dataclass
class Chunk:
    position: IVec3d
