from django.db.models.functions import Lower
from django_bm25.indexes import Bm25Index
from . import PostgreSQLTestCase

class Bm25IndexTests(PostgreSQLTestCase):
    def test_deconstruction_no_customization(self):
        index = Bm25Index(name="test_title_%s" % Bm25Index.suffix)
        path, args, kwargs = index.deconstruct()
        self.assertEqual(
            path, "django_bm25.indexes.%s" % Bm25Index.__name__
        )
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_%s" % Bm25Index.suffix,
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_expressions_no_customization(self):
        name = f"test_title_{Bm25Index.suffix}"
        index = Bm25Index(name=name)
        path, args, kwargs = index.deconstruct()
        self.assertEqual(
            path,
            f"django_bm25.indexes.{Bm25Index.__name__}",
        )
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": name,
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            }
        )

    def test_create_with_invalid_text_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                name="test_title_bm25",
                text_fields={"field": { 'invalid_name': 'value' }}
            )
    
    def test_create_with_invalid_numeric_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                name="test_title_bm25",
                numeric_fields={"field": { 'invalid_name': 'value' }}
            )
    
    def test_create_with_invalid_boolean_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                name="test_title_bm25",
                boolean_fields={"field": { 'invalid_name': 'value' }}
            )

    def test_create_with_invalid_json_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                name="test_title_bm25",
                json_fields={"field": { 'invalid_name': 'value' }}
            )
    
    def test_deconstruction(self):
        index = Bm25Index(name="test_title_bm25")
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )
    
    def test_deconstruction_with_text_fields_list(self):
        index = Bm25Index(name="test_title_bm25", text_fields=["title"])
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "text_fields": { "title": {} },
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_text_fields_dict(self):
        index = Bm25Index(
            name="test_title_bm25",
            text_fields={ "title": { "record": "basic", "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "text_fields": { "title": { "record": "basic", "fast": True } },
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_numeric_fields_list(self):
        index = Bm25Index(name="test_title_bm25", numeric_fields=["title"])
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "numeric_fields": { "title": {} },
                "text_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_text_fields_dict(self):
        index = Bm25Index(
            name="test_title_bm25",
            numeric_fields={ "title": { "stored": False, "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "numeric_fields": { "title": { "stored": False, "fast": True } },
                "text_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )


    def test_deconstruction_with_boolean_fields_list(self):
        index = Bm25Index(name="test_title_bm25", boolean_fields=["title"])
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "boolean_fields": { "title": {} },
                "text_fields": {},
                "numeric_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_boolean_fields_dict(self):
        index = Bm25Index(
            name="test_title_bm25",
            boolean_fields={ "title": { "stored": False, "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "boolean_fields": { "title": { "stored": False, "fast": True } },
                "text_fields": {},
                "numeric_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_json_fields_list(self):
        index = Bm25Index(name="test_title_bm25", json_fields=["title"])
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "json_fields": { "title": {} },
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
            },
        )

    def test_deconstruction_with_json_fields_dict(self):
        index = Bm25Index(
            name="test_title_bm25",
            json_fields={ "title": { "stored": False, "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "name": "test_title_bm25",
                "json_fields": { "title": { "stored": False, "fast": True } },
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
            },
        )
