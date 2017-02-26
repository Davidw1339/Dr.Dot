'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.loginview',
  'myApp.registerview',
  'myApp.mainview',
  'myApp.doctorview',
  'myApp.profileview'
]).
service('authentication', function() {
    this.user = {
      name: "none"
    };
    this.getUser = function() {
      return this.user;
    }
    this.setUser = function(x) {
      this.user = x;
    }
}).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider.otherwise({redirectTo: '/login'});
}]);
