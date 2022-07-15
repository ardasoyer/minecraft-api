from enum import Enum, auto
from dataclasses import dataclass

from utils import IVec3d


class BlockType(Enum):
    AIR = auto()


@dataclass
class Block:
    type: BlockType
    pos: IVec3d
