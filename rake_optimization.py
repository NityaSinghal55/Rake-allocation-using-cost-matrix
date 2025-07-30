import pandas as pd
import pulp

# Define cost matrix
cost_data = {
    'FROM': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'TO':   ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'cost': [ 9,   8,   1,   6,   8,   3,   5,   2,   4]
}

df = pd.DataFrame(cost_data)

# Initialize the LP problem
model = pulp.LpProblem("Minimize_Empty_Rake_Transfer_Cost", pulp.LpMinimize)

# Create decision variables
decision_vars = {
    (row.FROM, row.TO): pulp.LpVariable(f"x_{row.FROM}_{row.TO}", cat="Binary")
    for _, row in df.iterrows()
}

# Minimize total cost
model += pulp.lpSum(
    row.cost * decision_vars[(row.FROM, row.TO)]
    for _, row in df.iterrows()
)

# Each destination gets one rake
for dest in df['TO'].unique():
    model += pulp.lpSum(
        decision_vars[(src, dest)] for src in df['FROM'].unique()
    ) == 1

# Each source sends at most one rake
for src in df['FROM'].unique():
    model += pulp.lpSum(
        decision_vars[(src, dest)] for dest in df['TO'].unique()
    ) <= 1

# Solve
model.solve()

# Print results
print("Assignment and Total Cost:")
total_cost = 0
for key, var in decision_vars.items():
    if var.value() == 1:
        from_stn, to_stn = key
        cost = df[(df.FROM == from_stn) & (df.TO == to_stn)].cost.values[0]
        print(f"{from_stn} ➜ {to_stn} | Cost: {cost}")
        total_cost += cost

print(f"\n Total Minimum Cost: {total_cost}")
