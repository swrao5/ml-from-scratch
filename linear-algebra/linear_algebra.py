from typing import List

Vector = List[float]

def subtract(v: Vector, w: Vector) -> Vector:
   """Subtracts corresponding elements"""
   assert len(v) == len(w), "vectors must be the same length"
   return [v_i - w_i for v_i, w_i in zip(v, w)]

def add(v: Vector, w: Vector) -> Vector:
   """Adds corresponding elements"""
   assert len(v) == len(w), "vectors must be the same length"
   return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors : List[Vector]) -> Vector:
   """Sums all corresponding elements"""
   # Check that vectors is not empty
   assert vectors, "no vectors provided!"
   
   num_elements = len(vectors[0])
   assert all(len(v) == num_elements for v in vectors)

   # the i-th element of the result is the sum of every vector[i]
   return [sum(v[i] for v in vectors) for i in range(num_elements)]





if __name__ == "__main__":
   assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
   assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
   assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
   print("success")

