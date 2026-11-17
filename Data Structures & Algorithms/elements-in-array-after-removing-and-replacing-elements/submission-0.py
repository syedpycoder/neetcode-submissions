class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        num_dict = {}
        n = len(nums)
        prefix = 2 * n
        result = []

        for i in range(n):
            num_dict[i] = nums[i:]
        
        for j in range(n, 2*n):
            if j > n:
                mod_j = j % n
                num_dict[j] = nums[:mod_j]
            else:
                num_dict[j] = nums[j:]    


        for query in queries:
            time, indexQuery = query

            modResult = time % prefix 

            if modResult == n:
                result.append(-1)
            else:
                Arr_at_time = num_dict[modResult]
                val = Arr_at_time[indexQuery]
                result.append(val)

        return result               
        

       



       
            

            






