# Solar System Simulation

This is a simple Solar System simulation using Pygame. The simulation represents the Sun and planets orbiting around it with realistic speeds and distances. Stars are also randomly placed in the background to enhance the visual effect.

## Features
- Simulates the Sun and eight planets with different sizes and colors.
- Each planet orbits around the Sun at its respective speed.
- Saturn has a simple ring effect.
- Randomly generated stars for a more realistic space environment.

## Requirements
Make sure you have Python and Pygame installed before running the script.

### Installation
1. Install Python (if not installed already): [Download Python](https://www.python.org/downloads/)
2. Install Pygame using pip:
   ```sh
   pip install pygame
   ```

## How to Run
1. Download or clone the repository.
2. Navigate to the directory containing the script.
3. Run the script using:
   ```sh
   python solar_system.py
   ```

## Code Overview
- The `Planet` class defines the properties and movement of each planet.
- The `draw_orbit` function renders the planetary orbits.
- The `main` function initializes the planets, Sun, and background stars, then runs the simulation loop.
- The simulation runs until the user closes the window.

## Controls
- Close the window to exit the simulation.

## Future Improvements
- Add 3D rendering for a more immersive experience.
- Implement zoom and rotation controls.
- Improve the planet textures and animations.

## Author
This project was created for educational and visualization purposes using Pygame.

## License
This project is open-source and can be modified or distributed freely.