import random
from dataclasses import dataclass


@dataclass
class IVec2d:
    x: int
    y: int

    def dot(self, other) -> int:  # Dot product
        return self.x * other.x + self.y * other.y

    @staticmethod
    def pseudorandom():
        return IVec2d(random.randint(-1, 1), random.randint(-1, 1))
