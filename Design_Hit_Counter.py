# https://leetcode.com/problems/design-hit-counter/


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        [0,1] = [freq, timestamp]
        """
        self.storage = [[0, i+1] for i in range(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = int((timestamp-1)%300)

        if self.storage[idx][1] == timestamp:
            self.storage[idx][0] += 1
        else:
            self.storage[idx][0] = 1
            self.storage[idx][1] = timestamp

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0

        for element in self.storage:
            freq, time = element[0], element[1]
            if timestamp - time < 300:
                count += freq

        return count


if __name__ == "__main__":
    # Your HitCounter object will be instantiated and called as such:
    obj = HitCounter()
    obj.hit(timestamp=1)
    obj.hit(timestamp=3)
    obj.hit(timestamp=4)
    obj.hit(timestamp=300)
    obj.hit(timestamp=301)

    count = obj.getHits(timestamp=300)
    print(f'count at 300 {count}')
    count = obj.getHits(timestamp=301)
    print(f'count at 301 {count}')