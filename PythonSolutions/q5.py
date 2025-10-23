# Longest Palindromic Substring - Leetcode 5

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Return the longest palindromic substring in s.

        The function uses two pointers to expand around the center of the palindrome.
        It checks for odd length and even length palindromes.
        """
        resLen = 0
        res = ""

        for i in range(len(s)):
            # Check for odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the length of the palindrome is greater than the current result length
                if((r-l+1)>resLen):
                    # Update the result length and the result string
                    resLen = r-l+1
                    res = s[l:r+1]
                # Move the pointers outwards
                l-=1
                r+=1

            # Check for even length palindrome
            l, r = i, i+1
            while l>=0 and r <len(s) and s[l] == s[r]:
                # If the length of the palindrome is greater than the current result length
                if((r-l+1) >resLen):
                    # Update the result length and the result string
                    resLen = r-l+1
                    res = s[l:r+1]
                # Move the pointers outwards
                r+=1
                l-=1
        return res

        # Time complexity: O(n^2)
        # Space complexity: O(1)        