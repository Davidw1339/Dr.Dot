'use strict';   // See note about 'use strict'; below

console.log("test test");

var myApp = angular.module('myApp', [
 'ngRoute',
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/about.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);
