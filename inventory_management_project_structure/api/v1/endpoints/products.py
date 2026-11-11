from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_product():
    return {"message": "Create Product"}


@router.get("/")
async def read_products():
    return {"message": "Read Products"}


@router.get("/{product_id}")
async def read_product():
    return {"message": "Read Product"}


@router.put("/{product_id}")
async def update_product():
    return {"message": "Update Product"}


@router.delete("/{product_id}")
async def delete_product():
    return {"message": "Delete Product"}