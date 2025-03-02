from source.land import Land
from source.probe import Probe

from typing import List

class ProbeController:
    def __init__(self, land: Land):
        self.land = land
        self.probes: List[Probe] = []

    def add_probe(self, x: int, y: int, direction: str, commands: str):
        probe = Probe(x, y, direction, commands, self.land)
        self.probes.append(probe)

    def execute_probes(self):
        for probe in self.probes:
            probe.execute_comands()

    def show_probes_position(self):
        for probe in self.probes:
            print(probe)
    
    def show_probes_values(self):
        probes_values = []

        for probe in self.probes:
            probe_value = (probe.x, probe.y, probe.direction, probe.commands)
            probes_values.append(probe_value)

        return probes_values
