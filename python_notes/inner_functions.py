# noqa
# def parent():
#     print("Printing from parent()")

#     def first_child():
#         print("Printing from first_child()")

#     def second_child():
#         print("Printing from second_child()")

#     second_child()
#     first_child()


def parent(num):
    def first_child():
        return "Hi, I'm Ernest"

    def second_child():
        return "Call me Bart"

    if num == 1:
        return first_child
    else:
        return second_child