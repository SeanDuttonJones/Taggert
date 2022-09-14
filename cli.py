from taggert import Taggert
import click

taggert = Taggert()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("tags", nargs=-1)
def search(tags):
    taggert.search(tags)
    pass

@cli.command()
def list():
    taggert.list()
    pass

if __name__ == "__main__":
    cli()