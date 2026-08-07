class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b), val in zip(equations, values): 
            graph[a][b] = val
            graph[b][a] = 1/val

        def bfs(start, end): 
            if not start in graph or not end in graph: 
                return -1.0
            if start == end: 
                return 1.0
            visited = {start}
            queue = deque([(start, 1.0)])
            while queue:
                curr, curr_prod = queue.popleft()
                if curr == end: 
                    return curr_prod
                for neighbor, weight in graph[curr].items(): 
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        queue.append((neighbor, curr_prod * weight))
            return -1.0
        return [bfs(c,d) for c,d in queries]

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna