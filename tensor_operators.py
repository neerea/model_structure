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

    def tensor_res(d, f):
        res = d - f

        return res

    def tensor_div(d, f):
        div = d / f

        return div
