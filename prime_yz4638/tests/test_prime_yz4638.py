import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from prime_yz4638 import prime_yz4638

import math


@pytest.mark.parametrize("example, expected", [
    (2, True), (3, True), (5, True), (7, True), (11, True),
    (-3, False), (0, False), (1, False), (4, False), (6, False), 
])
def test_is_prime_param(example, expected):   
    result = prime_yz4638.is_prime(example)
    assert result == expected
