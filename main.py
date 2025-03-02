from source.land                import Land
from source.probe               import Probe
from source.probe_controller    import ProbeController

land = Land(5, 5)
probe_controller = ProbeController(land)

probe_controller.add_probe(1, 2, "N", "LMLMLMLMM")
probe_controller.add_probe(3, 3, "E", "MMRMMRMRRM")

probe_controller.show_probes_position()
probe_controller.execute_probes()
probe_controller.show_probes_position()