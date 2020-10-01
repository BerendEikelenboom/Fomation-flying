# =============================================================================
# This file contains the function to do Contract Net Protocol (CNP). 
# =============================================================================

def do_CNP(flight):
    # the do_CNP function takes a flight-agent object

    if not flight.departure_time:
        raise Exception("The object passed to the greedy protocol has no departure time, therefore it seems that it is not a flight.")
# =============================================================================
# Step 1:  determining managers and contractors
# Semiformal:
# For first step (not at any time point):
# -All agents determine neighborhood (the other agents that they can see)
# -Agents with biggest neighborhood are assigned manager
# -Remaining agents are assigned contractor
# =============================================================================

    for agent in flight:

