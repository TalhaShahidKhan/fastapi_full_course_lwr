from datetime import datetime, timezone

from models.base import Base
from sqlalchemy import TIMESTAMP, BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

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
    users = relationship("User", back_populates="category")
    products = relationship("Product", back_populates="category")
