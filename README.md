# 🧠 Random Agent vs Smart Agent

This project compares the performance of a **Random Agent** and a **Smart Agent** in a defined environment, demonstrating the effectiveness of strategic decision-making over random behavior in AI systems.


## 🤖 Agents Description

### Random Agent
- Makes decisions by choosing actions at random.
- No learning or strategy involved.
- Serves as a baseline for performance comparison.

### Smart Agent
- Uses a deterministic or learning-based approach (e.g., rule-based logic, reinforcement learning, or heuristic strategies).
- Aims to maximize performance through intelligent decision-making.

## 🧪 Environment

- Define your custom environment or use a standard one (e.g., GridWorld, Tic-Tac-Toe, OpenAI Gym environment).
- Both agents interact with the same environment under identical conditions.

## 📊 Evaluation

- Performance metrics may include:
  - Win rate
  - Average reward
  - Number of steps taken to reach goal
  - Time taken per episode

### Example Output

| Agent        | Win Rate | Avg. Reward | Avg. Steps |
|--------------|----------|-------------|------------|
| Random Agent | 20%      |  -15.2      | 78         |
| Smart Agent  | 85%      |  +9.8       | 32         |

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/random-vs-smart-agent.git
   cd random-vs-smart-agent


2. Install Dependencies:
      ```bash
   pip install -r requirements.txt


4. Launch the notebooks:

Run random_agent.ipynb to test the Random Agent.

Run smart_agent.ipynb to test the Smart Agent.

# 📌 Requirements
- Python 3.8+
- Jupyter Notebook
- NumPy
- Matplotlib
- (Optional) TensorFlow / PyTorch (if using ML)
