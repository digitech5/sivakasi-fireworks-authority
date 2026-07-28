/**
 * Sivakasi Fireworks Guide — Main JavaScript
 * Version 2.0 | Optimized for Core Web Vitals
 */

'use strict';

// =============================================
// UTILITY FUNCTIONS
// =============================================

const $ = (selector, context = document) => context.querySelector(selector);
const $$ = (selector, context = document) => [...context.querySelectorAll(selector)];

function debounce(fn, delay = 150) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function throttle(fn, limit = 100) {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= limit) {
      lastCall = now;
      fn(...args);
    }
  };
}

// =============================================
// 1. STICKY HEADER
// =============================================

function initStickyHeader() {
  const header = $('#siteHeader');
  if (!header) return;

  let lastScroll = 0;

  window.addEventListener('scroll', throttle(() => {
    const current = window.scrollY;

    if (current > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Hide header on scroll down, show on scroll up (optional UX enhancement)
    if (current > 300 && current > lastScroll) {
      header.style.transform = 'translateY(-100%)';
    } else {
      header.style.transform = 'translateY(0)';
    }

    lastScroll = Math.max(0, current);
  }, 50));
}

// =============================================
// 2. MOBILE HAMBURGER MENU
// =============================================

function initMobileMenu() {
  const hamburger = $('#hamburger');
  const nav = $('#mainNav');
  const overlay = document.createElement('div');
  overlay.className = 'nav-overlay';
  document.body.appendChild(overlay);

  if (!hamburger || !nav) return;

  function openMenu() {
    nav.classList.add('open');
    hamburger.classList.add('active');
    hamburger.setAttribute('aria-expanded', 'true');
    overlay.classList.add('show');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    nav.classList.remove('open');
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
    overlay.classList.remove('show');
    document.body.style.overflow = '';
  }

  hamburger.addEventListener('click', () => {
    const isOpen = nav.classList.contains('open');
    isOpen ? closeMenu() : openMenu();
  });

  overlay.addEventListener('click', closeMenu);

  // Close on link click
  $$('a', nav).forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

// =============================================
// 3. SEARCH BAR TOGGLE
// =============================================

function initSearch() {
  const toggle = $('#searchToggle');
  const bar = $('#searchBar');
  const input = $('#siteSearch');

  if (!toggle || !bar) return;

  toggle.addEventListener('click', () => {
    const isOpen = bar.classList.contains('open');
    bar.classList.toggle('open');
    bar.setAttribute('aria-hidden', isOpen ? 'true' : 'false');
    if (!isOpen && input) {
      setTimeout(() => input.focus(), 100);
    }
  });

  // Search submit
  if (input) {
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        const query = input.value.trim();
        if (query) {
          // Redirect to blog page with search param
          window.location.href = `/blog/index.html?search=${encodeURIComponent(query)}`;
        }
      }
    });
  }

  // Close on outside click
  document.addEventListener('click', (e) => {
    if (!bar.contains(e.target) && !toggle.contains(e.target)) {
      bar.classList.remove('open');
      bar.setAttribute('aria-hidden', 'true');
    }
  });
}

// =============================================
// 4. FAQ ACCORDION
// =============================================

function initFaqAccordion() {
  const faqItems = $$('.faq-item');

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    const icon = item.querySelector('.faq-icon');

    if (!question || !answer) return;

    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all others (comment out for multi-open behavior)
      faqItems.forEach(other => {
        if (other !== item) {
          other.classList.remove('active');
          const otherAnswer = other.querySelector('.faq-answer');
          if (otherAnswer) otherAnswer.style.maxHeight = null;
        }
      });

      item.classList.toggle('active', !isActive);

      if (!isActive) {
        answer.style.maxHeight = answer.scrollHeight + 'px';
      } else {
        answer.style.maxHeight = null;
      }
    });

    // Set initial icon
    if (!icon) {
      const plusIcon = document.createElement('span');
      plusIcon.className = 'faq-icon';
      plusIcon.textContent = '+';
      question.appendChild(plusIcon);
    }
  });
}

// =============================================
// 5. SCROLL TO TOP BUTTON
// =============================================

function initScrollToTop() {
  const btn = document.createElement('button');
  btn.className = 'scroll-top';
  btn.innerHTML = '↑';
  btn.setAttribute('aria-label', 'Scroll to top');
  document.body.appendChild(btn);

  window.addEventListener('scroll', throttle(() => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, 100));

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// =============================================
// 6. READING PROGRESS BAR
// =============================================

function initReadingProgress() {
  const bar = $('.reading-progress') || $('#readingProgress');
  if (!bar) return;

  const article = $('.article-body') || $('article') || $('main');
  if (!article) return;

  window.addEventListener('scroll', throttle(() => {
    const articleTop = article.offsetTop;
    const articleHeight = article.offsetHeight;
    const windowHeight = window.innerHeight;
    const scrolled = window.scrollY;

    const progress = Math.min(
      100,
      Math.max(0, ((scrolled - articleTop + windowHeight * 0.5) / articleHeight) * 100)
    );

    bar.style.width = progress + '%';
  }, 50));
}

// =============================================
// 7. TABLE OF CONTENTS AUTO-GENERATOR
// =============================================

function initTableOfContents() {
  const tocList = $('.toc-list');
  const articleBody = $('.article-body');

  if (!tocList || !articleBody) return;

  // Only auto-generate if TOC list is empty
  if (tocList.children.length > 0) return;

  const headings = $$('h2, h3', articleBody);
  if (headings.length === 0) return;

  headings.forEach((heading, i) => {
    // Ensure heading has an ID
    if (!heading.id) {
      heading.id = `section-${i + 1}-${heading.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 40)}`;
    }

    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = `#${heading.id}`;
    a.textContent = heading.textContent;

    if (heading.tagName === 'H3') {
      li.style.paddingLeft = '1rem';
      li.style.fontSize = '0.85rem';
    }

    li.appendChild(a);
    tocList.appendChild(li);
  });

  // Active TOC link highlighting on scroll
  const tocLinks = $$('a', tocList);
  const updateActiveToc = throttle(() => {
    const scrollPos = window.scrollY + 120;
    let activeId = '';

    headings.forEach(h => {
      if (h.offsetTop <= scrollPos) activeId = h.id;
    });

    tocLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${activeId}`);
    });
  }, 100);

  window.addEventListener('scroll', updateActiveToc);
}

// =============================================
// 8. SMOOTH SCROLL FOR ANCHOR LINKS
// =============================================

function initSmoothScroll() {
  document.addEventListener('click', (e) => {
    const target = e.target.closest('a[href^="#"]');
    if (!target) return;

    const id = target.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if (!el) return;

    e.preventDefault();

    const headerHeight = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-height')) || 72;

    window.scrollTo({
      top: el.offsetTop - headerHeight - 16,
      behavior: 'smooth'
    });

    // Update URL hash without page jump
    history.pushState(null, null, `#${id}`);
  });
}

// =============================================
// 9. ANIMATE ON SCROLL
// =============================================

function initAnimateOnScroll() {
  const elements = $$('.animate-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  elements.forEach(el => observer.observe(el));
}

// =============================================
// 10. LAZY-LOAD IMAGES
// =============================================

function initLazyLoad() {
  const images = $$('img[data-src], img[loading="lazy"]');

  if ('loading' in HTMLImageElement.prototype) {
    // Native lazy loading supported
    images.forEach(img => {
      if (img.dataset.src) {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
      }
    });
    return;
  }

  // Fallback with IntersectionObserver
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        if (img.dataset.src) {
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
        }
        observer.unobserve(img);
      }
    });
  }, { rootMargin: '200px' });

  images.forEach(img => observer.observe(img));
}

// =============================================
// 11. BLOG SEARCH FILTER (Blog Index Page)
// =============================================

function initBlogSearch() {
  const searchInput = $('#blogSearch');
  const cards = $$('.blog-card');

  if (!searchInput || !cards.length) return;

  // Check for URL search param
  const params = new URLSearchParams(window.location.search);
  if (params.has('search')) {
    searchInput.value = params.get('search');
    filterCards(params.get('search'));
  }

  searchInput.addEventListener('input', debounce((e) => {
    filterCards(e.target.value.trim());
  }, 200));

  function filterCards(query) {
    const lowerQuery = query.toLowerCase();
    let visibleCount = 0;

    cards.forEach(card => {
      const title = (card.dataset.title || card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const category = (card.dataset.category || card.querySelector('.card-category')?.textContent || '').toLowerCase();
      const matches = !query || title.includes(lowerQuery) || category.includes(lowerQuery);

      card.style.display = matches ? '' : 'none';
      if (matches) visibleCount++;
    });

    // Show/hide no results message
    const noResults = $('#noResults');
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }
}

// =============================================
// 12. CATEGORY TABS FILTER (Blog Index)
// =============================================

function initCategoryTabs() {
  const tabs = $$('.cat-tab');
  const cards = $$('.blog-card');

  if (!tabs.length || !cards.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const category = tab.dataset.category || 'all';

      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      cards.forEach(card => {
        const cardCat = (card.dataset.category || '').toLowerCase();
        const matches = category === 'all' || cardCat === category.toLowerCase();
        card.style.display = matches ? '' : 'none';
      });
    });
  });
}

// =============================================
// 13. NEWSLETTER FORM (Client-side Validation)
// =============================================

function initNewsletter() {
  const forms = $$('.newsletter-form');

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]');
      if (!email) return;

      const value = email.value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!emailRegex.test(value)) {
        email.style.borderColor = 'var(--danger)';
        showMessage(form, 'Please enter a valid email address.', 'error');
        return;
      }

      email.style.borderColor = 'var(--success)';
      email.value = '';
      showMessage(form, '🎆 You\'re subscribed! Welcome to Sivakasi Fireworks Guide.', 'success');
    });
  });

  function showMessage(form, text, type) {
    let msg = form.querySelector('.form-message');
    if (!msg) {
      msg = document.createElement('p');
      msg.className = 'form-message';
      msg.style.cssText = 'margin-top: 0.75rem; font-size: 0.875rem; font-weight: 600;';
      form.appendChild(msg);
    }
    msg.textContent = text;
    msg.style.color = type === 'success' ? 'var(--accent)' : '#ff6b6b';

    setTimeout(() => { if (msg) msg.remove(); }, 5000);
  }
}

// =============================================
// 14. DARK MODE TOGGLE
// =============================================

function initDarkMode() {
  const toggle = $('#darkModeToggle');
  if (!toggle) return;

  const saved = localStorage.getItem('darkMode');
  if (saved === 'true') {
    document.documentElement.classList.add('dark');
    toggle.textContent = '☀️';
  }

  toggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem('darkMode', isDark);
    toggle.textContent = isDark ? '☀️' : '🌙';
  });
}

// =============================================
// 15. ACTIVE NAV LINK HIGHLIGHTING
// =============================================

function initActiveNav() {
  const currentPath = window.location.pathname;
  const navLinks = $$('.nav-list a');

  navLinks.forEach(link => {
    const linkPath = new URL(link.href, window.location.origin).pathname;
    if (linkPath === currentPath || (currentPath !== '/' && currentPath.startsWith(linkPath) && linkPath !== '/')) {
      link.classList.add('active');
    }
  });
}

// =============================================
// 16. CHECKLIST SAVE STATE (localStorage)
// =============================================

function initChecklist() {
  const checklists = $$('.checklist');

  checklists.forEach((list, listIndex) => {
    const items = $$('li', list);

    items.forEach((item, itemIndex) => {
      const key = `checklist-${listIndex}-${itemIndex}`;
      const saved = localStorage.getItem(key);

      if (saved === 'done') item.classList.add('done');

      item.addEventListener('click', () => {
        item.classList.toggle('done');
        localStorage.setItem(key, item.classList.contains('done') ? 'done' : '');
      });
    });
  });
}

// =============================================
// 17. SHARE BUTTONS
// =============================================

function initShareButtons() {
  const copyBtns = $$('.share-btn.copy-link');

  copyBtns.forEach(btn => {
    btn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(window.location.href);
        const original = btn.textContent;
        btn.textContent = '✅ Copied!';
        setTimeout(() => { btn.textContent = original; }, 2000);
      } catch {
        // Fallback
        const input = document.createElement('input');
        input.value = window.location.href;
        document.body.appendChild(input);
        input.select();
        document.execCommand('copy');
        document.body.removeChild(input);
        btn.textContent = '✅ Copied!';
        setTimeout(() => { btn.textContent = '🔗 Copy Link'; }, 2000);
      }
    });
  });
}

// =============================================
// 18. COUNTER ANIMATION (Stats)
// =============================================

function initCounterAnimation() {
  const counters = $$('[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.count);
      const duration = 2000;
      const step = target / (duration / 16);
      let current = 0;

      const update = () => {
        current = Math.min(current + step, target);
        el.textContent = Math.floor(current).toLocaleString('en-IN') + (el.dataset.suffix || '');
        if (current < target) requestAnimationFrame(update);
      };

      requestAnimationFrame(update);
      observer.unobserve(el);
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
}

// =============================================
// INITIALIZE ALL MODULES ON DOM READY
// =============================================

function init() {
  initStickyHeader();
  initMobileMenu();
  initSearch();
  initFaqAccordion();
  initScrollToTop();
  initReadingProgress();
  initTableOfContents();
  initSmoothScroll();
  initAnimateOnScroll();
  initLazyLoad();
  initBlogSearch();
  initCategoryTabs();
  initNewsletter();
  initDarkMode();
  initActiveNav();
  initChecklist();
  initShareButtons();
  initCounterAnimation();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
