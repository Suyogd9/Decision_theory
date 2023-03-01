# Decision_theory

For this assignment, you will implement a basic decision support tool that is designed to build a decision tree, calculate values for the entries, and then report both the expected value of each lottery and the action for each decision node. 

You have been given a file that represents the decision tree shown in the example below. The file contains three types of entries:

1. Decision blocks: Represent a basic decision and include the specification of a name and a set of named choices, each of which leads to a named outcome, decision, or lottery. 

2. Lottery blocks: Specify a set of alternatives with probabilities attached. These, in turn, lead to named outcomes, decisions, or lotteries. 

3. Outcome lines: Specify a name and an integer utility value. 

Note that the file defines a compressed model, and the same item may appear under multiple locations, however, with the relevant utility value or choice. Your code will need to rerun the calculations differently in each case. Trees always begin with a node labeled "Start" and end with outcome leaves.

When run, your code should first generate a decision tree in memory using classes for the relevant items. As the tree is generated, you should log the creation of each new node in the tree where Number is a numeric index which is incremented for each node:

Adding Node `<Number> <Type> <Name> <Parent>`

Your code will then calculate the expected value of each lottery and the decision for each node and print the results to the screen:

Expected Value Node: `<Number>,<Name> <Value>`
Decision Node: `<Number>,<Name> <Decision> <Value>`

![image](https://user-images.githubusercontent.com/26815221/222036643-cbe51822-0625-4911-a18e-9392705a2fae.png)
