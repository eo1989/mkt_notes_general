# ruff: noqa: I001,INP001
import pytest
from box import BoxFullError, Fruit


@pytest.fixture()
def fruit():
    return Fruit("apple", 187)


def test_box_full_error(fruit):
    with pytest.raises(BoxFullError) as exc_info:
        raise BoxFullError(fruit)
    assert str(exc_info.value) == "Can't add apple to the box as it is full"

    ">= *** "