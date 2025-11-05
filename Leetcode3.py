"""

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

def lengthOfLongestSubstring(s: str) -> int:
    last = {}        # 문자 -> 마지막 인덱스
    left = 0         # 현재 윈도우의 왼쪽 경계
    best = 0

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            # 중복 발견: 윈도우 왼쪽을 (중복문자의 다음)으로 이동
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)

    return best
