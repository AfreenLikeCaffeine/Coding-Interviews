# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        """
        This function checks if a given string has valid parentheses.

        A valid string has the following properties:
        - All parentheses are closed (i.e., every opening parenthesis has a corresponding closing parenthesis)
        - All parentheses are properly nested (i.e., every opening parenthesis is closed before the next opening parenthesis is closed)

        :param s: The string to check for validity
        :return: True if the string is valid, False otherwise
        """
        stack = []
        parans = {
            ')': '(',
            ']': '[',
            '}':'{'
        }
        for char in s:
            # If it is an opening brace then append it to the stack
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            # Has one type of closing brace
            elif char in '}])':
                # If the stack is empty then there is no corresponding opening brace
                if len(stack) == 0:
                    return False
                # If the top of the stack does not match the current closing brace then the string is invalid
                elif stack[-1] != parans[char]:
                    return False
                # If the top of the stack matches the current closing brace then pop the opening brace from the stack
                else:
                    stack.pop()
        # The whole stack got popped which means the parentheses are valid
        if len(stack) == 0:
            return True
        # There are still some parentheses remaining in the stack
        return False

# Space Complexity: O(n)
# Time Complexity: O(n)            
        