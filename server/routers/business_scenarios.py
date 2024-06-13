from fastapi import APIRouter, HTTPException
from bson import ObjectId
from server.models import BusinessScenariosModel
from server.database import project_collection
from server.modules.business_scenarios.routes import BusinessModule
from server.utils.openaiUtils import Model
from pymongo import ReturnDocument
import json

router = APIRouter(
    tags=["business_scenarios"],
    prefix="/business_scenarios",
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/{project_id}",
)
async def get_business_scenarios(project_id: str):
    if (
        project := await project_collection.find_one({"_id": ObjectId(project_id)})
    ) is not None:
        business_scenarios = project["business_scenarios"]
        return business_scenarios
    else:
        raise HTTPException(status_code=404, detail=f"Project {project_id} not found")

@router.post("/generate/{project_id}")
async def generate_business_scenarios(project_id: str):
    project = await project_collection.find_one({"_id": ObjectId(project_id)})
    if project:
        business_scenarios = BusinessModule(Model.GPT3)
        forWho = project["for_who"]
        doingWhat = project["doing_what"]
        content = business_scenarios.get_content(forWho, doingWhat, False)
        data = json.loads(content.choices[0].message.content)
        business_scenarios_model = BusinessScenariosModel(**data)
        project["business_scenarios"] = business_scenarios_model.dict()
        await project_collection.find_one_and_update(
            {"_id": ObjectId(project_id)},
            {"$set": project},
            return_document=ReturnDocument.AFTER,
        )
        return business_scenarios_model
    raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
