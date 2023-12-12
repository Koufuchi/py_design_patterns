from threading import Lock, Thread


class SingletonMeta(type):

    _instances = {}

    _lock: Lock = Lock()

    # 讓這個類可以實例化，且實例化時執行此方法
    def __call__(cls, *args, **kwargs):
        # print("\ncls: ", cls, "\ncls._instances: ", cls._instances, "\n*args: ", *args, "\n**kwargs: ", **kwargs)
        print("\ncls: {}\ncls._instances: {}\n*args: {}\n**kwargs: {}".format(cls, cls._instances, args, kwargs))

        with cls._lock:  # 臨界區，先到者先拿鎖，後到者需等先到者釋放。
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)  # 使用父類別(type)原本的 __call__()
                cls._instances[cls] = instance
        return cls._instances[cls]  # 釋放鎖


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value, "\n")


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()

    test3 = test_singleton("CAT")
    test4 = test_singleton("DOG")