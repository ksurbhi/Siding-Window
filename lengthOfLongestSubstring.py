class Solution:
    # Time and Space Complexity: O(n), O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        i= 0
        j = 0
        max_len = 0
        freq_dict = {}
        for j in range(len(s)):
            r_char = s[j]
            if r_char not in freq_dict:
                freq_dict[r_char] = 0
                freq_dict[r_char] = 0
            freq_dict[r_char] += 1

            while j-i+1 > len(freq_dict):
                l_char = s[i]
                freq_dict[l_char] -= 1
                if freq_dict[l_char] == 0:
                    del freq_dict[l_char]
                i +=1
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len
