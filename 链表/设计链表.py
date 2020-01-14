""" 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向
下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

    get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
    addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
    果 index 等于链表的长度，则该节点将附加到链表的末尾。
    如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。



示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3  """
""" class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index > self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        if self.size == 0:
            self.head = Node(val)
            self.size += 1
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def addAtTail(self, val):
        if self.size == 0:
            self.head = Node(val)
            self.size += 1
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(val)
            self.size += 1

    def addAtIndex(self, index, val):
        if (index+1) > self.size:
            return -1
        elif index < 0 or self.size == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            insert_node = Node(val)
            insert_node.next = node.next
            node.next = insert_node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index > self.size-1 or self.size == 0:
            return -1

        elif index == 0:
            node = self.head
            self.head = node.next
            self.size -= 1

        else:
            node = self.head
            for i in range(index-1):
                node = node.next
            tem = node.next
            if tem.next == None:
                node.next = None
                self.size -= 1
            else:
                node.next = tem.next
                self.size -= 1

    def showLinkedlist(self):
        nodelist = []
        for i in range(self.size):
            nodelist.append(self.get(i))
        print(nodelist) """


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:

        if self.size == 0:
            return -1
        elif index < 0 or index > self.size - 1:
            return -1

        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.size += 1
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.size += 1

        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        new = Node(val)
        if index <= 0:
            self.addAtHead(val)
        if index > self.size:
            return -1
        else:
            node = self.head
            for i in range(index - 1):
                node = node.next
            if node.next is None:
                node.next = new
                self.size += 1
            else:
                new.next = node.next
                node.next = new
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index > self.size - 1 or self.size == 0:
            return -1

        elif index == 0:
            node = self.head
            self.head = node.next
            self.size -= 1

        else:
            node = self.head
            for i in range(index - 1):
                node = node.next
            tem = node.next
            if tem.next is None:
                node.next = None
                self.size -= 1
            else:
                node.next = tem.next
                self.size -= 1


if __name__ == '__main__':
    mylist = MyLinkedList()
    mylist.addAtHead(1)
    mylist.addAtTail(3)
    mylist.addAtIndex(1, 2)  # 链表变为1-> 2-> 3
    mylist.get(1)  # 返回2
    mylist.deleteAtIndex(1)  # 现在链表是1-> 3
    mylist.showLinkedlist()
    print(mylist.get(1))  # 返回3
