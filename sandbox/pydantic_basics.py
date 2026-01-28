import uuid

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
  

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel,populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(alias='title')
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


course_default_model = CourseSchema(
    id= 'Course_id',
    title = 'Playwright',
    maxScore = 100,
    minScore = 10,
    description = 'Playwright',
    estimatedTime = '1 week',
)

print(course_default_model)

course_dict = {
    "id": "Course 1",
    "title": "Course 1",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week",
  }

course_dict_model = CourseSchema(**course_dict)
print(course_dict_model)

course_json = """{
    "id": "Course 1",
    "title": "Course 1",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
  }"""

course_json_model = CourseSchema.model_validate_json(course_json)
print(course_json_model)


course_json_1 = course_json_model.model_dump_json(by_alias=True)
print(course_json_1)