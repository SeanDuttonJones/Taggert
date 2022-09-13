import click

from TagIndex import TagIndex

@click.group()
def cli():
    pass

@cli.command()
@click.argument("tags", nargs=-1)
def search(tags):
    print("Search")
    pass

@cli.command()
def list():
    print("List")
    pass

if __name__ == "__main__":
    cli()