# mystery_module

`mystery_module.py` provides a small utility for solving quadratic equations.

## What it does

The module defines a single function, `fn_x(a, b, c)`, which calculates the roots of a quadratic equation in the standard form:

```
a x^2 + b x + c = 0
```

It uses the quadratic formula and returns a tuple containing the two roots when the discriminant is non-negative.

## Function

### `fn_x(a, b, c)`

- `a` (`float` or `int`): coefficient of `x^2`
- `b` (`float` or `int`): coefficient of `x`
- `c` (`float` or `int`): constant term

Returns:

- `tuple[float, float]` when the equation has real roots
- `None` when the discriminant is negative (no real roots)

## Usage example

```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)
print(roots)  # output: (2.0, 1.0)

no_real_roots = fn_x(1, 0, 1)
print(no_real_roots)  # output: None
```

## Notes

- The function relies on `math.sqrt`, so it only returns real roots.
- If `a` is zero, the expression will raise a `ZeroDivisionError`.
