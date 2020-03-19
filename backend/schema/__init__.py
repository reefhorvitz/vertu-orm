from .property_metadata import Query as PropertyMetadataQuery
from .property import Query as PropertyQuery
from .appointment import Query as AppointmentQuery
from .common import Query as CommonQuery
from .user import Query as UserQuery


class Query(PropertyMetadataQuery, PropertyQuery, AppointmentQuery, CommonQuery, UserQuery):
    pass
