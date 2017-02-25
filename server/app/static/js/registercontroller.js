'use strict';

angular.module('myApp.registerview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/register', {
    templateUrl: '/static/partials/register.html',
    controller: 'RegisterController'
  });
}])

.controller('RegisterController', ['$scope', '$location', '$route', '$http', 'authentication', function($scope, $location, $route, $http, authentication) {
  $scope.onLogin = function() {
    //move to main page

    console.log("does it work?");
    $location.path("/login");
    //
  }
  $scope.onRegister = function() {
    var username = $('#inputUser').val();
    var name = $('#inputName').val();
    var password = $('#inputPassword').val();
    var address = $('#inputAddress').val();
    var phone1 = $('#inputPhone1').val();
    var phone2 = $('#inputPhone2').val();
    var regRequest = {
      method: 'POST',
      url: '/register_user',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        username: username,
        name: name,
        password: password,
        assistantphone: phone1,
        emergencyphone: phone2,
        address: address
      },
      transformRequest: function(obj) {
        var str = [];
        for(var p in obj)
        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        return str.join("&");
      }
    }
      $http(regRequest).then(function success(response) {
        if(response.data == "registered") {
          console.log("We win!");
          authentication.setUser({
            name: username,
          });
          $location.path('/main');
        }
        else {
          console.log("We lose!");
        }
      }, function error(response) {
        console.log("rip, we got register error");
      });
    };
    // $location.path("/register");

}]);
