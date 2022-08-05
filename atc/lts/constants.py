from enum import Enum


class ServiceRequestStatus(Enum):
    request = 'Open Request'
    offer = 'Received Offer'
    agreement = 'Agreement'


SERVICE_STATUS_CHOICES = ((c.name, c.value) for c in ServiceRequestStatus)
