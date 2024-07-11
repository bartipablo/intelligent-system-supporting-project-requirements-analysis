import ray

from pydantic import BaseModel
from typing import List

from server.models.models import generate_model, save_model_to_database
from server.modules.business_scenarios.routes import BusinessModule


class FeatureModel(BaseModel):
    feature_name: str
    description: str


class BusinessScenarioModel(BaseModel):
    title: str
    description: str
    features: List[FeatureModel]


class BusinessScenariosModel(BaseModel):
    business_scenario: BusinessScenarioModel


@ray.remote
def generate_business_scenarios(for_who: str, doing_what: str, additional_info: str) -> BusinessScenariosModel:
    return generate_model(BusinessModule, for_who, doing_what, additional_info, BusinessScenariosModel)


@ray.remote
def save_business_scenarios_to_database(project_id: str, collection, model: BusinessScenariosModel):
    save_model_to_database(project_id, collection, "business_scenarios", model)