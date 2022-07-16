from enum import Enum, auto
from dataclasses import dataclass

from utils import IVec3d


class BlockType(Enum):
    BEDROCK = auto()
    AIR = auto()
    DIRT = auto()
    GRASS = auto()
    STONE = auto()
    COAL_ORE = auto()
    IRON_ORE = auto()
    GOLD_ORE = auto()
    DIAMOND_ORE = auto()


@dataclass
class Block:
    type: BlockType
    position: IVec3d
