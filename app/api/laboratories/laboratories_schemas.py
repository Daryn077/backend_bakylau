from pydantic import BaseModel
from typing import List


class ResearcherRead(BaseModel):
    id: int
    full_name: str
    degree: str

    class Config:
        from_attributes = True


class LaboratoryCreate(BaseModel):
    name: str
    specialization: str
    university_id: int


class LaboratoryRead(BaseModel):
    id: int
    name: str
    specialization: str
    university_id: int
    researchers: List[ResearcherRead] = []

    class Config:
        from_attributes = True