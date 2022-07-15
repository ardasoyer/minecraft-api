from dataclasses import dataclass


@dataclass
class IVec3d:
    x: int
    y: int
    z: int

    def dot(self, other):  # Dot product
        return self.x * other.x + self.y * other.y + self.z * other.z
