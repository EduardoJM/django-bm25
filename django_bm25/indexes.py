import json
from django.contrib.postgres.indexes import PostgresIndex

TEXT_FIELD_CONFIGS = [
    'indexed',
    'stored',
    'fast',
    'fieldnorms',
    'tokenizer',
    'record',
    'normalizer'
]

NUMERIC_FIELD_CONFIGS = [
    'indexed',
    'stored',
    'fast',
]

BOOLEAN_FIELD_CONFIGS = [
    'indexed',
    'stored',
    'fast'
]

JSON_FIELD_CONFIGS = [
    'indexed',
    'stored',
    'fast',
    'expand_dots',
    'tokenizer',
    'record',
    'normalizer',
]

class Bm25Index(PostgresIndex):
    suffix = "bm25"
    text_fields = {}
    numeric_fields = {}
    boolean_fields = {}
    json_fields = {}

    def _convert_to_dict(self, list_data):
        data = {}
        for item in list_data:
            data[item] = {}
        return data
    
    def _validate_fields_name(self, data: dict, valid_names: list, property: str):
        if len(data.keys()) == 0:
            return
        for field in data.keys():
            for key in data[field].keys():
                if key not in valid_names:
                    raise AttributeError('Attribute %s is not valid for %s property.' % (key, property))

    def validate_text_fields(self):
        if type(self.text_fields) == list:
            self.text_fields = self._convert_to_dict(self.text_fields)
        self._validate_fields_name(self.text_fields, TEXT_FIELD_CONFIGS, 'text_fields')

    def validate_numeric_fields(self):
        if type(self.numeric_fields) == list:
            self.numeric_fields = self._convert_to_dict(self.numeric_fields)
        self._validate_fields_name(self.numeric_fields, NUMERIC_FIELD_CONFIGS, 'numeric_fields')

    def validate_boolean_fields(self):
        if type(self.boolean_fields) == list:
            self.boolean_fields = self._convert_to_dict(self.boolean_fields)
        self._validate_fields_name(self.boolean_fields, BOOLEAN_FIELD_CONFIGS, 'boolean_fields')

    def validate_json_fields(self):
        if type(self.json_fields) == list:
            self.json_fields = self._convert_to_dict(self.json_fields)
        self._validate_fields_name(self.json_fields, JSON_FIELD_CONFIGS, 'json_fields')

    def __init__(
        self,
        *expressions,
        fields=(),
        name=None,
        text_fields={},
        numeric_fields={},
        boolean_fields={},
        json_fields={},
    ):
        super().__init__(*expressions, fields=fields, name=name)
        
        self.text_fields = text_fields
        self.numeric_fields = numeric_fields
        self.boolean_fields = boolean_fields
        self.json_fields = json_fields
        
        self.validate_text_fields()
        self.validate_numeric_fields()
        self.validate_boolean_fields()
        self.validate_json_fields()

    def _get_with_item(self, name: str, data: dict):
        if len(data.keys()) == 0:
            return []
        return ['%s=\'%s\'' % (name, json.dumps(data))]

    def get_with_params(self):
        fields = ['text_fields', 'numeric_fields', 'boolean_fields', 'json_fields']
        
        params = []
        for field in fields:
            params = params + self._get_with_item(field, getattr(self, field))

        return params
    
    def deconstruct(self):
        path, args, kwargs = super().deconstruct()

        fields = ['text_fields', 'numeric_fields', 'boolean_fields', 'json_fields']
        for field in fields:
            kwargs[field] = getattr(self, field)

        return path, args, kwargs

    """
    def create_sql(self, model, schema_editor, using="", **kwargs):
        self.check_supported(schema_editor)
        sql_create_index = (
            "CREATE INDEX %(name)s ON %(table)s%(using)s "
            "(%(columns)s)%(include)s%(extra)s%(condition)s"
        )
        statement = super().create_sql(
            model, schema_editor, using=" USING %s" % (using or self.suffix), 
            sql=sql_create_index,
            **kwargs
        )
        with_params = self.get_with_params()
        if with_params:
            statement.parts["extra"] = " WITH (%s)%s" % (
                ", ".join(with_params),
                statement.parts["extra"],
            )
        return statement
    """

