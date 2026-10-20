(() => {
  "use strict";
  const root = document.documentElement;

  /* ---------- language ---------- */
  const store = {
    get() { try { return localStorage.getItem("lang"); } catch (e) { return null; } },
    set(v) { try { localStorage.setItem("lang", v); } catch (e) { /* storage blocked */ } }
  };
  function pickLang() {
    const q = new URLSearchParams(location.search).get("lang");
    if (q === "th" || q === "en") return q;
    const saved = store.get();
    if (saved === "th" || saved === "en") return saved;
    const nav = (navigator.language || "th").toLowerCase();
    return nav.startsWith("th") ? "th" : "en";
  }
  function applyLang(lang) {
    root.lang = lang;
    document.querySelectorAll("[data-i18n]").forEach(el => {
      const v = I18N[el.dataset.i18n];
      if (v) el.textContent = v[lang];
    });
    document.querySelectorAll("[data-i18n-alt]").forEach(el => {
      const v = I18N[el.dataset.i18nAlt];
      if (v) el.alt = v[lang];
    });
    document.querySelectorAll("[data-i18n-aria]").forEach(el => {
      const v = I18N[el.dataset.i18nAria];
      if (v) el.setAttribute("aria-label", v[lang]);
    });
    document.title = I18N.doc_title[lang];
    const meta = document.querySelector('meta[name="description"]');
    if (meta) meta.content = I18N.doc_desc[lang];
    document.querySelectorAll(".lang button").forEach(b =>
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang)));
  }
  document.querySelectorAll(".lang button").forEach(b => b.addEventListener("click", () => {
    const lang = b.dataset.lang;
    applyLang(lang);
    store.set(lang);
    const status = document.getElementById("lang-status");
    if (status) status.textContent = I18N.lang_done[lang];
    const url = new URL(location.href);
    url.searchParams.set("lang", lang);
    history.replaceState(null, "", url);
  }));
  const initial = pickLang();
  if (initial !== "th") applyLang(initial);

  /* ---------- contact links that have a URL ---------- */
  document.querySelectorAll("[data-link]").forEach(a => {
    const url = LINKS[a.dataset.link];
    if (url) { a.href = url; a.hidden = false; }
  });

  /* ---------- copy email ---------- */
  const copyBtn = document.querySelector(".copy-btn");
  const copyStatus = document.querySelector(".copy-status");
  if (copyBtn && navigator.clipboard && window.isSecureContext) {
    copyBtn.hidden = false;
    let timer;
    copyBtn.addEventListener("click", async () => {
      const lang = root.lang === "en" ? "en" : "th";
      try {
        await navigator.clipboard.writeText(copyBtn.dataset.copy);
        copyStatus.textContent = I18N.copied[lang];
      } catch (e) {
        copyStatus.textContent = I18N.copy_fail[lang];
      }
      clearTimeout(timer);
      timer = setTimeout(() => { copyStatus.textContent = ""; }, 4000);
    });
  }

  if (!("IntersectionObserver" in window)) return;

  /* ---------- nav follows the section being read ---------- */
  const navLinks = [...document.querySelectorAll(".nav a")];
  const byId = new Map(navLinks.map(a => [a.getAttribute("href").slice(1), a]));
  // The section in view is the last one whose top has passed 35% of the viewport.
  // Near the end of the page a short section cannot reach that line, so a nav
  // click there keeps the clicked section current instead of jumping to Contact.
  const sections = [...document.querySelectorAll(".sec")];
  let clicked = null;
  navLinks.forEach(a => a.addEventListener("click", () => { clicked = a.getAttribute("href").slice(1); }));
  function markNav() {
    const atEnd = innerHeight + scrollY >= document.documentElement.scrollHeight - 4;
    let id = null;
    for (const s of sections) if (s.getBoundingClientRect().top <= innerHeight * 0.35) id = s.id;
    if (atEnd) id = clicked || sections[sections.length - 1].id;
    else clicked = null;
    navLinks.forEach(a => {
      if (a.getAttribute("href").slice(1) === id) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
  }

  /* ---------- pipeline advances with the work being read ---------- */
  const ORDER = ["req", "spec", "build", "test"];
  const pipe = document.querySelector(".pipe");
  const steps = [...document.querySelectorAll(".step")];
  const works = [...document.querySelectorAll(".work")];
  const LAST = ORDER.length - 1;
  const stageOf = w => ORDER.indexOf(w.dataset.stage);

  // The reading line sits a little under the middle of the viewport.
  // The fill follows it continuously: inside a row it eases toward the next row's stage.
  function update() {
    ticking = false;
    markNav();
    const line = innerHeight * 0.5;
    let cur = -1;
    for (let i = 0; i < works.length; i++) {
      if (works[i].getBoundingClientRect().top <= line) cur = i; else break;
    }
    let p = 0, stage = 0;
    if (cur >= 0) {
      const r = works[cur].getBoundingClientRect();
      const frac = Math.min(1, Math.max(0, (line - r.top) / r.height));
      stage = stageOf(works[cur]);
      const next = cur + 1 < works.length ? stageOf(works[cur + 1]) : stage;
      p = (stage + frac * (next - stage)) / LAST;
    }
    pipe.style.setProperty("--p", p.toFixed(4));
    steps.forEach((s, n) => {
      s.classList.toggle("done", cur >= 0 && n < stage);
      s.classList.toggle("now", n === stage);
      if (n === stage) s.setAttribute("aria-current", "step"); else s.removeAttribute("aria-current");
    });
    works.forEach((w, i) => w.classList.toggle("is-current", i === cur));
  }
  let ticking = false;
  const request = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  addEventListener("scroll", request, { passive: true });
  addEventListener("resize", request);
  update();
})();
