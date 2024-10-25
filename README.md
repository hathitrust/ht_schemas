## Best Practices for Creating a JSON Schema

Below, you will find some of the good practices we should follow to create a JSON schema. 
We are following this guideline on ls front-end/back-end decoupling project.

We use the JSON schema to define the structure of the data and the validation rules for JSON data. 

* Provide clear titles and descriptions for your schema and its properties to make it easier to understand.
* Specify which properties are required to ensure that the JSON data includes all necessary information.
* Define the correct data types for each property (e.g., string, number, object, array, boolean, null).
* Use constraints like minLength, maxLength, minimum, maximum, pattern, etc., to enforce rules on the data.
* Use the enum keyword to specify a set of allowed values for a property.
* Clearly define the structure of nested objects and arrays, including their properties and constraints.
* Use `$ref` to reference reusable schema definitions to avoid duplication and maintain consistency.
* Include a version number in your schema to manage changes and ensure compatibility.
* Use tools to validate your schema against sample data to ensure it works as expected.
* Provide documentation or examples to help users understand how to use the schema.