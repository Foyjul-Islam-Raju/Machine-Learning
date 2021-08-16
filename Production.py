import scipy.optimize   #provides functions for minimizing
               #(or maximizing) objective functions possibly subject to constraints

# Objective Function: 50x_1 + 80x_2
# Constraint 1: 5x_1 + 2x_2 <= 20
# Constraint 2: -10x_1 + -12x_2 <= -90

result = scipy.optimize.linprog(   # minimize a linear objective function subject
                                   # to linear equality and inequality constraints.
    [50, 80],  # Cost function: 50x_1 + 80x_2
    A_ub=[[5, 2], [-10, -12]],  # Coefficients for inequalities
    b_ub=[20, -90],  # Constraints for inequalities: 20 and -90  #ub=upperbound
)

if result.success:     #result success hole result show korbe
    print(f"X1: {round(result.x[0], 2)} hours")   #f"X1 eta f string formatting
    print(f"X2: {round(result.x[1], 2)} hours")   #rounding result er jonno jehetu
                                    # 2 deya tai 2 decimal point porjonto result dekhabe
else:
    print("No solution")   #result success na hole no solution dekhabe