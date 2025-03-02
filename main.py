from source.land import Land
from source.probe import Probe

land = Land(5, 5)
probe = Probe(3, 3, "E", land)

probe.execute_comands("MMRMMRMRRM")

print(str(probe))