import ray

from typing import List
from pydantic import BaseModel

from server.models.models import generate_model, save_model_to_database
from server.modules.database_schema.routes import DatabaseSchemaModule


class DatabaseSchemaModel(BaseModel):
    schema: List[dict[str, dict[str, str]]]
    relationships: List[str]


@ray.remote
def generate_database_schema(for_who: str, doing_what: str, additional_info: str) -> DatabaseSchemaModel:
    return generate_model(DatabaseSchemaModule, for_who, doing_what, additional_info, DatabaseSchemaModel)


@ray.remote
def save_database_schema_to_database(project_id: str, collection, model: DatabaseSchemaModel):
    save_model_to_database(project_id, collection, "database_schema", model)