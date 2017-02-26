'use strict';

angular.module('myApp.mainview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/main', {
    templateUrl: '/static/partials/main.html',
    controller: 'MainController'
  });
}])

.controller('MainController', ['$scope', '$location', '$route', '$http', 'authentication', function($scope, $location, $route, $http, authentication) {
  console.log("We have it");
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
}]);
