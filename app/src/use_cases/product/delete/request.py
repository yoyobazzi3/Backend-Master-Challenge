# request.py
from decimal import Decimal

from typing import NamedTuple

class DeleteProductRequest(NamedTuple):
    product_id: str