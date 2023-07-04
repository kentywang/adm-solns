class ListPointer:
    def __init__(self, lst):
        self.lst = lst


class List:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insert(lstptr, x):
    """
    Functionally equivalent to:

    void insert_list(list **l, item_type x) {
        list *p; /* temporary pointer */

        p = malloc(sizeof(list));
        p->item = x;
        p->next = *l;
        *l = p;
    }
    """
    p = List(x, lstptr.lst)
    lstptr.lst = p


node_a = List('A')
start = ListPointer(node_a)
insert(start, 'B')
print(start.lst.val)
