from .endpoints import auth, customers, categories, dashboard, invoices, invoice_items, users, products
from fastapi import APIRouter
router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Auth"])

router.include_router(users.router, prefix="/users", tags=["Users"])

router.include_router(categories.router,prefix="/categories", tags=["Categories"])

router.include_router(customers.router,prefix="/customers",tags=["Customers"])

router.include_router(products.router,prefix="/products",tags=["Products"])

router.include_router(invoices.router,prefix="/invoices",tags=["Invoices"])

router.include_router(invoice_items.router,prefix="/invoice-items",tags=["Invoice_items"])

router.include_router(dashboard.router,prefix="/dashboard",tags=["Dashboard"])

