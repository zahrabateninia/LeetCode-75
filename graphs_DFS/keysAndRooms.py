#!/usr/bin/env python3

def canVisitAllRooms(rooms) -> bool:
    visited = set()
    def dfs(roomIdx) -> None:
        if roomIdx not in visited:
            visited.add(roomIdx)
            for key in rooms[roomIdx]:
                dfs(key)
    dfs(0) # the room at index 0 is always open
    return len(visited) == len(rooms)

# example usage
rooms = [[1],[2],[3],[]]
print(canVisitAllRooms(rooms))

