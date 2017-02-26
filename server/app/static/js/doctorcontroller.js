'use strict';

angular.module('myApp.doctorview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/doctors', {
    templateUrl: '/static/partials/main.html',
    controller: 'DoctorController'
  });
}])

.controller('DoctorController', ['$scope', '$location', '$route', '$http', 'authentication', function($scope, $location, $route, $http, authentication) {
  console.log("Hello JOE!!!")
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

  $("#doctorview").show();
  var username = authentication.getUser();
  console.log(username)
  $http({
    method: 'GET',
    url: '/get_doctor?username=' + username.name
  }).then(function successCallback(response) {
      if(response.data != "") {
        var doctor = angular.fromJson(response.data)
        $("#doctorname").html(doctor['doctor_name'])
        $("#phone").html(doctor['doctor_phone'])
        var address = doctor['doctor_address']
        $("#address").html(address)
        var map_source = "https://www.google.com/maps/embed/v1/place?key=AIzaSyB-7S3jUfAxUgQQqbwGVkqWBD-Tv1WTRiw&q="
        $("#google_map").attr('src', map_source + address)
      }
      else {
        console.log("we got problems")
        // $('#error').show();
      }
    }, function errorCallback(response) {
    //   $('#error').show();
    });
}]);
