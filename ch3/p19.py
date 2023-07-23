"""
After each insertion or deletion, run the existing O(lg n) min and max methods and cache the results. Simply return those
values for calls from external clients. This works because insert and delete are the old methods that can possibly alter
the min or max, and by running a O(lg n) method within those calls which are already O(lg n), no height time complexity
class is breached.
"""
