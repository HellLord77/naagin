from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
from enum import StrEnum
from os import startfile


class Client(StrEnum):
    DMM = "dmm"
    JOHREN = "johren"
    STEAM = "steam"
    STEAM_JP = "steam_jp"

    def get_uri(self) -> str:
        uri = ""
        match self:
            case Client.DMM:
                uri = "dmmgameplayer://play/GCL/doaxvv/cl/win"
            case Client.JOHREN:
                uri = "johren-launcher://mygame?titleId=doaxvv"
            case Client.STEAM:
                uri = "steam://rungameid/958260"
            case Client.STEAM_JP:
                uri = "steam://rungameid/1361350"
        return uri


def start(client: Client) -> None:
    uri = client.get_uri()
    startfile(uri)  # noqa: S606


def main() -> None:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--client", default=Client.STEAM, type=Client, choices=Client, help="Client type")
    args = parser.parse_args()
    start(args.client)


if __name__ == "__main__":
    main()
