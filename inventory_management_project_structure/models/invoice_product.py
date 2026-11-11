from datetime import datetime, timezone

from models.base import Base
from sqlalchemy import TIMESTAMP, BigInteger, Column, Double, ForeignKey, String
from sqlalchemy.orm import relationship


class InvoiceProduct(Base):
    __tablename__ = "invoice_products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("products.id"), nullable=False)
    invoice_id = Column(BigInteger, ForeignKey("invoices.id"), nullable=False)
    qty = Column(Double, nullable=False)
    sale_price = Column(Double, nullable=False)

    create_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationship
    invoices = relationship("Invoice", back_populates="invoice_products")
    products = relationship("Product", back_populates="invoice_products")
    users = relationship("User", back_populates="invoice_products")
