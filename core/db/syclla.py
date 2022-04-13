from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.policies import DCAwareRoundRobinPolicy, TokenAwarePolicy
from cassandra.auth import PlainTextAuthProvider
from core.config.env import SCYLLA_PORT, SCYLLA_USR, SCYLLA_PSWD, SCYLLA_LOCAL_DC, SCYLLA_CP_1, SCYLLA_CP_2, SCYLLA_CP_3

def getCluster():
    profile = ExecutionProfile(load_balancing_policy=TokenAwarePolicy(DCAwareRoundRobinPolicy(local_dc=SCYLLA_LOCAL_DC)))

    return Cluster(
        execution_profiles={EXEC_PROFILE_DEFAULT: profile},
        contact_points=[
            SCYLLA_CP_1, SCYLLA_CP_2, SCYLLA_CP_3
        ],
        port=SCYLLA_PORT,
        auth_provider = PlainTextAuthProvider(username=SCYLLA_USR, password=SCYLLA_PSWD))


def connect_cluster():
    print('Connecting to cluster')
    cluster = getCluster()
    session = cluster.connect()

    print('Connected to cluster %s' % cluster.metadata.cluster_name)

    print('Getting metadata')
    for host in cluster.metadata.all_hosts():
        print('Datacenter: %s; Host: %s; Rack: %s' % (host.datacenter, host.address, host.rack))

    cluster.shutdown()
