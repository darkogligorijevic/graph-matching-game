# Graph Matching Game

## Description
This project is a simple game that allows users to generate random 3D graphs and attempt to match them by manipulating a second graph. It is implemented using Python with PyQt5 for the GUI and OpenGL for rendering the 3D graphics. The main goal of this project is to help other students who have hard time with 3D graphs.

## Features
- Generate random 3D graphs with angles.
  ```python
  
  # angles in easy version [-360, -180, -90, 0, 90, 180, 360]
  def generate_random_angles(self):
    self.x_angle = random.choice([-360, -180, -90, 0, 90, 180, 360])
    self.y_angle = random.choice([-360, -180, -90, 0, 90, 180, 360])
    self.z_angle = random.choice([-360, -180, -90, 0, 90, 180, 360])
    self.update()
  
  # angles in hard version [-360, -180, -90, -60, -45, -30, 0, 30, 45, 60, 90, 180, 360]
  def generate_random_angles(self):
    self.x_angle = random.choice([-360, -180, -90, -60, -45, -30, 0, 30, 45, 60, 90, 180, 360])
    self.y_angle = random.choice([-360, -180, -90, -60, -45, -30, 0, 30, 45, 60, 90, 180, 360])
    self.z_angle = random.choice([-360, -180, -90, -60, -45, -30, 0, 30, 45, 60, 90, 180, 360])
    self.update()
  
  ```
- Manipulate a second graph to match the generated random graph.
- Graphical representation of 3D axes (X, Y, Z).
- Check if the two graphs match.

## Requirements
- Python 3.x
- PyQt5
- PyOpenGL

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/darkogligorijevic/graph-matching-game.git
   ```
2. Install the required dependencies:
   ```bash
   pip install PyQt5 PyOpenGL
   ```

## Usage
### If you want to explore more with python code:
1. Run the scripts (easy.py and hard.py):
   ```bash
   py easy.py
   py hard.py
   ```
2. Use the "Generate Random Graph" button to generate a random 3D graph.
3. Manipulate the second graph to match the generated graph.
4. Have fun while learning!

### If you want to run it rigt away:
1. **Download:** Clone the repository or download the `.zip` file.
2. **Extract Files:** If you downloaded the `.zip` file, extract its contents to a location of your choice.
3. **Run the Executable:**
    - Double-click on the `easy.exe` or `hard.exe` file.


## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/darkogligorijevic/graph-matching-game/blob/master/LICENSE) file for details.
