import pytest

# The function we want to test
def format_user_name(first: str, last: str) -> str:
    if not first or not last:
        raise ValueError("Names cannot be empty")
    return f"{first.capitalize()} {last.capitalize()}"

# 1. A Fixture: Prepares data for tests
@pytest.fixture
def sample_user():
    return {"first": "guido", "last": "van rossum"}

# 2. Test cases
def test_format_user_name(sample_user):
    result = format_user_name(sample_user["first"], sample_user["last"])
    assert result == "Guido Van rossum"

def test_format_user_name_error():
    with pytest.raises(ValueError):
        format_user_name("", "Python")

# To run this: pytest 01_unit_testing.py