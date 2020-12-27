from typing import Tuple, Iterable, List
import numpy as np

from models.entity import Entity


def mate(one: Entity, two: Entity) -> Tuple[Entity, Entity]:
    new_one = breed(one, two)
    new_two = breed(two, one)
    return new_one, new_two


def breed(one: Entity, two: Entity) -> Entity:
    output_genes = {}
    for key, _ in one.genes.items():
        output_genes = {**output_genes, key: splice(one.genes[key], two.genes[key])}
    return Entity(one.search_radius, output_genes, 0)


def splice(one: List[int], two: List[int]) -> List[int]:
    splice_point = np.random.randint(0, len(one))
    spliced_gene = one[0:splice_point]
    spliced_gene += two[splice_point:]
    return spliced_gene


def cull(population: List[Entity], proportion: float):
    pass
# todo
