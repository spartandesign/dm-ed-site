/* Light is the default (best for projectors). Toggle flips to dark and
   remembers the choice. Storage is wrapped so it never throws in a
   sandboxed preview — the toggle still works for the session. */
(function () {
  var root = document.documentElement;
  var KEY = "dmed-theme";
  function save(t) { try { localStorage.setItem(KEY, t); } catch (e) {} }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-theme-toggle]");
    if (!btn) return;
    var next = root.dataset.theme === "dark" ? "light" : "dark";
    if (next === "dark") root.dataset.theme = "dark"; else delete root.dataset.theme;
    save(next);
  });
})();
