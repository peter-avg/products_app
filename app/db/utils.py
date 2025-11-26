from sqlalchemy import insert, select, delete
from typing import Dict

from ..schemas import ProductSchema
from .schemas import Product, Tag
from ..llm import get_tags

def _insert_tags(engine, product_id: int, tags: Tag) -> None:
    with engine.begin() as conn:
        for tag in tags.tags:
            stmt = insert(Tag).values(
                product_id=product_id,
                tag=tag,
            )
            conn.execute(stmt)


def _create_product(engine, product: ProductSchema) -> Dict:
    with engine.begin() as conn:
        stmt = insert(Product).values(
            name=product.name,
            description=product.description
        ).returning(Product.id)

        ident = conn.execute(stmt).scalar()

    return ident


def create_product(
    engine, product: ProductSchema
) -> Dict[str, str]:
    ident = _create_product(engine, product)

    tags = get_tags(product.description)

    _insert_tags(engine, ident, tags)

    return {"message": "Product created"}


def create_product_with_params(
    engine, name: str, description: str
) -> Dict[str, str]:
    product = ProductSchema(name=name, description=description)

    ident = _create_product(engine, product)

    tags = get_tags(product.description)

    _insert_tags(engine, ident, tags)

    return {"message": "Product created"}


def get_product_by_id(engine, product_id: int) -> Dict:
    with engine.connect() as conn:
        stmt = select(Product).where(Product.c.id == product_id)
        result = conn.execute(stmt).mappings().first()

    return result


def get_all_products(engine) -> Dict:
    with engine.connect() as conn:
        stmt = select(Product)
        result = conn.execute(stmt).mappings().all()

    return result


def delete_product(engine, product_id: int) -> Dict[str, str]:
    with engine.begin() as conn:
        stmt = delete(Product).where(Product.c.id == product_id)
        conn.execute(stmt)

    return {"message": f"Product with id {product_id} deleted"}


def delete_all_products(engine):
    with engine.begin() as conn:
        stmt = delete(Product)
        conn.execute(stmt)

    return {"message": "All products deleted"}


def regenerate_product_tags(engine, product_id: int):
    with engine.connect() as conn:
        stmt = select(Product).where(Product.c.id == product_id)
        result = conn.execute(stmt).mappings().first()

    new_tags = get_tags(result[1])

    with engine.begin() as conn:
        stmt = delete(Tag).where(Tag.product_id == product_id)
        conn.execute(stmt)

    with engine.begin() as conn:
        for tag in new_tags.tags:
            stmt = insert(Tag).values(
                product_id=product_id,
                tag=tag,
            )
            conn.execute(stmt)

    return {"message": f"Tags for product id {product_id} regenerated"}


def get_product_tags(engine, product_id: int) -> Dict:
    with engine.connect() as conn:
        stmt = select(Tag).where(Tag.product_id == product_id)
        result = conn.execute(stmt).mappings().all()

    return result
