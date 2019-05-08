#!/usr/bin/env python
"""
 Created by howie.hu at 2019/5/8.
 需求：
    当你依次访问完一串页面 a-b-c 之后，点击浏览器的后退按钮，就可以查看之前浏览过的页面 b 和 a。
    当你后退到页面 a，点击前进按钮，就可以重新查看页面 b 和 c。
    但是，如果你后退到页面 b 后，点击了新的页面 d，那就无法再通过前进、后退功能查看页面 c
 解决方案：
    两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X
    当点击后退按钮时，再依次从栈 X 中出栈，并将出栈的数据依次放入栈 Y。
    当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。
    当栈 Y 中没有数据，那就说明没有页面可以点击前进按钮浏览了
"""

from linked_stack import LinkedStack


class NewLinkedStack(LinkedStack):
    def is_empty(self):
        return not self._top


class Browser:
    def __init__(self):
        # X
        self.forward_stack = NewLinkedStack()
        # Y
        self.back_stack = NewLinkedStack()

    def can_forward(self):
        if self.back_stack.is_empty():
            return False

        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            return False

        return True

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return

        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print("back to %s" % top, end="\n")

    def forward(self):
        if self.back_stack.is_empty():
            return

        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print("forward to %s" % top, end="\n")


if __name__ == "__main__":

    browser = Browser()
    browser.open("a")
    browser.open("b")
    browser.open("c")
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()
