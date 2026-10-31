"""Plain REST endpoints for listings — no AI involved."""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..db import Property, get_session, search_properties

router = APIRouter(prefix="/properties", tags=["properties"])


@router.get("", response_model=list[Property])
def list_properties(
    city: str | None = None,
    property_type: str | None = None,
    listing_type: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    min_bedrooms: int | None = None,
    limit: int = 50,
    session: Session = Depends(get_session),
):
    return search_properties(
        session, city, property_type, listing_type, min_price, max_price, min_bedrooms, limit
    )


@router.get("/{property_id}", response_model=Property)
def get_property(property_id: int, session: Session = Depends(get_session)):
    prop = session.get(Property, property_id)
    if prop is None:
        raise HTTPException(404, "Property not found")
    return prop


@router.post("", response_model=Property, status_code=201)
def create_property(prop: Property, session: Session = Depends(get_session)):
    prop.id = None
    session.add(prop)
    session.commit()
    session.refresh(prop)
    return prop
