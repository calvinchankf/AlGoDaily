"""
    1st: topological ordering
    - if there are more than one zero indegree node in the process of building the sequence,
        it means there are more than one topological order
    
    e.g. seqs = [[1, 2], [1, 3]]

    In the iterations we build the order, zero indegrees in queue
    queue = [1]
    queue = [2, 3]
    It means we can build [1,2,3] or [1,3,2]

    Time    O(N + E)
    Space   O(N)
    472 ms, faster than 51.30%
"""


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        nodesSet = set()
        for seq in seqs:
            for x in seq:
                nodesSet.add(x)
        nodes = list(nodesSet)
        # init adjacents and indegrees for all nodes
        connections = {}
        indegrees = {}
        for node in nodes:
            connections[node] = []
            indegrees[node] = 0
        # get all the adjacents list and indegree
        for seq in seqs:
            for i in range(1, len(seq)):
                src = seq[i-1]
                dest = seq[i]
                # add node to the adjacent list
                connections[src].append(dest)
                # add indegree for each node
                indegrees[dest] += 1
        # get the nodes with 0 indegree
        queue = []
        for key in indegrees:
            if indegrees[key] == 0:
                queue.append(key)
        # dequeue node from the queue and put it into the result
        res = []
        maxZeroIndegreeCount = 0
        while len(queue) > 0:
            # track the number of zero indegree nodes
            maxZeroIndegreeCount = max(maxZeroIndegreeCount, len(queue))
            # deqeue
            node = queue.pop(0)
            res.append(node)
            children = connections[node]
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)
        # return [] if there is a cycle
        for key in indegrees:
            if indegrees[key] > 0:
                return False
        # if, in the process of building the sequence, there are more than one zero indegree node,
        # it means there are more than one topological order
        return tuple(res) == tuple(org) and maxZeroIndegreeCount == 1


s = Solution()

a = [1, 2, 3]
b = [[1, 2], [1, 3]]
print(s.sequenceReconstruction(a, b))

a = [1, 2, 3]
b = [[1, 2], [1, 3], [2, 3]]
print(s.sequenceReconstruction(a, b))

a = [4, 1, 5, 2, 6, 3],
b = [[5, 2, 6, 3], [4, 1, 5, 2]]
print(s.sequenceReconstruction(a, b))
