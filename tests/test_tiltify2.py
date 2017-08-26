import pytest

from tiltify2.tiltify import Tiltify2, Order


class TestTiltify2Initialisation:
    @pytest.mark.parametrize('api_key', [
        '',
        None
    ])
    def test_not_passing_valid_api_key_throws_exception(self, api_key):
        with pytest.raises(ValueError):
            tiltify = Tiltify2(api_key)

test_api_key = 'test_479c924413fe9168952891e9a36'

"""
This test suite assumes that the reply from the Tiltify test API never changes
"""
class TestTiltify2Donations:
    tiltify = None

    def setup_method(self):
        self.tiltify = Tiltify2(api_key=test_api_key)

    def test_retrieving_all_donations_without_parameters(self):
        donations = self.tiltify.get_donations()
        # Assert number of donations present
        assert 4 == len(donations)
        # Assert they are ordered by ID by default
        for i in range(4, 0):
            assert 10000 + i == donations[i]['id']

    def test_get_donations_with_limit_1(self):
        donations = self.tiltify.get_donations(limit=1)
        assert 1 == len(donations)
        assert 10004 == donations[0]['id']
        assert 10.0 == donations[0]['amount']

    def test_get_donations_with_limit_2(self):
        donations = self.tiltify.get_donations(limit=2)
        assert 2 == len(donations)
        assert 10004 == donations[0]['id']
        assert 10.0 == donations[0]['amount']
        assert 10003 == donations[1]['id']
        assert 100.0 == donations[1]['amount']

    def test_get_donations_in_ascending_order(self):
        donations = self.tiltify.get_donations(donation_order=Order.ASC)
        assert 4 == len(donations)
        for i in range(1, 5):
            assert 10000 + i == donations[i - 1]['id']

    def test_getting_donations_in_descending_order(self):
        donations = self.tiltify.get_donations(donation_order=Order.DESC)
        assert 4 == len(donations)
        for i in range(4, 0):
            assert 10000 + i == donations[i]['id']

    def test_getting_donations_ordered_by_amount(self):
        donations = self.tiltify.get_donations(donation_order=Order.DESC, order_by=Order.AMOUNT)
        amounts = (730, 100, 50, 10)
        assert len(amounts) == len(donations)
        for i in range(0,  4):
            assert amounts[i] == donations[i]['amount']

    def test_getting_donations_ordered_by_creation_time_starting_from_oldest(self):
        donations = self.tiltify.get_donations(donation_order=Order.ASC, order_by=Order.CREATED_AT)
        times = (
            '2015-09-17 16:06:21 -0400',
            '2015-09-17 20:22:47 -0400',
            '2015-09-17 20:51:12 -0400',
            '2015-09-18 15:20:42 - 400'
        )
        assert len(times) == len(donations)
        for i in range(0, len(times)):
            assert times[i] == donations[i]['created']

    def test_getting_limited_donations_ordered_by_creation_time_from_latest(self):
        donations = self.tiltify.get_donations(limit=2, donation_order=Order.DESC, order_by=Order.CREATED_AT)
        times = (
            '2015-09-18 15:20:42 - 400',
            '2015-09-17 20:51:12 -0400',
        )
        assert len(times) == len(donations)
        for i in range(0, len(times)):
            assert times[i] == donations[i]['created']
