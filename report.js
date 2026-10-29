(function(){
  var $ = function(id){ return document.getElementById(id); };
  var fUpd = $("f-updated"), fHorde = $("f-horde"), fClass = $("f-class"), fSearch = $("f-search"), fCount = $("f-count");
  var KEY = "forever-atlas-filters";
  try {
    var saved = JSON.parse(localStorage.getItem(KEY) || "null");
    if (saved) { fUpd.checked = !!saved.upd; fHorde.checked = !!saved.horde; fClass.value = saved.cls || "all"; fSearch.value = saved.q || ""; }
  } catch (e) {}
  function apply(){
    var showUpd = fUpd.checked, showHorde = fHorde.checked, cls = fClass.value, q = (fSearch.value || "").trim().toLowerCase();
    var rows = document.querySelectorAll("tr.qrow"), shown = 0;
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i], hide = false;
      if (!showUpd && r.getAttribute("data-status") === "updated") hide = true;
      if (!showHorde && r.getAttribute("data-side") === "2") hide = true;
      var rc = r.getAttribute("data-class") || "none";
      if (cls === "none" && rc !== "none") hide = true;
      else if (cls !== "all" && cls !== "none" && rc !== "none" && rc.split(",").indexOf(cls) < 0) hide = true;
      if (q && (r.getAttribute("data-name") || "").indexOf(q) < 0) hide = true;
      r.classList.toggle("hidden-row", hide);
      if (!hide) shown++;
    }
    var zones = document.querySelectorAll("section.zone");
    for (var j = 0; j < zones.length; j++) {
      var z = zones[j], any = z.querySelector("tr.qrow:not(.hidden-row)");
      z.classList.toggle("all-hidden", !!z.querySelector("tr.qrow") && !any);
    }
    fCount.textContent = shown + " of " + rows.length + " quest rows shown";
    try { localStorage.setItem(KEY, JSON.stringify({upd: showUpd, horde: showHorde, cls: cls, q: q})); } catch (e) {}
  }
  [fUpd, fHorde, fClass].forEach(function(el){ el.addEventListener("change", apply); });
  fSearch.addEventListener("input", apply);
  apply();
})();
