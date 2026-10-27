import math

def calculate_surprisal(probability):
  if probability <= 0 or probability > 1:
        raise ValueError("Probability must be greater than 0 and at most 1.")

    return -math.log2(probability)
print(calculate_surprisal(0.25))
print(calculate_surprisal(0.5))
