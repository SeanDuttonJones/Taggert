from taggert import Taggert
import click

taggert = Taggert()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("tag", nargs=1)
def search(tag):
    result = taggert.search(tag)
    if(len(result) > 0):
        click.echo(result)
    else:
        click.echo("No results found.")

@cli.command()
def list():
    tags = taggert.list()
    if(len(tags) > 0):
        click.echo(tags)
    else: 
        click.echo("No tags found.")

if __name__ == "__main__":
    cli()