


class Test:

    @classmethod
    def a_plus_b(cls, a, b):
        cls.ab = a + b
        print(cls.ab)


n = Test.a_plus_b(1, 2)


