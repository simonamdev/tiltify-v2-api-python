import pytest

from tiltify2.tiltify import Tiltify2


class TestTiltify2:
    @pytest.mark.parametrize('api_key', [
        '',
        None
    ])
    def test_not_passing_valid_api_key_throws_exception(self, api_key):
        with pytest.raises(ValueError):
            tiltify = Tiltify2(api_key)

