Auto_Analysis — System Overview
Project Description

Auto_Analysis is an automated data analysis workflow system.

A user provides:

a natural language goal (what they want to learn), and
one or more datasets (CSV, Excel, JSON, etc.)

The system then autonomously:

explores the data
selects appropriate analytical methods
executes code
iteratively refines its approach
produces a final report

A large language model (Claude) is responsible for reasoning, planning, and choosing analytical strategies, while the surrounding system acts as a harness that provides tools, enforces structure, and records all steps.

Core Workflow
User Goal + Data
        ↓
   Planner / Coordinator
        ↓
   Claude Reasoning Step
        ↓
   Decide Next Action
        ↓
   ┌──────────────────────────────┐
   │ Can we proceed with action?  │
   └──────────────────────────────┘
           ↓ yes                     ↓ no
     Tool Execution            Ask User (Clarify)
           ↓                          ↓
     run_python / SQL         Receive User Input
           ↓                          ↓
     Observe Results  ←───────────────┘
           ↓
     Update State / Memory
           ↓
     Re-plan Next Step
           ↓
     (Loop until analysis is complete)
           ↓
     Generate Final Report
Agent Responsibilities (Claude)

Claude is responsible for:

Interpreting the user’s goal
Inspecting dataset structure
Forming hypotheses about the data
Selecting appropriate analytical methods (EDA, regression, classification, clustering, etc.)
Writing analysis code (Python / SQL)
Interpreting execution results
Deciding when clarification is required
Producing a final human-readable report
System Responsibilities (Harness)

The surrounding system is responsible for:

Providing a controlled execution environment (run_python, run_sql)
Managing file/data access
Enforcing step-by-step workflow structure
Capturing execution outputs and errors
Maintaining session state and analysis history
Handling user clarification prompts (ask_user)
Logging all actions for reproducibility
Key Design Principle

Claude performs reasoning.
The system enforces execution, structure, and reliability.

This separation ensures:

consistent analytical behavior
real execution of code (not hallucinated results)
iterative improvement through feedback loops
traceable, reproducible workflows

If you want, I can next turn this into a 
1-page “README.md style spec” or a 
diagram-ready architecture block for your repo.
