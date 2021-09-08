from ipywidgets import interact
import numpy as np
import random

PRIZES = ['Car', 'Goat 1', 'Goat 2']

def monty_hall(example_num=0):
    '''
    Simulates one round of the Monty Hall Problem. Outputs a tuple of
    (result if stay, result if switch, result behind opened door) where
    each results is one of PRIZES.
    '''
    pick = random.choice(PRIZES)
    opened = random.choice(
        [p for p in PRIZES if p != pick and p != 'Car']
    )
    remainder = next(p for p in PRIZES if p != pick and p != opened)
    return (pick, remainder, opened)

