document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("a[href]").forEach(a => {
    if (!a.href.startsWith(window.location.origin) && !a.href.startsWith("#")) {
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
    }
  });
});