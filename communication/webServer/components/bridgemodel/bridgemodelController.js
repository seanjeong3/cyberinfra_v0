/**
 * Define StatesController for the states component of CS142 project #4
 * problem #2.  The model data for this view (the states) is available
 * at window.cs142models.statesModel().
 */

MonitoringApp.controller('BridgemodelController', ['$scope', function($scope) {

   if ($scope.main) {
      $scope.main.title = 'I275 Monitoring - Bridge model';
   }

   $scope.bridge = '';
   $scope.baseURL = 'http://eilcloud.westus2.cloudapp.azure.com/';

	$scope.changelink = function() {
        var linka = document.getElementById("linka");
        linka.setAttribute('href', $scope.baseURL + 'geometricmodel/' + $scope.bridge);
        var linkb = document.getElementById("linkb");
        linkb.setAttribute('href', $scope.baseURL + 'femodel/' + $scope.bridge + '?format=xml');
        var linkc = document.getElementById("linkc");
        linkc.setAttribute('href', $scope.baseURL + 'femodel/' + $scope.bridge + '?format=xlsx');

	};

}]);
