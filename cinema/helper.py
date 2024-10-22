import os
import pathlib
import uuid

from django.utils.text import slugify
from cinema.models import Movie


def movies_image_path(movie: "Movie", filename: str) -> str:
    filename = (
        f"{slugify(movie.title)}-"
        f"{uuid.uuid4()}"
        f"{pathlib.Path(filename).suffix}"
    )

    return os.path.join("upload-image", filename)
