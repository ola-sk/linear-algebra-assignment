import types
from typing import Tuple, Union, Any, cast, TypeVar, Generic
import numpy as np

# Define a constrained type variable for floating point types
T_Float = TypeVar('T_Float', float, np.floating)
class Vector3D(np.ndarray, Generic[T_Float]):
    """
    The Vector3D class extends np.ndarray with a minimal initialization overhead,
    so it inherits the performance characteristics of NumPy arrays.

    Initialization of Vector3D should happen via its `create` method, where a verification logic is implemented.
    This allows static type checkers to understand the expected type of the vector, i.e. a 3 element NumPy ndarray holding floats.

    Main Benefits:
    - type checking,
    -validation at creation time,
    - ensuring the vector is a 3D float array.

    Performance characteristics:
    - Minimal memory overhead: Since there are no additional instance variables, a Vector3D has the same memory footprint as an np.ndarray.
    - No initialization penalty: The class adds minimal initialization logic via `create` method.
    - Vectorised operations: All NumPy optimized C-based operations still apply, so mathematical operations remain fast.
    - Type checking cost: The only cost comes at initialization time when static method `create()` with the validation logic is called, not during normal operations.
    """
    @classmethod
    def __class_getitem__(cls, item: Any) -> type['Vector3D[T_Float]']:
        """
        Extra logic for static type checking to allow or disallow a Vector3D type to be parameterised: only float or numpy.floating types are allowed.
        e.g. Vector3D[float] and Vector3D[np.float64] would work, but Vector3D[int] or Vector3D[str] would raise a type error.

        This __class_getitem__ method is focused only on restricting what type parameters can be used with the class, not the shape or size of instances.
        """
        # We explicitly check for float and any numpy floating type
        if isinstance(item, type) and (item is float or issubclass(item, np.floating)):
            return cls
        elif hasattr(item, "__or__") or hasattr(item, "__ror__"):  # Handle | (pipe) operator in Python 3.10+
            # Check if this is a union-like type (either from | operator or Union)
            origin = getattr(item, "__origin__", None)
            args = getattr(item, "__args__", None)
            if origin is Union or origin is types.UnionType:
                if all(isinstance(t, type) and (t is float or issubclass(t, np.floating)) for t in args):
                    return cls
            raise TypeError(f"All types in Union or | expression must be float or numpy floating types, got {item}")
        else:
            allowed_types_str = "float, np.floating (np.float16, np.float32, np.float64, np.float128, etc.)"
            raise TypeError(f"Vector3D only supports floating point types: {allowed_types_str}, got {item}")

    @classmethod
    def create(cls,
               arr: Tuple[float | int, float | int, float | int] |
                    list[float | int] |
                    np.ndarray,
               origin: Tuple[float | int, float | int, float | int] |
                       list[float | int] |
                       np.ndarray = (0, 0, 0),
               ) -> 'Vector3D[T_Float]':
        """
        Create a Vector3D from an array-like object.

        Parameters:
            :param arr: array-like object (tuple, list, or ndarray) with 3 elements.
                 Elements can be int or float types, which will be converted to float.
            :param origin: the vector's values would be calculated relative to this origin.

        Returns:
            New Vector3D array (numpy arrays of shape (3,) and dtype float).

        Raises:
            ValueError: If input shapes are not (3,).
            TypeError: If input elements cannot be converted to floating point types.

        """
        try:
            print(arr, origin)
            # Allow numeric types (int, float) that can be safely converted to float, error out for non-numeric types.
            arr = np.asarray(arr, dtype=float)
            origin = np.asarray(origin, dtype=float)
            print(arr, arr.shape, origin, origin.shape)

            # Check shape
            if arr.shape != (3,):
                raise ValueError(f"Array argument (arr) to Vector3D.create() must have shape (3,), got {arr.shape}")
            if origin.shape != (3,):
                raise ValueError(f"Array argument (origin) to Vector3D.create() must have shape (3,), got {origin.shape}")
            arr[0] += origin[0]
            arr[1] += origin[1]
            arr[2] += origin[2]
            # cast to Vector3D instance after all above checks passed and absolute coordinates have been calculated.
            # casting to a view is intentional and part of NumPy's efficient memory model - views don't duplicate data,
            # therefore the declaration below just creates a reference of different type pointing to the same memory block.
            return cast('Vector3D[T_Float]', arr.view(cls))
        except (ValueError, TypeError) as e:
            if "could not convert" in str(e):
                raise TypeError(
                    f"Vector3D requires numeric elements that can be converted to float, got {type(arr)} with elements of incompatible types")
            raise

    def __str__(self) -> str:
        """Return a string representation of the vector used in str(), formatted like a regular NumPy array."""
        return np.ndarray.__str__(self)

    def __repr__(self) -> str:
        """Return a string representation of the vector, formatted like a regular NumPy array."""
        return np.ndarray.__str__(self)

def edge_3d(tail: Vector3D[float], head: Vector3D[float]) -> np.ndarray:
    """
    Create an edge from tail to head vectors.

    Parameters:
        tail: The starting point of the edge
        head: The end point of the edge

    Returns:
        A 2x3 NumPy array containing 3-element vectors with tail and head coordinates.
    """
    return np.array([head, tail])

