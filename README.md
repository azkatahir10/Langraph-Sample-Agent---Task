# LangGraph Decision Agent

A simple decision-making agent built with LangGraph that evaluates numerical input against a threshold and routes processing accordingly.

## Features

- Evaluates numerical input against configurable threshold (default: 50)
- Conditional routing based on evaluation ("high" or "low")
- State management throughout execution
- Clear console visualization of the decision flow
- Output saved to `visualizations/` directory

## Requirements

- Python 3.8+
- LangGraph
- (Optional) Graphviz for advanced visualization

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/langgraph-decision-agent.git
   cd langgraph-decision-agent
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the decision agent:
```bash
python decision_agent.py
```

Example output:
```
High value result: {'input_value': 75, 'evaluation_result': 'high', 'final_message': 'The value 75 is high!'}
Low value result: {'input_value': 25, 'evaluation_result': 'low', 'final_message': 'The value 25 is low.'}

Graph Structure:
+-------------+
|  evaluator  |
+------+------+
       |
       +-----> high_handler -> END
       |
       +-----> low_handler -> END
```

## Project Structure

```
.
├── decision_agent.py       # Main application code
├── requirements.txt        # Dependencies
├── visualizations/         # Output files
│   └── graph_structure.txt # Graph visualization
└── README.md               # This file
```

## Customization

1. Change the threshold value in `evaluate_number()` function
2. Add new conditions by modifying the `decide_path()` function
3. Extend with additional handlers as needed

## Visualization Options

1. Basic ASCII output (included)
2. For advanced visualization:
   ```bash
   pip install graphviz
   ```
   Download Graphviz from https://graphviz.org/download/



   git push
   ```
