(function () {
    'use strict';

    var deps = ['$mdToast', 'message'];
    function toastCtrl($mdToast, message) {
        var self = this; // jshint ignore:line
        self.message = message;

        self.closeToast = function () {
            $mdToast.hide();
        };
    }

    toastCtrl.$inject = deps;
    angular.module('App').controller('ToastController', toastCtrl);
})();
