

from formation_flying.model import FormationFlying
from formation_flying.SimpleContinuousModule import SimpleCanvas
from formation_flying.agents.flight import Flight
from formation_flying.agents.airports import Airport
from formation_flying.negotiations.CNP import do_CNP
from formation_flying.parameters import model_params

model = FormationFlying(n_origin_airports=1, n_destination_airports=1, n_flights=1) #order matters: what is 'made' first

do_CNP(model.schedule.agents[-1]) #[-1] gets the flights
