from models.db import db
from sqlalchemy.orm import Mapped, mapped_column


class Contact(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(128), unique=False, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(128), unique=False, nullable=False)

