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

        print(num_dict)
        for query in queries:
            time, indexQuery = query
            modResult = time % prefix 
            print(f'{modResult} for {time}')
            Arr_at_time = num_dict[modResult]
            if Arr_at_time:
                result.append(Arr_at_time[indexQuery])
            else:
                result.append(-1)    

        return result               
        

       



       
            

            






