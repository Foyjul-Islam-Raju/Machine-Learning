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


def backtrack(assignment):       #it's a fuction.etar maddhome backtrack kora hoise
    """Runs backtracking search to find an assignment."""

    # Check if assignment is complete
    if len(assignment) == len(VARIABLES):   #assignment er length & variable er length
                                            #soman hoile assignment return korbe. loop e r jabe na
        return assignment

    # Try a new variable
    var = select_unassigned_variable(assignment)  #var er moddhe ekta unassignment variable ache
    for value in ["Sunday", "Tuesday", "Wednesday"]:  # Set of domain
        new_assignment = assignment.copy()  #assignment er ekta copy new assignment e rakha hoise
        new_assignment[var] = value   #new_assignment[var] ekkhane jekono ekta domain assign korse
        if consistent(new_assignment):  # JODI consistent e new assignment ta thake
            result = backtrack(new_assignment)  #new assignment ta backtrack e pass hoye jabe
            if result is not None:  #result e kichu thakle resuilt ta return hobe
                return result
    return None    # ressult e kichu na thakle no result show korbe


def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order."""
    for variable in VARIABLES:
        if variable not in assignment:     # variabe ta jodi assignment e na thake
            return variable                #sobgula jodi na thake none return korbe
    return None


def consistent(assignment):
    """Checks to see if an assignment is consistent."""
    for (x, y) in CONSTRAINTS:

        # Only consider arcs where both are assigned
        if x not in assignment or y not in assignment:  #assignment e x & y value na thakle loop ta
                     #continue korbe 1st theke
            continue

        # If both have same value, then not consistent
        if assignment[x] == assignment[y]: # x jodi y er soman hoy tahole false return korbe
            return False

    # If nothing inconsistent, then assignment is consistent
    return True


solution = backtrack(dict())   #empty ekta dictionary pass kora hoise solution er moddhe
print(solution)  #solution ta print korbe