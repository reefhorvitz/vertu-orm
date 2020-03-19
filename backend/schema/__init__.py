from .property_metadata import Query as PropertyMetadataQuery
from .property import Query as PropertyQuery


class Query(PropertyMetadataQuery, PropertyQuery):
    pass
