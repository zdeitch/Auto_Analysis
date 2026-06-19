# Auto_Analysis
The project is an automated data analysis workflow.
A user would interact with an interface by putting in a prompt and any files containing their data of interest. The system would then process the data, query it, and conduct analyses.
The workflow can be seen roughly as follows:
===========================================
User Goal + Data
        ↓
  Planner/Coordinator
        ↓
  Claude Reasoning Step
        ↓
Can I proceed?
      /     \
    Yes      No
     |        |
Choose tool   Ask user
     |        |
Execute code  Receive answer
     |        |
Observe results
     ↓
Update plan
     ↓
Repeat until finished
     ↓
Generate report
===========================================
A large language model (Claude) will make decisions, form hypotheses, and determine which analyses to run, but our system will act as a harness that regulates the analysis, and keeps a record of the exact steps involved.
