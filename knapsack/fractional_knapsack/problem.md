# Knapsack Problem

## Input

- No of items: `n`
- Weights: `W1, W2, ..., Wn`
- Value: `V1, V2, ..., Vn`
- Capacity of Knapsack: `W`

## Output

Maximum total value of fractions of items that fit into the bag of capacity W.

## Naive algo

- create a fraction array:
  - `V1/W1, V2/W2, ..., Vn/Wn`
- Sort the fraction array
- Take the first item
  - if W1 > W:
    - put fraction of W1 into bag, return the result
  - else:
    - put W1 into bag. Reduce W by W1, and run fractional knapsack on (W - W1) with remaining array.
