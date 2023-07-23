from diagrams import Diagram
from the_startup.network.private import PrivateSubnet
from the_startup.network.public import PublicSubnet
from the_startup.network.third_party.third_party import ThirdParty


class TheStartupDiagram:
    def __init__(self) -> None:
        with Diagram("The Startup Infrastructure", show=True, direction="TB"):
            PublicSubnet()
            ThirdParty()
            PrivateSubnet()
