import numpy as np
import cv2

class DensityMap:
    def __init__(self, grid=(16, 16)):
        self.grid = grid

    def compute(self, people, frame_shape):
        h, w = frame_shape[:2]
        gh, gw = self.grid
        density = np.zeros(self.grid)
        for p in people:
            cx, cy = p["center"]
            gi = min(int(cy / h * gh), gh - 1)
            gj = min(int(cx / w * gw), gw - 1)
            density[gi, gj] += 1
        return density

    def to_heatmap(self, density, size):
        norm = density / (density.max() + 1e-6)
        heat = cv2.resize(norm.astype(np.float32), size)
        heat = (heat * 255).astype(np.uint8)
        return cv2.applyColorMap(heat, cv2.COLORMAP_JET)
