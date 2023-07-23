from diagrams.firebase.develop import Authentication

from the_startup.custom_cluster import CustomCluster


class Firebase(CustomCluster):
    label: str = "Firebase"
    direction: str = "LR"

    def __init__(self):
        super().__init__(self.label, self.direction)
        with self:
            self.authentication = Authentication("Authentication")
