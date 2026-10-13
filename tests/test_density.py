import numpy as np
from src.density_map import DensityMap

def test_density_empty():
    dm = DensityMap()
    d = dm.compute([], (480, 640, 3))
    assert d.sum() == 0

def test_density_one():
    dm = DensityMap((4, 4))
    d = dm.compute([{"center": [320, 240]}], (480, 640, 3))
    assert d.sum() == 1
