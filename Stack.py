#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    """
    The Stack class can be used to represent a stack of any type: Stack[int], Stack[Tuple[int, str]], etc
    """

    def __init__(self) -> (None):
        """

        """
        self.items: List[T] = []

    def push(self, item: T) -> (None):
        """

        :param item:
        :return:
        """
        print(type(item))
        print(T)
        self.items.append(item)

    def pop(self) -> (T):
        """

        :return:
        """
        return self.items.pop()

    def empty(self) -> (bool):
        """

        :return:
        """
        return not self.items
