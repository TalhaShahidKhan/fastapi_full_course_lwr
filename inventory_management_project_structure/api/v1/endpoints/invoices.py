from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_invoice():
    return {"message": "Create Invoice"}


@router.get("/")
async def read_invoices():
    return {"message": "Read Invoices"}


@router.get("/{invoice_id}")
async def read_invoice():
    return {"message": "Read Invoice"}


@router.put("/{invoice_id}")
async def update_invoice():
    return {"message": "Update Invoice"}


@router.delete("/{invoice_id}")
async def delete_invoice():
    return {"message": "Delete Invoice"}