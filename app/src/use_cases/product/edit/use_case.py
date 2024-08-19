from typing import Any, Optional

from app.src.core import Product
from app.src.exceptions.business.product import ProductNotFoundException
from app.src.repositories import ProductRepository
from app.src.exceptions import (
    ProductAlreadyExistsException,
    ProductNoneException,
    ProductRepositoryException,
    ProductBusinessException,
)

from .response import EditProductResponse
from .request import EditProductRequest

class EditProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
        
    def __verify_product_exists(
        self, product: Optional[Product], request_entity_id: str
    ) -> None:
        if product is None:
            raise ProductNotFoundException(product_id=request_entity_id)
        
    def __call__(
        self, request: EditProductRequest
    ) -> Optional[EditProductResponse]:
        try:
            existing_product = self.product_repository.get_by_id(request.product_id)
            
            self.__verify_product_exists(
                existing_product, request_entity_id=request.product_id
            )
            
            self.product_repository.edit(
                product_id=request.product_id,
                name=request.name,
                description=request.description,
                price=request.price,
                location=request.location,
                status=request.status,
                is_available=request.is_available
            )
            
            response = EditProductResponse(
                product_id=request.product_id,
                user_id=request.user_id,
                name=request.name,
                description=request.description,
                price=request.price,
                location=request.location,
                status=request.status,
                is_available=request.is_available
            )
            
            return response

        except ProductNotFoundException as e:
            raise ProductBusinessException(str(e))
        except Exception as e:
            raise ProductRepositoryException(str(e))