# Include all global variables in this file.
# These are used across different modules/packages
# where required.

# Service Name
SVC_NAME = 'game-scout'

# DB Settings
DB_HOST_WRITER = '127.0.0.1'
DB_HOST_READER = '127.0.0.1'
DB_PORT = 5432
DB_NAME = 'game_scout'
DB_USER = 'postgres'
DB_PASS = ''

# Sentry Settings
SENTRY_DSN = ''
SENTRY_TRACES_SAMPLE_RATE = 1.0
SENTRY_PROFILES_SAMPLE_RATE = 1.0
SENTRY_ENV = 'development'

# Scrapper Settings
STEAM_URL = 'https://store.steampowered.com/search/?filter=topsellers'
MAX_SCROLL = 10
SLEEP_LIMIT = 2

# FASTAPI Settings
FASTAPI_PORT = 8001
FASTAPI_DEBUG = True