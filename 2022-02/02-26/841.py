from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        room_set = set([0])
        while room_set:
            next_set = set()
            for r in room_set:
                for next_r in rooms[r]:
                    if next_r not in visited:
                        visited.add(next_r)
                        next_set.add(next_r)
            room_set = next_set
        return len(visited) == len(rooms)


if __name__ == "__main__":
    sol = Solution()
    # rooms = [[1],[2],[3],[]]
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(sol.canVisitAllRooms(rooms))

