import pytest  # noqa: INP001

from box import Box, BoxFullError, Fruit


@pytest.fixture()
def small_box():
    return Box(200)


@pytest.fixture()
def big_box():
    return Box(500)


@pytest.fixture()
def apple():
    return Fruit("apple", 187)


@pytest.fixture()
def banana():
    return Fruit("banana", 156.1)


def test_box_init():
    box = Box(500)
    assert box.capacity == 500
    assert box.fruits == []


def test_box_str(small_box):
    assert str(small_box) == "Box contains 0 fruit(s)"


def test_box_repr(small_box):
    assert repr(small_box) == "Box(capacity=200, fruits=[])"


def test_box_add_fruit(small_box, apple):
    small_box.add_fruit(apple)
    assert small_box.fruits == [apple]
    assert small_box.volume == apple.volume


def test_box_add_multiple_fruits(big_box, apple, banana):
    big_box.add_fruit(apple)
    big_box.add_fruit(banana)
    assert big_box.fruits == [apple, banana]
    assert big_box.volume == apple.volume + banana.volume


def test_box_multiple_fruits_to_fill(small_box, apple, banana):
    small_box.add_fruit(apple)
    assert small_box.fruits == [apple]
    assert small_box.volume == apple.volume

    with pytest.raises(BoxFullError) as exc_info:
        small_box.add_fruit(banana)
    assert str(exc_info.value) == "Can't add banana to the box as it is full"


def test_box_add_fruit_with_add_operator(small_box, apple):
    small_box.add_fruit(apple)
    assert small_box.fruits == [apple]
    assert small_box.volume == apple.volume


def test_box_add_fruit_with_iadd_operator(small_box, apple):
    small_box += apple
    assert small_box.fruits == [apple]
    assert small_box.volume == apple.volume


def test_box_fruit_with_add_operator_invalid_type(small_box, big_box):
    with pytest.raises(TypeError) as exc_info:
        small_box = small_box + big_box
    assert str(exc_info.value) == "unsupported operand type(s) for +: 'Box' and 'Box'"


def test_box_fruit_with_iadd_operator_invalid_type(small_box, big_box):
    with pytest.raises(TypeError) as exc_info:
        small_box = small_box + big_box
    assert str(exc_info.value) == "unsupported operand type(s) for +: 'Box' and 'Box'"


def test_box_full_str(small_box, apple):
    small_box.add_fruit(apple)
    assert str(small_box) == "Box contains 1 fruit(s)"


def test_box_full_repr(small_box, apple):
    small_box.add_fruit(apple)
    assert (
        repr(small_box) == "Box(capacity=200, fruits=[Fruit(name='apple', volume=187)])"
    )
