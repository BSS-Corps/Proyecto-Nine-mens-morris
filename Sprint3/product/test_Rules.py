from cgi import test
import pytest
from Rules import Rules

@test
def test_check_mill():
    assert Rules.check_mill(1,[1,3]) == False