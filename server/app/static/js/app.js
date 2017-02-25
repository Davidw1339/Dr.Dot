// 'use strict';   // See note about 'use strict'; below
//
// console.log("best test");
//
// var myApp = angular.module('myApp', [
//  'ngRoute',
// ]);
//
// myApp.config(['$routeProvider',
//      function($routeProvider) {
//          $routeProvider.
//              when('/', {
//                  templateUrl: '/static/partials/login.html',
//                  controller: 'LoginController'
//              }).
//              otherwise({
//                  redirectTo: '/'
//              });
//     }]);


'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.loginview',
  'myApp.registerview'
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
