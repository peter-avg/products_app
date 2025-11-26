from fastapi import FastAPI, HTTPException

from .schemas import ProductSchema
from app.db import (
        ENGINE,
        create_product,
        create_product_with_params,
        get_product_by_id,
        get_all_products,
        regenerate_product_tags,
        delete_all_products,
        delete_product,
        get_product_tags,
)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/products")
async def create_product_route(product: ProductSchema):
    try:
        return create_product(ENGINE, product)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/products/{name}/{description}")
async def create_product_route_params(name: str, description: str):
    try:
        return create_product_with_params(ENGINE, name, description)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/products/{product_id}")
async def get_product_by_id_route(product_id: int):
    try:
        product = get_product_by_id(ENGINE, product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")

        return product

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/products")
async def get_all_products_route():
    try:
        return get_all_products(ENGINE)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/products/{product_id}/regenerate_tags")
async def regenerate_product_tags_route(product_id: int):
    try:
        return regenerate_product_tags(ENGINE, product_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/products/{product_id}")
async def delete_product_route(product_id: int):
    try:
        return delete_product(ENGINE, product_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_all")
async def delete_all_products_route():
    try:
        return delete_all_products(ENGINE)

    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))


@app.get("/tags/{product_id}")
async def get_product_tags_route(product_id: int):
    try:
        return get_product_tags(ENGINE, product_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
