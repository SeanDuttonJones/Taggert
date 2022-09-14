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
        click.echo(tag + ":")
        for file in result:
            click.echo("\t" + file)
    else:
        click.echo("No results found.")

@cli.command()
def list():
    tags = taggert.list()
    if(len(tags) > 0):
        click.echo("TAGS:")
        for tag in sorted(tags):
            click.echo("\t" + tag)
    else: 
        click.echo("No tags found.")

if __name__ == "__main__":
    cli()