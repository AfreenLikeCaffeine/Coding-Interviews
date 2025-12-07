class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Returns True if the string s can be segmented into words in the word dictionary wordDict, False otherwise.

        The function uses dynamic programming to solve the problem. It creates a boolean array dp of size len(s) + 1, where dp[i] is True if the string s can be segmented into words in the word dictionary from index 0 to i. It then iterates over the string s from right to left and for each index i, it checks all the words in the word dictionary that end at index i. If the word is in the word dictionary and dp[i + len(word)] is True, then dp[i] is set to True. Finally, it returns dp[0].

        :param s: The string to be segmented.
        :type s: str
        :param wordDict: The word dictionary.
        :type wordDict: List[str]
        :return: True if the string s can be segmented into words in the word dictionary wordDict, False otherwise.
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:len(w) + i] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

# Time complexity: O(n * m * k), where n = len(s), m = len(wordDict), k = average length of words in wordDict
# Space complexity: O(n)