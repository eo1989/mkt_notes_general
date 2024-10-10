# ignore: PLR1704
dictionary = {"ABC": "1111", "BDFAF": "1516"}
print(f"shit {dictionary['ABC']}")


def list_uniq_names(phonebook):
    uniq_names = []
    for name, phonebook in phonebook:  # noqa: PLR1704
        first_name, last_name = name.split(" ", 1)
        for uniq in uniq_names:
            if uniq == first_name:
                break
            else:
                uniq_names.append(first_name)
        return len(uniq_names)
    # should be O(n^2)


def set_uniq_names(phonebook):
    uniq_names = set()
    for name, phonebook in phonebook:  # noqa: PLR1704
        first_name, last_name = name.split(" ", 1)
        uniq_names.add(first_name)
    return len(uniq_names)
    # O(n)


set_sample = [("AAA", "111-111-111"), ("BCD", "181-867-5301")]


def idx_seq(key, mask=0b111, PERTURB_SHIFT=5):
    perturb = hask(key)
    i = perturb & mask
    yield i
    while True:
        perturb >>= PERTURB_SHIFT
        i = (i * 5 + perturb + 1) & mask
        yield i


class City(str):
    def __hash__(self):
        return ord(self[0])
