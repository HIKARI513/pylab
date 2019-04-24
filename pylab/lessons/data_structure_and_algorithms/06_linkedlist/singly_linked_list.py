# 实现单链表的插入、删除、查找等操作
# 默认数据类型为int

from typing import Optional, Union


class Node:
    """
    链表结构的节点
    """

    def __init__(self, data: int, next=None):
        """
        初始化Node节点
        :param data: 存储的数据
        :param next: 后继指针
        """
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        """初始化单链表"""
        self._head = None

    def find_by_index(self, index: int) -> Optional[Node]:
        p = self._head
        position = 0
        while p and position != index:
            p = p.next
            position += 1
        return p

    def find_by_value(self, value: int) -> Optional[Node]:
        """
        根据值查找相应的节点
        :param value:
        :return:
        """
        p: Union[Node, None] = self._head
        while p and p.data != value:
            p = p.next
        return p

    def insert_value_to_head(self, value: int):
        """
        插入一个Node到头结点
        :param value: 新头结点的值
        :return:
        """
        new_node = Node(data=value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        """
        构建头结点，让后继指针指向下一个节点
        :param new_node: 新的头结点
        :return:
        """
        if new_node:
            new_node.next = self._head
            self._head = new_node

    def insert_value_before(self, node: Node, value: int):
        """
        在某个节点前插入节点
        :param node: 目标节点
        :param value: 待插入节点值
        :return:
        """
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        """
        新节点替代当前节点的位置，然后将新节点的后继指针指向当前节点，当前节点作为新节点的后继元素
        :param node: 当前节点
        :param new_node: 新节点
        :return:
        """
        if not self._head or not node or not new_node:
            return

        if self._head == node:
            self.insert_node_to_head(new_node)
            return

        current = self._head
        while current.next and current.next != node:
            current = current.next

        if not current.next:
            return

        current.next = new_node
        new_node.next = node

    def delete_by_node(self, node: Node):
        """
        删除链表中的某个节点
        :param node:
        :return:
        """
        if not self._head or not node:
            return

        if node.next:
            node.data = node.next.data
            node.next = node.next.next
            return

        # 如果node是尾结点或者不在列表
        current = self._head
        while current and current.next != node:
            current = current.next
        if not current:
            return
        current.next = node.next

    def delete_by_value(self, value: int):
        """
        根据值删除某一节点
        :param value:
        :return:
        """
        if not self._head or not value:
            return

        fake_head = Node(value + 1)
        fake_head.next = self._head
        prev, current = fake_head, self._head

        while current:
            if current.data != value:
                # 修改此时prev节点的后继指针指向当前节点
                prev.next = current
                # prev节点的后继指针指向的节点重新赋值给prev节点
                prev = prev.next
            current = current.next
        if prev.next:
            # 防止prev节点与None之间有删除的节点
            prev.next = None
        self._head = fake_head.next

    def print_all(self):
        current: Union[Node, None] = self._head

        if current:
            print(f"{current.data}", end="")
            current = current.next
        while current:
            print(f"->{current.data}", end="")
            current = current.next
        print("\n")

    def __repr__(self) -> str:
        nums = []
        current: Union[Node, None] = self._head

        while current:
            nums.append(current.data)
            current = current.next
        if len(nums) > 0:
            return "->".join(str(num) for num in nums)
        else:
            return ""


if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    print(l)
    node9 = l.find_by_value(9)
    l.insert_value_before(node9, 20)
    print(l)
    l.insert_value_before(node9, 16)
    print(l)
    l.insert_value_before(node9, 16)
    print(l)
    l.delete_by_value(16)
    print(l)
    node11 = l.find_by_index(3)
    print(node11.data, node11.next.data)
    l.delete_by_node(node11)
    print(l)
    l.delete_by_node(l._head)
    print(l)
