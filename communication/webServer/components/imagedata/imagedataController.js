/**
 * Define StatesController for the states component of CS142 project #4
 * problem #2.  The model data for this view (the states) is available
 * at window.cs142models.statesModel().
 */

MonitoringApp.controller('ImagedataController', ['$scope', function($scope) {

   if ($scope.main) {
      $scope.main.title = 'I275 Monitoring - Image Data';
   }

   $scope.camera = 'test';
   $scope.begin = '2016-07-01T06:00:00';
   $scope.end = '2016-08-25T06:00:10';
   $scope.imageDataList = '';

	$scope.searchImageData = function() {
		var url = 'http://eilcloud.westus2.cloudapp.azure.com/imagedata';
		// var url = 'http://localhost:3000/imagedata';
		if ($scope.camera != '') {
			url = url + '/' + $scope.camera;
		} 
		if ($scope.begin != '' || $scope.end != '') {
			url = url + '?';
		};
		if ($scope.begin != '') {
			if ($scope.month != '') {
				url = url + '&';
			}
			url = url + 'event_time_begin=' + $scope.begin;
		};
		if ($scope.end != '') {
			if ($scope.month != '' || $scope.end != '') {
				url = url + '&';
			}
			url = url + 'event_time_end=' + $scope.end;
		};

		$scope.FetchModel(url, function(model) {
            $scope.$apply(function() {
            	var newcontent = [];
            	for (i = 0; i < model.content.length; i++) {
            		var img = 'data:image/jpeg;base64,' + btoa(String.fromCharCode.apply(null, model.content[i].image.data));
            		var temp = {"event_time": model.content[i].event_time, "image": img};
            		newcontent.push(temp);
            	}
            	console.log(newcontent);
            	model.content = newcontent;
                $scope.imageDataList = model;
            });
        });
	};

}]);
