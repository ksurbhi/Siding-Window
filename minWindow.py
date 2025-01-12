class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if `t` is longer than `s` or `t` is empty, return an empty string
        if len(t) > len(s) or t == '':
            return ''
        
        # Create frequency maps for the target string `t` and the current window in `s`
        countT, window = {}, {}
        
        # Populate the frequency map for `t`
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # Variables to track progress
        have, need = 0, len(countT)  # `need` is the number of unique characters in `t`
        res, resL = [-1, -1], float('infinity')  # Store the result window and its length
        i = 0  # Left pointer of the sliding window

        # Iterate over `s` with the right pointer `j`
        for j in range(len(s)):
            r = s[j]
            # Add the current character to the window frequency map
            window[r] = 1 + window.get(r, 0)
            
            # If the character matches the required frequency in `t`, increment `have`
            if r in countT and window[r] == countT[r]:
                have += 1

            # Try to shrink the window while all characters in `t` are satisfied
            while need == have:
                # Update the result if the current window is smaller than the previous result
                if j - i + 1 < resL:
                    res = [i, j]
                    resL = j - i + 1
                
                # Shrink the window from the left
                l = s[i]
                window[l] -= 1
                # If removing this character causes the window to no longer satisfy `t`
                if l in countT and window[l] < countT[l]:
                    have -= 1
                i += 1  # Move the left pointer forward
        
        # Extract the result substring using the `res` indices
        i, j = res
        return s[i:j+1] if resL != float('infinity') else ''

# Space Complexity:
# - The space complexity = O(1) for the `window` and `countT` dictionaries, 
#   as they store character frequencies and there are at most 26 characters in the English alphabet.

# Time Complexity:
# - The time complexity is O(n), where `n` is the length of the string `s`. 
#   Both pointers (`i` and `j`) traverse the string once, resulting in a linear runtime.
