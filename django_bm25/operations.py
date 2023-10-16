from django.contrib.postgres.operations import CreateExtension

class Bm25Extension(CreateExtension):
    def __init__(self):
        self.name = "pg_bm25"
