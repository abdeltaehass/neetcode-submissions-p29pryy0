from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}  # userId -> list of (time, tweetId)
        self.following = {}  # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following.get(userId, set()) | {userId}
        
        for u in users:
            if u in self.tweets and self.tweets[u]:
                time, tweetId = self.tweets[u][-1]
                idx = len(self.tweets[u]) - 1
                heapq.heappush(heap, (-time, tweetId, u, idx - 1))
        
        res = []
        while heap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                t, tid = self.tweets[u][idx]
                heapq.heappush(heap, (-t, tid, u, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)