"""
Brute force:
Starting from the first position, for each n-k positions, mark the value and compare with the k values ahead.
If there is ever a match, we don't have a k-unique array. Time: O((n-k) * k) = O(nk - k^2)

Option 2:
Sort copy of array with references to original index in O(n lg n) time. We also want to preserve original order,
so that the index refs are sorted. Then go through the sorted list and for each unique number, check that the range
of adjacent indices don't intersect. That part is O(n), so total is O(n lg n)

Option 3:
For each position, take its value and index and insert it into a hashtable, hashing the value and storing the value and
index. If we encounter the same value later on, we hash to the list, traverse the list and check that each node
whose value matches has a index outside of the range. We can replace each node of the same value we iterate over,
since we won't need to check an older node if we have a newer node with a further along index.
Best case: O(n)
Worst case: O(n^2), if max collisions in hash table.

Option 4:
Similar to above, but insert into a BST. Once we've iterated past k nodes, start removing nodes (decided by negative
offset from index). This will keep BST to k members, which we'll check against to decide if there's a dupe in range.
Time: O(n lg k)
"""
