from datetime import datetime, timezone

from models.base import Base
from sqlalchemy import TIMESTAMP, BigInteger, Column, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    mobile = Column(String, nullable=False)
    password = Column(String, nullable=False)
    otp = Column(String, nullable=False)
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
    categories = relationship("Category", back_populates="user")
    products = relationship("Product", back_populates="user")
    invoices = relationship("Invoice", back_populates="user")
    invoice_products = relationship("InvoiceProduct", back_populates="user")
    customers = relationship("Customer", back_populates="user")
