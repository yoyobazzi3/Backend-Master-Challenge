from decimal import Decimal

from typing import NamedTuple

from ....core import ProductStatuses


class DeleteProductResponse(NamedTuple):
    message: str