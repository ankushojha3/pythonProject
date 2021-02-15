import os

DB_DETAILS = {
    'dev' : {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'LOCALHOST',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('source_retail_user'),
            'DB_PASS': os.environ.get('source_db_pass')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'LOCALHOST',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('target_retail_user'),
            'DB_PASS': os.environ.get('target_db_pass')
        }
}
}
