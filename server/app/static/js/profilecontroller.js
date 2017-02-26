'use strict';

angular.module('myApp.profileview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/profile', {
    templateUrl: '/static/partials/main.html',
    controller: 'ProfileController'
  });
}])

.controller('ProfileController', ['$scope', '$location', '$route', '$http', 'authentication', function($scope, $location, $route, $http, authentication) {
  $("#profileview").show();
  $("#usernameHeading").html(authentication.getUser().name);
  $scope.openNav = function() {
      document.getElementById("mySidenav").style.width = "250px";
      document.getElementById("main").style.marginLeft = "250px";
  }

  $scope.closeNav = function() {
      document.getElementById("mySidenav").style.width = "0";
      document.getElementById("main").style.marginLeft= "0";
  }

  $scope.goDoctor = function() {
      console.log("heyo");
      $location.path("/doctors");
  }

  $scope.goProfile = function() {
      $location.path("/profile");
  }

  $scope.goMain = function() {
      $location.path("/main");
  }

  var username = authentication.getUser().name;
  if(username != "none") {
  $http({
    method: 'GET',
    url: '/get_user?username=' + username
  }).then(function successCallback(response) {
      if(response.data) {
          var user = angular.fromJson(response.data)
          $("#inputAddress").val(user['address'])
          $("#inputPhone1").val(user['assistantphone'])
          $("#inputPhone2").val(user['emergencyphone'])
      }
      else {
          $('#error').show();
      }
    }, function errorCallback(response) {
      $('#error').show();
  }); }
}]);
