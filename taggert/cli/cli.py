from taggert.core.taggert import Taggert
from taggert.diff.filetree import FileTree

import click
import appdirs

import os

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

@cli.command()
def lstat():
    print(os.lstat("."))

@cli.command()
def tree():
    cwd = os.getcwd() + "/taggert"

    file_tree = FileTree(cwd)
    file_tree.build()
    file_tree.print()
    file_tree.save(cwd, "tree.json")
    
    file_tree.load(cwd + "/tree.json")

    print("FILES")
    for file in file_tree.list_files():
        print(file.get_path())

    print("\nDIRECTORIES")
    for dir in file_tree.list_directories():
        print(dir.get_path())

@cli.command()
def cache():
    # package_install_loc = os.path.dirname(tggt.__file__)
    # os.mkdir(package_install_loc + "/__cache__")
    # print(package_install_loc)
    cache_dir = appdirs.user_cache_dir("Taggert", "Taggert")
    click.echo(cache_dir)