"""
Naive backtracking search without any heuristics or inference.
"""

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]     #set of variable
CONSTRAINTS = [       #constraint set
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]


def backtrack(assignment):
    """Runs backtracking search to find an assignment."""

    # Check if assignment is complete
    if len(assignment) == len(VARIABLES):   
        return assignment

    # Try a new variable
    var = select_unassigned_variable(assignment) 
    for value in ["Sunday", "Tuesday", "Wednesday"]:  # Set of domain
        new_assignment = assignment.copy()  
        new_assignment[var] = value   
        if consistent(new_assignment):  
            result = backtrack(new_assignment)  
            if result is not None:  
                return result
    return None

def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order."""
    for variable in VARIABLES:
        if variable not in assignment:    
            return variable
    return None

def consistent(assignment):
    """Checks to see if an assignment is consistent."""
    for (x, y) in CONSTRAINTS:
        if x not in assignment or y not in assignment:  # Only consider arcs where both are assigned
            continue
        if assignment[x] == assignment[y]:  # If both have same value, then not consistent
            return False
    return True  # If nothing inconsistent, then assignment is consistent


solution = backtrack(dict())   
print(solution)
