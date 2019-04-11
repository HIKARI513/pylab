# 实现数组的插入、删除和随机访问


class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __len__(self) -> int:
        return len(self._data)

    def delete(self, index):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return None

    def find(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None

    def insert(self, index, value):
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        for item in self._data:
            print(item)


def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    print(array._data)
    array.insert(0, 4)
    print(array._data)
    array.insert(1, 5)
    print(array._data)
    array.insert(3, 9)
    print(array._data)
    array.insert(3, 10)
    print(array._data)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()
