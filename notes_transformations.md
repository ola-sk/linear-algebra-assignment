## Cartesian Space Assumption

In standard linear algebra and geometry, we assume:

* Each axis (x, y, z, etc.) is **orthogonal** (i.e., at 90°) to every other axis.
* Each axis is a **unit vector** (length = 1).

This setup defines an **orthonormal basis**, allowing us to:

* Apply Euclidean distance formulas directly
* Treat each dimension as independent
* Use simple, interpretable transformations (like rotations)

## Transformations, behaviour
##### Rotations: 
- Act within a 2D plane at a time.
- All other coordinates (dimensions) outside the scope of the rotation remain unchanged.
- Only the coordinates in the two dimensions involved in the rotation change; the rest remain the same.

##### Scaling is applied in all dimensions.

##### Translation is applied in one or more dimensions at a time.

Additionally, in my application, transformations will be applied to multiple vectors at once, so here is an analysis of how different transformations will affect multiple vectors in relation to each other.
## Multi-vector transformations: orthogonal vs non-orthogonal
Orthogonal transformations (e.g., rotations, translations, reflections) naturally:
- Preserve geometric relationships among transformed vectors: their relative angles and distances.
- Preserve the length of the transformed vectors in the 2D plane involved in the rotation, and by extension, the norm of the whole vector.
- Preserve angles in relation to other dimensions for each transformed vector.
- Preserve relative angles—and therefore the dot product values—between all vectors when the same orthogonal transformation is applied.

In contrast, non-orthogonal transformations like shearing in a 2D subspace or scaling (in 2D or higher dimensions)
either affect the overall length of the vector or the relative angles of all transformed vectors. 
For example, they affect the dot product in the following ways:
- If orthogonal vectors are involved in scaling, the dot product stays 0; otherwise, it scales along with the vectors' transformation.
- Shearing changes the dot product in a less intuitive way, but it is sufficient to say it alters the value of the dot product.