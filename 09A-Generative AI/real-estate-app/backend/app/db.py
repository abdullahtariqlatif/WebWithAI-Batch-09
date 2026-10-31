"""SQLite database (via SQLModel) holding the property listings."""

import json
from collections.abc import Iterator

from sqlmodel import Field, Session, SQLModel, create_engine, select

from .config import DATA_DIR, get_settings


class Property(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    city: str = Field(index=True)
    neighborhood: str
    property_type: str = Field(index=True)  # house | apartment | condo | townhouse | plot
    listing_type: str = Field(index=True)  # sale | rent
    price: float  # sale price, or monthly rent
    bedrooms: int
    bathrooms: float
    area_sqft: int
    year_built: int | None = None
    amenities: str = ""  # comma-separated
    description: str


engine = create_engine(get_settings().database_url, connect_args={"check_same_thread": False})


def init_db() -> None:
    """Create tables and load sample listings the first time the app starts."""
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if session.exec(select(Property)).first() is None:
            rows = json.loads((DATA_DIR / "properties.json").read_text())
            session.add_all(Property(**row) for row in rows)
            session.commit()


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session


def search_properties(
    session: Session,
    city: str | None = None,
    property_type: str | None = None,
    listing_type: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    min_bedrooms: int | None = None,
    limit: int = 20,
) -> list[Property]:
    """Filter listings. Shared by the REST API and the AI agent's tool."""
    query = select(Property)
    if city:
        query = query.where(Property.city.ilike(f"%{city}%"))
    if property_type:
        query = query.where(Property.property_type == property_type.lower())
    if listing_type:
        query = query.where(Property.listing_type == listing_type.lower())
    if min_price is not None:
        query = query.where(Property.price >= min_price)
    if max_price is not None:
        query = query.where(Property.price <= max_price)
    if min_bedrooms is not None:
        query = query.where(Property.bedrooms >= min_bedrooms)
    return list(session.exec(query.order_by(Property.price).limit(limit)))
