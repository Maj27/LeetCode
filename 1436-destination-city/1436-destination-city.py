class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        for path in paths:
            source.add(path[0])
        
        for path in paths:
            if path[1] not in source:
                return path[1]
            
            
                