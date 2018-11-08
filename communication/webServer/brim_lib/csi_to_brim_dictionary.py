# Mapping Rule
# From CSIBridge Excel
# To   BrIM
# Format: Dictionary = {'Object':{'Sheet':{'Column':'Parameter'}}}
# ***: needs further mapping

csi_to_brim_dictionary = {'Node':{'Joint Coordinates':{'Joint':'N','CoordSys':'CoordinateSystem','CoordType':'CoordinateType','XorR':'X','Y':'Y','Z':'Z','T':'Theta'},
							      'Joint Restraint Assignments':{'Joint':'N','U1':'Tx','U2':'Ty','U3':'Tz','R1':'Rx','R2':'Ry','R3':'Rz'}},
						  'FELine':{'Connectivity - Frame':{'Frame':'N','JointI':'Node1','JointJ':'Node2','IsCurved':'IsCurved'},
						            'Frame Auto Mesh':{'Frame':'N','AutoMesh':'AutoMesh','AtJoints':'AtJoints','AtFrames':'AtFrames','NumSegments':'NumberOfSegments','MaxLength':'MaxLength','MaxDegrees':'MaxDegrees'},
						            'Frame Releases 1 - General':{'Frame':'N', 'PI':'Node1P', 'V2I':'Node1V2', 'V3I':'Node1V3', 'TI':'Node1T', 'M2I':'Node1M2', 'M3I':'Node1M3', 'PJ':'Node2P', 'V2J':'Node2V2', 'V3J':'Node2V3', 'TJ':'Node2T', 'M2J':'Node2M2', 'M3J':'Node2M3'},
						            'Frame Section Assignments':{'Frame':'N', 'AnalSect':'Section'}},
						  'FESurface':{'Area Auto Mesh Assignments':{'Area':'N', 'MeshType':'MeshType', 'MeshGroup':'MeshGroup', 'PtsFromLine':'PointFromLine', 'PtsFromPt':'PointFromPoint', 'LocalEdge':'LocalEdge', 'LocalFace':'LocalFace', 'SuppEdge':'ConstraintEdge', 'SuppFace':'ConstraintFace', 'SubMesh':'SubMesh'},
						               'Area Edge Constraint Assigns':{'Area':'N', 'Constrained':'EdgeConstraint'},
						               'Area Overwrites - Joint Offsets':{'Area':'N', 'Offset1':'Offset1', 'Offset2':'Offset2', 'Offset3':'Offset3', 'Offset4':'Offset4'},
						               'Area Section Assignments':{'Area':'N', 'Section':'Section'},
						               'Area Spring Assignments':{'Area':'N', 'Type':'SpringType', 'Stiffness':'SpringStiffness', 'SimpleType':'SpringSimpleType', 'Face':'SpringFace', 'Dir1Type':'SpringDir1Type', 'NormalDir':'SpringNormalDir'},
						               'Connectivity - Area':{'Area':'N', 'NumJoints':'NumJoints', 'Joint1':'Node1', 'Joint2':'Node2', 'Joint3':'Node3', 'Joint4':'Node4'}},
						  'FELineSection':{'Frame Props 01 - General':{'SectionName':'N', 'Material':'Material', 'Shape':'Shape', 't3':'Height', 't2':'Width', 'tf':'FlangeThickness', 'tw':'WebThickness', 'EccV2':'EccV2'}},
						  'FESurfaceSection':{'Area Section Properties':{'Section':'N', 'Material':'Material', 'MatAngle':'MatAngle', 'AreaType':'SurfaceType', 'Type':'Type', 'DrillDOF':'DrillDOF', 'Thickness':'Thickness', 'BendThick':'BendThickness'}},
						  'Material':{'MatProp 01 - General':{'Material':'N', 'Type':'Type', 'SymType':'SymType', 'TempDepend':'TempDepend'},
						              'MatProp 02 - Basic Mech Props':{'Material':'N', 'UnitMass':'d', 'E1':'E', 'G12':'G', 'U12':'Nu', 'A1':'a'},
						              'MatProp 03a - Steel Data':{'Material':'N', 'Fy':'Fy', 'Fu':'Fu', 'EffFy':'EffFy', 'EffFu':'EffFu'},
						              'MatProp 03b - Concrete Data':{'Material':'N', 'Fc':'Fc28'},
						              'MatProp 03e - Rebar Data':{'Material':'N', 'Fy':'Fy', 'Fu':'Fu', 'EffFy':'EffFy', 'EffFu':'EffFu'},
						              'MatProp 03f - Tendon Data':{'Material':'N', 'Fy':'Fy', 'Fu':'Fu'},
						              'MatProp 06 - Damping Parameters':{'Material':'N', 'ModalRatio':'ModalRatio', 'VisMass':'VisMass', 'VisStiff':'VisStiff', 'HysMass':'HysMass', 'HysStiff':'HysStiff'}},
						  'Rebar':{'Rebar Sizes':{'RebarID':'N', 'Area':'Area', 'Diameter':'Diameter'}},
				          'FECoordinateSystem':{'Coordinate Systems':{'Name':'N', 'Type':'Type', 'X':'X', 'Y':'Y', 'Z':'Z', 'AboutZ':'RZ', 'AboutY':'RY', 'AboutX':'RX'}}, 
				          'Alignment':{'Bridge Layout Line 1 - General':{'LayoutLine':'N', 'CoordSys':'CoordinateSystem', 'X':'X', 'Y':'Y', 'Z':'Z'}}, # ***
				          'Straight':{'Bridge Layout Line 2 - Horiz':{'LayoutLine':'N', 'SegType':'SegType', 'Station':'Station', 'Radius':'Radius', 'Bearing':'Azimuth'}},
				          #'Circular':{'Bridge Layout Line 2 - Horiz':{'LayoutLine':'N', 'SegType':'SegType', 'Station':'Station', 'Radius':'Radius', 'Bearing':'Azimuth'}},
						  #'Spiral':{'Bridge Layout Line 2 - Horiz':{'LayoutLine':'N', 'SegType':'SegType', 'Station':'Station', 'Radius':'Radius', 'Bearing':'Azimuth'}},
						  'ElevationPoint':{'Bridge Layout Line 3 - Vertical':{'LayoutLine':'N', 'SegType':'SegType', 'Station':'Station', 'Grade':'Grade', 'CoordSys':'CoordinateSystem'}},
						  'FEGrid':{'Grid Lines':{'CoordSys':'CoordinateSystem', 'AxisDir':'AxisDirection', 'GridID':'GridID', 'XRYZCoord':'Coordinate', 'TAngle':'Angle', 'LineType':'LineType',}},
						  'FELane':{'Lane Definition Data':{'Lane':'N', 'LaneFrom':'LaneFrom', 'LayoutLine':'ReferenceLayout', 'Frame':'ReferenceFrame', 'Station':'Station', 'Width':'Width', 'Offset':'Offset', 'Radius':'Radius', 'DiscAlong':'DiscAlong', 'DiscAcross':'DiscAcross', 'LeftType':'LeftType', 'RightType':'RightType'}},
						  'FEVehicle':{'Vehicles 2 - Gen Vehicles 1':{'VehName':'N', 'NumInter':'NumLoad'}}, # ***
						  'FEVehicleClass':{'Vehicles 4 - Vehicle Classes':{'VehClass':'N', 'VehName':'VehName','ScaleFactor':'ScaleFactor'}},
						  'FEVehicleLoad':{'Vehicles 3 - Gen Vehicles 2':{'VehName':'N', 'LoadType':'LoadType', 'UnifLoad':'UnifLoad', 'UnifType':'UnifType', 'UnifWidth':'UnifWidth', 'AxleLoad':'AxleLoad', 'AxleType':'AxleType', 'AxleWidth':'AxleWidth', 'MinDist':'MinDist', 'MaxDist':'MaxDist'}},
						  'FELoadPattern':{'Load Pattern Definitions':{'LoadPat':'N', 'DesignType':'DesignType', 'SelfWtMult':'SelfWeightFactor'}}, # ***
						  'FEMultiStep':{'Multi-Step Moving 1 - General':{'LoadPat':'N', 'LoadDur':'LoadDuration', 'LoadDisc':'LoadDiscretization'},
						                 'Multi-Step Moving 2 - Veh Data':{'LoadPat':'N', 'Vehicle':'Vehicle', 'Lane':'Lane', 'Station':'Station', 'StartTime':'StartTime', 'Direction':'Direction', 'Speed':'Speed'}},
						  'FEFunction':{'Function - PSD - User':{'Name':'N', 'Frequency':'Frequency', 'Value':'Value'}, # ***
						                'Function - Resp Spect - User':{'Name':'N', 'Period':'Period', 'Accel':'Accel', 'FuncDamp':'FuncDamp'},
						                'Function - Steady State - User':{'Name':'N', 'Frequency':'Frequency', 'Value':'Value'},
						                'Function - Time History - User':{'Name':'N', 'Time':'Time', 'Value':'Value'}},
						  'FELoadCase':{'Load Case Definitions':{'Case':'N', 'Type':'Type', 'InitialCond':'InitialCondition','DesignType':'DesignType','RunCase':'RunCase'}},
						  'FEStatic':{'Case - Static 1 - Load Assigns':{'Case':'N', 'LoadType':'LoadType', 'LoadName':'LoadName', 'LoadSF':'ScaleFactor'}},
						  'FEModal':{'Case - Modal 1 - General':{'Case':'N', 'ModeType':'ModeType', 'MaxNumModes':'MaxNumModes', 'MinNumModes':'MinNumModes', 'EigenShift':'FrequencyShift', 'EigenCutoff':'CutoffFrequency', 'EigenTol':'ConvergenceTolerance'}},
						  'FEMultiStepStatic':{'Case - MSStat 1 - Load Assigns':{'Case':'N', 'LoadType':'LoadType', 'LoadName':'LoadName', 'LoadSF':'ScaleFactor'}},
						  'FEDirectIntegrationHistory':{'Case - Direct Hist 1 - General':{'Case':'N', 'OutSteps':'NumStep', 'StepSize':'StepSize'},
						                 	 			'Case - Direct Hist 2 - Loads':{'Case':'N', 'LoadType':'LoadType', 'LoadName':'LoadName', 'Function':'Function', 'LoadSF':'ScaleFactor', 'TimeFactor':'TimeFactor', 'ArrivalTime':'ArrivalTime'},
						                 	 			'Case - Direct Hist 3 - Damping':{'Case':'N', 'MassCoeff':'MassCoefficient', 'StiffCoeff':'StiffCoefficient'},
						                				'Case - Direct Hist 4 - Int Pars':{'Case':'N', 'IntMethod':'IntegrationMethod', 'Gamma':'Gamma', 'Beta':'Beta', 'Alpha':'Alpha'}},
						  # Need revision here..
            			  'SectionDesigner':{'SD 01 - General':{'SectionName':'N', 'DesignType':'DesignType', 'DsgnOrChck':'DsgnOrChck', 'IncludeVStr':'IncludeVStr'}}, # *****
            			  'ShapePlate':{'SD 11 - Shape Plate':{'SectionName':'N', 'ShapeName':'ShapeName', 'ShapeMat':'ShapeMat', 'ZOrder':'ZOrder', 'XCenter':'XCenter', 'YCenter':'YCenter', 'Thickness':'Thickness', 'Width':'Width', 'Rotation':'Rotation', 'Reinforcing':'Reinforcing', 'RebarMat':'RebarMat', 'BarMatType':'BarMatType'}},
            			  'ShapeSolidRectangle':{'SD 12 - Shape Solid Rectangle':{'SectionName':'N', 'ShapeName':'ShapeName', 'ShapeMat':'ShapeMat', 'ZOrder':'ZOrder', 'XCenter':'XCenter', 'YCenter':'YCenter', 'Height':'Height', 'Width':'Width', 'Rotation':'Rotation', 'Reinforcing':'Reinforcing', 'RebarMat':'RebarMat', 'BarMatType':'BarMatType'}},
            			  'FiberGeneral':{'SD 30 - Fiber General':{'SectionName':'N', 'NumFibersD2':'NumFibersD2', 'NumFibersD3':'NumFibersD3', 'CoordSys':'CoordSys', 'GridAngle':'GridAngle', 'LumpRebar':'LumpRebar', 'FiberPMM':'FiberPMM', 'FiberMC':'FiberMC'}},
						 }




