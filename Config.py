import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 6534707))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "4bcc61d959a9f403b2f20149cbbe627a")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5442493323:AAHPw8TNe0hh2zCAQKm_2O2o6KdmQ3Okgf8")
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgres://dgdxlptb:uP0wjJhot4kqWrwXg8ENLEFAuEd2yk4d@mouse.db.elephantsql.com/dgdxlptb")
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "animedualaudiozippercartoonist")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 6534707
    API_HASH = "4bcc61d959a9f403b2f20149cbbe627a"
    BOT_TOKEN = "5442493323:AAHPw8TNe0hh2zCAQKm_2O2o6KdmQ3Okgf8"
    DATABASE_URL = "postgres://dgdxlptb:uP0wjJhot4kqWrwXg8ENLEFAuEd2yk4d@mouse.db.elephantsql.com/dgdxlptb"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "animedualaudiozippercartoonist"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
