#!/usr/bin/env node
// 841. Keys and Rooms

// There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room 
// without having its key.
// When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you 
// to unlock the other rooms.

// Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

// Input: rooms = [[1],[2],[3],[]]
// Output: true
// Explanation: 
// We visit room 0 and pick up key 1.
// We then visit room 1 and pick up key 2.
// We then visit room 2 and pick up key 3.
// We then visit room 3.
// Since we were able to visit every room, we return true.

// Input: rooms = [[1,3],[3,0,1],[2],[0]]
// Output: false
// Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

/** 
* @param {number[][]} rooms
* @return {boolean} 
*/

//  rooms are like nodes and keys are like edges
function canVisitAllRooms(rooms) {
    const visitedRooms = new Set(); // Set to keep track of visited rooms

    // Define a DFS (Depth-First Search) function to visit rooms
    function exploreRoom(roomIndex) {
        // If the room has already been visited, exit
        if (visitedRooms.has(roomIndex)) return;

        // Mark the current room as visited
        visitedRooms.add(roomIndex);

        // Explore all the keys in the current room
        for (const key of rooms[roomIndex]) {
            exploreRoom(key); // Recursively explore the room corresponding to the key
        }
    }

    // Start DFS from room 0
    exploreRoom(0);

    // Check if all rooms have been visited
    return visitedRooms.size === rooms.length;
}


// example usage
let rooms = [[1],[2],[3],[]];
let rooms2 = [[1,3],[3,0,1],[2],[0]]
console.log(canVisitAllRooms(rooms))
console.log(canVisitAllRooms(rooms2))


// My Note

// In Python, the equivalent loop structure to for (variable of iterable) { statement } in JavaScript is the for loop with the in keyword.
// The has() method of Set instances returns a boolean indicating whether an element with the specified value exists in this set or not
// add() function in JavaScript is used to insert an element in the set.