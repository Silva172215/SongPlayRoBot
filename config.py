import os
API_ID = int(os.getenv("16460251"))
API_HASH = os.getenv("67068034caedfb02e3bbfef339f827bd")
BOT_TOKEN = os.getenv("5199710332:AAGlVnPnWQlxZSrUPiYCW1_ZHDksi7cKBdI")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
