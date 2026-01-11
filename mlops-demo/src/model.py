"""Simple model placeholder for CI/CD demo."""

from typing import Any


def predict(value: int) -> str:
    """Return a deterministic label for the input integer.

    The function returns "LOW" when ``value`` is less than 10, and "HIGH"
    otherwise. It is intentionally simple and contains no randomness or ML
    dependencies; this is only for demonstration and testing in CI/CD.

    Args:
        value: Integer input to classify.

    Returns:
        A string, either "LOW" or "HIGH".

    Raises:
        TypeError: If ``value`` is not an int.
    """
    if not isinstance(value, int):
        raise TypeError("value must be an int")

    return "LOW" if value < 10 else "HIGH"
