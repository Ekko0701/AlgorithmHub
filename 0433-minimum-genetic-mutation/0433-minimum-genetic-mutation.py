from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        genes = ["A", "C", "G", "T"]

        queue = deque([startGene])
        visited = set([startGene])
        dist = {startGene: 0}

        while queue:
            curr_gene = queue.popleft()

            if curr_gene == endGene:
                return dist[curr_gene]
            
            for i in range(len(curr_gene)):
                for g in genes:
                    if curr_gene[i] != g:
                        new_gene = curr_gene[:i] + g + curr_gene[i+1:]

                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append(new_gene)
                            dist[new_gene] = dist[curr_gene] + 1

        return -1

        def bfs(start_node, graph):
            queue = deque([start_node])
            visited = set([start_node])

            while queue:
                curr_node = queue.popleft()

                for next_node in graph[curr_node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)
            return -1
