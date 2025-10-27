import unittest
from converters.length_converter import LengthConverter
from converters.mass_converter import MassConverter
from converters.temperature_converter import TemperatureConverter

class TestConverters(unittest.TestCase):
    def test_length_meter_km(self):
        c = LengthConverter()
        self.assertAlmostEqual(c.convert(1000, 'meter', 'kilometer'), 1.0)

    def test_length_mile_meter(self):
        c = LengthConverter()
        self.assertAlmostEqual(c.convert(1, 'mile', 'meter'), 1609.34, places=2)

    def test_mass_kg_g(self):
        m = MassConverter()
        self.assertAlmostEqual(m.convert(1, 'kilogram', 'gram'), 1000.0)

    def test_mass_lb_kg(self):
        m = MassConverter()
        self.assertAlmostEqual(m.convert(1, 'pound', 'kilogram'), 0.453592, places=6)

    def test_temp_c_f(self):
        t = TemperatureConverter()
        self.assertAlmostEqual(t.convert(0, 'celsius', 'fahrenheit'), 32.0)

    def test_temp_k_c(self):
        t = TemperatureConverter()
        self.assertAlmostEqual(t.convert(273.15, 'kelvin', 'celsius'), 0.0, places=5)

if __name__ == '__main__':
    unittest.main()
