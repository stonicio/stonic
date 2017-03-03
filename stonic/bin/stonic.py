from pathlib import Path

import click

from stonic.core.playbook import Playbook


@click.group()
def main():
    pass


@main.command()
@click.argument('playbook_path', metavar='playbook', type=Path)
def play(playbook_path):
    playbook = Playbook(playbook_path)
    playbook.run()
