# frontend

## Install dependencies

### One-time action

```bash
pip install poetry
poetry config virtualenvs.in-project true
source .env\Scripts\activate
```

### For each projet

```bash
poetry init
poetry install
```

## Usage

```bash
python -m frontend
```

## Resources used

```bash
sqlalchemy - lib. Work with different DBMS
pydantic - lib. Data validation and settings management
```
