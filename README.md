# Hangman-Game
A fun and interactive Hangman game where users can either choose their own word or let the computer select a random word. The game checks if user-provided words are valid by searching online dictionaries, and the computer can generate words based on specified lengths or randomly. The executable file is included for easy play!
---

- [How It Works](#how-it-works)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## How It Works
- **Word Validation**: For user-provided words, the game checks online dictionaries to ensure the word is valid.
- **Word Generation**: For computer-chosen words, the game selects a word from an online library based on the specified criteria (length or random).
- **Game Logic**: The game tracks guessed letters, remaining attempts, and updates the display accordingly.

---

## Features
- **User-Chosen Words**: Players can input their own word, and the game will verify its validity using online dictionaries.
- **Computer-Chosen Words**: The computer can generate a random word, either with a specified number of letters or completely random.
- **Interactive Gameplay**: Classic Hangman gameplay with a user-friendly interface.
- **Executable File**: An `.exe` file is included for easy installation and play on Windows.

---
## Installation
To play the Hangman game, follow these steps:

1. **Download the Repository**:
   - Clone the repository:
     ```bash
     git clone https://github.com/your-username/hangman-game.git
     ```
   - Or download the ZIP file and extract it.

2. **Run the Game**:
   - Navigate to the project directory:
     ```bash
     cd hangman-game
     ```
   - Run the executable file:
     - Double-click the `hangman.exe` file (for Windows users).

3. **Optional: Run from Source Code**:
   - Ensure you have Python installed (if running from source).
   - Install dependencies (if any):
     ```bash
     pip install -r requirements.txt
     ```
   - Run the game:
     ```bash
     python hangman main.py
     ```

---

## Usage
1. **Launch the Game**:
   - Run the `hangman.exe` file or the Python script.

2. **Choose a Word**:
   - Select whether you want to input your own word or let the computer choose one.
   - If you choose your own word, the game will verify it using online dictionaries.
   - If the computer chooses, you can specify the number of letters or let it pick randomly.

3. **Play Hangman**:
   - Guess letters one at a time to reveal the hidden word.
   - You have a limited number of attempts before the hangman is fully drawn.

4. **Win or Lose**:
   - Guess the word correctly to win!
   - If you run out of attempts, the game will reveal the word, and you can try again.

---

## Contributing
Contributions are welcome! If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name

---
## Acknowledgements
- [Python](https://www.python.org) - The programming language used.

- [Online Dictionaries](https://www.merriam-webster.com) - For validating user-provided words.

- Random Word Libraries - For generating computer-chosen words
