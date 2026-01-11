"""Feature engineering utilities."""

from typing import Any


def text_to_number(text: str) -> int:
    """Deterministically convert ``text`` to an integer.

    The function computes the sum of Unicode code points for each character in
    the input string. It is pure and deterministic: the same input always
    produces the same integer output. An empty string returns 0.

    Args:
        text: The input string to convert.

    Returns:
        An integer representation of the input text.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Sum of Unicode code points provides a simple, deterministic mapping.
    return sum(ord(ch) for ch in text)
