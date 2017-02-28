import click


@click.group()
def main():
    pass


@main.command()
@click.argument('playbook')
def play(playbook):
    print(playbook)
