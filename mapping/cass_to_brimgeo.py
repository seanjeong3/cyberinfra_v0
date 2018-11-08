import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra.query import dict_factory
from cassandra  import ConsistencyLevel
import dateutil.parser
from cassandra.auth import PlainTextAuthProvider

outputFileName = 'brim_lib/trb_brim_geo_retrieved.xml'
keyspace = 'i275monitoring'
serverIp = ['52.175.219.213','52.175.210.149','52.175.213.66','52.175.212.242','52.175.200.215']

def connectCassandra():
	auth_provider = PlainTextAuthProvider(username='admin', password='0000')
	cluster  = Cluster(contact_points=serverIp, auth_provider=auth_provider, control_connection_timeout = 60)
	session  = cluster.connect(keyspace)
	session.row_factory = dict_factory
	return   session

def prettify(elem):
    rough_string = ET.tostring(elem)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="   ")

def CreateElement(attributes, elemType='O', parentElement=None, duplicationPolicy='New'):
	element = ET.Element(elemType)

	if parentElement != None:
		if duplicationPolicy == 'New':
			parentElement.append(element)
		elif duplicationPolicy == 'Merge':
			if elemType == 'O': 
				existingElement = parentElement.find('./' + elemType + '[@N="'+ attributes['N'] + '"]' + '[@T="'+ attributes['T'] + '"]' )
			else:
				existingElement = parentElement.find('./' + elemType + '[@N="'+ attributes['N'] + '"]' )
			if existingElement != None:
				element = existingElement
			else:
				parentElement.append(element)
		else:
			raise Exception('Error: Unavailable duplicationPolicy')
	for key in attributes:
		element.set(key,attributes[key])
	
	return element

def CreateParameter(param, obj):
	if param != '':
		paramSplit = param.split('\n')
		for param in paramSplit:
			param = param.strip()
			if param != "":
				obj.append(ET.fromstring(param))

def CleanData(data):
	cleanedData = {}
	for item in data:
		if data[item] != None:
			cleanedData[item] = data[item]
	return cleanedData

def ParseData(data):
	attribute = {}
	parameter = ''
	child = {}
	for item in data:
		if item in ['n', 't', 'x', 'y', 'z', 'rx', 'ry', 'rz', 'ax', 'ay', 'az']:
			attribute[item.upper()] = data[item]
		elif item in ['extends']:
			attribute['Extends'] = data[item]
		elif item in ['child']:
			child = data[item]
		elif item in ['uid']:
			uid = data[item]
		elif item in ['parent']:
			continue
		else:
			parameter = data[item]
	return [attribute, parameter, child, uid]

def RetrieveDataByKey(key, cf, parent = None):
	# prepared_stmt = session.prepare ( 'SELECT * FROM ' + cf + ' WHERE uid = ?')
	# bound_stmt = prepared_stmt.bind([key])
	# stmt = session.execute(bound_stmt)
	# data = CleanData(stmt[0])
	data = CleanData(geometry[key])
	[attributes, parameter, children, uid] = ParseData(data)
	obj = CreateElement(attributes)
	if attributes['T'] == 'Group':
		(CreateElement({'N':'uid', 'V':uid.urn}, elemType='P', parentElement=obj))
	CreateParameter(parameter, obj)
	if children:
		for child in children:
			obj.append(RetrieveDataByKey(child, children[child], obj))
	return obj

def RetrieveDataByName(name, cf, parent = None):
	prepared_stmt = session.prepare ( 'SELECT * FROM ' + cf + ' WHERE N = ?')
	bound_stmt = prepared_stmt.bind([name])
	stmt = session.execute(bound_stmt)
	data = CleanData(stmt[0])
	[attributes, parameter, children, uid] = ParseData(data)
	obj = CreateElement(attributes)
	CreateParameter(parameter, obj)
	if children:
		for child in children:
			obj.append(RetrieveDataByKey(child, children[child], obj))
	return obj

def retrieveAllByTable(cf):
	prepared_stmt = session.prepare ( 'SELECT * FROM ' + cf)
	bound_stmt = prepared_stmt.bind([])
	stmt = session.execute(bound_stmt)
	result = {}
	for item in stmt:
		result[item['uid']] = item
	return result


if __name__ == '__main__':

	session = connectCassandra()
	geometry = retrieveAllByTable('Geometry')
	
	projectRoot = RetrieveDataByName('TRB_GEO', 'Project')

	result = prettify(projectRoot)
	f = open(outputFileName, 'w')
	f.write(result)
	f.close()

	print outputFileName
