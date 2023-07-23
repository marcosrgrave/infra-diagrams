from diagrams.aws.storage import S3

from the_startup.custom_cluster import CustomCluster


class S3Storage(CustomCluster):
    label: str = "S3 Storage"
    direction: str = "LR"

    def __init__(self):
        super().__init__(self.label, self.direction)
        with self:
            self.assets = S3("Assets")
