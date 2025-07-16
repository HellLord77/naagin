from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
from enum import StrEnum
from os import startfile


class Client(StrEnum):
    STEAM = "steam"
    JOHREN = "johren"

    def get_uri(self) -> str:
        uri = ""
        match self:
            case Client.STEAM:
                uri = "steam://rungameid/958260"
            case Client.JOHREN:
                uri = "johren-launcher://mygame?titleId=doaxvv"
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
