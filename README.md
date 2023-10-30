# TensorCalculator
TensorCalculator is a Python module that provides utility functions for working with tensors using the PyTorch library. This module includes methods for creating tensors filled with ones, zeros, and random values, as well as performing basic arithmetic operations on tensors.

# Installation
To use this module, you need to have PyTorch installed. You can install PyTorch using the following command:
  pip install torch

# Usage
Here's how you can use the TensorCalculator module in your Python code:

from tensor_calculator import TensorCalculator

These are the functions used:

tensor_ones(dim_x, dim_y, dim_z): Create a tensor filled with ones of the specified dimensions.

tensor_zeros(dim_x, dim_y, dim_z): Create a tensor filled with zeros of the specified dimensions.

tensor_rand(dim_x, dim_y, dim_z): Create a tensor filled with random values of the specified dimensions.

tensor_plus(d, f): Perform element-wise addition of two tensors.

tensor_mul(d, f): Perform element-wise multiplication of two tensors.

tensor_res(d, f): Perform element-wise subtraction of two tensors.

tensor_div(d, f): Perform element-wise division of two tensors.

tensor_concatenate(d, f, axis): Concatenate two tensors along the specified axis. (0,1,2)

# License
This code is provided under the MIT License. You are free to use and modify it in your projects.
