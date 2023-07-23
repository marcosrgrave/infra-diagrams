from diagrams import Cluster
from diagrams.aws.database import RDS


class DatabaseProd:
    def __init__(self) -> None:
        with Cluster("Database Prod"):
            self.rds_prod = RDS("RDS")
