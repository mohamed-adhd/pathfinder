# Pathfinding Visualizer (BFS & DFS)

> Interactive pathfinding visualizer built with Python and Pygame, demonstrating Breadth-First Search and Depth-First Search in a grid-based environment.

---

##  Overview :D

This project is an interactive visualization tool simulating the steps of search algorithms bfs and dfs.
a user can customize its own grid environments, place start/end points, draw obstacles and watch how algorithms explore and find paths in real time.

It also provides step-by-step insight into how both of the search algorithms behave, including time taken , explored nodes, frontier expansion, and final path construction.

---

##  Features

* 🧱 Interactive grid system
* 🎯 Custom start and end node placement
* 🚧 Dynamic wall creation (click & drag)
* 🔍 Real-time visualization of:

        * Breadth-First Search (BFS)
        * Depth-First Search (DFS)
* 📊 Performance metrics:

        * Nodes explored(amount of cells checked)
        * Execution time(seconds taken from start to finish of search)
        * Path length
* Color-coded algorithm states! :

        * Visited nodes(gray blue)
        * Frontier(light blue)
        * Current node((dark blue)
        * Final path(yellow)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Library:** Pygame
* **Core Concepts:**

  * Graph traversal algorithms
  * Queue (BFS)
  * Stack (DFS)
  * Grid-based pathfinding

---

## :p Installation:

```bash
git clone https://github.com/midou5098/pathfinder.git
cd pathfinder
pip install pygame
```

---

##  Usage >_<:

Run the application:

```bash
python main.py
```

---

## 🎮 Controls

| Action | Description                            |
| ------ | -------------------------------------- |
| walls  | Draw or erase walls (left/right click) |
| start  | Place starting node                    |
| end    | Place target node                      |
| bfs    | Start Breadth-First Search             |
| dfs    | Start Depth-First Search               |
| clear  | Reset the grid                         |

🖱️ You can also click and drag to draw walls continuously.

---

## 🎨 Visualization Legend

| Color         | Meaning                 |
| ------------- | ----------------------- |
| ⚪ White       | Empty cell              |
| ⬛ Black       | Wall                    |
| 🟢 Green      | Start node              |
| 🔴 Red        | End node                |
| 🔵 Blue       | Currently explored node |
| 🔷 Light Blue | Visited nodes           |
| 🟡 Yellow     | Final path              |

---

## 📊 Algorithm Details

### Breadth-First Search (BFS)

* Guarantees shortest path in an unweighted grid
* Uses a queue (FIFO)
* Explores level by level

### Depth-First Search (DFS)

* Does not guarantee shortest path
* Uses a stack (LIFO)
* Explores as deep as possible before backtracking

---

## 📁 Project Structure

```
project/
├── main.py          # Main visualization loop and UI
├── source2.py       # BFS, DFS, and Button logic
├── font.ttf         # Custom font (optional)
├── README.md
```

---

## 📸 Demo
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/2571a2ad-31d8-4845-b0ee-794d9be994fd" />
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/06d9ae5b-9cd5-47c2-ba42-d605f91ea3aa" />
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/24291a9f-13d0-49d9-b118-82db15e387e6" />
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/a03673a3-6c5b-4368-9bec-9684ae04f2da" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6c6b9097-a8de-41dd-aab6-d3fda483f5af" />







---

## 🎯 Purpose

my goal in 3rd year of uni is being accepted in ai engeneering , 
so i wanted to start learning ai basics asap ,
took the bfs and dfs concepts from cs50ai and then made a project out of it .

---

## 🧠 What I Learned

i already knew the defenitions of dfs and bfs 
, but this project helped me understand more abt step-by-step machines 
, using the yield and swithcing from a default dfs algorithm to a visualisation friendly one.

---

## 🚧 Status

* Core visualization: implemented
* BFS implementation: implemented 
* DFS implementation: implemented
* UI interaction: polished enough
* Additional algorithms: ⏳ may comback later to add the A* search or dijkstra , as i already find dem interesting.


---


## 📄 License

aint got no liscence ngl
