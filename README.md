# 🪨 Asteroids Game

A classic Asteroids game built using Python and Pygame.


![asteroids](https://github.com/user-attachments/assets/c809f4a6-382f-41ec-8df0-37bea9ba19a6)


## 🚀 Features

- **Smooth Gameplay:** Navigate and destroy asteroids with a responsive spaceship.

- **Asteroid Splitting:** Large asteroids break into smaller ones upon impact.

- **Explosions:** Animated explosion effects when asteroids are destroyed.

- **Shooting Mechanism:** Fire projectiles to destroy asteroids.

- **Randomized Asteroid Spawning:** New asteroids appear dynamically at screen edges.

- **Collision Detection:** Player and bullet collisions trigger game events.


## 🎮 Controls

- **Left Arrow (←):** Rotate left

- **Right Arrow (→):** Rotate right

- **Up Arrow (↑):** Move forward

- **Down Arrow (↓):** Move backward

- **Spacebar:** Fire projectiles


## 🛠️ Installation

1. Clone the Repository
```
git clone https://github.com/yourusername/asteroids-game.git
cd asteroids-game
```

2. Create a Virtual Environment (Optional but Recommended)
```
python -m venv /path/to/new/virtual/environment
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Run the Game

```
python main.py
```

## 📂 Project Structure
```
📦 asteroids-game
├── 📂 images                # Game assets (asteroids, spaceship, explosions, background)
├── 📜 asteroid.py           # Asteroid class (movement, splitting, rendering)
├── 📜 asteroidfield.py      # Handles spawning and managing asteroids
├── 📜 circleshape.py        # Base class for circular game objects
├── 📜 constants.py          # Game settings and constants
├── 📜 explosion.py          # Explosion animation handler
├── 📜 main.py               # Main game loop and initialization
├── 📜 player.py             # Player spaceship class (movement, shooting, collisions)
├── 📜 shot.py               # Projectile handling
├── 📜 .gitignore            # Ignored files/folders (venv, __pycache__)
└── 📜 README.md             # Project documentation
```

## 🔧 To-Do Features

[ ] **Power-ups:** Introduce shields, speed boosts, and extra lives.

[ ] **Multiplayer Mode:** Allow multiple players to compete or cooperate.

[ ] **Leaderboards:** Track high scores and display rankings.

[ ] **More Enemy Types:** Introduce alien ships and different asteroid behaviors.

[ ] **Sound Effects & Music:** Add immersive background music and explosion sounds.

[ ] **Customizable Spaceship:** Allow players to choose or upgrade their spaceship.


## 🤝 Contributing

Contributions are welcome! If you find a bug or have an improvement, feel free to open an issue or submit a pull request.


## 📜 License

This project is licensed under the MIT License.


## Enjoy blasting asteroids! 🚀
