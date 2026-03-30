from clean_lab.infrastructure.sql_repo import SqlOrderRepository

class SqlUnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.orders = SqlOrderRepository(self.session)
        return self

    def __exit__(self, *args):
        self.session.close()

    def commit(self):
        self.session.commit()