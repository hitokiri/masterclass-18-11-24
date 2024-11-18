from decouple import config

HASURA_GRAPHQL_URL = config('HASURA_GRAPHQL_URL', default='http://192.168.1.12:8082/v1/graphql')
HASURA_GRAPHQL_ADMIN_SECRET = config('HASURA_GRAPHQL_ADMIN_SECRET', default='lol')