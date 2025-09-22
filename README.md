# Pac-Man-Game
# Pacman Console Game 🎮  

A fun **Pacman-inspired terminal game** built with Python and ASCII art. Pacman must move around the grid, eat pills, and avoid ghosts.  

---

## 🚀 Features  

- **Pacman Movement**:  
  Control Pacman using **W (up), A (left), S (down), D (right)**.  

- **Ghost AI**:  
  Ghosts move randomly around the board but avoid walls and overlapping.  

- **Win & Lose Conditions**:  
  - **Win**: Collect almost all pills (≤2 left).  
  - **Lose**: If a ghost catches Pacman.  

- **Colored ASCII UI** (via `termcolor`):  
  - Blue walls  
  - Yellow Pacman  
  - Red ghosts  
  - Grey pills  

- **Dynamic Board Rendering**:  
  The board updates in real-time with each move.  

---

## 🔧 Fixes Made  

1. **Movement Boundaries Fixed**  
   - Prevented ghosts and Pacman from moving outside the board.  

2. **Ghost Overlap Prevention**  
   - Ghosts no longer overlap each other or replace pills incorrectly.  

3. **Win/Lose Logic Fixed**  
   - Corrected pill count detection and fixed swapped win/lose messages.  

---

## 🎮 How to Play 

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   
2. Install dependencies:
   ```bash
   pip install termcolor

3. Run the game:
   ```bash
   python game.py

4. Controls:
  - W → Move up
  - A → Move left
  - S → Move down
  - D → Move right

🏆 Winning & Losing
  - Win → Eat almost all pills.
  - Lose → Get caught by a ghost.

