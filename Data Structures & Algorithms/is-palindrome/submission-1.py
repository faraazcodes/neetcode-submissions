class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        lowercase = s.lower()

        while left < right:
            if not lowercase[left].isalnum():
                left += 1
                continue

            if not lowercase[right].isalnum():
                right -= 1
                continue

            if lowercase[left] != lowercase[right]:
                return False

            left = left + 1
            right = right - 1

        
        return True