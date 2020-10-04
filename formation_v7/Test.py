

from formation_flying.model import FormationFlying
from formation_flying.SimpleContinuousModule import SimpleCanvas
from formation_flying.agents.flight import Flight
from formation_flying.agents.airports import Airport
from formation_flying.negotiations.CNP import do_CNP
from formation_flying.parameters import model_params

model = FormationFlying(n_origin_airports=20, n_destination_airports=20, n_flights=50) #order matters: what is 'made' first
all_agents = model.schedule.agents
flight_agents = []
for agent in all_agents:
    if type(agent) is Flight:
        flight_agents.append(agent)

Flight.assign_manager(flight_agents[0])
print(flight_agents[0].manager)
print(flight_agents[0].auctioneer)

#do_CNP(model.schedule.agents[-1]) #[-1] gets the flights

