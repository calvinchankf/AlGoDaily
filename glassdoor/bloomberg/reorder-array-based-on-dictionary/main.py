from collections import *

"""
    Consider a vector of employees with a name and their title:
    [<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

    And a dictionary where the keys report to the values:
    {[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

    Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, however the dictionary only contains the title orderings.

    Sample output:
    [<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

    Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, which is manager. They can also be in either order in this case.
"""


def reorderArray(employees, order):
    """
        topo sort
        - sort the role
        - put the names by roles in result
        - reverse the result

        Time    O(V+E)
        Space   O(V)
    """
    hierarchy = defaultdict(list)
    graph = defaultdict(list)
    indegrees = Counter()

    for role, boss in order:
        graph[boss].append(role)
        indegrees[role] += 1

    for name, role in employees:
        hierarchy[role].append(name)

    q = []
    for role in graph:
        if indegrees[role] == 0:
            q.append(role)
    res = []
    while len(q) > 0:
        role = q.pop(0)
        res += [(person, role) for person in hierarchy[role]]
        for _role in graph[role]:
            indegrees[_role] -= 1
            if indegrees[_role] == 0:
                q.append(_role)
    return res[::-1]


a = [('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'),
     ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer')]
b = [['CTO', 'CEO'], ['Manager', 'CTO'], [
    'Engineer', 'Manager'], ['CFO', 'CEO']]
print(reorderArray(a, b))
