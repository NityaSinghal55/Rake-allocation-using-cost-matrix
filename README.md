# Rake-allocation-using-cost-matrix
This project demonstrates a basic Linear Programming approach using Python and PuLP to minimize the cost of transferring empty rakes (railway wagons) between sources and destinations.

It models a classic assignment problem, ensuring each destination gets exactly one rake, and each source sends at most one.

% Problem Statement:

You are given a cost matrix that represents the cost of transferring a rake from a source location (A, B, C) to a destination (X, Y, Z). The goal is to find the optimal assignment of rakes from sources to destinations that minimizes the total cost, while satisfying:

* Each destination receives exactly one rake

* Each source sends at most one rake

% Example Cost Matrix:

| FROM | TO | Cost |
| ---- | -- | ---- |
| A    | X  | 9    |
| A    | Y  | 8    |
| A    | Z  | 1    |
| B    | X  | 6    |
| B    | Y  | 8    |
| B    | Z  | 3    |
| C    | X  | 5    |
| C    | Y  | 2    |
| C    | Z  | 4    |

% Technologies Used:

* Python

* pandas – For handling tabular data

* PuLP – Linear programming modeling library

% Project Structure:

* optimize_rake_assignment.py  # Main script

* README.md                    # Documentation

% Sample Output:

Assignment and Total Cost:

A ➜ Z | Cost: 1

B ➜ X | Cost: 6

C ➜ Y | Cost: 2

Total Minimum Cost: 9

% Concepts Used:

* Binary Decision Variables

* Objective Function: Cost Minimization

* Constraints:

    * One rake per destination

    * One rake at most per source

