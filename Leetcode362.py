

from collections import deque
from typing import Deque, Tuple

class HitCounter:
    def __init__(self):
        # q holds (timestamp, count) buckets; at most ~300 buckets (one per second)
        self.q: Deque[Tuple[int, int]] = deque()
        self.total: int = 0  # running sum of counts within the 300s window

    def hit(self, timestamp: int) -> None:
        """
        Record a hit at `timestamp`.
        Evict outdated buckets here to keep space bounded (≤ 300 buckets).
        """
        border = timestamp - 300
        # Remove buckets that are at or before the border: (t-300, t] window only
        while self.q and self.q[0][0] <= border:
            _, cnt = self.q.popleft()
            self.total -= cnt

        # Same-second merge to keep q compact (one bucket per second)
        if self.q and self.q[-1][0] == timestamp:
            ts, cnt = self.q[-1]
            self.q[-1] = (ts, cnt + 1)
        else:
            self.q.append((timestamp, 1))

        self.total += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the last 300 seconds ending at `timestamp`.
        Also evict here to handle time jumps with no intervening hits.
        """
        border = timestamp - 300
        while self.q and self.q[0][0] <= border:
            _, cnt = self.q.popleft()
            self.total -= cnt

        return self.total
