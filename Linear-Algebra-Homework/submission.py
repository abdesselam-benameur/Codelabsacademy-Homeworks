
import numpy as np
from numpy.linalg import norm

def transpose(m):
    return m.T

def check_diagonal(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if i != j and m[i,j] != 0:
                return False
    return True

def check_lower_triagonal(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if i < j and m[i,j] != 0:
                return False
    return True

def check_upper_triagonal(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if i > j and m[i,j] != 0:
                return False
    return True

def check_triagonal(m):
    return check_lower_triagonal(m) or check_upper_triagonal(m)

def check_identity(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if i != j and m[i,j] != 0:
                return False
            if i == j and m[i,j] != 1:
                return False
    return True

def calculate_norm1_of_column(m, col):
    return norm(m[:,col], 1)

def calculate_norm2_of_column(m, col):
    return norm(m[:,col], 2)
