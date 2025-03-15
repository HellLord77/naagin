import config
import csv_
import flow
import game


def main():
    if config.FLOW:
        flow.to_model()

    if config.CSV:
        csv_.to_model()

    if config.GAME:
        game.to_tmp()


if __name__ == "__main__":
    main()
