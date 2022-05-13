# py-play-pgbackup
CLI for backing up PostgreSQL databases locally or to AWS S3. 

## Usage
Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:
```
 pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
```

Local Example w/ local path:
```
  pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups
```

## Installation
- `cd` into project's folder
- Run `pip install --user -e .`

## Development
- [ ] Ensure pip and pipenv are installed
- [ ] Clone repository
- [ ] `cd` into /pgbackup
- [ ] Activate virtualenv: `pipenv shell`
- [ ] Install dependencies: `pipenv install`