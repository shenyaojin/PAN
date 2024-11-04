import numpy as np

# PDE base object

class PDEBase():


    def __init__(self):
        self.grid = None
        self.solver = None
        self.bcs = None