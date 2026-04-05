"""
LA Linear Transformations Module

A comprehensive concept-structured module on linear transformations.

Concepts:
1. What is a Linear Transformation?
2. Matrix Representation of Linear Transformations
3. Kernel and Image
4. Composition and Inverse
5. Change of Basis and Geometric Interpretation
"""

import importlib

# Dynamically import concept modules with numeric names
def load_concepts():
    concepts = {}
    for i in range(1, 6):
        module_name = f'{i:02d}_*'
        # Map numerical index to concept folders
        folder_names = {
            1: '01_what_is_linear_transformation',
            2: '02_matrix_representation',
            3: '03_kernel_and_image',
            4: '04_composition_and_inverse',
            5: '05_change_of_basis',
        }
        folder_name = folder_names[i]
        try:
            concept = importlib.import_module(f'.{folder_name}', package=__name__)
            concepts[f'concept_{i}'] = concept
        except ImportError:
            pass
    return concepts

# Load all concepts
_concepts = load_concepts()

# Make concepts available
concept_1 = _concepts.get('concept_1')
concept_2 = _concepts.get('concept_2')
concept_3 = _concepts.get('concept_3')
concept_4 = _concepts.get('concept_4')
concept_5 = _concepts.get('concept_5')

# Quiz at root level
from .quiz import QUIZ

__all__ = [
    'concept_1',
    'concept_2',
    'concept_3',
    'concept_4',
    'concept_5',
    'QUIZ',
]
