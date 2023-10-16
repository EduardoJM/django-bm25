from django.db.models.expressions import Expression

class TableStar(Expression):
    def __repr__(self):
        return "'*'"

    def as_sql(self, compiler, connection):
        db_table = compiler.query.get_meta().db_table
        return "%s.*" % db_table, []
