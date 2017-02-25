'use strict';

angular.module('myApp.loginview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: '/static/partials/login.html',
    controller: 'LoginController'
  });
}])

.controller('LoginController', ['$scope', '$location', '$route', '$http', 'authentication', function($scope, $location, $route, $http, authentication) {
  $scope.onLogin = function() {
    //move to main page
    console.log("hello");
    //
  }
  $scope.onRegister = function() {
    console.log("does it work?");
    // $location.path("/register");
  }
}]);
