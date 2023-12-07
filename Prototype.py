import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class CyberSoldier:
    """
    Python provides its own interface of Prototype via `copy.copy` and
    `copy.deepcopy` functions. And any class that wants to implement custom
    implementations have to override `__copy__` and `__deepcopy__` member
    functions.
    """

    def __init__(self, level, item_lists, some_circular_ref):
        self.level = level
        self.item_lists = item_lists
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Create a shallow copy. This method will be called whenever someone calls
        `copy.copy` with this object and the returned value is returned as the
        new shallow copy.
        """

        # First, let's create copies of the nested objects.
        item_lists = copy.copy(self.item_lists)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.level, item_lists, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Create a deep copy. This method will be called whenever someone calls
        `copy.deepcopy` with this object and the returned value is returned as
        the new deep copy.

        What is the use of the argument `memo`? Memo is the dictionary that is
        used by the `deepcopy` library to prevent infinite recursive copies in
        instances of circular references. Pass it to all the `deepcopy` calls
        you make in the `__deepcopy__` implementation to prevent infinite
        recursions.
        """
        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        item_lists = copy.deepcopy(self.item_lists, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.level, item_lists, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    print("generate cyber_soldier and shallow_copied_cyber_soldier ...")

    item_lists = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    cyber_soldier = CyberSoldier(5, item_lists, circular_ref)
    circular_ref.set_parent(cyber_soldier)

    shallow_copied_cyber_soldier = copy.copy(cyber_soldier)

    print("- cyber_soldier.item_lists :", cyber_soldier.item_lists)
    print("- shallow_copied_cyber_soldier.item_lists :", shallow_copied_cyber_soldier.item_lists, "\n")

    print("Adding elements to shallow_copied_cyber_soldier.item_lists ...")
    shallow_copied_cyber_soldier.item_lists.append("another object")
    print("- cyber_soldier.item_lists :", cyber_soldier.item_lists)
    print("- shallow_copied_cyber_soldier.item_lists :", shallow_copied_cyber_soldier.item_lists, "\n")

    print("Changing objects in the cyber_soldier.item_lists ...")
    cyber_soldier.item_lists[1].add(4)
    print("- cyber_soldier.item_lists :", cyber_soldier.item_lists)
    print("- shallow_copied_cyber_soldier.item_lists :", shallow_copied_cyber_soldier.item_lists, "\n")

    print("generate deep_copied_cyber_soldier ...")
    deep_copied_cyber_soldier = copy.deepcopy(cyber_soldier)

    print("Adding elements to deep_copied_cyber_soldier.item_lists ...")
    deep_copied_cyber_soldier.item_lists.append("one more object")
    print("- cyber_soldier.item_lists :", cyber_soldier.item_lists)
    print("- deep_copied_cyber_soldier.item_lists :", deep_copied_cyber_soldier.item_lists, "\n")

    print("Changing objects in the cyber_soldier.item_lists ...")
    cyber_soldier.item_lists[1].add(10)
    print("- cyber_soldier.item_lists :", cyber_soldier.item_lists)
    print("- deep_copied_cyber_soldier.item_lists :", deep_copied_cyber_soldier.item_lists, "\n")

    print(
        f"id(cyber_soldier.some_circular_ref.parent): "
        f"{id(cyber_soldier.some_circular_ref.parent)}"
    )
    print(
        f"id(cyber_soldier.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(cyber_soldier.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        f"id(shallow_copied_cyber_soldier.some_circular_ref.parent): "
        f"{id(shallow_copied_cyber_soldier.some_circular_ref.parent)}"
    )
    print(
        f"id(shallow_copied_cyber_soldier.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(shallow_copied_cyber_soldier.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_cyber_soldier.some_circular_ref.parent): "
        f"{id(deep_copied_cyber_soldier.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_cyber_soldier.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_cyber_soldier.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ This shows that deepcopied objects contain same reference, they "
        "are not cloned repeatedly."
    )