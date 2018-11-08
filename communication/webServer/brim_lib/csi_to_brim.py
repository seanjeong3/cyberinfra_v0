from csi_to_brim_dictionary import csi_to_brim_dictionary as ctobDict
import xlrd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import re

inputFileName = 'New_TRB4_cleaned.xlsx'
outputFileName = 'trb_brim_fem.xml'

#############################################

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

def ScanAttributes(attributeDict, sheet):
	columnDict = {}
	ncol = sheet.ncols
	for i in range(0, ncol):
		att = sheet.cell(1,i).value
		if att in attributeDict:
			columnDict[attributeDict[att]] = i
	return columnDict 

def CreateParameter(rowData, obj, sheet, columnDict):
	for key in rowData:
		if key == 'N':
			continue
		else:
			data = rowData[key]
			if type(data) in [int, float]:
				if sheet.cell(2, columnDict[key]).value == 'Text':
					data = str(int(data))
					CreateElement({'N':key,'V':data,'Type':'Expr'}, elemType='P', parentElement=obj)
				else:
					data = str(data)
					CreateElement({'N':key,'V':data}, elemType='P', parentElement=obj)
			elif key == 'Azimuth' and data != '':
				data = str(float(re.findall('\d+', data)[0]) / 10000)
				CreateElement({'N':key,'V':data}, elemType='P', parentElement=obj)
			elif data != '':
				CreateElement({'N':key,'V':data,'Type':'Expr'}, elemType='P', parentElement=obj)
			
def updateAttributeIndex(rowData, columnDict, increment):
	newRowData = {}
	newColumnDict = {}
	for key in rowData: 
		newKey = key
		idx = re.findall('\d+', newKey)
		if idx:
			newIdx = str(int(idx[0]) + increment)
			newKey = re.findall('[a-zA-Z]+', key)[0] + newIdx
		if rowData != '' and rowData != None:
			newRowData[newKey] = rowData[key]
			newColumnDict[newKey] = columnDict[key]
	return [newRowData, newColumnDict]

def ReadSheetData(columnDict, sheet, objectRoot, objectType, duplicationPolicy):
	nrow = sheet.nrows
	for i in range(3, nrow):
		rowData = {}
		for att in columnDict:
			rowData[att] = sheet.cell(i,columnDict[att]).value
		if 'N' in rowData: 
			name = rowData['N']
			if type(name) in [int, float]:
				name = str(int(name))
			obj = CreateElement({'N':name,'T':objectType}, parentElement=objectRoot, duplicationPolicy=duplicationPolicy)
		else:
			obj = CreateElement({'T':objectType}, parentElement=objectRoot, duplicationPolicy=duplicationPolicy)
		CreateParameter(rowData, obj, sheet, columnDict)

def ReadChildSheetData(columnDict, sheet, objectRoot, objectType, parentType, duplicationPolicy):
	nrow = sheet.nrows
	for i in range(3, nrow):
		rowData = {}
		for att in columnDict:
			rowData[att] = sheet.cell(i,columnDict[att]).value
		if 'N' in rowData: 
			name = rowData['N']
			if type(name) in [int, float]:
				name = str(int(name))
			parentObj = CreateElement({'N':name,'T':parentType}, parentElement=objectRoot, duplicationPolicy='Merge')
			obj = CreateElement({'N':name,'T':objectType}, parentElement=parentObj, duplicationPolicy=duplicationPolicy)
		else:
			parentObj = CreateElement({'N':name,'T':parentType}, parentElement=objectRoot, duplicationPolicy='Merge')
			obj = CreateElement({'T':objectType}, parentElement=parentObj, duplicationPolicy=duplicationPolicy)
		CreateParameter(rowData, obj, sheet, columnDict)

def ReadSurfaceVertexData(columnDict, sheet, objectRoot, objectType, duplicationPolicy):
	nrow = sheet.nrows
	prevName = ''
	increment = 4
	for i in range(3, nrow):
		rowData = {}
		for att in columnDict:
			rowData[att] = sheet.cell(i,columnDict[att]).value
		name = rowData['N']
		if type(name) in [int, float]:
			name = str(int(name))
		if name == prevName:
			[newRowData, newColumnDict] = updateAttributeIndex(rowData, columnDict, increment)
			increment = increment + 4
			obj = CreateElement({'N':name,'T':objectType}, parentElement=objectRoot, duplicationPolicy=duplicationPolicy)
			CreateParameter(newRowData, obj, sheet, newColumnDict)
		else:
			increment = 4
			obj = CreateElement({'N':name,'T':objectType}, parentElement=objectRoot, duplicationPolicy=duplicationPolicy)
			CreateParameter(rowData, obj, sheet, columnDict)
		prevName = name
		

#############################################
if __name__ == '__main__':

	book = xlrd.open_workbook(inputFileName)

	projectRoot = CreateElement({'N':'TRB_FEM','T':'Project'})
	femRoot = CreateElement({'N':'FEM','T':'Group'}, parentElement=projectRoot)

	for objectType in ctobDict:

		if objectType in ['Node','FELine','Material','FEVehicle','FESurface','Alignment','FEMultiStep','FELoadCase']:
			dupPolicy = 'Merge'
		elif objectType in ['FELineSection','FESurfaceSection','Rebar','FECoordinateSystem','FEGrid','FELane','FELoadPattern','SectionDesigner','ShapePlate','ShapeSolidRectangle','FiberGeneral','Straight','Circular','Spiral','ElevationPoint','FEVehicleLoad','FEVehicleClass','FEStatic','FEModal','FEMultiStepStatic','FEDirectIntegrationHistory','FEFunction']:
			dupPolicy = 'New'
		else: 
			continue
		for sheetName in ctobDict[objectType]:
			sheet = book.sheet_by_name(sheetName)
			columnDict = ScanAttributes(ctobDict[objectType][sheetName], sheet)
			if objectType in ['Straight','ElevationPoint']:
				objectRoot = CreateElement({'N':'Alignment','T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
				ReadChildSheetData(columnDict, sheet, objectRoot, objectType, 'Alignment', dupPolicy)
			elif objectType in ['FEVehicleLoad']:
				objectRoot = CreateElement({'N':'FEVehicle','T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
				ReadChildSheetData(columnDict, sheet, objectRoot, objectType, 'FEVehicle', dupPolicy)
			elif objectType in ['FEMultiStep']:
				objectRoot = CreateElement({'N':'FELoadPattern','T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
				ReadChildSheetData(columnDict, sheet, objectRoot, objectType, 'FELoadPattern', dupPolicy)
			elif objectType in ['FEStatic','FEModal','FEMultiStepStatic','FEDirectIntegrationHistory']:
				objectRoot = CreateElement({'N':'FELoadCase','T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
				ReadChildSheetData(columnDict, sheet, objectRoot, objectType, 'FELoadCase', dupPolicy)
			elif objectType in ['FEFunction']:
				objectRoot = CreateElement({'N':'FEFunction','T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
				ReadChildSheetData(columnDict, sheet, objectRoot, objectType, 'FEFunction', dupPolicy)
			elif sheetName in ['Area Overwrites - Joint Offsets', 'Connectivity - Area']: 
				objectRoot = CreateElement({'N':objectType,'T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
				ReadSurfaceVertexData(columnDict, sheet, objectRoot, objectType, dupPolicy)
			else:
				objectRoot = CreateElement({'N':objectType,'T':'Group'}, parentElement=femRoot, duplicationPolicy='Merge')
 				ReadSheetData(columnDict, sheet, objectRoot, objectType, dupPolicy)

	result = prettify(projectRoot)
	f = open(outputFileName, 'w')
	f.write(result)
	f.close()
	

