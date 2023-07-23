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
            self.database_prod = self.database.rds_prod

            self.storage = S3Storage()
            self.s3_bucket = self.storage.assets

            self.resident()
            self.internal()
            self.worker()
            self.manager()

    def manager(self) -> None:
        self.manager = ManagerServices()
        self.manager.instances >> self.s3_bucket
        self.manager.instances >> self.database_prod

    def worker(self) -> None:
        self.worker = WorkersServices()
        self.worker.instances >> self.s3_bucket
        self.worker.instances >> self.database_prod

    def internal(self) -> None:
        self.internal = GeneralInternalServices()
        self.internal.instances >> self.s3_bucket
        self.internal.instances >> self.database_prod

    def resident(self) -> None:
        self.resident = ResidentServices()
        self.resident.instances >> self.s3_bucket
        self.resident.instances >> self.database_prod
