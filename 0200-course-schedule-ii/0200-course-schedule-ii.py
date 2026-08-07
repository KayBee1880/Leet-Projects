class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree, queue
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites: 
            graph[prereq].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []
        while queue: 
            curr = queue.popleft()
            result.append(curr)
            for neighbor in graph[curr]: 
                indegree[neighbor]  -= 1
                if indegree[neighbor] == 0: 
                    queue.append(neighbor)
        return result if numCourses == len(result) else []


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna