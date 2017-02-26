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
}]);
