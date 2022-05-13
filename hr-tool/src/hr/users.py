import csv
import json
import pwd
from typing import IO, Dict, List

User = Dict[str, str]
Users = List[User]


def get() -> Users:
    result: Users = []
    for user in pwd.getpwall():
        if user.pw_uid < 1000 or 'home' not in user.pw_dir:
            continue

        result.append({
            'id': user.pw_uid,
            'name': user.pw_name,
            'home': user.pw_dir,
            'shell': user.pw_shell,
        })

    return result


def to_json(file: IO[str]):
    json.dump(get(), file, indent=4)


def to_csv(file: IO[str]):
    file.write('id,name,home,shell\n')
    writer = csv.writer(file)
    users = get()
    rows = [
        [user['id'], user['name'], user['home'], user['shell']]
        for user in users
    ]
    writer.writerows(rows)
