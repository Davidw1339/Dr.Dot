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

    var username = $('#inputUser').val();
    var password = $('#inputPassword').val();

    $http({
      method: 'GET',
      url: '/login?username=' + username + "&password=" + password
    }).then(function successCallback(response) {
        if(response.data != "no-auth") {
          authentication.setUser({
            name: username,
          });
          console.log("successful auth")
          $location.path("/main");
        }
        else {
          $('#error').show();
        }
      }, function errorCallback(response) {
        $('#error').show();
      });

    console.log("hello");
    //
  }
  $scope.onRegister = function() {
    console.log("does it work?");
    $location.path("/register");
  }
}]);
