from abc import ABC, abstractmethod
from diagrams import Cluster
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3


class CustomCluster(ABC, Cluster):
    @property
    @abstractmethod
    def label(self) -> str:
        ...

    @property
    @abstractmethod
    def direction(self) -> str:
        ...


class ClusterBuilder(Cluster):
    def __init__(
        self,
        contents: list[CustomCluster],
        label: str = "cluster",
        direction: str = "LR",
    ):
        super().__init__(label, direction)
        with self:
            for content in contents:
                content()


class MyCluster(CustomCluster):
    def __init__(self) -> None:
        self.rds_prod = RDS("RDS")
        self.aws_s3 = S3("S3 Bucket")
