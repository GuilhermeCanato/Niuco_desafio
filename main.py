from source.land                import Land
from source.probe               import Probe
from source.probe_controller    import ProbeController

from fastapi    import FastAPI, HTTPException
from pydantic   import BaseModel
from typing     import List

app = FastAPI()

class LandEntry(BaseModel):
    height: int
    width: int

class ProbeEntry(BaseModel):
    x: int
    y: int
    direction: str
    command: str

class EntryData(BaseModel):
    land: LandEntry
    probes: List[ProbeEntry]

@app.post("/entry-data")
def data_entry(data: EntryData):
    try:
        land_entry = data.land
        probes_entry = data.probes

        land = Land(land_entry.height, land_entry.width)
        probe_controller = ProbeController(land)

        for probe in probes_entry:
            probe_controller.add_probe(probe.x, probe.y, probe.direction, probe.command)

        probe_controller.execute_probes()

        return {           
            "sondas": [{
                "x": x,
                "y": y,
                "Direção": direction
                } for (x, y, direction, _) in probe_controller.show_probes_values()]
        }
    except Exception as e:
        raise HTTPException(status_code = 400, detail = f"Error: {e}")