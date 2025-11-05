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
