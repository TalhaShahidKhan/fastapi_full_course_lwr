from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_invoice_item():
    return {"message": "Create Invoice Item"}


@router.get("/")
async def read_invoice_items():
    return {"message": "Read Invoice Items"}


@router.get("/{invoice_item_id}")
async def read_invoice_item():
    return {"message": "Read Invoice Item"}


@router.put("/{invoice_item_id}")
async def update_invoice_item():
    return {"message": "Update Invoice Item"}


@router.delete("/{invoice_item_id}")
async def delete_invoice_item():
    return {"message": "Delete Invoice Item"}