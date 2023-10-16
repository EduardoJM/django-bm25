from typing import Any
from django.db.models import Lookup

class FullTextSearchLookup(Lookup):
    lookup_name = 'ftsearch'

    def get_prep_lookup(self) -> Any:
        print("OIEE???")
        return super().get_prep_lookup()

    def as_sql(self, compiler, connection):
        print("AQUI???")
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "%s @@@ %s" % (lhs, rhs), params
