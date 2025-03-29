# BaseApp/schemas.py
from pydantic import BaseModel, field_validator, HttpUrl
from datetime import date

class StarCreate(BaseModel):
    name: str
    bio: str | None = None
    birth_date: date
    profession: str
    country: str | None = None
    photo_url: HttpUrl | None = None

    @field_validator('birth_date')
    def validate_birth_date(cls, value):
        today = date.today()
        if value > today:
            raise ValueError("Дата рождения не может быть в будущем")
        return value