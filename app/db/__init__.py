from .utils import (
    create_product,
    create_product_with_params,
    get_product_by_id,
    get_all_products,
    regenerate_product_tags,
    delete_product,
    delete_all_products,
    get_product_tags,
)

from .config import ENGINE, BASE

BASE.metadata.create_all(ENGINE)

__all__ = [
    "ENGINE",
    "create_product",
    "create_product_with_params",
    "get_product_by_id",
    "get_all_products",
    "regenerate_product_tags",
    "delete_product",
    "delete_all_products",
    "get_product_tags",
]
