class Encoder:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __result(self):
        return self.__a * self.__b * 0.1

    def get(self):
        return self.__result()




en = Encoder(4,20)
print(en.get())
