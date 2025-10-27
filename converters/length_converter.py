from .base_converter import UnitConverter

class LengthConverter(UnitConverter):
    _map = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
    }

    def units(self):
        return list(self._map.keys())

    def convert(self, value, from_unit, to_unit):
        base = value * self._map[from_unit]
        return base / self._map[to_unit]
