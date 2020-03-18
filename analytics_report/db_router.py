
class DatabaseRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to db_frendy.
        """
        return 'db_frendy'
