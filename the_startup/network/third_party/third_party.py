from the_startup.custom_cluster import CustomCluster
from the_startup.network.third_party.firebase import Firebase


class ThirdParty(CustomCluster):
    label: str = "Third Party"
    direction: str = "LR"

    def __init__(self):
        super().__init__(self.label, self.direction)
        with self:
            self.firebase = Firebase()
