from split_settings.tools import include

include(
    'components/__init__.py',
    'components/databases.py',
    'components/apps.py',
    'components/internationalization.py',
    'components/middlewares.py',
    'components/templates.py',
    'components/auth.py'
)