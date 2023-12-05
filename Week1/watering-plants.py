class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        real_capacity = capacity
        for i, plant in enumerate(plants):
            # steps+=1
            if capacity<plant:
                capacity = real_capacity
                steps= steps+(2*(i))
            steps+=1
            capacity -= plant
        return steps