class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseFlow = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            courseFlow[crs].append(pre)
            
        taken = set() 
        visited = set()
        def dfs(course):
            if course in taken:
                return True
            if course in visited:
                return False
            visited.add(course)
            prereqs = courseFlow[course]
        
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            
            taken.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True