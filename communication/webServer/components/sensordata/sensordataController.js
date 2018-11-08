/**
 * Define StatesController for the states component of CS142 project #4
 * problem #2.  The model data for this view (the states) is available
 * at window.cs142models.statesModel().
 */

MonitoringApp.controller('SensordataController', ['$scope', function($scope) {

   if ($scope.main) {
      $scope.main.title = 'I275 Monitoring - Sensor Data';
   }

   $scope.sensorID = 'TRB_u07_ch0';
   $scope.begin = '2014-10-02T00:00:00';
   $scope.end = '2014-10-02T23:59:59';
   $scope.sensorDataList = '';

	$scope.searchSensorData = function() {
		var url = 'http://eilcloud.westus2.cloudapp.azure.com/sensordata';
		if ($scope.sensorID != '') {
			url = url + '/' + $scope.sensorID;
		} 
		if ($scope.begin != '' || $scope.end != '') {
			url = url + '?';
		};
		if ($scope.begin != '') {
			url = url + 'event_time_begin=' + $scope.begin;
		};
		if ($scope.end != '') {
			if ($scope.end != '') {
				url = url + '&';
			}
			url = url + 'event_time_end=' + $scope.end;
		};
		

		$scope.FetchModel(url, function(model) {
            console.log(model);
            $scope.$apply(function() {
                $scope.sensorDataList = model;
            });
        });
	};

}]);
