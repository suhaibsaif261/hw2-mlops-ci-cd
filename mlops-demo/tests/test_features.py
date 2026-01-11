import pytest

from src.features import text_to_number


def test_text_to_number_empty():
    assert text_to_number("") == 0


def test_text_to_number_known():
    # 'abc' => 97 + 98 + 99 = 294
    assert text_to_number("abc") == 97 + 98 + 99


def test_text_to_number_deterministic():
    assert text_to_number("Hello, world!") == text_to_number("Hello, world!")


def test_text_to_number_type_error():
    with pytest.raises(TypeError):
        text_to_number(None)


def test_text_to_number_repeated_calls():
    """Verify deterministic behavior across multiple calls."""
    sample = "deterministic"
    first = text_to_number(sample)
    for _ in range(10):
        assert text_to_number(sample) == first
