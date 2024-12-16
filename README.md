# Minimum Arrow Shift

This repository contains a solution to a problem from Codility. It is a Python programming exercise focused on optimization and logic to solve the arrow rotation problem.

## Problem Description

You are given a string `S` representing a sequence of `N` arrows. Each arrow in the sequence points in one of the four directions: **up (`^`)**, **down (`v`)**, **left (`<`)**, or **right (`>`)**. In one move, an arrow can be rotated 90 degrees clockwise, following this sequence:

- `^` becomes `>`
- `>` becomes `v`
- `v` becomes `<`
- `<` becomes `^`

Each arrow can only move to the next direction in the specified sequence, and it is not possible to move an arrow to any arbitrary direction.

Your task is to write a function:

```python
def solution(S):
```

that, given a string `S` of length `N` denoting the directions of the arrows, returns the **minimum number of moves required** to make all arrows point in the same direction.

### Example

For `S = "vv>>vv"`, the function should return `4`. The optimal solution is to rotate the arrows so that all point to the right (`>`).

### Assumptions

- `N` is an integer within the range `[1..100]`.
- The string `S` contains only the following characters: `^`, `v`, `<`, `>`.



## Testing

Several test cases are included to validate the logic of the program:

| Input              | Expected Output | Explanation                                                 |
|--------------------|-----------------|-------------------------------------------------------------|
| `"vv>>vv"`         | 4               | Rotating all arrows to `>` requires 4 moves.               |
| `"<<<<<"`          | 0               | All arrows are already pointing in the same direction.     |
| `"<<^>>"`          | 5               | Minimum effort when aligning all to `<`.                   |
| `"^^^>>>>>vvv<<<<"`| 20              | Balancing rotations to the optimal direction minimizes effort.|

### Legal Notes

All rights to the problem belong to Codility. This repository contains only a solution implemented as a Python learning exercise.

