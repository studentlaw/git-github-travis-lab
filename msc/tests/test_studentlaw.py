from nose.tools import assert_equal

from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char_a():
    assert_equal("Y", rot13_char("L"))
