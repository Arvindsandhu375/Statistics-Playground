import snowflake.connector
import os
import dotenv
from pathlib import Path

def snowflake_connection():

    dotenv.load_dotenv(dotenv.find_dotenv(Path.cwd() / '..' / '.env'))

    """
    - Specifies the path to locate .env file in the directory to access the credentials.

    - Establishes a connection with snowflake using the credentials stored locally.
    """

    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USERNAME'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        use_warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
        role=os.getenv('SNOWFLAKE_ROLE')
    )

    """
    - Returns a curr to connect to snowflake to interact with snowflake database.
    """

    curr = conn.cursor()
    return curr