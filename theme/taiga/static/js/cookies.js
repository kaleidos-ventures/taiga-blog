/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * Copyright (c) 2021-present Kaleidos Ventures SL
 */

(function() {
  (function() {
    var getCookie, setCookie;
    setCookie = function(cname, cvalue, exdays) {
      var d, expires;
      d = new Date();
      d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
      expires = "expires=" + d.toUTCString();
      return document.cookie = cname + "=" + cvalue + "; " + expires;
    };
    getCookie = function(cname) {
      var c, ca, name, _i, _len;
      name = cname + "=";
      ca = document.cookie.split(';');
      for (_i = 0, _len = ca.length; _i < _len; _i++) {
        c = ca[_i];
        while (c.charAt(0) === ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) !== -1) {
          return c.substring(name.length, c.length);
        }
      }
    };
    if (getCookie('cookieConsent') !== '1') {
      $('.cookies').show();
    }
    return $('.cookies').find('.fa').on('click', function() {
      $('.cookies').fadeOut('fast');
      return setCookie('cookieConsent', 1, 730);
    });
  })();

}).call(this);
