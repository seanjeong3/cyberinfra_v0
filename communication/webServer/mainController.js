"use strict";


var MonitoringApp = angular.module('MonitoringApp', ['ngRoute','ngMaterial', 'ngResource']);



MonitoringApp.config(['$routeProvider','$locationProvider',
  function($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider.
      when('/sensor', {
        templateUrl: 'components/sensor/sensorTemplate.html',
        controller: 'SensorController'
      }).
      when('/sensordata', {
        templateUrl: 'components/sensordata/sensordataTemplate.html',
        controller: 'SensordataController'
      }).
      when('/imagedata', {
        templateUrl: 'components/imagedata/imagedataTemplate.html',
        controller: 'ImagedataController'
      }).
      when('/bridgemodel', {
        templateUrl: 'components/bridgemodel/bridgemodelTemplate.html',
        controller: 'BridgemodelController'
      }).
      when('/login-register', {
          templateUrl: 'components/login-register/login-registerTemplate.html',
          controller: 'LoginRegisterController'
      }).
      otherwise({
        redirectTo: '/sensor'
      });
  }]);



MonitoringApp.controller('MainController', ['$scope', '$rootScope', '$location', '$resource', '$http',
    function($scope, $rootScope, $location, $resource, $http) {


    $scope.loggedInUser = [];
    
    var noOneIsLoggedIn = function() {
        if ($scope.loggedInUser.length > 0) {
            return true;
        }
        return false;
    };

    $scope.logout = function() {
      var userLogout = $resource('/admin/logout');
      userLogout.save({}, function (response) {
          $scope.loggedInUser = [];
          $rootScope.$broadcast('userLogout');
          $location.path("/login-register");
      }, function errorHandling(err) {
          console.log(err);
      });
    };

    $rootScope.$on( "$routeChangeStart", function(event, next, current) {
        if (!noOneIsLoggedIn()) {
            $scope.logout();
        // no logged user, redirect to /login-register unless already there
        if (next.templateUrl !== "components/login-register/login-registerTemplate.html") {
                $location.path("/login-register");
            }
        }
    });


   // We defined an object called 'main' with a single property 'title' that is used
   // by the html view template to get the page's title in the browser tab.
   $scope.main = {};
   $scope.main.title = 'I275 Monitoring';
   $scope.main.motto = 'I275 Monitoring User Interface';
   $scope.main.nextView = 'sensor';
   

   $scope.buttonClick = function(buttonName) {
      $scope.main.nextView = buttonName;
   };

   $scope.FetchModel = function(url, doneCallback) {

      var xhr = new XMLHttpRequest();
      function xhrHandler() {
          if (xhr.readyState !== 4) {
              return;
          }
          if (xhr.status !== 200) {
              console.log("error: " + xhr.status);
              return;
          }
          var model = JSON.parse(xhr.response);
          doneCallback(model);
      }
      xhr.onreadystatechange = xhrHandler;
      xhr.open("GET", url);
      xhr.send();
      
  };


}]);


