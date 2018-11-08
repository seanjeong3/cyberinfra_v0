import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra.query import dict_factory
from cassandra  import ConsistencyLevel
import dateutil.parser
from cassandra.auth import PlainTextAuthProvider

outputFileName = 'brim_lib/trb_brim_fem_retrieved.xml'
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

def CreateParameter(params, obj):
	for key in params:
		data = params[key]
		if type(data) in [int, float]:
			data = str(data)
			CreateElement({'N':key,'V':data}, elemType='P', parentElement=obj)
		elif data != '':
			CreateElement({'N':key,'V':data,'Type':'Expr'}, elemType='P', parentElement=obj)

def CleanData(data):
	cleanedData = {}
	for item in data:
		if data[item] != None:
			cleanedData[item] = data[item]
	return cleanedData

def ParseData(data):
	attribute = {}
	parameter = {}
	child = {}
	for item in data:
		if item in ['n', 't']:
			attribute[item.upper()] = data[item]
		elif item in ['child']:
			child = data[item]
		elif item in ['parent', 'uid']:
			continue
		else:
			parameter[item] = data[item]
	return [attribute, parameter, child]

def RetrieveDataByKey(key, cf, parent = None):
	# prepared_stmt = session.prepare ( 'SELECT * FROM ' + cf + ' WHERE uid = ?')
	# bound_stmt = prepared_stmt.bind([key])
	# stmt = session.execute(bound_stmt)
	# data = CleanData(stmt[0])
	data = CleanData(collection[cf][key])
	[attributes, parameters, children] = ParseData(data)
	obj = CreateElement(attributes)
	CreateParameter(parameters, obj)
	if children:
		for child in children:
			obj.append(RetrieveDataByKey(child, children[child], obj))
	return obj

def RetrieveDataByName(name, cf, parent = None):
	prepared_stmt = session.prepare ( 'SELECT * FROM ' + cf + ' WHERE N = ?')
	bound_stmt = prepared_stmt.bind([name])
	stmt = session.execute(bound_stmt)
	data = CleanData(stmt[0])
	[attributes, parameters, children] = ParseData(data)
	obj = CreateElement(attributes)
	CreateParameter(parameters, obj)
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
	collection = {}

	collection['Unit'] = retrieveAllByTable('Unit')
	collection['Project'] = retrieveAllByTable('Project')
	collection['Group'] = retrieveAllByTable('Group')
	collection['Node'] = retrieveAllByTable('Node')
	collection['FELine'] = retrieveAllByTable('FELine')
	collection['FESurface'] = retrieveAllByTable('FESurface')
	collection['FELineSection'] = retrieveAllByTable('FELineSection')
	collection['FESurfaceSection'] = retrieveAllByTable('FESurfaceSection')
	collection['Material'] = retrieveAllByTable('Material')
	collection['Rebar'] = retrieveAllByTable('Rebar')
	collection['FECoordinateSystem'] = retrieveAllByTable('FECoordinateSystem')
	collection['Alignment'] = retrieveAllByTable('Alignment')
	collection['Straight'] = retrieveAllByTable('Straight')
	collection['ElevationPoint'] = retrieveAllByTable('ElevationPoint')
	collection['FEGrid'] = retrieveAllByTable('FEGrid')
	collection['FELane'] = retrieveAllByTable('FELane')
	collection['FEVehicle'] = retrieveAllByTable('FEVehicle')
	collection['FEVehicleClass'] = retrieveAllByTable('FEVehicleClass')
	collection['FEVehicleLoad'] = retrieveAllByTable('FEVehicleLoad')
	collection['FELoadPattern'] = retrieveAllByTable('FELoadPattern')
	collection['FEMultiStep'] = retrieveAllByTable('FEMultiStep')
	collection['FEFunction'] = retrieveAllByTable('FEFunction')
	collection['FELoadCase'] = retrieveAllByTable('FELoadCase')
	collection['FEStatic'] = retrieveAllByTable('FEStatic')
	collection['FEModal'] = retrieveAllByTable('FEModal')
	collection['FEMultiStepStatic'] = retrieveAllByTable('FEMultiStepStatic')
	collection['FEDirectIntegrationHistory'] = retrieveAllByTable('FEDirectIntegrationHistory')
	collection['SectionDesigner'] = retrieveAllByTable('SectionDesigner')
	collection['ShapePlate'] = retrieveAllByTable('ShapePlate')
	collection['ShapeSolidRectangle'] = retrieveAllByTable('ShapeSolidRectangle')
	collection['FiberGeneral'] = retrieveAllByTable('FiberGeneral')


	projectRoot = RetrieveDataByName('TRB_FEM', 'Project')


	result = prettify(projectRoot)
	f = open(outputFileName, 'w')
	f.write(result)
	f.close()

	print outputFileName
