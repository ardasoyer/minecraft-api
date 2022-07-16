import random
from dataclasses import dataclass


@dataclass
class IVec2d:
    x: int = 0
    y: int = 0

    def dot(self, other) -> int:  # Dot product
        return self.x * other.x + self.y * other.y

    # Reference: http://mathworld.wolfram.com/SpherePointPicking.html
    @staticmethod
    def pseudorandom():  # x^2 + y^2 = 1.0
        random_point = [random.gauss(0, 1) for _ in range(2)]
        scale = sum(n * n for n in random_point) ** -0.5
        return IVec2d(*tuple(coord * scale for coord in random_point))


@dataclass
class IVec3d:
    x: int = 0
    y: int = 0
    z: int = 0

    def dot(self, other):  # Dot product
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Reference: http://mathworld.wolfram.com/SpherePointPicking.html
    @staticmethod
    def pseudorandom():  # x^2 + y^2 = 1.0
        random_point = [random.gauss(0, 1) for _ in range(3)]
        scale = sum(n * n for n in random_point) ** -0.5
        return IVec2d(*tuple(coord * scale for coord in random_point))


if __name__ == "__main__":
    a = IVec2d.pseudorandom()
    print(a)
