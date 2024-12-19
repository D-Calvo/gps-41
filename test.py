"""
Aquest mòdul conté tests unitaris per provar les transformacions de strings.
"""

import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """Classe per provar les transformacions de strings."""

    def test_is_upper(self):
        """Comprova si una cadena es transforma correctament a majúscules."""
        string = transform.to_upper_case("hello")
        self.assertEqual(string, "HELLO")

    def test_is_lower(self):
        """Comprova si una cadena es transforma correctament a minúscules."""
        string = transform.to_lower_case("HELLO")
        self.assertEqual(string, "hello")

    def test_is_capitalize(self):
        """Comprova si una cadena es transforma correctament a format capitalitzat."""
        string = transform.to_capitalize("HELLO")
        self.assertEqual(string, "Hello")


if __name__ == '__main__':
    unittest.main()
