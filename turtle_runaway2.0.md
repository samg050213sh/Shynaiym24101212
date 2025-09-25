# Turtle Runaway Game


## Game Description
A Python game where the player controls a red turtle (arrow keys/WASD) to catch a blue turtle with AI. Game duration: 60 seconds.

## Implemented Features & Improvements

### 1. Intelligent AI for Blue Turtle
- Escape mode: Accelerates when player approaches
- Smart behavior: Runs in opposite direction from chaser
- Random movement: Moves unpredictably when player is far away

### 2. Enhanced Collision System
- Teleportation: Both turtles move to random positions after catch
- Anti-instant-catch: Prevents immediate re-catch after teleportation
- Score system: +10 points per catch with counter display

### 3. Smooth Visual Interface
- Stable text display: No flickering with optimized drawing
- Game timer: Countdown display with final score

### 4. Game Balance
- Red turtle: Speed 15, turn rate 15
- Blue turtle: Speed 12, turn rate 10 (+5 when escaping)
- Catch radius: 50 pixels

## Controls
 - Arrow Keys or WASD: Move red turtle
 - Objective: Catch blue turtle as many times as possible in 60 seconds

## Image
![Screenshot](<img width="809" height="688" alt="turtle_runaway2 0" src="https://github.com/user-attachments/assets/bc6a62f5-3bc4-488b-a253-e5b761a71aa3" />
) 
 
## How to Run
```bash

!python turtle2.0.py


