# =============================================================================
# This file contains the function to do Contract Net Protocol (CNP). 
# =============================================================================
from typing import Any


def do_CNP(flight):
    # the do_CNP function takes a flight-agent object

    if not flight.departure_time:
        raise Exception("The object passed to the CNP protocol has no departure time, therefore it seems that it is not a flight.")
# =============================================================================
# Step 1:  determining managers and contractors
# Semiformal:
# For first step (not at any time point):
# -All agents determine neighborhood (the other agents that they can see)
# -Agents with biggest neighborhood are assigned manager
# -Remaining agents are assigned contractor
# =============================================================================


     # communication range: 1000 km defined in 'model'
    # neighborhood = flight.get_neighbors(radius:communication_range)
    # print ('Neighborhood', neighborhood)



