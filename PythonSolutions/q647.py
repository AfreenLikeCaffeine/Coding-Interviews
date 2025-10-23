# Palindromic Substrings - Leetcode 647

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Returns the number of palindromic substrings in s.

        A palindromic substring is a contiguous sequence of characters within s that reads the same backwards as forwards.

        The count includes single-character substrings, which are trivially palindromic.

        :param s: The string to search for palindromic substrings.
        :return: The number of palindromic substrings in s.
        """
        count = 0
        for i in range(len(s)):
            # odd length substrings
            l, r = i - 1, i + 1
            count += 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # increment count for each palindromic substring
                count += 1
                # move pointers outwards
                l -= 1
                r += 1
            
            # even length substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # increment count for each palindromic substring
                count += 1
                # move pointers outwards
                l -= 1
                r += 1
        return count

        # Time complexity: O(n^2)
        # Space complexity: O(1)