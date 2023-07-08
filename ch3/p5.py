"""
(a)
    Inserting 4 elements will cost 1+2+4=7 copies.
    Deleting 1 element will make it fall to 3/8 filled elements, trigger array size reduction, meaning copying 3 times.
    Subsequently, if you alternate between an insertion and a delete, that costs 4 copies and 3 copies, respectively.
    Thus each alternating insertion and deletion costs O(n) copies.

(b)
    Try resizing once array falls to 1/4th its full capacity. In this way you need to delete at least 50% of a newly
    extended array's elements before copying happens. So along the lines of the example above, if you have 4 elements in
    an 8-element array, you need to delete two elements before a resize costing 2 copies, which means each delete
    amortizes to O(1).
"""
