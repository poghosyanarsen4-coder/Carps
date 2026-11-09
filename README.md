# Carps
Object-Oriented Python implementation of the classic Craps dice game with console output.


# Craps Dice Game (OOP Python Implementation)

A Python implementation of the classic casino game **Craps**, built using Object-Oriented Programming (OOP) principles and the standard `random` library.

---

## Game Rules

1. **First Roll (Come-Out Roll):**
   - **Instant Win:** If the sum of the two dice is **7** or **11**, the player wins immediately.
   - **Instant Loss (Craps):** If the sum of the two dice is **2**, **3**, or **12**, the casino wins immediately.
   - **Goal Established:** If the sum is **4, 5, 6, 8, 9, or 10**, that total becomes the player's **"Goal"** number.

2. **Subsequent Rolls:**
   - The player continues rolling the two dice until one of two events occurs:
     - **Player Wins:** The player rolls the **Goal** number again.
     - **Casino Wins:** The player rolls a **7** before hitting their Goal number.

---

## Features & Requirements

- Built entirely in **Python**.
- Uses Python's standard `random` library for die rolls.
- Implemented using **Object-Oriented Programming (OOP)** (`CrapsGame` class).
- Utilizes `while` loops, conditional structures (`if`/`elif`/`else`), custom methods, and formatted console outputs.

---

## Code Structure

- `CrapsGame`: The main class managing game state and logic.
  - `__init__()`: Initializes the game attributes (e.g., `self.goal`).
  - `roll_dice()`: Generates two random integers between 1 and 6, prints individual dice values and their sum, and returns the total.
  - `play()`: Handles the game sequence, initial roll outcomes, and the game loop for goal chasing.

---

## How to Run

### Prerequisites
- Python 3.x installed on your machine. No external dependencies are required.

### Execution

1. Clone or download this repository.
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the script:

```bash
python main.py
=======
# Carps
Object-Oriented Python implementation of the classic Craps dice game with console output.
>>>>>>> db682f60768d568b04571e0edfe9c77683c11bb0
