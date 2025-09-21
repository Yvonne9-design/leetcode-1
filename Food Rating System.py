Food Rating System 
import heapq

class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_ratings = {}
        
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            
            if cuisine not in self.cuisine_ratings:
                self.cuisine_ratings[cuisine] = []
            
            # Python's heapq is a min-heap. We store negative ratings to simulate a max-heap.
            
            heapq.heappush(self.cuisine_ratings[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food] 
        heapq.heappush(self.cuisine_ratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the max-heap for the given cuisine
        heap = self.cuisine_ratings[cuisine]
        
                   
        while heap[0][0] != -self.food_to_rating[heap[0][1]]:
            heapq.heappop(heap)
            
        return heap[0][1]