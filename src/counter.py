class LineCounter:
    def __init__(self, line_y):
        self.line_y = line_y
        self.tracks = {}
        self.count_in = 0
        self.count_out = 0

    def update(self, tracks):
        for t in tracks:
            tid = t["id"]
            cy = (t["bbox"][1] + t["bbox"][3]) / 2
            prev = self.tracks.get(tid)
            if prev is not None:
                if prev < self.line_y <= cy:
                    self.count_in += 1
                elif prev > self.line_y >= cy:
                    self.count_out += 1
            self.tracks[tid] = cy
        return {"in": self.count_in, "out": self.count_out}
