from diagrams import Diagram
from the_startup.network.private import PrivateSubnet


class TheStartupDiagram:
    def __init__(self) -> None:
        with Diagram("The Startup Infrastructure", show=True, direction="TB"):
            # ThirdParty()
            # PublicSubnet()
            PrivateSubnet()
