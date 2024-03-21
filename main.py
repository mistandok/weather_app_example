import argparse

from src.app.app import App


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--env", type=str, default="deploy/env/.env.local")

    return parser


if __name__ == "__main__":
    app_parser = get_parser()
    args = app_parser.parse_args()

    app = App(args.env)
    app.start()
