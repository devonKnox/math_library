'''
This is a library for performing basic linear algebra operations, including both
matrix and vector operations.

Created by: Devon Knox
'''

import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, scalar):
        return Vector(*[a * scalar for a in self.components])
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
    
    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def cross(self, other):
        if len(self.components) == 2 and len(other.components) == 2:
            a1, a2 = self.components
            b1, b2 = other.components
            return a1 * b2 - a2 * b1
        elif len(self.components) == 3 and len(other.components) == 3:
            a1, a2, a3 = self.components
            b1, b2, b3 = other.components
            return Vector(a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
        else:
            raise ValueError("Cross product is only defined for 2D or 3D vectors")
    
    def __str__(self):
        return f"({', '.join(map(str, self.components))})"

    def __repr__(self):
        return self.__str__()

class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
    
    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[self.rows[i][j] + other.rows[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)]
        return Matrix(result)
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            # Matrix multiplication
            if self.num_cols != other.num_rows:
                raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix")
            result = [[sum(self.rows[i][k] * other.rows[k][j] for k in range(self.num_cols)) for j in range(other.num_cols)] for i in range(self.num_rows)]
            return Matrix(result)
        elif isinstance(other, Vector):
            # Matrix-vector multiplication
            if self.num_cols != len(other.components):
                raise ValueError("Matrix columns must equal vector size for multiplication")
            result = [sum(self.rows[i][j] * other.components[j] for j in range(self.num_cols)) for i in range(self.num_rows)]
            return Vector(*result)
        else:
            raise ValueError("Unsupported operand type(s) for *: 'Matrix' and '{}'".format(type(other).__name__))
    
    def __str__(self):
        return '\n'.join(['[' + ', '.join(map(str, row)) + ']' for row in self.rows])
    
    def __repr__(self):
        return self.__str__()
