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

## Detailed Solr fields

Solr query to get fields that does not exit `-field:[* TO *] ==> -author:["" TO *]`

Miss or empty fields in Solr index: 
* author
* bothPublishDate
* date
* enumPublishDate


Required fields in Solr index:
* title_display
* id
* record_no
* rights

Calculated fields in ls interface:
* bookID => may be possible for an item not to have a book ID - 
            if it is not a Google-scanned item and has no OCLC #, ISBN, or LCCN? 
            But it is probably not currently used in the front end at least for full-text 
            (although there could be some connection to the link in pageturner to the item in google books, 
            or the find in a library link, or something?)
* "useDate" => if the bothPublishDate is empty and date is empty, then useDate does not exist
* date => it will be empty if date is not included in the solr index
* enumDate => it will be empty if enumPublishDate is not included in the solr index
* bothDate => it will be empty if bothPublishDate is not included in the solr index

==> Many of the item fields are not currently used in the front end and could be omitted
    (bookID, EnumDate, BothDate, ABLabel, result_number, relevance, PtSearchHref, PtHref)


## Python libraries for JSON schema

* https://python-jsonschema.readthedocs.io/en/latest/referencing/
* https://builtin.com/software-engineering-perspectives/python-json-schema