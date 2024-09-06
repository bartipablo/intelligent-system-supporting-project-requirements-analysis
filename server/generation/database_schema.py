import json

from .generate import Generate
from models import DatabaseSchema
from utils.decorators import override
from generation.generate import extract_json
from generation.generate import make_model_from_reply
from models import ComponentIdentify


expected_format = """ Don't return the same values in the database! just be inspired by it!
  "tables": [
    {
      "name": "string",
      "columns": [
        { "name": "string", 
          "type": "string", (int, date, string, boolean)
          "primary_key": "boolean" (true, false),
           "foreign_key": "string"  (foreign key to another table (e.g. book_id) OR null)
        },
      ]
  ],
  "relationships": [
    {
      "from_table": "string",
      "to_table": "string",
      "relationship_type": "string", (one-to-one, one-to-many, many-to-many)
      "on_column": "string"
    }
  ]
"""


class DatabaseSchemaGenerate(Generate):
    def __init__(self):
        super().__init__(
            DatabaseSchema,
            "database schema",
            expected_format,
            ComponentIdentify.DATABASE_SCHEMA,
        )

    @override
    def update_by_ai(self, ai_model, changes_request):
        json_val_format = json.dumps(self.value, default=lambda x: x.__dict__)
        request = ai_model.parse_update_query(
            self.what, json_val_format, changes_request, self.expected_format
        )

        reply = ai_model.make_ai_call(request)
        reply_json_str = extract_json(reply)
        self.value = make_model_from_reply(self.model_class, reply_json_str)

        return self.value