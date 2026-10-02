import sys

# Compatibilidad de PyMySQL / MySQLdb
try:
    import MySQLdb
except ImportError:
    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

# Bypass de versión y sintaxis RETURNING para MariaDB 10.4
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures as MySQLDatabaseFeatures

# 1. Desactivar la verificación estricta de versión
MySQLDatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Desactivar la característica RETURNING en el objeto Features
MySQLDatabaseFeatures.can_return_columns_from_insert = False
MySQLDatabaseFeatures.can_return_rows_from_bulk_insert = False