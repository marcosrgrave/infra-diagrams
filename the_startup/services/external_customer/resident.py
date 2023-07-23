from diagrams import Cluster
from diagrams.aws.compute import EC2AutoScaling
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB


class ResidentServices:
    def __init__(self) -> None:
        with Cluster("Resident Services"):
            self.lb = ELB("LoadBalancer")
            self.auto_scaling = EC2AutoScaling("Auto Scaling")

            with Cluster("Auto Scalling Instances"):
                self.instances = [
                    EC2("Instance 1"),
                    EC2("Instance 2"),
                    EC2("Instance 3"),
                ]

        self.lb >> self.auto_scaling >> self.instances
