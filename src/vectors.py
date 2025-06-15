import types
from typing import Tuple, Union, Any, cast, TypeVar, Generic
import numpy as np

# Define a constrained type variable for floating point types
T_Float = TypeVar('T_Float', float, np.floating)
class Vector3D(np.ndarray, Generic[T_Float]):
    """
    The Vector3D class extends np.ndarray with just a minimal initialization overhead,
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
                    np.ndarray
               ) -> 'Vector3D[T_Float]':
        """
        Create a Vector3D from an array-like object.

        Parameters:
            arr: Input array-like object (tuple, list, or ndarray) with 3 elements.
                 Elements can be int or float types, which will be converted to float.

        Returns:
            New Vector3D array (numpy arrays of shape (3,) and dtype float).

        Raises:
            ValueError: If input shapes are not (3,).
            TypeError: If input elements cannot be converted to floating point types.
        """
        try:
            # Allow numeric types (int, float) that can be safely converted to float, error out for non-numeric types.
            arr = np.asarray(arr, dtype=float)

            # Check shape
            if arr.shape != (3,):
                raise ValueError(f"Array argument (arr) to Vector3D.create() must have shape (3,), got {arr.shape}")

            # Return the Vector3D instance after all above checks passed
            # The `.view(cls)` method in NumPy is used to create a new array view
            # that shares the same data but is interpreted as a different array type - in this case, a Vector3D.
            return cast('Vector3D[T_Float]', arr.view(cls))
        except (ValueError, TypeError) as e:
            if "could not convert" in str(e):
                raise TypeError(
                    f"Vector3D requires numeric elements that can be converted to float, got {type(arr)} with elements of incompatible types")
            raise


def edge_3d(tail: Vector3D[float], head: Vector3D[float]
            ) -> Tuple[Vector3D[float], Vector3D[float]]:
    return head, tail
