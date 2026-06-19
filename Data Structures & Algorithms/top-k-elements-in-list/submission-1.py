class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        output = []

        for number in nums:
            if number not in num_dict:
                num_dict[number] = 1
                continue
            
            num_dict[number] += 1


        sorted_items = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        count = 0
        for key, values in sorted_items:
            output.append(key)
            count += 1
            if count == k:
                break


        return output