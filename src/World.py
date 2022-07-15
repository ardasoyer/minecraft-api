from typing import List
from enum import Enum, auto
from dataclasses import dataclass

from Chunk import Chunk


class WorldType(Enum):
    OVERWORLD = auto()
    NETHER = auto()
    END = auto()


@dataclass
class World:
    type: WorldType
    chunks: List[Chunk]
