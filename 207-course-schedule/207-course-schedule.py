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
        
            coverAll = True
            for prereq in prereqs:
                coverAll = coverAll and dfs(prereq)
            if coverAll:
                taken.add(course)
            return coverAll
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True