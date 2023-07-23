from the_startup.custom_cluster import CustomCluster
from the_startup.database.db_mysql import DatabaseProd
from the_startup.services.external_customer.manager import ManagerServices
from the_startup.services.external_customer.resident import ResidentServices
from the_startup.services.external_customer.worker import WorkersServices
from the_startup.services.internal_customer.general import GeneralInternalServices
from the_startup.storage.s3.buckets import S3Storage


class PrivateSubnet(CustomCluster):
    label: str = "Private Subnet"
    direction: str = "LR"

    def __init__(self):
        super().__init__(self.label, self.direction)
        with self:
            self.database = DatabaseProd()
            self.storage = S3Storage()

            self.__resident()
            self.__internal()
            self.__worker()
            self.__manager()

    def __manager(self) -> None:
        self.manager = ManagerServices()
        self.manager.instances >> self.storage.assets
        self.manager.instances >> self.database.rds_prod

    def __worker(self) -> None:
        self.worker = WorkersServices()
        self.worker.instances >> self.storage.assets
        self.worker.instances >> self.database.rds_prod

    def __internal(self) -> None:
        self.internal = GeneralInternalServices()
        self.internal.instances >> self.storage.assets
        self.internal.instances >> self.database.rds_prod

    def __resident(self) -> None:
        self.resident = ResidentServices()
        self.resident.instances >> self.storage.assets
        self.resident.instances >> self.database.rds_prod
