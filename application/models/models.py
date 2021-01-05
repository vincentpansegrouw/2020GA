from typing import Dict, List


class Entity:
    search_radius: int
    genes: Dict[str, List[int]]
    score: float

    def __init__(self, radius, genes, score):
        self.search_radius = radius
        self.genes = genes
        self.score = score
