from diagrams import Diagram

from the_startup.network.private import PrivateSubnet
from the_startup.network.public import PublicSubnet
from the_startup.network.third_party.third_party import ThirdParty


class TheStartupDiagram:
    def __init__(self) -> None:
        with Diagram("The Startup Infrastructure", show=False, direction="TB"):
            public = PublicSubnet()

            third_party = ThirdParty()
            public.gateway >> third_party.firebase.authentication
            third_party.firebase.authentication >> public.gateway

            private = PrivateSubnet()
            public.gateway >> private.resident.lb
            public.gateway >> private.internal.lb
            public.gateway >> private.manager.lb
            public.gateway >> private.worker.lb
