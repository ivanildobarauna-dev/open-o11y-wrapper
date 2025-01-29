import os
from pydantic import BaseModel


class ApplicationAttributes(BaseModel):
    application_name: str
    environment: str = os.getenv("__SCOPE__", "Production")
    from_wrapper: bool = True

    def to_dict(self):
        return self.model_dump()