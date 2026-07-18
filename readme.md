<div align="center">

  <h1>Pathfinder Visualizer</h1>

  <p>
    <b>A Python/Pygame grid visualizer for watching BFS and DFS search through walls, frontiers, visited cells, and final paths.</b>
  </p>

  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="Pygame" src="https://img.shields.io/badge/Pygame-0E7A3E?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="BFS" src="https://img.shields.io/badge/BFS-00C2A8?style=for-the-badge" />
    <img alt="DFS" src="https://img.shields.io/badge/DFS-7C3AED?style=for-the-badge" />
    <img alt="Grid Search" src="https://img.shields.io/badge/Grid_Search-FFB703?style=for-the-badge" />
  </p>

  <p>
    <a href="#features">
      <img alt="Features" src="https://img.shields.io/badge/Features-00C2A8?style=for-the-badge" />
    </a>
    <a href="#demo-video">
      <img alt="Demo video" src="https://img.shields.io/badge/Demo_Video-FF3864?style=for-the-badge" />
    </a>
    <a href="#controls">
      <img alt="Controls" src="https://img.shields.io/badge/Controls-F59E0B?style=for-the-badge" />
    </a>
    <a href="#how-it-works">
      <img alt="How it works" src="https://img.shields.io/badge/How_It_Works-2563EB?style=for-the-badge" />
    </a>
  </p>

</div>

---

## Overview

**Pathfinder Visualizer** is an interactive grid search simulator built with Python and Pygame. You draw walls, place a start node, place an end node, then run either BFS or DFS and watch the algorithm explore the grid step by step.

The visualizer uses generator-based search functions, so the algorithm does not just compute the answer instantly. It yields intermediate states that the Pygame loop can render: active node, frontier, visited cells, final path, elapsed time, and explored node count.

## Demo Video


```md
when i find some time :p
```

## Preview Space

<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/2571a2ad-31d8-4845-b0ee-794d9be994fd" />
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/06d9ae5b-9cd5-47c2-ba42-d605f91ea3aa" />
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/24291a9f-13d0-49d9-b118-82db15e387e6" />
<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/a03673a3-6c5b-4368-9bec-9684ae04f2da" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6c6b9097-a8de-41dd-aab6-d3fda483f5af" />

## Features

<table>
  <tr>
    <td><b>Interactive grid</b></td>
    <td>Uses a <code>9x24</code> grid with <code>40px</code> cells.</td>
  </tr>
  <tr>
    <td><b>Wall editing</b></td>
    <td>Click and drag to add walls; right-click and drag to remove them.</td>
  </tr>
  <tr>
    <td><b>Start/end placement</b></td>
    <td>Move the start and destination cells from the toolbar.</td>
  </tr>
  <tr>
    <td><b>BFS mode</b></td>
    <td>Visualizes breadth-first search with a queue.</td>
  </tr>
  <tr>
    <td><b>DFS mode</b></td>
    <td>Visualizes depth-first search with a stack.</td>
  </tr>
  <tr>
    <td><b>Live search states</b></td>
    <td>Shows explored nodes, frontier cells, current node, and final path.</td>
  </tr>
  <tr>
    <td><b>Stats panel</b></td>
    <td>Displays explored node count, elapsed time, and path length.</td>
  </tr>
</table>

## Tech Stack

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-1D4ED8?style=flat-square&logo=python&logoColor=white" />
  <img alt="Pygame" src="https://img.shields.io/badge/Pygame-16A34A?style=flat-square&logo=python&logoColor=white" />
  <img alt="Deque" src="https://img.shields.io/badge/collections.deque-F97316?style=flat-square" />
  <img alt="Generators" src="https://img.shields.io/badge/Python_Generators-9333EA?style=flat-square" />
  <img alt="Pathfinding" src="https://img.shields.io/badge/Pathfinding-06B6D4?style=flat-square" />
</p>

| Layer | Technology | Role |
| --- | --- | --- |
| Language | `Python` | App logic, grid state, BFS/DFS, and stats. |
| UI/rendering | `pygame` | Window, toolbar buttons, grid drawing, colors, and events. |
| BFS queue | `collections.deque` | FIFO frontier for breadth-first search. |
| DFS stack | Python list | LIFO frontier for depth-first search. |
| Search stepping | Python generators | Yield intermediate algorithm states for animation. |

## Project Structure

```text
.
|-- app.py                 # Top-level placeholder
|-- requirements.txt       # Top-level placeholder
|-- font.ttf               # Top-level font asset
|-- README.md              # Project documentation
|-- pathfinder/
|   |-- test.py            # Main runnable Pygame visualizer
|   |-- source2.py         # Button class, Grid helper, BFS, DFS
|   |-- requirements.txt   # Inner project dependency file
|   |-- readme.md          # Existing short notes
|   `-- font.ttf           # Inner font asset used by the runnable app
`-- .venv/                 # Local virtual environment artifact
```

The runnable app currently lives in the nested `pathfinder/` directory.

## Run Locally

Create and activate a virtual environment:

```bash
cd pathfinder
python3 -m venv .venv
source .venv/bin/activate
```

Install Pygame:

```bash
pip install pygame
```

Run the visualizer:

```bash
python test.py
```

## Controls

| Control | Action |
| --- | --- |
| `WALLS` | Switch to wall editing mode. |
| `START` | Place or move the start cell. |
| `END` | Place or move the destination cell. |
| `CLEAR` | Reset grid, search state, timing, and path. |
| `BFS` | Run breadth-first search. |
| `DFS` | Run depth-first search. |
| Left click / drag | Add walls while in wall mode. |
| Right click / drag | Remove walls while in wall mode. |
| Window close | Quit. |

## Search Visualization

| Color / state | Meaning |
| --- | --- |
| Black | Wall. |
| Green | Start cell. |
| Red | End cell. |
| Blue | Currently explored cell. |
| Light blue | Visited cell. |
| Darker blue | Frontier cell waiting to be explored. |
| Yellow | Final path. |

## How It Works

### 1. Grid Model

The grid is a `9x24` list of lists:

| Value | Meaning |
| --- | --- |
| `0` | Empty cell |
| `1` | Wall |
| `2` | Start |
| `3` | End |

Mouse input changes those values depending on the selected toolbar mode.

### 2. BFS

`bfs()` uses a `deque` queue. It explores cells in first-in, first-out order, which makes it reliable for shortest paths on an unweighted grid.

Each step yields a dictionary containing the current node, frontier, visited cells, and explored node count.

### 3. DFS

`dfs()` uses a Python list as a stack. It explores deeply before backing up, which makes it useful for comparing traversal behavior against BFS.

DFS also yields intermediate dictionaries so the renderer can show the active stack, visited cells, and final path when found.

### 4. Generator-Based Animation

The Pygame loop stores the active search generator in `search_engine`. Every tick, it calls:

```python
search_result = next(search_engine)
```

That result drives the coloring and stats panel. This keeps the visualization step-by-step instead of blocking until the search finishes.

## Why I Built This

>ai is a must have skill and aside from all the ai utilitites i already know , wanted to get depper into the ai by this project , idea isnpired by a scren i saw while taking cs50ai 





## Current Status

| Area | Status |
| --- | --- |
| Wall drawing | Working |
| Wall removal | Working |
| Start/end placement | Working |
| BFS visualization | Working |
| DFS visualization | Working |
| Runtime stats | Working |
| A* / Dijkstra | Not implemented yet |

## Known Limitations

| Limitation | Current state |
| --- | --- |
| Algorithms | Only BFS and DFS are implemented. |
| Grid size | Fixed in `test.py`. |
| Project layout | The runnable app lives in nested `pathfinder/`. |
| Requirements | Top-level `requirements.txt` is a placeholder. |
| Logging | Console output is verbose during searches. |
| Speed | Search animation ticks at a fixed `5 FPS`. |

## Roadmap Ideas

| Idea | Why it would help |
| --- | --- |
| Add A* | Show heuristic-driven search. |
| Add Dijkstra | Compare weighted/unweighted search behavior. |
| Speed slider | Let the user slow down or speed up the search. |
| Move runnable app to root | Simplify setup and run commands. |
| Add maze generation | Make harder test maps quickly. |
| Add clean requirements | Make dependency install predictable. |

---

<div align="center">
  <sub>Built with Python, Pygame, BFS queues, DFS stacks, and generator-driven search animation.</sub>
</div>
