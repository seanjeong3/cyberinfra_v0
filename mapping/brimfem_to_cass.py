import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from cassandra.cluster import Cluster 	# INTERFACE WITH CASSANDRA DB
from cassandra.query import BatchStatement
from cassandra  import ConsistencyLevel
import dateutil.parser  				# FOR DATETIEM CALCULATION
import uuid
from cassandra.auth import PlainTextAuthProvider

inputFileName = 'trb_brim_fem.xml'
ids = {}
keyspace = 'i275monitoring'

serverIp = ['52.175.219.213']
batch = BatchStatement()

USEBATCH     = False
MAXBATCH     = 100


class InsertionHandler:

	def add_query(self, stmt, values):
		self.currentNum = self.currentNum + 1
		statement = self.session.prepare(stmt)
		if not self.isBatch:
			self.bound_stmt = statement.bind(values)
			self.flush_query()
		else: 
			self.batch.add(statement, values)
			if self.currentNum == MAXBATCH:
				self.flush_query()

	def flush_query(self):
		if self.currentNum == 0: return
		if not self.isBatch:
			self.currentNum = 0
			try:
				self.session.execute(self.bound_stmt, timeout=30)
			except Exception as e:
				self.success = False
		else:
			try:
				self.session.execute(self.batch, timeout=30)
			except Exception as e:
				self.success = False
			self.currentNum = 0
			self.batch = BatchStatement()

	def __init__(self, session):
		self.session = session
		self.currentNum = 0
		self.success = True
		if USEBATCH and MAXBATCH != 1: 
			self.isBatch = USEBATCH
			self.batch = BatchStatement()
			self.numBatch = MAXBATCH
		else:
			self.isBatch = False
		

def connectCassandra():
	auth_provider = PlainTextAuthProvider(username='admin', password='0000')
	cluster  = Cluster(contact_points=serverIp, auth_provider=auth_provider, control_connection_timeout = 60)
	session  = cluster.connect(keyspace)
	return   session

def prettify(elem):
    rough_string = ET.tostring(elem)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="   ")

def GetAttribute(items):
	attribute = {}
	for item in items:
		attribute[item[0]] = item[1]
	return attribute

def GetParameter(params):
	parameter = {}
	paramAttr = {}
	if params :
		for param in params:
			paramAttr = GetAttribute(param.items())
			paramVal = paramAttr['V']
			if 'Type' not in paramAttr:
				paramVal = float(paramVal)
			parameter[paramAttr['N']] = paramVal
	return parameter

def CreateKey(type):
	if type in ids:
		ids[type] = ids[type] + 1
	else:
		ids[type] = 0
	key = type + '_' + str(int(ids[type]))
	return key

def CreateQuery(key, attribute, parameter, childObj, parentObj):
	numvar = 0
	cf = attribute['T']
	cols = ['uid']
	vals = ['?']
	value = [key]
	for att in attribute:
		cols.append(att)
		vals.append('?')
		value.append(attribute[att])
	for par in parameter:
		cols.append(par)
		vals.append('?')
		value.append(parameter[par])
	if childObj:
		cols.append('child')
		vals.append('?')
		value.append(childObj)
	if parentObj is not None:
		cols.append('parent')
		vals.append('?')
		value.append(parentObj)

	stmt = 'INSERT INTO ' + cf + ' (' + ",".join(cols) + ') VALUES (' + ",".join(vals) + ')'
	return stmt, value

def ParseObject(corrObj, parentObj, queryHandler):
	attribute = {}
	parameter = {}
	childObjs = {}

	attribute = GetAttribute(corrObj.items())
	parameter = GetParameter(corrObj.findall('P'))
	# key = CreateKey(attribute['T'])
	key = uuid.uuid1()
	for childObj in corrObj.findall('O'):
		[k, t] = ParseObject(childObj, {key: attribute['T']}, queryHandler)
		childObjs[k] = t

	typ = attribute['T']
	[stmt, value] = CreateQuery (key, attribute, parameter, childObjs, parentObj)
	queryHandler.add_query(stmt, value)

	return key, typ

if __name__ == '__main__':

	session = connectCassandra()
	queryHandler = InsertionHandler(session)
	root = ET.parse(inputFileName).getroot()
	ParseObject(root, None, queryHandler)
