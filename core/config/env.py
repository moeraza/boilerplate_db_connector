import os

MYSQL_ENDPOINT = os.getenv("MYSQL_ENDPOINT", "")
MYSQL_PORT = os.getenv("MYSQL_PORT", "")
MYSQL_REGION = os.getenv("MYSQL_REGION", "")
MYSQL_DBNAME = os.getenv("MYSQL_DBNAME", "")
MYSQL_PWD = os.getenv("MYSQL_PWD", "")
MYSQL_SSL_CA = os.getenv("MYSQL_SSL_CA", "")
MYSQL_BOTOPROFILENAME = os.getenv("MYSQL_BOTOPROFILENAME", "")

REDSHIFT_HOST = os.getenv("REDSHIFT_HOST", "")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT", "")
REDSHIFT_USER = os.getenv("REDSHIFT_USER", "")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD", "")
REDSHIFT_DBNAME = os.getenv("REDSHIFT_DBNAME", "")

S3BUCKETNAME = os.getenv("S3BUCKETNAME", "")
S3SUBDIRECTORYNAME = os.getenv("S3SUBDIRECTORYNAME", "")

SCYLLA_USR = os.getenv("SCYLLA_USR", "")
SCYLLA_PSWD = os.getenv("SCYLLA_PSWD", "")
SCYLLA_PORT = os.getenv("SCYLLA_PORT", "")
SCYLLA_LOCAL_DC = os.getenv("SCYLLA_LOCAL_DC", "")
SCYLLA_CP_1 = os.getenv("SCYLLA_CP_1", "")
SCYLLA_CP_2 = os.getenv("SCYLLA_CP_2", "")
SCYLLA_CP_3= os.getenv("SCYLLA_CP_3", "")