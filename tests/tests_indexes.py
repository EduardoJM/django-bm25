from django.db.models import CharField, F, Index
from django.db.models.expressions import Expression
from django.db.models.functions import Cast, Collate, Length, Lower
from django_bm25.indexes import Bm25Index
from . import PostgreSQLSimpleTestCase
from .models import CharFieldModel

class Star(Expression):
    def __repr__(self):
        return "'*'"

    def as_sql(self, compiler, connection):
        db_table = compiler.query.get_meta().db_table
        return "%s.*" % db_table, []

class IndexTestMixin:
    def test_name_auto_generation(self):
        index = self.index_class(fields=["field"])
        index.set_name_with_model(CharFieldModel)
        self.assertRegex(
            index.name, r"tests_charf_field_[0-9a-f]{6}_%s" % self.index_class.suffix
        )

    def test_deconstruction_no_customization(self):
        index = self.index_class(
            fields=["title"], name="test_title_%s" % self.index_class.suffix
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(
            path, "django_bm25.indexes.%s" % self.index_class.__name__
        )
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_%s" % self.index_class.suffix,
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_expressions_no_customization(self):
        name = f"test_title_{self.index_class.suffix}"
        index = self.index_class(Lower("title"), name=name)
        path, args, kwargs = index.deconstruct()
        self.assertEqual(
            path,
            f"django_bm25.indexes.{self.index_class.__name__}",
        )
        self.assertEqual(args, (Lower("title"),))
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


class Bm25IndexTests(IndexTestMixin, PostgreSQLSimpleTestCase):
    index_class = Bm25Index

    def test_create_with_invalid_text_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                fields=["field"],
                name="test_title_bm25",
                text_fields={"field": { 'invalid_name': 'value' }}
            )
    
    def test_create_with_invalid_numeric_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                fields=["field"],
                name="test_title_bm25",
                numeric_fields={"field": { 'invalid_name': 'value' }}
            )
    
    def test_create_with_invalid_boolean_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                fields=["field"],
                name="test_title_bm25",
                boolean_fields={"field": { 'invalid_name': 'value' }}
            )

    def test_create_with_invalid_json_fields_property(self):
        with self.assertRaises(AttributeError):
            Bm25Index(
                fields=["field"],
                name="test_title_bm25",
                json_fields={"field": { 'invalid_name': 'value' }}
            )
    
    def test_deconstruction(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )
    
    def test_deconstruction_with_text_fields_list(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            text_fields=["title"]
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "text_fields": { "title": {} },
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_text_fields_dict(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            text_fields={ "title": { "record": "basic", "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "text_fields": { "title": { "record": "basic", "fast": True } },
                "numeric_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_numeric_fields_list(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            numeric_fields=["title"]
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "numeric_fields": { "title": {} },
                "text_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_text_fields_dict(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            numeric_fields={ "title": { "stored": False, "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "numeric_fields": { "title": { "stored": False, "fast": True } },
                "text_fields": {},
                "boolean_fields": {},
                "json_fields": {},
            },
        )


    def test_deconstruction_with_boolean_fields_list(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            boolean_fields=["title"]
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "boolean_fields": { "title": {} },
                "text_fields": {},
                "numeric_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_boolean_fields_dict(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            boolean_fields={ "title": { "stored": False, "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "boolean_fields": { "title": { "stored": False, "fast": True } },
                "text_fields": {},
                "numeric_fields": {},
                "json_fields": {},
            },
        )

    def test_deconstruction_with_json_fields_list(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            json_fields=["title"]
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "json_fields": { "title": {} },
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
            },
        )

    def test_deconstruction_with_json_fields_dict(self):
        index = Bm25Index(
            fields=["title"],
            name="test_title_bm25",
            json_fields={ "title": { "stored": False, "fast": True } }
        )
        path, args, kwargs = index.deconstruct()
        self.assertEqual(path, "django_bm25.indexes.Bm25Index")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {
                "fields": ["title"],
                "name": "test_title_bm25",
                "json_fields": { "title": { "stored": False, "fast": True } },
                "text_fields": {},
                "numeric_fields": {},
                "boolean_fields": {},
            },
        )

    def test_sql(self):
        index = Bm25Index(
            Star(),
            name='idx_city_name',
            text_fields=['field',]
        )
        from django.db import connection
        with connection.schema_editor() as schema_editor:
            print(
                index.create_sql(CharFieldModel, schema_editor)
            )
