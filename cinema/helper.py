import os
import pathlib
import uuid
from typing import Optional
from django.utils.text import slugify


def movies_image_path(movie: Optional["Movie"], filename: str) -> str:
    filename = (
        f"{slugify(movie.title)}-"
        f"{uuid.uuid4()}"
        f"{pathlib.Path(filename).suffix}"
    )
    return os.path.join("upload-image", filename)
