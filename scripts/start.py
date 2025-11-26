from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
from enum import StrEnum
from logging import getLogger
from os import startfile
from sys import argv

logger = getLogger(__name__)


class Client(StrEnum):
    DMM = "dmm"
    JOHREN = "johren"
    STEAM = "steam"
    STEAM_JP = "steam_jp"

    def get_uri(self, steam_id: int | None) -> str:
        uri = None
        if steam_id is None:
            match self:
                case Client.DMM:
                    uri = "dmmgameplayer://play/GCL/doaxvv/cl/win"
                case Client.JOHREN:
                    uri = "johren-launcher://mygame?titleId=doaxvv"
                case Client.STEAM:
                    uri = "steam://rungameid/958260"
                case Client.STEAM_JP:
                    uri = "steam://rungameid/1361350"
        else:
            match self:
                case Client.STEAM:
                    uri = rf"tcno:\\s:{steam_id} -silent steam://rungameid/958260"
                case Client.STEAM_JP:
                    uri = rf"tcno:\\s:{steam_id} -silent steam://rungameid/1361350"
        if uri is None:
            raise NotImplementedError
        return uri


def start(client: Client, steam_id: int | None) -> None:
    uri = client.get_uri(steam_id)
    logger.warning("uri=%s", uri)
    startfile(uri)  # noqa: S606


def main() -> None:
    logger.warning("argv=%s", argv)
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--client", default=Client.STEAM, type=Client, choices=Client, help="Client type")
    parser.add_argument("-s", "--steam", type=int, help="Steam ID")
    args = parser.parse_args()
    start(args.client, args.steam)


if __name__ == "__main__":
    main()
