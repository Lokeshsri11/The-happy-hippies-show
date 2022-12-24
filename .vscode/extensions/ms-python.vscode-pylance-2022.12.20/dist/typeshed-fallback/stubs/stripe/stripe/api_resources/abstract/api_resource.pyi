from _typeshed import Self
from typing import Any

from stripe import api_requestor as api_requestor, error as error
from stripe.stripe_object import StripeObject as StripeObject

class APIResource(StripeObject):
    @classmethod
    def retrieve(cls: type[Self], id, api_key: Any | None = ..., **params) -> Self: ...
    def refresh(self: Self) -> Self: ...
    @classmethod
    def class_url(cls) -> str: ...
    def instance_url(self) -> str: ...
