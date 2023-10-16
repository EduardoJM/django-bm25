
class FullTextSearchMixin:
    @classmethod
    def search(cls, query: str, score=True):
        db_table = cls._meta.db_table
        queryset = cls.objects.extra(where=[db_table + " @@@ %s"], params=[query])
        
        if not score:
            return queryset
        
        queryset = queryset.extra(select={
            'score': 'paradedb.rank_bm25(ctid)',
        })

        return queryset
