import torch

__all__ = ['TensorCalculator']


class TensorCalculator():

    def __init__(self):
        return None

    def tensor_ones(dim_x,
                    dim_y,
                    dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])

        return ones

    def tensor_zeros(dim_x,
                     dim_y,
                     dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])

        return zeros

    def tensor_rand(dim_x, dim_y, dim_z):
        rand = torch.rand([dim_x, dim_y, dim_z])

        return rand

    def tensor_plus(d, f):
        plus = d + f

        return plus

    def tensor_mul(d, f):
        mul = d * f

        return mul


dim_x = (4)
dim_y = (2)
dim_z = (2)

d = TensorCalculator.tensor_ones(dim_x, dim_y, dim_z)
d

e = TensorCalculator.tensor_zeros(dim_x, dim_y, dim_z)
e

f = TensorCalculator.tensor_rand(dim_x, dim_y, dim_z)
f

g = TensorCalculator.tensor_plus(d, f)
g

h = TensorCalculator.tensor_mul(f, f)
h