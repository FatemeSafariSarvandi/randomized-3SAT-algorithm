from pysat.formula import CNF
import numpy as np
import random


class CnfResolver:
    def __init__(self, path_to_file):
        self.literals_values = []
        self.cnf = CNF(from_file=path_to_file)
        self.nv = self.cnf.nv
        self.clauses_size = len(self.cnf.clauses)
        self.clauses = self.cnf.clauses
        
    
