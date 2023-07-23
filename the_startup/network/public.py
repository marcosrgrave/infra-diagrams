from diagrams.aws.network import APIGateway

from the_startup.custom_cluster import CustomCluster


class PublicSubnet(CustomCluster):
    label: str = "Public Subnet"
    direction: str = "LR"

    def __init__(self):
        super().__init__(self.label, self.direction)
        with self:
            self.gateway = APIGateway("API Gateway")
