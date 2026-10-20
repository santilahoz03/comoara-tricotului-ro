// Fade-in on scroll
(function () {
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.fade-in').forEach(function (el) { obs.observe(el); });
  // Fallback: reveal all after 2.5s
  setTimeout(function () {
    document.querySelectorAll('.fade-in').forEach(function (el) { el.classList.add('visible'); });
  }, 2500);
})();
