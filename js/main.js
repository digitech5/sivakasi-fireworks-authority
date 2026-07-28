/**
 * Sivakasi Fireworks Guide — Production JS v4.0
 * Modules: Header, Mobile Nav, Search, FAQ, Scroll, Lazy Load, Animations, Dark Mode, Counter
 */
'use strict';

/* ── Utilities ── */
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];
const on = (el, ev, fn, opts) => el && el.addEventListener(ev, fn, opts);

/* ================================================================
   1. HEADER — sticky hide/show on scroll
   ================================================================ */
(function initHeader() {
  const header = $('.site-header');
  if (!header) return;
  let lastY = 0, ticking = false;
  const THRESHOLD = 80;

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(() => {
        const y = window.scrollY;
        header.classList.toggle('is-scrolled', y > 10);
        // Hide on scroll down past threshold, show on scroll up
        if (y > THRESHOLD) {
          header.classList.toggle('is-hidden', y > lastY + 8);
        } else {
          header.classList.remove('is-hidden');
        }
        lastY = y;
        ticking = false;
      });
      ticking = true;
    }
  }

  on(window, 'scroll', onScroll, { passive: true });
  onScroll();
})();

/* ================================================================
   2. MOBILE NAV
   ================================================================ */
(function initMobileNav() {
  const hamburger = $('#hamburger');
  const mobileNav = $('.mobile-nav');
  const overlay = $('.nav-overlay');
  const closeBtn = $('.mobile-nav__close');

  function open() {
    hamburger?.classList.add('is-active');
    mobileNav?.classList.add('is-open');
    overlay?.classList.add('is-visible');
    hamburger?.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    mobileNav?.querySelector('.mobile-nav__link')?.focus();
  }

  function close() {
    hamburger?.classList.remove('is-active');
    mobileNav?.classList.remove('is-open');
    overlay?.classList.remove('is-visible');
    hamburger?.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    hamburger?.focus();
  }

  on(hamburger, 'click', () => {
    mobileNav?.classList.contains('is-open') ? close() : open();
  });

  on(overlay, 'click', close);
  on(closeBtn, 'click', close);

  // Close on nav link click
  $$('.mobile-nav__link').forEach(link => on(link, 'click', close));

  // Close on Escape
  on(document, 'keydown', e => {
    if (e.key === 'Escape' && mobileNav?.classList.contains('is-open')) close();
  });

  // Active nav link
  const currentPath = location.pathname.split('/').pop() || 'index.html';
  $$('.primary-nav__link, .mobile-nav__link').forEach(link => {
    const href = link.getAttribute('href')?.split('/').pop();
    if (href && (href === currentPath || (currentPath === '' && href === 'index.html'))) {
      link.classList.add('is-active');
    }
  });
})();

/* ================================================================
   3. SEARCH OVERLAY
   ================================================================ */
(function initSearch() {
  const toggle = $('#searchToggle');
  const overlay = $('.search-overlay');
  const input = $('.search-overlay__input');
  const closeBtn = $('.search-overlay__close');
  const resultsBox = $('.search-overlay__results');
  if (!toggle || !overlay) return;

  // Article index for search (replace with real data)
  const articles = [
    { title: 'Complete Sivakasi Crackers Online Buying Guide 2026', cat: 'Buying', url: '/blog/sivakasi-crackers-online-buying-guide.html' },
    { title: 'Diwali Safety Tips: Complete Family Guide 2026', cat: 'Safety', url: '/blog/diwali-safety-tips-complete-guide.html' },
    { title: 'Types of Fireworks in India Explained', cat: 'Guide', url: '/blog/types-of-fireworks-in-india.html' },
    { title: 'Best Sparklers to Buy Online for Diwali 2026', cat: 'Sparklers', url: '/blog/best-sparklers-for-diwali.html' },
    { title: 'How to Store Crackers Safely', cat: 'Safety', url: '/blog/how-to-store-crackers-safely.html' },
    { title: 'Kids Fireworks Safety Guide', cat: 'Safety', url: '/blog/kids-fireworks-safety-guide.html' },
    { title: 'Crackers Price List 2026 — What Everything Costs', cat: 'Price', url: '/blog/crackers-price-list-2026.html' },
    { title: 'Online Crackers vs Local Shop — 2026 Comparison', cat: 'Buying', url: '/blog/online-crackers-vs-local-shop.html' },
    { title: 'Rockets Fireworks Buying Guide', cat: 'Rockets', url: '/blog/rocket-fireworks-buying-guide.html' },
    { title: 'Flower Pots Fireworks Guide', cat: 'Types', url: '/blog/flower-pots-fireworks-guide.html' },
    { title: 'Gift Box Crackers Guide', cat: 'Buying', url: '/blog/gift-boxes-fireworks-guide.html' },
    { title: 'Sivakasi History — Fireworks Capital of India', cat: 'History', url: '/blog/sivakasi-history-fireworks-capital.html' },
    { title: 'Eco-Friendly Fireworks India 2026', cat: 'Guide', url: '/blog/eco-friendly-fireworks-india.html' },
    { title: 'Ground Chakkars — Complete Guide', cat: 'Types', url: '/blog/ground-chakkars-guide.html' },
    { title: 'Fancy Fireworks Guide', cat: 'Types', url: '/blog/fancy-fireworks-guide.html' },
  ];

  let debounceTimer;
  function doSearch(q) {
    if (!q.trim() || q.length < 2) { if(resultsBox) resultsBox.innerHTML=''; return; }
    const matches = articles.filter(a => a.title.toLowerCase().includes(q.toLowerCase())).slice(0, 6);
    if (!resultsBox) return;
    if (!matches.length) {
      resultsBox.innerHTML = `<div class="search-empty">No results found for "<strong>${q}</strong>"</div>`;
      return;
    }
    resultsBox.innerHTML = matches.map(m => `
      <a href="${m.url}" class="search-result-item">
        <span class="search-result-item__cat">${m.cat}</span>
        <span class="search-result-item__title">${m.title}</span>
      </a>`).join('');
  }

  function openSearch() {
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    setTimeout(() => input?.focus(), 100);
  }

  function closeSearch() {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    if (input) input.value = '';
    if (resultsBox) resultsBox.innerHTML = '';
  }

  on(toggle, 'click', openSearch);
  on(closeBtn, 'click', closeSearch);
  on(overlay.querySelector('.search-overlay__backdrop'), 'click', closeSearch);
  on(document, 'keydown', e => { if (e.key === 'Escape') closeSearch(); });
  on(input, 'input', e => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => doSearch(e.target.value), 200);
  });
})();

/* ================================================================
   4. FAQ ACCORDION
   ================================================================ */
(function initFAQ() {
  $$('.faq-question').forEach(btn => {
    btn.setAttribute('role', 'button');
    const answerId = btn.getAttribute('aria-controls');
    const answer = answerId ? document.getElementById(answerId) : btn.closest('.faq-item')?.querySelector('.faq-answer');
    if (!answer) return;

    on(btn, 'click', () => {
      const isOpen = btn.getAttribute('aria-expanded') === 'true';

      // Close all in same list
      const list = btn.closest('.faq-list');
      if (list) {
        $$('.faq-question', list).forEach(q => {
          q.setAttribute('aria-expanded', 'false');
          const a = document.getElementById(q.getAttribute('aria-controls') || '') || q.closest('.faq-item')?.querySelector('.faq-answer');
          if (a) a.setAttribute('aria-hidden', 'true');
        });
      }

      if (!isOpen) {
        btn.setAttribute('aria-expanded', 'true');
        answer.setAttribute('aria-hidden', 'false');
      }
    });

    on(btn, 'keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); btn.click(); }
    });
  });
})();

/* ================================================================
   5. SCROLL-TO-TOP
   ================================================================ */
(function initScrollTop() {
  const btn = $('.scroll-top');
  if (!btn) return;
  const SHOW_AT = 400;
  on(window, 'scroll', () => {
    btn.classList.toggle('is-visible', window.scrollY > SHOW_AT);
  }, { passive: true });
  on(btn, 'click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
})();

/* ================================================================
   6. READING PROGRESS BAR
   ================================================================ */
(function initReadingProgress() {
  const bar = $('.reading-progress');
  const article = $('.article-body') || $('main');
  if (!bar || !article) return;

  on(window, 'scroll', () => {
    const rect = article.getBoundingClientRect();
    const articleTop = rect.top + window.scrollY;
    const articleH = article.offsetHeight;
    const progress = Math.min(1, Math.max(0, (window.scrollY - articleTop) / (articleH - window.innerHeight)));
    bar.style.transform = `scaleX(${progress})`;
  }, { passive: true });
})();

/* ================================================================
   7. TABLE OF CONTENTS — auto-generate & highlight
   ================================================================ */
(function initTOC() {
  const tocList = $('.toc__list');
  const articleBody = $('.article-body');
  if (!tocList || !articleBody) return;

  const headings = $$('h2, h3', articleBody);
  if (!headings.length) return;

  headings.forEach((h, i) => {
    if (!h.id) h.id = `section-${i + 1}`;
    const li = document.createElement('div');
    li.className = `toc__item${h.tagName === 'H3' ? ' toc__item--h3' : ''}`;
    li.innerHTML = `<span class="toc__num">${h.tagName === 'H2' ? i + 1 + '.' : '↳'}</span>
      <a href="#${h.id}" class="toc__link">${h.textContent}</a>`;
    tocList.appendChild(li);
  });

  // Intersection Observer for active link
  const links = $$('.toc__link', tocList);
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        links.forEach(l => l.classList.remove('is-active'));
        const link = tocList.querySelector(`[href="#${entry.target.id}"]`);
        link?.classList.add('is-active');
      }
    });
  }, { rootMargin: `-${(parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-h')) || 76) + 32}px 0px -60% 0px` });

  headings.forEach(h => observer.observe(h));
})();

/* ================================================================
   8. LAZY IMAGE LOADING
   ================================================================ */
(function initLazyImages() {
  if ('loading' in HTMLImageElement.prototype) {
    $$('img[data-src]').forEach(img => {
      img.src = img.dataset.src;
      if (img.dataset.srcset) img.srcset = img.dataset.srcset;
      img.removeAttribute('data-src');
    });
    return;
  }
  // Fallback IO
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const img = entry.target;
      img.src = img.dataset.src || img.src;
      if (img.dataset.srcset) img.srcset = img.dataset.srcset;
      img.classList.add('loaded');
      const wrap = img.closest('.img-wrap');
      if (wrap) wrap.classList.add('img-loaded');
      io.unobserve(img);
    });
  }, { rootMargin: '200px 0px' });

  $$('img[data-src]').forEach(img => io.observe(img));

  // Regular lazy load fade-in
  $$('img.img-lazy').forEach(img => {
    if (img.complete) { img.classList.add('loaded'); return; }
    on(img, 'load', () => img.classList.add('loaded'));
  });
})();

/* ================================================================
   9. SCROLL REVEAL ANIMATIONS
   ================================================================ */
(function initReveal() {
  const els = $$('.reveal, .reveal-scale');
  if (!els.length || !('IntersectionObserver' in window)) {
    els.forEach(el => el.classList.add('is-visible'));
    return;
  }
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -60px 0px', threshold: .1 });
  els.forEach(el => io.observe(el));
})();

/* ================================================================
   10. ANIMATED COUNTERS
   ================================================================ */
(function initCounters() {
  const counters = $$('[data-count]');
  if (!counters.length) return;

  function animateCounter(el) {
    const target = parseFloat(el.dataset.count);
    const isDecimal = String(target).includes('.');
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const duration = 1600;
    const start = performance.now();

    function tick(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3);
      const current = target * ease;
      el.textContent = prefix + (isDecimal ? current.toFixed(1) : Math.round(current).toLocaleString('en-IN')) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        io.unobserve(entry.target);
      }
    });
  }, { threshold: .5 });

  counters.forEach(el => io.observe(el));
})();

/* ================================================================
   11. DARK MODE
   ================================================================ */
(function initDarkMode() {
  const toggle = $('#darkModeToggle');
  const html = document.documentElement;
  const STORAGE_KEY = 'sfg-theme';

  const saved = localStorage.getItem(STORAGE_KEY);
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isDark = saved ? saved === 'dark' : prefersDark;

  if (isDark) html.setAttribute('data-theme', 'dark');
  updateIcon(isDark);

  function updateIcon(dark) {
    if (!toggle) return;
    toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    toggle.innerHTML = dark
      ? `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
  }

  on(toggle, 'click', () => {
    const dark = html.getAttribute('data-theme') !== 'dark';
    html.setAttribute('data-theme', dark ? 'dark' : 'light');
    localStorage.setItem(STORAGE_KEY, dark ? 'dark' : 'light');
    updateIcon(dark);
  });
})();

/* ================================================================
   12. NEWSLETTER FORM
   ================================================================ */
(function initNewsletter() {
  $$('.newsletter-form').forEach(form => {
    on(form, 'submit', e => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button[type="submit"]');
      if (!input?.value) return;
      const originalText = btn.textContent;
      btn.textContent = '✅ Subscribed!';
      btn.style.background = 'var(--clr-success)';
      btn.disabled = true;
      input.value = '';
      setTimeout(() => {
        btn.textContent = originalText;
        btn.style.background = '';
        btn.disabled = false;
      }, 4000);
    });
  });
})();

/* ================================================================
   13. SHARE BUTTONS
   ================================================================ */
(function initShare() {
  on(document, 'click', e => {
    const btn = e.target.closest('[data-share]');
    if (!btn) return;
    const action = btn.dataset.share;
    const url = encodeURIComponent(location.href);
    const title = encodeURIComponent(document.title);

    const actions = {
      whatsapp: `https://wa.me/?text=${title}%20${url}`,
      twitter: `https://twitter.com/intent/tweet?text=${title}&url=${url}`,
      copy: null,
    };

    if (action === 'copy') {
      navigator.clipboard.writeText(location.href).then(() => {
        btn.textContent = '✅ Copied!';
        setTimeout(() => btn.textContent = '🔗 Copy Link', 2000);
      });
    } else if (actions[action]) {
      window.open(actions[action], '_blank', 'noopener,width=600,height=400');
    }
  });
})();

/* ================================================================
   14. CATEGORY FILTER (blog page)
   ================================================================ */
(function initCategoryFilter() {
  const tabs = $$('.category-tab');
  const cards = $$('.article-card[data-cat]');
  if (!tabs.length) return;

  tabs.forEach(tab => {
    on(tab, 'click', () => {
      tabs.forEach(t => t.classList.remove('is-active'));
      tab.classList.add('is-active');
      const cat = tab.dataset.cat;

      cards.forEach(card => {
        const show = cat === 'all' || card.dataset.cat === cat;
        card.style.display = show ? '' : 'none';
        // Re-trigger reveal
        if (show) card.classList.add('is-visible');
      });
    });
  });
})();

/* ================================================================
   15. SMOOTH ANCHOR SCROLL
   ================================================================ */
on(document, 'click', e => {
  const anchor = e.target.closest('a[href^="#"]');
  if (!anchor) return;
  const target = document.querySelector(anchor.getAttribute('href'));
  if (!target) return;
  e.preventDefault();
  target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  history.replaceState(null, '', anchor.getAttribute('href'));
});

/* ================================================================
   16. INIT — DOMContentLoaded
   ================================================================ */
document.addEventListener('DOMContentLoaded', () => {
  // Add scroll-top button if not in HTML
  if (!$('.scroll-top')) {
    const btn = document.createElement('button');
    btn.className = 'scroll-top';
    btn.setAttribute('aria-label', 'Scroll to top');
    btn.setAttribute('title', 'Scroll to top');
    btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"/></svg>`;
    document.body.appendChild(btn);
    on(btn, 'click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    on(window, 'scroll', () => btn.classList.toggle('is-visible', window.scrollY > 400), { passive: true });
  }

  // Add reading progress if not in HTML and article body exists
  if (!$('.reading-progress') && $('.article-body')) {
    const bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-label', 'Reading progress');
    document.body.prepend(bar);
  }
});
