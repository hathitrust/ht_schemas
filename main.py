import json
import os
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from jsonschema.exceptions import ValidationError
from pathlib import Path



# referencing.Resource: which represents a specific JSON Schema (often a Python dict) along with
# a specific referencing.Specification it is to be interpreted under.
# referencing.Specification is a class that represents a specific version of
# the JSON Schema specification. => Draft202012Validator

from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012

def register_schemas(path_schema: str = None, uri: str = None):

    #dir_name = os.path.dirname(__file__)
    #schema_dir = os.path.join(dir_name, 'fulltext_schemas')

    with open(path_schema) as f:
        schema_content = json.load(f)

    schema = Resource.from_contents(schema_content)

    registry = Registry().with_resource(uri, schema)

    print(registry.contents(uri=uri))

    return registry

def main(schema_name: str = None, path_schema: str = None, path_document: str = None,
         ht_register: Registry = None):

    with open(path_schema) as f:
        schema = json.load(f)

    with open(path_document) as f:
        document = json.load(f)

    #print(ht_register.contents(uri=f'https://hathitrust.org/fulltext_schemas/fulltext_item_schema'))
    validator = Draft202012Validator(schema, registry=ht_register)

    try:
        #validate(instance=document, schema=schema, )
        validator.validate(document)
        print(f"The document is valid according to the schema {schema_name}")
    except ValidationError as e:
        print(f"The document is invalid according to the schema {schema_name}")
        print(f"Error message: {e.message}")


if __name__ == "__main__":

    # Register the schemas
    dir_name = os.path.dirname(__file__)
    schema_dir = os.path.join(dir_name, 'fulltext_schemas')

    for file in os.listdir(schema_dir):
        print(file)
        if file.endswith(".json"):
            register = register_schemas(path_schema= os.path.join(schema_dir, file),
                         uri=f'https://hathitrust.org/fulltext_schemas/{file}')

    # Validate full_text interface
    main(schema_name="fulltext_item_schema", path_schema=f'{schema_dir}/fulltext_item_schema.json',
         path_document='full_text_json/fulltext_item.json', ht_register=register)

    main(schema_name="fulltext_interface", path_schema=f'{schema_dir}/fulltext_interface_schema.json',
         path_document='full_text_json/fulltext_interface.json', ht_register=register)