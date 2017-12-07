 function offset(a) {
     for (var b = 0; a;) b += parseInt(a.offsetTop), a = a.offsetParent;
     return b
 }
 var s = !0;
 window.onload = function () {
     var a = document.querySelector(".header"),
         b = offset(a),
         f = window.getComputedStyle ? getComputedStyle(a, "") : a.currentStyle,
         d = a.offsetHeight + parseInt(f.marginTop) || 0,
         e = offset(document.querySelector(".form_block"));
     window.onscroll = function () {
         var c = window.pageYOffset || document.documentElement.scrollTop,
             c = e - (c + d + b);
         s != 0 < c && ((s = 0 < c) ? (a.style.top = b + "px", a.style.position = "fixed") : (a.style.top = e - d + "px", a.style.position = "absolute"))
     }
 };