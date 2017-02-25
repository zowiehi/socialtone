
from django.conf import settings
from yelp.client import Client


def _scrape_yelp(query):
    client = Client(settings.YELP_AUTH)
    results = client.search('Phoenix', term=query).businesses
    reviews = list(map(lambda x: client.get_business(x.id).business.reviews[0].excerpt, results))
    return reviews
