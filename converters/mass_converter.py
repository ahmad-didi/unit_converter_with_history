from .base_converter import UnitConverter

class MassConverter(UnitConverter):
    _map = {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495,
    }

    def units(self):
        return list(self._map.keys())

    def convert(self, value, from_unit, to_unit):
        base = value * self._map[from_unit]
        return base / self._map[to_unit]
