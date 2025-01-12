class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize variables
        freq_map = {}  # Dictionary to store the frequency of each character in the current window
        most_freq_char = 0  # Tracks the count of the most frequent character in the current window
        max_len = 0  # Maximum length of the substring that can be formed
        l = 0  # Left pointer of the sliding window

        # Iterate over the string with the right pointer 'r'
        for r in range(len(s)):
            right_char = s[r]
            # Add the current character to the frequency map
            freq_map[right_char] = 1 + freq_map.get(right_char, 0)
            # Update the count of the most frequent character in the window
            most_freq_char = max(most_freq_char, freq_map[right_char])

            # Shrink the window if the remaining characters (non-most frequent ones) 
            # exceed the number of replacements allowed
            while r - l + 1 - most_freq_char > k:
                left_char = s[l]
                # Decrease the frequency of the left character as it exits the window
                freq_map[left_char] -= 1
                # Remove the character from the frequency map if its count is zero
                if freq_map[left_char] == 0:
                    del freq_map[left_char]
                # Move the left pointer to the right
                l += 1

            # Update the maximum length of the valid substring
            max_len = max(max_len, r - l + 1)

        return max_len  # Return the maximum length of the substring that can be formed

# Space Complexity:
# The space complexity = O(1), as the dictionary `freq_map` stores at most 26 entries 
# (one for each letter of the English alphabet).

# Time Complexity:
# The time complexity is O(n), where `n` is the length of the string. 
# Both the left and right pointers traverse the string once, making the sliding window approach linear.
