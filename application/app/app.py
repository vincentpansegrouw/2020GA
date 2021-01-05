import math
from typing import List

import numpy as np

from application.models.models import Entity


def mate(one: Entity, two: Entity) -> List[Entity]:
    new_one = breed(one, two)
    new_two = breed(two, one)
    return [new_one, new_two]


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


def return_sorted_culled_population(population: List[Entity], proportion: float) -> List[Entity]:
    sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
    total_length = len(population)
    members_to_keep = math.floor(total_length * (1 - proportion))
    return sorted_population[:members_to_keep]


def return_population_with_normalised_scores(population: List[Entity]) -> List[Entity]:
    total_score = 0
    normalised_population = []
    for member in population:
        total_score += member.score
    for member in population:
        normalised_score = member.score / total_score
        new_member = Entity(member.search_radius, member.genes, normalised_score)
        normalised_population.append(new_member)
    return normalised_population


def return_filled_generation(population: List[Entity], population_size: int) -> List[Entity]:
    random_float_1 = np.random.random_sample()
    random_float_2 = np.random.random_sample()
    new_population = population
    parent_1 = None
    parent_2 = None
    while len(new_population) < population_size:
        current_range_1 = 0
        current_range_2 = 0
        for member in population:
            current_range_1 += member.score
            current_range_2 += member.score
            if current_range_1 > random_float_1 and not parent_1:
                parent_1 = member
            if current_range_2 > random_float_2 and not parent_2 and parent_1 is not member:
                parent_2 = member
            if parent_1 and parent_2:
                break
        new_members = mate(parent_1, parent_2)
        new_population += new_members
    return new_population


def new_mutation(entity: Entity, mutation_constant: float) -> Entity:
    new_genes = {}
    genes = entity.genes
    for k, v in genes.items():
        new_gene = []
        for item in v:
            if np.random.random_sample() < mutation_constant:
                new_gene.append(np.random.randint(0, 9))
            else:
                new_gene.append(item)
        new_genes += {k, new_gene}
    return Entity(entity.search_radius, new_genes, 0)


def compute_generation(population: List[Entity], mutation_constant: float) -> List[Entity]:
    pass
