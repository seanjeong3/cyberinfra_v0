/**
 * Define StatesController for the states component of CS142 project #4
 * problem #2.  The model data for this view (the states) is available
 * at window.cs142models.statesModel().
 */

MonitoringApp.controller('SensorController', ['$scope', function($scope) {

   if ($scope.main) {
      $scope.main.title = 'I275 Monitoring - Sensor';
   }

   $scope.sensorID = '';
   $scope.sensorType = '';
   $scope.install = '';
   $scope.remove = '';
   $scope.sensorList = '';


	$scope.searchSensor = function() {
		var url = 'http://eilcloud.westus2.cloudapp.azure.com/sensor';
		if ($scope.sensorID != '') {
			url = url + '/' + $scope.sensorID;
		} else {
			if ($scope.sensorType != '' || $scope.install != '' || $scope.remove != '') {
				url = url + '?';
			};
			if ($scope.sensorType != '') {
				url = url + 'sensorType=' + $scope.sensorType;
			};
			if ($scope.install != '') {
				if ($scope.sensorType != '') {
					url = url + '&';
				}
				url = url + 'install=' + $scope.install;
			};
			if ($scope.remove != '') {
				if ($scope.sensorType != '' || $scope.install != '') {
					url = url + '&';
				}
				url = url + 'remove=' + $scope.remove;
			};
		};

		$scope.FetchModel(url, function(model) {
            $scope.$apply(function() {
                $scope.sensorList = model;
            });
        });
	};

}]);
