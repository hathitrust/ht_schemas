import json
import os
from jsonschema.validators import Draft202012Validator
from jsonschema.exceptions import ValidationError

# referencing.Resource: which represents a specific JSON Schema (often a Python dict) along with
# a specific referencing.Specification it is to be interpreted under.
# referencing.Specification is a class that represents a specific version of
# the JSON Schema specification. => Draft202012Validator

from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

def create_schema_reference(schema_directory: str):
    """
    Set up the jsonschema validator to load local files
    :param schema_directory: The folder containing the schemas
    :return: The schema reference.
    Each schema is a tuple with the schema id and the schema content
    """
    ht_references = []
    for file in os.listdir(schema_directory):
        if file.endswith(".json"):
            print(f'https://hathitrust.org/fulltext_schemas/{file}')
            with open(os.path.join(schema_directory, file)) as f:
                schema_content = json.load(f)
                ht_references.append((schema_content['$id'], Resource.from_contents(schema_content, DRAFT202012)))

    return ht_references

def register_schemas(ht_references: list = None):

    ht_registry = Registry()
    for reference in ht_references:
        ht_registry = ht_registry.with_resource(reference[0], reference[1])
    return ht_registry

def validate_schema(path_schema: str = None, path_document: str = None,
         default_register: Registry = None):

    schema_name = os.path.basename(path_schema)

    with open(path_schema) as f:
        schema = json.load(f)

    with open(path_document) as f:
        document = json.load(f)

    validator = Draft202012Validator(schema, registry=default_register)

    try:
        validator.validate(document)
        print(f"The document is valid according to the schema {schema_name}")
    except ValidationError as e:
        print(f"The document is invalid according to the schema {schema_name}")
        print(f"Error message: {e.message}")


if __name__ == "__main__":

    # Register the schemas
    dir_name = os.path.dirname(__file__)
    schema_dir = os.path.join(dir_name, 'fulltext_schemas')

    references = create_schema_reference(schema_directory=schema_dir)

    ht_register = register_schemas(ht_references=references)

    # Validate full_text item
    validate_schema(path_schema=f'{schema_dir}/each_document.json',
                    path_document='fulltext_json/each_document.json', default_register=ht_register)

    # Validate full_text each facets
    validate_schema(path_schema=f'{schema_dir}/facets.json',
                    path_document='fulltext_json/facets.json', default_register=ht_register)

    # Validate full_text list of facets
    validate_schema(path_schema=f'{schema_dir}/all_facets.json',
                    path_document='fulltext_json/all_facets.json', default_register=ht_register)

    # Validate full_text interface
    validate_schema(path_schema=f'{schema_dir}/output_interface.json',
                    path_document='fulltext_json/output_interface.json', default_register=ht_register)