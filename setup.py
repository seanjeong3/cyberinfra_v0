import json
import sys
import os
import socket

def read_arg():
	if len(sys.argv) < 2:
		print('Error: You need to provide one argument (install or uninstall).')
		exit(0)
	elif sys.argv[1] not in ["install", "uninstall"]:
		print('Error: Unknown argument {0}. Valid argument is (install or uninstall).'.format(sys.argv[1]))
		exit()
	return sys.argv[1]


def prepare_param():
	param = json.loads(open("setup.json").read())
	param["home_path"] = os.path.expanduser('~')
	if param["data_repo_path"][0] != "/":
		param["data_repo_path"] = "{0}/{1}".format(os.getcwd(),param["data_repo_path"])
	param["current_path"] = os.getcwd()
	param["storage_path"] = "{0}/storage".format(os.getcwd())
	param["cassandra_path"] = "{0}/storage/apache-cassandra-3.7".format(os.getcwd())
	param["ip_address"] = socket.gethostbyname(socket.gethostname())
	param["listen_address"] = 'localhost'
	return param


def give_user_warning(arg, param):
	action = "OVERWRITE" if arg == "install" else "REMOVE"
	while True:
		print('This action will {0} data in following directories:'.format(action))
		print('- {0}'.format(param["current_path"]))
		print('- {0}'.format(param["data_repo_path"]))
		ans = raw_input('Do you want to proceed? (yes/no): ')
		if ans == 'yes':
			break
		elif ans == 'no':
			print('Installation has been canceled.')
			exit(0)
		else:
			print('Please answer in "yes" or "no".')
	return


##### Install Dependencies #####
def install_dependency():
	os.system('sudo apt-get update')
	os.system('sudo apt install openjdk-8-jre-headless')


##### Cassandra setup #####
def install_cassandra(param):
	### Remove path ###
	os.system('sudo rm -rf {0}'.format(param["cassandra_path"]))

	### Install pacakages required by Cassandra DB ###
	os.system('sudo apt install python-pip')
	os.system('pip install cassandra-driver')

	### Unzip Cassandra
	os.system('tar -zxvf storage/apache-cassandra-3.7-bin.tar.gz -C {0}'.format(param["storage_path"]))
	os.system('sudo chown -R $USER:$GROUP {0}'.format(param["cassandra_path"]))

	### Create Cassandra DB data repository folder ###
	os.system('sudo mkdir -p {0}'.format(param["data_repo_path"]))
	os.system('sudo chown -R $USER:$GROUP {0}'.format(param["data_repo_path"]))

	### Update configuration file (cassandra.yaml) ###
	with open('{0}/conf/cassandra.yaml'.format(param["cassandra_path"]), 'r') as f :
		filedata = f.read()
	filedata = filedata.replace('cluster_name: \'Test Cluster\'', 'cluster_name: \'{0}\''.format(param["cluster_name"]))
	filedata = filedata.replace('# hints_directory: /var/lib/cassandra/hints', 'hints_directory: {0}'.format(param["data_repo_path"]))
	filedata = filedata.replace('authenticator: AllowAllAuthenticator', 'authenticator: PasswordAuthenticator')
	filedata = filedata.replace('authorizer: AllowAllAuthorizer', 'authorizer: CassandraAuthorizer')
	filedata = filedata.replace('# data_file_directories:', 'data_file_directories:')
	filedata = filedata.replace('#     - /var/lib/cassandra/data', '     - {0}/data'.format(param["data_repo_path"]))
	filedata = filedata.replace('# commitlog_directory: /var/lib/cassandra/commitlog', 'commitlog_directory: {0}/commitlog'.format(param["data_repo_path"]))
	filedata = filedata.replace('# saved_caches_directory: /var/lib/cassandra/saved_caches', 'saved_caches_directory: {0}/saved_caches'.format(param["data_repo_path"]))
	filedata = filedata.replace('- seeds: "127.0.0.1"', '- seeds: "{0}"'.format(param["ip_address"]))
	filedata = filedata.replace('listen_address: localhost', 'listen_address: {0}'.format(param["listen_address"]))
	filedata = filedata.replace('# broadcast_address: 1.2.3.4', 'broadcast_address: {0}'.format(param["ip_address"]))
	filedata = filedata.replace('rpc_address: localhost', 'rpc_address: 0.0.0.0')
	filedata = filedata.replace('# broadcast_rpc_address: 1.2.3.4', 'broadcast_rpc_address: {0}'.format(param["ip_address"]))
	filedata = filedata.replace('# rpc_min_threads: 16', 'rpc_min_threads: 8')
	filedata = filedata.replace('# rpc_max_threads: 2048', 'rpc_max_threads: 256')
	filedata = filedata.replace('read_request_timeout_in_ms: 5000', 'read_request_timeout_in_ms: 20000')
	filedata = filedata.replace('range_request_timeout_in_ms: 10000', 'range_request_timeout_in_ms: 60000')
	filedata = filedata.replace('write_request_timeout_in_ms: 2000', 'write_request_timeout_in_ms: 30000')
	filedata = filedata.replace('counter_write_request_timeout_in_ms: 5000', 'counter_write_request_timeout_in_ms: 30000')
	filedata = filedata.replace('cas_contention_timeout_in_ms: 1000', 'cas_contention_timeout_in_ms: 10000')
	filedata = filedata.replace('truncate_request_timeout_in_ms: 60000', 'truncate_request_timeout_in_ms: 60000')
	filedata = filedata.replace('request_timeout_in_ms: 10000', 'request_timeout_in_ms: 10000')
	filedata = filedata.replace('endpoint_snitch: SimpleSnitch', 'endpoint_snitch: SimpleSnitch')
	filedata = filedata.replace('dynamic_snitch_reset_interval_in_ms: 600000', 'dynamic_snitch_reset_interval_in_ms: 600000')
	filedata = filedata.replace('batch_size_warn_threshold_in_kb: 5', 'batch_size_warn_threshold_in_kb: 5000')
	filedata = filedata.replace('batch_size_fail_threshold_in_kb: 50', 'batch_size_fail_threshold_in_kb: 50000')
	filedata += '\n'
	filedata += 'auto_bootstrap: false'
	with open('{0}/conf/cassandra.yaml'.format(param["cassandra_path"]), 'w') as f :
		f.write(filedata)

	# ### Export Cassandra path ###
	# os.system('export CQLSH_NO_BUNDLED=true')
	# os.system('export PATH="/opt/apache-cassandra-3.7/bin:$PATH"')

	### Make session keep alive ###
	os.system('sudo sysctl -w net.ipv4.tcp_keepalive_time=60 net.ipv4.tcp_keepalive_probes=3 net.ipv4.tcp_keepalive_intvl=10')

	### Enable auth ###
	os.system('mkdir {0}/.cassandra'.format(home))
	os.system('touch {0}/.cassandra/cqlshrc'.format(home))
	os.system('echo "[authentication]" >> {0}/.cassandra/cqlshrc'.format(home))
	os.system('echo "username = cassandra" >> {0}/.cassandra/cqlshrc'.format(home))
	os.system('echo "password = cassandra" >> {0}/.cassandra/cqlshrc'.format(home))
	





if __name__ == '__main__':
	# Read command line argument
	arg = read_arg()
	# Prepare install parameters and read params from JSON file "setup.json"
	param = prepare_param()
	# Give user warning.
	_ = give_user_warning(arg, param)
	if arg == "install":
		install_dependency()
		install_cassandra(param)

		



