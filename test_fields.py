# disjoint set


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.rank: int
        self.parent: Node


def make_set(x: Node) -> None:
    """
    make x as a set
    Rank is the distance from x to it's parent
    Roots rank is 0
    """
    x.rank = 0
    x.parent = x


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    Set with bigger rank should be parent, so that
    the disjoint set tree will be flatter
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return
    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank == 1


def find_set(x: Node) -> Node:
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def find_python_set(node: Node) -> set:
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)


def test_disjoint_set() -> None:
    """
    >>> test_disjoint_set()
    """
    vertex = [Node(i) for i in range(6)]
    for v in vertex:
        make_set(v)

    union_set(vertex[0], vertex[1])
    union_set(vertex[1], vertex[2])
    union_set(vertex[3], vertex[4])
    union_set(vertex[3], vertex[5])

    for node0 in vertex:
        for node1 in vertex:
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)


if __name__ == "__main__":
    test_disjoint_set()