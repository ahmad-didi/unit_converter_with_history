from .base_converter import UnitConverter

class TemperatureConverter(UnitConverter):
    def units(self):
        return ['celsius', 'fahrenheit', 'kelvin']

    def convert(self, value, from_unit, to_unit):
        f = from_unit.lower()
        t = to_unit.lower()
        if f == t:
            return value
        if f == 'celsius':
            c = value
        elif f == 'fahrenheit':
            c = (value - 32) * 5.0/9.0
        elif f == 'kelvin':
            c = value - 273.15
        else:
            raise ValueError('Unknown temperature unit')
        if t == 'celsius':
            return c
        elif t == 'fahrenheit':
            return c * 9.0/5.0 + 32
        elif t == 'kelvin':
            return c + 273.15
        else:
            raise ValueError('Unknown temperature unit')
