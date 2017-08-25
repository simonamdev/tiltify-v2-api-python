import pytest

from tiltify2.tiltify import Tiltify2


class TestTiltify2:
    def test_not_passing_valid_api_key_throws_exception(self):
        with pytest.raises(ValueError):
            tiltify = Tiltify2('')

