class vulnerabilitiesDB_router:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'search':
            return 'vulnerabilitiesDB'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'search':
            return 'vulnerabilitiesDB'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._state.db == 'vulnerabilitiesDB' or
            obj2._state.db == 'vulnerabilitiesDB'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'vulnerabilitiesDB':
            return app_label == 'search'
        elif app_label == 'search':
            return False
        return None