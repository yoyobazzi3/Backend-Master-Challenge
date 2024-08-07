# request.py
from decimal import Decimal

from typing import NamedTuple

from ....core import ProductStatuses
class DeleteProductRequest(NamedTuple):
    product_id: str