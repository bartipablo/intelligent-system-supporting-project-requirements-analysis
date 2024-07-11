import ray

from typing import List
from pydantic import BaseModel

from server.models.models import generate_model, save_model_to_database
from server.modules.title.routes import TitleModule


class TitleModel(BaseModel):
    names: List[str]


@ray.remote
def generate_title(for_who: str, doing_what: str, additional_info: str) -> TitleModel:
    return generate_model(TitleModule, for_who, doing_what, additional_info, TitleModel)


@ray.remote
def save_title_to_database(project_id: str, collection, model: TitleModel):
    save_model_to_database(project_id, collection, "tite", model)