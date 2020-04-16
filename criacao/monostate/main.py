class Monostate:

    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


if __name__ == "__main__":
    m1 = Monostate()
    m2 = Monostate()
    m1.x = 4
    print(m1)
    print(f"X value: {m1.x}")
    print(m2)
    print(f"X value: {m2.x}")
