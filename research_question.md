# Language Model Surprisal Analysis

## Research question

Is higher word surprisal associated with longer human reading times?

## Key concepts

- **Surprisal:** how unexpected a word is given its preceding context.
- **Reading time:** the time a participant takes to read a word or text segment.
- **Hypothesis:** words with higher surprisal may be associated with longer reading times.

## Analysis plan

1. Obtain word probabilities from a language model.
2. Calculate surprisal using -log2(probability).
3. Compare surprisal values with human reading times.
4. Visualize and statistically analyse the relationship.
   
## Variables

- **Predictor:** word surprisal, measured in bits.
- **Outcome:** human reading time, measured in milliseconds.
- **Research hypothesis:** higher surprisal is associated with longer reading times.

## Planned implementation

- Use Python to load a pretrained language model.
- Extract the probability of each target token given its preceding context.
- Convert probability to surprisal using -log2(probability).
- Compare surprisal with human reading-time data.
