# Tiltify v2 API wrapper for Python 3

A wrapper for the 2nd version of the API provided by https://tiltify.com, an awesome site to combine fundraising and livestreaming.

## Supported Python Versions

* 3.*

## Tested Versions

* 3.5

## Installation

`pip3 install tiltify2`

## Usage

Import the Tiltify object from the library of the version you wish to use.

`from tiltify2.tiltify import Tiltify`

Initialise an instance using your API key retrieved from [Tiltify](https://tiltify.com/). You can also state a timeout (in seconds) if you wish

`tiltfy = Tiltify(api_key=my_api_key, timeout=2)`

Retrieve donations, with option parameters `limit`, `order_by` and/or `donation_order`.

`from tiltify2.tiltify import Tiltify2, Order`

`tiltfy = Tiltify(api_key=my_api_key, timeout=2)`


`five_donations_starting_from_latest_time_created = tiltify.get_donations(limit=2, donation_order=Order.DESC, order_by=Order.CREATED_AT)`

## Contributions

If you wish to contribute - simply open a branch from `develop` then open a Pull Request back into `develop` with your changes. Here are various items which I did not add in the initial version:

* Methods to retrieve data about awards
* Methods to retrieve data about the campaign
* Methods to order donations by values other than ID, Amount and Time Created
* Async option
* Setting up Travis for CI

## Credits

Initial version written by [Purrcat259](www.github.com/purrcat259), for use within the [Charitybot Project](https://github.com/purrcat259/charitybot2) 
during [Special Effect](http://www.specialeffect.org.uk/)'s [One Special Day](http://www.onespecialday.org.uk/) event.

## Licence

MIT Licence
