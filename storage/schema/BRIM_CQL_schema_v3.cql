-- Create Keyspace

CREATE KEYSPACE IF NOT EXISTS i275monitoring
WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'DC1' : 3 };

DROP TABLE i275monitoring.Unit;
CREATE TABLE IF NOT EXISTS i275monitoring.Unit
(uid uuid, N text, T text,
  length text, force text, angle text, temperature text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.Project;
CREATE TABLE IF NOT EXISTS i275monitoring.Project
(uid uuid, N text, T text,
  child map<uuid,text>, PRIMARY KEY(uid));
CREATE INDEX ON i275monitoring.Project(N);

DROP TABLE i275monitoring.Group;
CREATE TABLE IF NOT EXISTS i275monitoring.Group
(uid uuid, N text, T text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));
-- General

-- Engineering model

DROP TABLE i275monitoring.Node;
CREATE TABLE IF NOT EXISTS i275monitoring.Node
(uid uuid, N text, T text,
  x double, y double, z double, tx text, ty text, tz text,
  rx text, ry text, rz text, coordinatesystem text, coordinatetype text, 
  r double, theta double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FELine;
CREATE TABLE IF NOT EXISTS i275monitoring.FELine
(uid uuid, N text, T text, 
  node1 text, node2 text, section text, betaangle double,
  automesh text, atjoints text, atframes text, numberofsegments int, maxlength double, 
  maxdegrees double, node1p text, node1v2 text, node1v3 text, node1t text, node1m2 text, node1m3 text, iscurved text,
  node2p text, node2v2 text, node2v3 text, node2t text, node2m2 text, node2m3 text, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FESurface;
CREATE TABLE IF NOT EXISTS i275monitoring.FESurface
(uid uuid, N text, T text, 
  numjoints int, node1 text, node2 text, node3 text, node4 text, node5 text, 
  node6 text, node7 text, node8 text, node9 text, node10 text,
  node11 text, node12 text, node13 text, node14 text, node15 text, 
  node16 text, node17 text, node18 text, node19 text, node20 text, 
  node21 text, node22 text, node23 text, node24 text, node25 text, 
  thickness double, material text, section text, meshtype text, numberofobject1 double,
  meshgroup text, maxsize1 double, numberofobject2 double, maxsize2 double, pointfromline text, 
  pointfrompoint text, localedge text, localface text, constraintedge text, 
  constraintface text, submesh text, edgeconstraint text, offset1 double, offset2 double, offset3 double, 
  offset4 double, offset5 double, offset6 double, offset7 double, offset8 double, 
  offset9 double, offset10 double, offset11 double, offset12 double, offset13 double, 
  offset14 double, offset15 double, offset16 double, offset17 double, offset18 double, 
  offset19 double, offset20 double, offset21 double, offset22 double, offset23 double, 
  offset24 double, offset25 double, 
  springtype text, springstiffness double, springsimpletype text, springface text, 
  springdir1type text, springnormaldir text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FELineSection;
CREATE TABLE IF NOT EXISTS i275monitoring.FELineSection
(uid uuid, N text, T text, 
  material text, shape text, width double, height double, 
  webthickness double, flangethickness double, eccv2 double,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FESurfaceSection;
CREATE TABLE IF NOT EXISTS i275monitoring.FESurfaceSection
(uid uuid, N text, T text, 
  material text, matangle double, surfacetype text, type text,
  thickness double, bendthickness double, drilldof text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.Material;
CREATE TABLE IF NOT EXISTS i275monitoring.Material
(uid uuid, N text, T text, 
  e double, nu double, d double, a double, fy double, fu double, fc28 double, type text,  
  symtype text, tempdepend text, g double, efffy double, efffu double, modalratio double, 
  vismass double, visstiff double, hysmass double, hysstiff double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.Rebar;
CREATE TABLE IF NOT EXISTS i275monitoring.Rebar
(uid uuid, N text, T text,
  diameter double, area double, weight double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FECoordinateSystem;
CREATE TABLE IF NOT EXISTS i275monitoring.FECoordinateSystem
(uid uuid, N text, T text,
  type text, x double, y double, z double, rx double, ry double, rz double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.Alignment;
CREATE TABLE IF NOT EXISTS i275monitoring.Alignment
(uid uuid, N text, T text,
  x double, y double, z double,
  station double, azimuth double, latitude double, longitude double, coordinatesystem text, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.Straight;
CREATE TABLE IF NOT EXISTS i275monitoring.Straight
(uid uuid, N text, T text,
  SegType text, Station double, Radius double, Azimuth double,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.ElevationPoint;
CREATE TABLE IF NOT EXISTS i275monitoring.ElevationPoint
(uid uuid, N text, T text,
  SegType text, Station double, Grade double, coordinatesystem text, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEGrid;
CREATE TABLE IF NOT EXISTS i275monitoring.FEGrid
(uid uuid, N text, T text,
  coordinatesystem text, gridid text, axisdirection text, coordinate double, angle double, linetype text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FELane;
CREATE TABLE IF NOT EXISTS i275monitoring.FELane
(uid uuid, N text, T text,
  lanefrom text, referencelayout text, referenceframe text, station double, width double, 
  offset double, radius double, discalong int, discacross int, lefttype text, righttype text, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEVehicle;
CREATE TABLE IF NOT EXISTS i275monitoring.FEVehicle
(uid uuid, N text, T text,
  numload int,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEVehicleClass;
CREATE TABLE IF NOT EXISTS i275monitoring.FEVehicleClass
(uid uuid, N text, T text,
  vehname text, scalefactor double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEVehicleLoad;
CREATE TABLE IF NOT EXISTS i275monitoring.FEVehicleLoad
(uid uuid, N text, T text,
  loadtype text, unifload double, uniftype text, unifwidth double, axleload double, 
  axletype text, axlewidth double, mindist double, maxdist double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FELoadPattern;
CREATE TABLE IF NOT EXISTS i275monitoring.FELoadPattern
(uid uuid, N text, T text,
  designtype text, selfweightfactor double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEMultiStep;
CREATE TABLE IF NOT EXISTS i275monitoring.FEMultiStep
(uid uuid, N text, T text,
  loadduration double, loaddiscretization double, vehicle text, lane text, 
  station double, starttime double, direction  text, Speed double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEFunction;
CREATE TABLE IF NOT EXISTS i275monitoring.FEFunction
(uid uuid, N text, T text,
  functiontype text, frequency double, time double, value double, 
  period double, accel double, funcdamp double,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FELoadCase;
CREATE TABLE IF NOT EXISTS i275monitoring.FELoadCase
(uid uuid, N text, T text,
  type text, initialcondition text, designtype text, runcase text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEStatic;
CREATE TABLE IF NOT EXISTS i275monitoring.FEStatic
(uid uuid, N text, T text,
  loadtype text, loadname text, scalefactor double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEModal;
CREATE TABLE IF NOT EXISTS i275monitoring.FEModal
(uid uuid, N text, T text,
  modetype text, maxnummodes int, minnummodes int, frequencyshift double, 
  cutofffrequency double, convergencetolerance double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEMultiStepStatic;
CREATE TABLE IF NOT EXISTS i275monitoring.FEMultiStepStatic
(uid uuid, N text, T text,
  loadtype text, loadname text, scalefactor double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FEDirectIntegrationHistory;
CREATE TABLE IF NOT EXISTS i275monitoring.FEDirectIntegrationHistory
(uid uuid, N text, T text,
  numstep int, stepsize double, loadtype text, loadname text, function text, 
  scalefactor double, timefactor double, arrivaltime double, 
  masscoefficient double, stiffcoefficient double,
  integrationmethod text, gamma double, beta double, alpha double, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.SectionDesigner;
CREATE TABLE IF NOT EXISTS i275monitoring.SectionDesigner
(uid uuid, N text, T text,
  designtype text, dsgnorchck text, includevstr text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.ShapePlate;
CREATE TABLE IF NOT EXISTS i275monitoring.ShapePlate
(uid uuid, N text, T text,
  shapename text, shapemat text, zorder int, xcenter double, ycenter double, thickness double, 
  width double, rotation double, reinforcing text, rebarmat text, barmattype text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.ShapeSolidRectangle;
CREATE TABLE IF NOT EXISTS i275monitoring.ShapeSolidRectangle
(uid uuid, N text, T text,
  shapename text, shapemat text, zorder int, xcenter double, ycenter double, height double,
  width double, rotation double, reinforcing text, rebarmat text, barmattype text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));

DROP TABLE i275monitoring.FiberGeneral;
CREATE TABLE IF NOT EXISTS i275monitoring.FiberGeneral
(uid uuid, N text, T text,
  numfibersd2 text, numfibersd3 text, coordsys text, gridangle text, 
  lumprebar text, fiberpmm text, fibermc text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(uid));


-- Sensor 

CREATE TABLE IF NOT EXISTS i275monitoring.Sensor 
(sensor_id text, N text, T text,
  long_name text, short_name text, model_number text, manufacturer text, sensor_type text, 
  intended_application text, sensor_name text, keywords list<text>, description text, 
  input text, output text, input_uom text, output_uom text, sampling_rate double, gain double, 
  conversion_factor double, install timestamp, remove timestamp, position_description text, 
  local_coordinate text, global_coordinate text, data_link text, weight double, 
  length double, width double, height double, weight_uom text, length_uom text, voltage text, 
  voltage_uom text, current_type text, amp_range text, amp_range_uom text, sensing_range text, 
  sensitivity text, sampling_period text, responsible_party text, telephone text, address text, 
  manual text, fenode text, target_object uuid, note text, 
  bridge_name text, sensor_status text, contact_phone text, contact_email text,
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(sensor_id, install));
CREATE INDEX IF NOT EXISTS ON i275monitoring.Sensor(sensor_type);
CREATE INDEX IF NOT EXISTS ON i275monitoring.Sensor(target_object);

CREATE TABLE IF NOT EXISTS i275monitoring.SensorData
(sensor_id text, year text, event_time timestamp, data list<double>, PRIMARY KEY((sensor_id, year), event_time));

CREATE TABLE IF NOT EXISTS i275monitoring.SensorDataRaw
(sensor_id text, year text, event_time timestamp, data list<double>, PRIMARY KEY((sensor_id, year), event_time));


CREATE TABLE IF NOT EXISTS i275monitoring.SensorDataOneDay
(sensor_id text, event_time timestamp, data double, PRIMARY KEY(sensor_id, event_time));

CREATE TABLE IF NOT EXISTS i275monitoring.SensorDataOneWeek
(sensor_id text, event_time timestamp, data double, PRIMARY KEY(sensor_id, event_time));

CREATE TABLE IF NOT EXISTS i275monitoring.SensorDataOneMonth
(sensor_id text, event_time timestamp, data double, PRIMARY KEY(sensor_id, event_time));

CREATE TABLE IF NOT EXISTS i275monitoring.SensorDataThreeMonth
(sensor_id text, event_time timestamp, data double, PRIMARY KEY(sensor_id, event_time));

CREATE TABLE IF NOT EXISTS i275monitoring.SensorDataOneYear
(sensor_id text, event_time timestamp, data double, PRIMARY KEY(sensor_id, event_time));



CREATE TABLE IF NOT EXISTS EventData
(sensor_id text, event_time timestamp, event_type text, event_info text, event_detail text, PRIMARY KEY(sensor_id, event_time));

CREATE INDEX IF NOT EXISTS ON EventData(event_type);

-- DEPRECATED!!!
CREATE TABLE IF NOT EXISTS i275monitoring.datafilelist
(daq_id text, event_time timestamp, file_list list<text>, PRIMARY KEY(daq_id, event_time));

CREATE TABLE IF NOT EXISTS i275monitoring.daqevent
(p_key text, event_time timestamp, sensor list<text>, PRIMARY KEY(p_key, event_time)) WITH CLUSTERING ORDER BY (event_time ASC);

CREATE TABLE IF NOT EXISTS i275monitoring.ImageData
(camera_id text, month text, event_time timestamp, image blob, PRIMARY KEY((camera_id, month), event_time));

-- DEPRECATED!!!
CREATE TABLE IF NOT EXISTS i275monitoring.Trafficimage
(bridge text, date text, event_time timestamp, image blob, PRIMARY KEY((bridge, date), event_time));

-- Inspection

CREATE TABLE IF NOT EXISTS i275monitoring.Inspection (
  inspection_id uuid, N text, T text,
  inspection_date timestamp, inspection_project text, inspection_type text, nbe_code text, 
  inspected_item text, target_object uuid, rank text, total_quantity double, 
  stage1 double, stage2 double, stage3 double, stage4 double, stage5 double, quantity_uom text, 
  damage_type text, damage_location text, damage_amount double, damage_uom text, 
  note text, data_link text, image blob, 
  parent map<uuid,text>, child map<uuid,text>, PRIMARY KEY(inspection_id, inspection_date));
CREATE INDEX IF NOT EXISTS ON i275monitoring.Inspection(target_object);

-- Geometry

CREATE TABLE IF NOT EXISTS i275monitoring.Geometry
(uid uuid, T text, N text, extends text, 
  x text, y text, z text, rx text, ry text, rz text, ax text, ay text, az text, 
  parent map<uuid,text>, child map<uuid,text>, parameter text, PRIMARY KEY(uid));
CREATE INDEX IF NOT EXISTS ON i275monitoring.Geometry(N);



-- Userlist
CREATE TABLE IF NOT EXISTS i275monitoring.UserList
(user_id text, password text, email text, first_name text, last_name text, PRIMARY KEY(user_id));



-- Weatherdata
CREATE TABLE IF NOT EXISTS i275monitoring.WeatherData
(city text, state text, event_time timestamp, temperature double, wind_chill double, dew_point double, humidity double, pressure double, visibility double, wind_direction text, wind_speed double, gust_speed double, precipitation double, events text, conditions text, PRIMARY KEY((city, state), event_time));











