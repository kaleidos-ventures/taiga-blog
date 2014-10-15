(function() {
  (function() {
    var getCookie, setCookie;
    setCookie = function(cname, cvalue) {
      return document.cookie = cname + "=" + cvalue + ";";
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
      return setCookie('cookieConsent', 1);
    });
  })();

}).call(this);

