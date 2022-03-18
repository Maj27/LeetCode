class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        filteredList = []
        for restaurant in restaurants:
            idi, ratingi, veganFriendlyi, pricei, distancei = restaurant
            if pricei<=maxPrice and distancei<=maxDistance:
                if (not veganFriendly) or (veganFriendly and veganFriendlyi):
                    filteredList.append(restaurant)
                    
        filteredList.sort(key=lambda x:(x[1], x[0]), reverse= True)
        
        res = [i[0] for i in filteredList]
        return res