// lab.js -- highlights the current section in the left menu.
// Highlight the current section in the sidebar
  (function () {
    var links = Array.prototype.slice.call(document.querySelectorAll('nav.toc a[href^="#"]'));
    var targets = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
    function update() {
      var y = window.scrollY + 80, idx = 0;
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top + window.scrollY <= y) idx = i; });
      // A section hidden inside a collapsed part highlights the part's own link instead
      var current = links[idx], group = current.closest('details');
      if (group && !group.open) current = group.querySelector('summary a');
      links.forEach(function (a) { a.classList.toggle('active', a === current); });
    }
    window.addEventListener('scroll', update, { passive: true });
    document.querySelectorAll('nav.toc details').forEach(function (d) { d.addEventListener('toggle', update); });
    update();
  })();
