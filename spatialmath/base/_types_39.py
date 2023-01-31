# for Python >= 3.9

from typing import overload, Union, List, Tuple, Type, TextIO, Any, Callable, Optional
from typing import Literal as L

from numpy import ndarray, dtype, floating
from numpy.typing import NDArray, DTypeLike

# array like

# these are input to many functions in spatialmath.base, and can be a list, tuple or
# ndarray.  The elements are generally float, but some functions accept symbolic 
# arguments as well, which leads to a NumPy array with dtype=object
#
# The variants like ArrayLike2 indicate that a list, tuple or ndarray of
# length 2 is expected.  Static checking of tuple length is possible but not a lists.
# This might be possible in future versions of Python, but for now it is a hint to the
# coder about what is expected 


ArrayLike = Union[float, List[float], Tuple[float], ndarray[Any, dtype[floating]]]
ArrayLike2 = Union[List, Tuple[float,float], ndarray[Tuple[L[2,]], dtype[floating]]]
ArrayLike3 = Union[List,Tuple[float,float,float],ndarray[Tuple[L[3,]], dtype[floating]]]
ArrayLike4 = Union[List,Tuple[float,float,float,float],ndarray[Tuple[L[4,]], dtype[floating]]]
ArrayLike6 = Union[List,Tuple[float,float,float,float,float,float],ndarray[Tuple[L[6,]], dtype[floating]]]

# real vectors
R2 = ndarray[Tuple[L[2,]], dtype[floating]]  # R^2
R3 = ndarray[Tuple[L[3,]], dtype[floating]]  # R^3
R4 = ndarray[Tuple[L[4,]], dtype[floating]]  # R^3
R6 = ndarray[Tuple[L[6,]], dtype[floating]]  # R^6

# real matrices
R2x2 = ndarray[Tuple[L[2,2]], dtype[floating]]  # R^{2x2} matrix
R3x3 = ndarray[Tuple[L[3,3]], dtype[floating]]  # R^{3x3} matrix
R4x4 = ndarray[Tuple[L[4,4]], dtype[floating]]  # R^{4x4} matrix
R6x6 = ndarray[Tuple[L[6,6]], dtype[floating]]  # R^{6x6} matrix
R1x3 = ndarray[Tuple[L[1,3]], dtype[floating]]  # R^{1x3} row vector
R3x1 = ndarray[Tuple[L[3,1]], dtype[floating]]  # R^{3x1} column vector
R1x2 = ndarray[Tuple[L[1,2]], dtype[floating]]  # R^{1x2} row vector
R2x1 = ndarray[Tuple[L[2,1]], dtype[floating]]  # R^{2x1} column vector

Points2 = ndarray[(2,Any), dtype[floating]]  # R^{2xN} matrix
Points3 = ndarray[(3,Any), dtype[floating]]  # R^{2xN} matrix

RNx3 = ndarray[(Any,3), dtype[floating]]  # R^{Nx3} matrix

def a(x:Points2):
    return x

import numpy as np
b = np.zeros((2,10))
z=a('sss')
z=a(b)


# Lie group elements
SO2Array = ndarray[Tuple[L[2,2]], dtype[floating]]  # SO(2) rotation matrix
SE2Array = ndarray[Tuple[L[3,3]], dtype[floating]]  # SE(2) rigid-body transform
SO3Array = ndarray[Tuple[L[3,3]], dtype[floating]]  # SO(3) rotation matrix
SE3Array = ndarray[Tuple[L[4,4]], dtype[floating]]  # SE(3) rigid-body transform

# Lie algebra elements
so2Array = ndarray[Tuple[L[2,2]], dtype[floating]]  # so(2) Lie algebra of SO(2), skew-symmetrix matrix
se2Array = ndarray[Tuple[L[3,3]], dtype[floating]]  # se(2) Lie algebra of SE(2), augmented skew-symmetrix matrix
so3Array = ndarray[Tuple[L[3,3]], dtype[floating]]  # so(3) Lie algebra of SO(3), skew-symmetrix matrix
se3Array = ndarray[Tuple[L[4,4]], dtype[floating]]  # se(3) Lie algebra of SE(3), augmented skew-symmetrix matrix

# quaternion arrays
QuaternionArray = ndarray[Tuple[L[4,]], dtype[floating]]
UnitQuaternionArray = ndarray[Tuple[L[4,]], dtype[floating]]

Rn = Union[R2,R3]

SOnArray = Union[SO2Array,SO3Array]
SEnArray = Union[SE2Array,SE3Array]

sonArray = Union[so2Array,so3Array]
senArray = Union[se2Array,se3Array]