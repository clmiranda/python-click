import json_operations
import click
from prettytable.colortable import ColorTable, Themes
from colorama import init, Fore, Back, Style


table = ColorTable(theme=Themes.OCEAN)
table.field_names = ["id", "name", "lastname"]
init(autoreset=True)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", required=True, help="Name of the user")
@click.option("--lastname", required=True, help="Lastname of the user")
@click.pass_context
def new(context, name, lastname):
    users = json_operations.read_json()
    if not name or not lastname:
        context.fail(Style.BRIGHT + Fore.RED + "Name and Lastname are required")
    elif json_operations.search_name_repeated(name) >= 1:
        context.fail(Style.BRIGHT + Fore.RED + "User already exists")
    else:
        new_id = len(users) + 1
        new_user = {"id": new_id, "name": name, "lastname": lastname}
        users.append(new_user)
        json_operations.write_json(users)
        print(
            Style.BRIGHT
            + Fore.GREEN
            + f"User {name} {lastname} has been created successfully with id: {new_id}",
        )


@cli.command()
def users():
    for user in json_operations.read_json():
        table.add_row([user["id"], user["name"], user["lastname"]])
    print(table)


@cli.command()
@click.argument("id", type=int)
def user(id):
    data = json_operations.read_json()
    user = next((i for i in data if i["id"] == id), None)
    if user is None:
        print(Style.BRIGHT + Fore.RED + f"User with id {id} not found")
    else:
        print(
            Style.BRIGHT
            + Fore.GREEN
            + f"{user['id']} - {user['name']} - {user['lastname']}"
        )


@cli.command()
@click.argument("id", type=int)
@click.option("--name", help="Name of the user")
@click.option("--lastname", help="Lastname of the user")
def update(id, name, lastname):
    data = json_operations.read_json()
    for user in data:
        if user["id"] == id:
            if name is not None:
                user["name"] = name
            if lastname is not None:
                user["lastname"] = lastname
            break
    json_operations.write_json(data)
    print(
        Style.BRIGHT + Fore.GREEN + f"User with id {id} has been updated successfully"
    )


@cli.command()
@click.argument("id", type=int)
def delete(id):
    data = json_operations.read_json()
    user = next((i for i in data if i["id"] == id), None)
    if user is None:
        print(Style.BRIGHT + Fore.RED + f"User with id {id} not found")
    else:
        data.remove(user)
        json_operations.write_json(data)
        print(
            Style.BRIGHT
            + Fore.GREEN
            + f"User with id {id} has been deleted successfully"
        )


if __name__ == "__main__":
    cli()
