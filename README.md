### PeDMN-Prototype

This repository contains short testing scripts for highlighting the expressivity of PeDMN by modeling several example processes using PeDMN. The example processes are designed to highlight specific execution semantics instead of practical examples, so labels are {'A', 'B', etc}. To verify that the models correctly represent the intended execution semantics they are also compared to several event logs that were simulated by executing imperative versions of the example processes with timeouts as endpoints.

#### Repository Structure

project-name/
├── src/                # Main source code
│   ├── main.py         # Entry point
│   ├── utils.py        # Helper functions
│   └── __init__.py     # Package initializer
├── tests/              # Unit and integration tests
│   ├── test_main.py
│   └── test_utils.py
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies

PeDMN-Prototype/
├── logs/ # Contains the log files used for verifying PeDMN
│   ├── ExA1.xes.yaml # Individualt Logs files from A1 over A5 to E5
│   ├── ...
│   ├── ExE5.xes.yaml
├── constraint.py # Contains the encoded PeDMN constraint tables
├── EventHistory.py # A simple eventlog class
├── iter\_testing.py # Simulates execution using the example constraint table in the paper
├── preprocessing.py # Preprocssing of the .xml.yaml logs
├── README.md # You are reading it 
├── testing.py # Testing the evaluation of the example constraint table
├── run.py # Script for testing the 5 example processes with the 5 logs, example usage below


#### Example PeDMN execution with synthetic logs 

1. git clone 
2. pip install requirements.txt
3. python3 run.py ExA1

This script can be used to compare the execution that would be proposed according to the PeDMN model with the executions that happend through the imperative execution described by the event logs. The possible parameters are ExA1 to ExE5, where ExA1 refers to comparing execution of procss A with Log 1. For each process we generated 5 example logs with varied dataobjects, so ExA2/ExB3/ExC1 are all valid calls.

The results can be interpreted as follows: In each Line we state what the previous event was starting with "Before first event". Next there is a implies arrow that leads to a List []. The Activity labels in the List (e.g., ['A', 'B', etc]) are the possible activites that can be started in the next event. In addition it also always states the set O {} containing the dataobjects with their current values. Next we check what event was executed next according to the log, the rules are evaluated again to check the possible set of next activities and the (potentially updated) dataobjects O are printed again. A good way to check that the log would be a potential result according to the PeDMN model is to verify that a) the logs does not continue after ['end'] appears in the set of consequence and b) Whenever a new event is called it was previously in the set of possible activities. 


### Syntax validation of PeDMN examples in the Paper

This can be used to verify the syntax of the example conditions given in the paper.

1. git clone
2. pip install requirements.txt
3. python3 iterative\_testing.py
4. and/or python3 testing.py 
