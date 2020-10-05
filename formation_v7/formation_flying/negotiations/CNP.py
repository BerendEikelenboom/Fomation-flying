# =============================================================================
# This file contains the function to do Contract Net Protocol (CNP). 
# =============================================================================
from typing import Any


def do_CNP(flight):
    # the do_CNP function takes a flight-agent object

    if not flight.departure_time:
        raise Exception("The object passed to the CNP protocol has no departure time, therefore it seems that it is not a flight.")

    # If contractor is not yet in a formation, start finding managers.
    if flight.formation_state == 0:
        formation_targets = flight.find_greedy_candidate()




