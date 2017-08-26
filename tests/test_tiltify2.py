import json
from pprint import pprint

import pytest

from tiltify2.tiltify import Tiltify2


class TestTiltify2Initialisation:
    @pytest.mark.parametrize('api_key', [
        '',
        None
    ])
    def test_not_passing_valid_api_key_throws_exception(self, api_key):
        with pytest.raises(ValueError):
            tiltify = Tiltify2(api_key)

"""
Please note that at the time of writing, version 2 of the Tiltify API returned the following body
as a response on their test API:

{"campaign_id":"0","owner":"Tilty","owner_img":"https://s3-us-west-2.amazonaws.com/tiltify-production-assets/assets/def
ault_member_avatar.png","mission":"A Perfect Mission","campaign":"My Awesome Campaign","cause":"A Great Cause","cause_l
ogo_url":"","donation_url":"https://tiltify.com/events/\u003cevent name\u003e/donate","campaign_url":"http://tiltify.co
m/events/\u003cevent name\u003e","banner_url":"","thumbnail":"","description":"This is a great campaign!","goal":6000.0
,"original_fundraiser_goal":0.0,"total_raised":890.0,"percent_raised":"15%","top_donor":"Mickey","top_donor_amount":730
.0,"starts":"09/16 12:45PM","ends":"09/30 02:00PM","currency_code":"USD","levels":[{"title":"Level 1","amount":10.0},{"
title":"Level 2","amount":20.0}],"rewards":[{"reward_id":"1","always_active":null,"name":"Picture of Me","amount":10.0,
"kind":null,"quantity":5.0,"remaining":2.0,"fmv":10.0,"starts_at":"2015-09-17 20:22:47 -0400","ends_at":"2015-09-17 22:
22:47 -0400","description":"This is a description.","rules_url":"","shipping_address_required":"true","shipping_note":n
ull,"image_url":"http://tiltify.com/image.jpg","currency_code":"USD","donate_url":"http://tiltify.com/events/\u003ceven
t name\u003e/donate?event_prize_id=","created":"2015-09-17 16:06:21 -0400"},{"reward_id":"0","always_active":null,"name
":"Pushups!","amount":20.0,"kind":null,"quantity":0.0,"remaining":0.0,"fmv":20.0,"starts_at":"2015-09-17 20:22:47 -0400
","ends_at":"2015-09-17 22:22:47 -0400","description":"I will do a pushup.","rules_url":"","shipping_address_required":
"false","shipping_note":null,"image_url":"http://tiltify.com/image.jpg","currency_code":"USD","donate_url":"http://tilt
ify.com/events/\u003cevent name\u003e/donate?event_prize_id=","created":"2015-09-17 16:06:21 -0400"}],"activities":[{"n
ame":"activity 1","starts_at":"2015-09-17 16:06:21 -0400","ends_at":"2015-09-17 16:06:21 -0400","description":null,"ima
ge_url":""},{"name":"activity 2","starts_at":"2015-09-17 16:06:21 -0400","ends_at":"2015-09-17 16:06:21 -0400","descrip
tion":null,"image_url":""}],"challenges":[],"supporting_parent_name":null,"donations":[{"name":"Anonymous","comment":nu
ll,"amount":10.0,"currency_code":"USD","created":"2015-09-18 15:20:42 - 400","reward":null,"reward_id":null,"challenge"
:null,"challenge_id":null,"id":10004},{"name":"Anonymous","comment":null,"amount":100.0,"currency_code":"USD","created"
:"2015-09-17 20:51:12 -0400","reward":null,"reward_id":null,"challenge":null,"challenge_id":null,"id":10003},{"name":"J
oe","comment":null,"amount":50.0,"currency_code":"USD","created":"2015-09-17 20:22:47 -0400","reward":null,"reward_id":
null,"challenge":null,"challenge_id":null,"id":10002},{"name":"Mickey","comment":"Awesome game!!","amount":730.0,"curre
ncy_code":"USD","created":"2015-09-17 16:06:21 -0400","reward":null,"reward_id":null,"challenge":null,"challenge_id":nu
ll,"id":10001}]}

This body will be hardcoded as a mock response for most of the tests below to avoid causing unnecessary load on the
Tiltify API.
"""


mock_response_string = '{"campaign_id":"0","owner":"Tilty","owner_img":"https://s3-us-west-2.amazonaws.com/tiltify' \
                       '-production-assets/assets/default_member_avatar.png","mission":"A Perfect Mission","campai' \
                       'gn":"My Awesome Campaign","cause":"A Great Cause","cause_logo_url":"","donation_url":"http' \
                       's://tiltify.com/events/\u003cevent name\u003e/donate","campaign_url":"http://tiltify.com/e' \
                       'vents/\u003cevent name\u003e","banner_url":"","thumbnail":"","description":"This is a grea' \
                       't campaign!","goal":6000.0,"original_fundraiser_goal":0.0,"total_raised":890.0,"percent_ra' \
                       'ised":"15%","top_donor":"Mickey","top_donor_amount":730.0,"starts":"09/16 12:45PM","ends":' \
                       '"09/30 02:00PM","currency_code":"USD","levels":[{"title":"Level 1","amount":10.0},{"title"' \
                       ':"Level 2","amount":20.0}],"rewards":[{"reward_id":"1","always_active":null,"name":"Pictur' \
                       'e of Me","amount":10.0,"kind":null,"quantity":5.0,"remaining":2.0,"fmv":10.0,"starts_at":"' \
                       '2015-09-17 20:22:47 -0400","ends_at":"2015-09-17 22:22:47 -0400","description":"This is a ' \
                       'description.","rules_url":"","shipping_address_required":"true","shipping_note":null,"imag' \
                       'e_url":"http://tiltify.com/image.jpg","currency_code":"USD","donate_url":"http://tiltify.c' \
                       'om/events/\u003cevent name\u003e/donate?event_prize_id=","created":"2015-09-17 16:06:21 -0' \
                       '400"},{"reward_id":"0","always_active":null,"name":"Pushups!","amount":20.0,"kind":null,"q' \
                       'uantity":0.0,"remaining":0.0,"fmv":20.0,"starts_at":"2015-09-17 20:22:47 -0400","ends_at":' \
                       '"2015-09-17 22:22:47 -0400","description":"I will do a pushup.","rules_url":"","shipping_a' \
                       'ddress_required":"false","shipping_note":null,"image_url":"http://tiltify.com/image.jpg",' \
                       '"currency_code":"USD","donate_url":"http://tiltify.com/events/\u003cevent name\u003e/dona' \
                       'te?event_prize_id=","created":"2015-09-17 16:06:21 -0400"}],"activities":[{"name":"activit' \
                       'y 1","starts_at":"2015-09-17 16:06:21 -0400","ends_at":"2015-09-17 16:06:21 -0400","descri' \
                       'ption":null,"image_url":""},{"name":"activity 2","starts_at":"2015-09-17 16:06:21 -0400","' \
                       'ends_at":"2015-09-17 16:06:21 -0400","description":null,"image_url":""}],"challenges":[],"' \
                       'supporting_parent_name":null,"donations":[{"name":"Anonymous","comment":null,"amount":10.0' \
                       ',"currency_code":"USD","created":"2015-09-18 15:20:42 - 400","reward":null,"reward_id":nul' \
                       'l,"challenge":null,"challenge_id":null,"id":10004},{"name":"Anonymous","comment":null,"amo' \
                       'unt":100.0,"currency_code":"USD","created":"2015-09-17 20:51:12 -0400","reward":null,"rewa' \
                       'rd_id":null,"challenge":null,"challenge_id":null,"id":10003},{"name":"Joe","comment":null,' \
                       '"amount":50.0,"currency_code":"USD","created":"2015-09-17 20:22:47 -0400","reward":null,"r' \
                       'eward_id":null,"challenge":null,"challenge_id":null,"id":10002},{"name":"Mickey","comment"' \
                       ':"Awesome game!!","amount":730.0,"currency_code":"USD","created":"2015-09-17 16:06:21 -040' \
                       '0","reward":null,"reward_id":null,"challenge":null,"challenge_id":null,"id":10001}]}'


test_api_key = 'test_479c924413fe9168952891e9a36'


class TestTiltify2Donations:
    tiltify = None

    def setup_method(self):
        self.tiltify = Tiltify2(api_key=test_api_key)

        def return_mock_response(url=None, params=None):
            mock_return = json.loads(mock_response_string)
            if 'rewards' in url:
                return mock_return['rewards']
            elif 'donations' in url:
                return mock_return['donations']
            return mock_return

        self.tiltify.make_request = return_mock_response

    def test_retrieving_all_donations_without_parameters(self):
        donations = self.tiltify.get_donations()
        pprint(donations)
        # Assert number of donations present
        assert 4 == len(donations)
        # Assert they are ordered by ID by default
        for i in range(4, 0):
            assert 10000 + i == donations[i]['id']
