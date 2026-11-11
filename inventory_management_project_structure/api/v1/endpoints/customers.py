from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_customer():
    return {"message": "Create Customer"}


@router.get("/")
async def read_customers():
    return {"message": "Read Customers"}


@router.get("/{customer_id}")
async def read_customer():
    return {"message": "Read Customer"}


@router.put("/{customer_id}")
async def update_customer():
    return {"message": "Update Customer"}


@router.delete("/{customer_id}")
async def delete_customer():
    return {"message": "Delete Customer"}