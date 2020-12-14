class ValueNotFoundType:
    def __bool__(self):
        raise ValueError("Boolean type cast disallowed")


ValueNotFound = ValueNotFoundType()
