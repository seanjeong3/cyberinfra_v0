brim_to_csi_dictionary = {'FEVehicleLoad': {'Vehicles 3 - Gen Vehicles 2': {'maxdist': 'MaxDist', 'loadtype': 'LoadType', 'unifwidth': 'UnifWidth', 'axleload': 'AxleLoad', 'N': 'VehName', 'mindist': 'MinDist', 'uniftype': 'UnifType', 'unifload': 'UnifLoad', 'axlewidth': 'AxleWidth', 'axletype': 'AxleType'}},

					 'ShapePlate': {'SD 11 - Shape Plate': {'ycenter': 'YCenter', 'shapename': 'ShapeName', 'xcenter': 'XCenter', 'reinforcing': 'Reinforcing', 'thickness': 'Thickness', 'width': 'Width', 'zorder': 'ZOrder', 'shapemat': 'ShapeMat', 'rotation': 'Rotation', 'N': 'SectionName', 'rebarmat': 'RebarMat', 'barmattype': 'BarMatType'}},

					 'FESurfaceSection': {'Area Section Properties': {'bendthickness': 'BendThick', 'drilldof': 'DrillDOF', 'surfacetype': 'AreaType', 'material': 'Material', 'N': 'Section', 'matangle': 'MatAngle', 'thickness': 'Thickness', 'type': 'Type'}},

					 'FEModal': {'Case - Modal 1 - General': {'minnummodes': 'MinNumModes', 'convergencetolerance': 'EigenTol', 'N': 'Case', 'modetype': 'ModeType', 'cutofffrequency': 'EigenCutoff', 'maxnummodes': 'MaxNumModes', 'frequencyshift': 'EigenShift'}},

					 'FESurface': {'Area Edge Constraint Assigns': {'edgeconstraint': 'Constrained', 'N': 'Area'},
								 'Connectivity - Area': {'N': 'Area', 'numjoints': 'NumJoints', 'node1': 'Joint1', 'node3': 'Joint3', 'node2': 'Joint2', 'node4': 'Joint4'},
								 'Area Section Assignments': {'section': 'Section', 'N': 'Area'},
								 'Area Spring Assignments': {'springnormaldir': 'NormalDir', 'springface': 'Face', 'springdir1type': 'Dir1Type', 'springstiffness': 'Stiffness', 'springsimpletype': 'SimpleType', 'N': 'Area', 'springtype': 'Type'},
								 'Area Overwrites - Joint Offsets': {'offset4': 'Offset4', 'N': 'Area', 'offset1': 'Offset1', 'offset2': 'Offset2', 'offset3': 'Offset3'},
								 'Area Auto Mesh Assignments': {'constraintface': 'SuppFace', 'meshtype': 'MeshType', 'constraintedge': 'SuppEdge', 'localedge': 'LocalEdge', 'pointfromline': 'PtsFromLine', 'N': 'Area', 'pointfrompoint': 'PtsFromPt', 'meshgroup': 'MeshGroup', 'submesh': 'SubMesh', 'localface': 'LocalFace'}},

					 'Node': {'Joint Coordinates': {'coordinatetype': 'CoordType', 'coordinatesystem': 'CoordSys', 'N': 'Joint', 'theta': 'T', 'y': 'Y', 'x': 'XorR', 'z': 'Z'},
					 			'Joint Restraint Assignments': {'tz': 'U3', 'tx': 'U1', 'ty': 'U2', 'rx': 'R1', 'ry': 'R2', 'rz': 'R3', 'N': 'Joint'}},

					 'FEMultiStepStatic': {'Case - MSStat 1 - Load Assigns': {'scalefactor': 'LoadSF', 'loadtype': 'LoadType', 'loadname': 'LoadName', 'N': 'Case'}},

					 'Rebar': {'Rebar Sizes': {'diameter': 'Diameter', 'area': 'Area', 'N': 'RebarID'}},

					 'Material': {'MatProp 03f - Tendon Data': {'fy': 'Fy', 'fu': 'Fu', 'N': 'Material'},
								 'MatProp 03a - Steel Data': {'efffy': 'EffFy', 'fy': 'Fy', 'efffu': 'EffFu', 'fu': 'Fu', 'N': 'Material'},
								 'MatProp 02 - Basic Mech Props': {'a': 'A1', 'e': 'E1', 'd': 'UnitMass', 'g': 'G12', 'N': 'Material', 'nu': 'U12'},
								 'MatProp 06 - Damping Parameters': {'modalratio': 'ModalRatio', 'visstiff': 'VisStiff', 'hysmass': 'HysMass', 'N': 'Material', 'hysstiff': 'HysStiff', 'vismass': 'VisMass'},
								 'MatProp 01 - General': {'symtype': 'SymType', 'type': 'Type', 'tempdepend': 'TempDepend', 'N': 'Material'},
								 'MatProp 03e - Rebar Data': {'efffy': 'EffFy', 'fy': 'Fy', 'efffu': 'EffFu', 'fu': 'Fu', 'N': 'Material'},
								 'MatProp 03b - Concrete Data': {'N': 'Material', 'fc28': 'Fc'}},

					 'SectionDesigner': {'SD 01 - General': {'designtype': 'DesignType', 'includevstr': 'IncludeVStr', 'dsgnorchck': 'DsgnOrChck', 'N': 'SectionName'}},

					 'FEStatic': {'Case - Static 1 - Load Assigns': {'scalefactor': 'LoadSF', 'loadtype': 'LoadType', 'loadname': 'LoadName', 'N': 'Case'}},

					 'FELoadPattern': {'Load Pattern Definitions': {'designtype': 'DesignType', 'N': 'LoadPat', 'selfweightfactor': 'SelfWtMult'}},

					 'ElevationPoint': {'Bridge Layout Line 3 - Vertical': {'grade': 'Grade', 'station': 'Station', 'segtype': 'SegType', 'coordinatesystem': 'CoordSys', 'N': 'LayoutLine'}},

					 'FiberGeneral': {'SD 30 - Fiber General': {'fiberpmm': 'FiberPMM', 'lumprebar': 'LumpRebar', 'N': 'SectionName', 'coordsys': 'CoordSys', 'gridangle': 'GridAngle', 'fibermc': 'FiberMC', 'numfibersd2': 'NumFibersD2', 'numfibersd3': 'NumFibersD3'}},

					 'FEMultiStep': {'Multi-Step Moving 2 - Veh Data': {'lane': 'Lane', 'direction': 'Direction', 'N': 'LoadPat', 'station': 'Station', 'starttime': 'StartTime', 'vehicle': 'Vehicle', 'speed': 'Speed'},
					 				'Multi-Step Moving 1 - General': {'loadduration': 'LoadDur', 'loaddiscretization': 'LoadDisc', 'N': 'LoadPat'}},

					 'ShapeSolidRectangle': {'SD 12 - Shape Solid Rectangle': {'ycenter': 'YCenter', 'shapename': 'ShapeName', 'xcenter': 'XCenter', 'reinforcing': 'Reinforcing', 'N': 'SectionName', 'width': 'Width', 'zorder': 'ZOrder', 'shapemat': 'ShapeMat', 'rotation': 'Rotation', 'height': 'Height', 'rebarmat': 'RebarMat', 'barmattype': 'BarMatType'}},

					 'Straight': {'Bridge Layout Line 2 - Horiz': {'azimuth': 'Bearing', 'segtype': 'SegType', 'station': 'Station', 'radius': 'Radius', 'N': 'LayoutLine'}},

					 'FELine': {'Frame Releases 1 - General': {'node2v3': 'V3J', 'node1t': 'TI', 'node1p': 'PI', 'node2t': 'TJ', 'node2p': 'PJ', 'N': 'Frame', 'node2m2': 'M2J', 'node2v2': 'V2J', 'node1v2': 'V2I', 'node1v3': 'V3I', 'node1m3': 'M3I', 'node1m2': 'M2I', 'node2m3': 'M3J'},
								 'Connectivity - Frame': {'node1': 'JointI', 'node2': 'JointJ', 'iscurved': 'IsCurved', 'N': 'Frame'},
								 'Frame Auto Mesh': {'automesh': 'AutoMesh', 'maxdegrees': 'MaxDegrees', 'atjoints': 'AtJoints', 'atframes': 'AtFrames', 'numberofsegments': 'NumSegments', 'N': 'Frame', 'maxlength': 'MaxLength'},
								 'Frame Section Assignments': {'section': 'AnalSect', 'N': 'Frame'}},

					 'FECoordinateSystem': {'Coordinate Systems': {'rx': 'AboutX', 'ry': 'AboutY', 'rz': 'AboutZ', 'N': 'Name', 'y': 'Y', 'x': 'X', 'z': 'Z', 'type': 'Type'}},

					 'FEFunction': {'Function - Resp Spect - User': {'funcdamp': 'FuncDamp', 'period': 'Period', 'accel': 'Accel', 'N': 'Name'},
									 'Function - PSD - User': {'frequency': 'Frequency', 'value': 'Value', 'N': 'Name'},
									 'Function - Time History - User': {'time': 'Time', 'value': 'Value', 'N': 'Name'},
									 'Function - Steady State - User': {'frequency': 'Frequency', 'value': 'Value', 'N': 'Name'}},

					 'FELane': {'Lane Definition Data': {'referenceframe': 'Frame', 'discalong': 'DiscAlong', 'lanefrom': 'LaneFrom', 'N': 'Lane', 'width': 'Width', 'referencelayout': 'LayoutLine', 'station': 'Station', 'radius': 'Radius', 'discacross': 'DiscAcross', 'offset': 'Offset', 'lefttype': 'LeftType', 'righttype': 'RightType'}},

					 'FELoadCase': {'Load Case Definitions': {'designtype': 'DesignType', 'runcase': 'RunCase', 'initialcondition': 'InitialCond', 'type': 'Type', 'N': 'Case'}},

					 'FELineSection': {'Frame Props 01 - General': {'material': 'Material', 'N': 'SectionName', 'width': 't2', 'shape': 'Shape', 'flangethickness': 'tf', 'height': 't3', 'webthickness': 'tw', 'eccv2': 'EccV2'}},

					 'FEDirectIntegrationHistory': {'Case - Direct Hist 4 - Int Pars': {'alpha': 'Alpha', 'beta': 'Beta', 'integrationmethod': 'IntMethod', 'gamma': 'Gamma', 'N': 'Case'},
													 'Case - Direct Hist 3 - Damping': {'stiffcoefficient': 'StiffCoeff', 'masscoefficient': 'MassCoeff', 'N': 'Case'},
													 'Case - Direct Hist 2 - Loads': {'function': 'Function', 'loadtype': 'LoadType', 'loadname': 'LoadName', 'timefactor': 'TimeFactor', 'N': 'Case', 'arrivaltime': 'ArrivalTime', 'scalefactor': 'LoadSF'},
													 'Case - Direct Hist 1 - General': {'numstep': 'OutSteps', 'stepsize': 'StepSize', 'N': 'Case'}},

					 'FEVehicleClass': {'Vehicles 4 - Vehicle Classes': {'scalefactor': 'ScaleFactor', 'N': 'VehClass', 'vehname':'VehName'}},
					 'FEVehicle': {'Vehicles 2 - Gen Vehicles 1': {'numload': 'NumInter', 'N': 'VehName'}},

					 'FEGrid': {'Grid Lines': {'angle': 'TAngle', 'gridid': 'GridID', 'coordinatesystem': 'CoordSys', 'linetype': 'LineType', 'coordinate': 'XRYZCoord', 'axisdirection': 'AxisDir'}},

					 'Alignment': {'Bridge Layout Line 1 - General': {'y': 'Y', 'x': 'X', 'z': 'Z', 'coordinatesystem': 'CoordSys', 'N': 'LayoutLine'}}}