import json_operations
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("-name", required=True, help="Name of the user")
@click.option("-lastname", required=True, help="Lastname of the user")
@click.pass_context
def new(context, name, lastname):
    users = json_operations.read_json()
    if not name or not lastname:
        context.fail("Name and Lastname are required")
    elif json_operations.search_name_repeated(name) >= 1:
        context.fail("User already exists")
    else:
        new_id = len(users) + 1
        new_user = {"id": new_id, "name": name, "lastname": lastname}
        users.append(new_user)
        json_operations.write_json(users)
        print(f"User {name} {lastname} has been created successfully with id: {new_id}")


@cli.command()
def users():
    for user in json_operations.read_json():
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


if __name__ == "__main__":
    cli()
