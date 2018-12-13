import re
import unittest

from ..fhdl.ast import *


__all__ = ["FHDLTestCase"]


class FHDLTestCase(unittest.TestCase):
    def assertRepr(self, obj, repr_str):
        obj = Statement.wrap(obj)
        repr_str = re.sub(r"\s+",   " ",  repr_str)
        repr_str = re.sub(r"\( (?=\()", "(", repr_str)
        repr_str = re.sub(r"\) (?=\))", ")", repr_str)
        self.assertEqual(repr(obj), repr_str.strip())
