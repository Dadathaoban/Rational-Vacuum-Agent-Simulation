# Rational Vacuum Agent Simulation

## 📌 Project Overview
This project implements a **Rational Vacuum Cleaner Agent** operating in a **4×4 grid environment**, inspired by classic problems in **Artificial Intelligence (AI)** and **Intelligent Agents**.

The agent is designed to:
- Identify dirty locations
- Navigate efficiently through the environment
- Clean all dirt while respecting **energy constraints** and **bag capacity**
- Return to the home location after task completion

The simulation follows a **deterministic, rule-based decision model** and evaluates agent performance using clear metrics.

---

## 🧠 Problem Description
The environment consists of:
- A **4×4 grid** labeled from **A to P**
- **10 predefined dirty locations**
- A vacuum agent that:
  - Starts at location **A**
  - Has **100 units of energy**
  - Uses a dust bag with a **capacity of 10**
  - Must return home with an **empty bag** after cleaning all dirt

The agent must achieve the goal **rationally**, minimizing unnecessary actions while ensuring task completion.

---

## 🎯 Agent Goals
The agent is considered successful when:
1. All dirty locations are cleaned
2. The agent returns to the home location (A)
3. The dust bag is empty
4. Energy constraints are respected

---

## ⚙️ Key Features
- Grid-based environment modeling
- State tracking (location, dirt status, energy, bag load)
- Manhattan-distance-based path selection
- Rational decision-making using percept–action rules
- Performance metrics and efficiency scoring
- Clear separation of logic and execution

---

## 🏗️ System Design

### Agent State Variables
- Current location
- Energy level
- Bag load and capacity
- Dirt status of all grid cells
- Action counters and visited locations

### Decision-Making Strategy
The agent uses:
- **Percept-based rules**
- **Greedy nearest-dirty-location search**
- **Constraint checking** (energy, bag capacity)
- Deterministic movement logic

---

## 🧩 Core Technologies
- **Programming Language:** Python
- **Paradigm:** Object-Oriented Programming (OOP)
- **AI Concepts:** Rational agents, state space, performance measures

---

## 📊 Performance Evaluation
The simulation tracks:
- Total actions performed
- Number of moves
- Cleaning actions
- Bag emptying actions
- Energy consumption
- Grid coverage

A **performance score** is calculated based on:
- Reward for cleaned locations
- Penalty for excessive actions

---

## 🧪 Sample Output
The simulation provides:
- Step-by-step grid visualization
- Agent status after each action
- Final performance report summarizing efficiency

---

## 📈 Scalability & Extensions
The project discusses extensions for:
- Larger grid environments
- Dynamic obstacles
- Advanced pathfinding (A*, Dijkstra)
- Learning-based optimization
- Real-world robotic vacuum adaptations

---

## 📚 Learning Outcomes
This project reinforces:
- Intelligent agent architecture
- State management complexity
- Constraint-based reasoning
- Deterministic vs adaptive agent behavior
- Transition from theoretical AI models to real-world systems

---

## 👤 Author
**Dada Muhammed Thaoban**

---

## 📄 License
This project is intended for **academic and educational use only**.
