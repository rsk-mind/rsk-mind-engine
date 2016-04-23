import geoip2.database


class GeoipCountryWrapper(object):

    """Wrapper for countries in geoip2.

    This class reads the GeoLite2 database and
    exposes some fields of the country model.
    """

    def __init__(self):
        """Create an object."""
        # reader for database
        self.reader = geoip2.database.Reader(
            './fraud_backend/countries_db/GeoLite2-Country.mmdb'
        )
        # an array of tuples (country.geoname_id, country.iso_code)
        self.countries_list = []

    def country(self, ip):
        """Get an object of type `Country`."""
        data = self.reader.country(ip)
        entry = (data.country.geoname_id, data.country.iso_code)
        self.countries_list.append(entry)
        return data

    def geoname_id(self, ip):
        """ Get geoname_id of country of ip."""
        data = self.country(ip)
        return data.country.geoname_id
