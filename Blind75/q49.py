# Group Anagrams - LeetCode 49

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        This function groups a list of strings based on their anagrams.

        The function takes a list of strings as input and returns a list of lists of strings, where each sublist contains strings that are anagrams of each other.

        The function uses a defaultdict to store the strings in the list, with the key being the count of characters in the string and the value being a list of strings.

        The function then iterates over the list of strings and for each string, it counts the characters in the string and adds the string to the list of strings in the defaultdict with the corresponding key.

        Finally, the function returns a list of lists of strings, where each sublist contains strings that are anagrams of each other.

        :param strs: A list of strings.
        :type strs: List[str]
        :return: A list of lists of strings, where each sublist contains strings that are anagrams of each other.
        :rtype: List[List[str]]
        """

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            # Count the characters in the string
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

# Time complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
# Space complexity: O(n * k) where n is the number of strings and k is the maximum length of a string


if __name__ == "__main__":
    from q49_test import run_tests
    run_tests()