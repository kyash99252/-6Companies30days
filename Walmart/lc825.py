class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        ages.sort()
        total_requests = 0
        
        for idx, person_age in enumerate(ages):
            if person_age < 15:
                continue
            lower_bound = self.getLowerBound(idx, ages)
            if lower_bound >= 0:
                upper_bound = self.getUpperBound(idx, ages)
                total_requests += (upper_bound - lower_bound)
        
        return total_requests
    
    def getLowerBound(self, current_index, sorted_ages):
        left = 0
        right = current_index
        min_acceptable_age = 0.5 * sorted_ages[current_index] + 7
        
        while left < right:
            middle = (left + right) // 2
            if sorted_ages[middle] <= min_acceptable_age:
                left = middle + 1
            else:
                right = middle
        
        return left

    def getUpperBound(self, current_index, sorted_ages):
        left = current_index
        right = len(sorted_ages) - 1
        max_acceptable_age = sorted_ages[current_index]
        
        while left < right:
            middle = (left + right + 1) // 2
            if sorted_ages[middle] > max_acceptable_age:
                right = middle - 1
            else:
                left = middle
        
        return right