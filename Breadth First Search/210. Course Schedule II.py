题目：
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
             
             
             
主题思路跟207一模一样，只是最后的输出topological sorting的结果，若有环，则输出None

此题有个注意点：在graph的创建上跟207一样，但这道题需要result.reverse()????????????????

code:

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.create_graph(numCourses, prerequisites)
        
        indegrees = self.count_indegrees(graph)
        
        start_nodes = []
        for node in graph:
            if indegrees[node] == 0:
                start_nodes.append(node)
        queue = collections.deque(start_nodes)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(result) == numCourses:
            result.reverse()
            return result
        else:
            return None
        
    
    def create_graph(self, node, neighbor):
        graph = {}
        for n in range(node):
            graph[n] = set()
        for edge in neighbor:
            sub_node, node = edge[0], edge[1]
            graph[sub_node].add(node)
        return graph
    
    def count_indegrees(self, graph):
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
