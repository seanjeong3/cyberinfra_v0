'use strict';

MonitoringApp.controller('LoginRegisterController', ['$scope','$resource','$location','$rootScope',
    function ($scope, $resource, $location, $rootScope) {

        $scope.username = '';

        $scope.main.title = 'Please Login';

        $scope.loginMessage = '';

        $scope.login = function() {
            var userLogin = $resource('/admin/login');
            userLogin.save({user_id: $scope.username, password: $scope.pw}, function (response) {
                $scope.loggedInUser.push(response);
                $location.path('/sensor');
                $rootScope.$broadcast('userLogin');
            }, function errorHandling(err) {
                if (err.status === 400) {
                    $scope.loginMessage = err.data;
                } else {
                    console.log(err);
                }
            });
        };

        // $scope.registrationMode = false;

        // $scope.registration = function() {
        //     $scope.registrationMode = true;
        // };

        // $scope.cancelRegistration = function() {
        //     $scope.registrationMode = false;
        // };

        // $scope.registerResultMessage = '';

        // $scope.register = function() {
        //     if($scope.password!==$scope.passwordCheck) {
        //         $scope.registerResultMessage = "Passwords are not consistent.";
        //     }
        //     var userRegister = $resource('/user');
        //     userRegister.save({login_name: $scope.loginname, 
        //                     password: $scope.password,
        //                     first_name: $scope.firstname,
        //                     last_name: $scope.lastname,
        //                     location: $scope.location,
        //                     description: $scope.description,
        //                     occupation: $scope.occupation
        //     }, function (response) {
        //         $scope.registerResultMessage = '';
        //         $scope.loginMessage = "Regiester success!";
        //         $scope.registrationMode = false;
        //     }, function errorHandling(err) {
        //         $scope.registerResultMessage = err.data;
        //         console.log(err);
        //     });
        //     delete $scope.loginname;
        //     delete $scope.password;
        //     delete $scope.passwordCheck;
        //     delete $scope.firstname;
        //     delete $scope.lastname;
        //     delete $scope.location;
        //     delete $scope.description;
        //     delete $scope.occupation;
        // };
    }]);
