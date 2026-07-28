import os, glob, re, shutil

root = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"

# ---------------------------------------------------------
# 1. Update js/main.js for FAQ single accordion & search
# ---------------------------------------------------------
main_js_path = os.path.join(root, "js", "main.js")
with open(main_js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace initFAQ function to ensure single accordion open & add live FAQ search
old_faq_js_pattern = re.compile(r'\(function initFAQ\(\) \{.*?\}\)\(\);', re.DOTALL)

new_faq_js = '''(function initFAQ() {
  const questions = $$('.faq-question');
  if (!questions.length) return;

  questions.forEach(btn => {
    btn.setAttribute('role', 'button');
    const answerId = btn.getAttribute('aria-controls');
    const answer = answerId ? document.getElementById(answerId) : btn.closest('.faq-item')?.querySelector('.faq-answer');
    if (!answer) return;

    on(btn, 'click', () => {
      const isOpen = btn.getAttribute('aria-expanded') === 'true';

      // Close all open accordions across the entire page (Bug 1 requirement: only one accordion opens at a time)
      $$('.faq-question').forEach(q => {
        q.setAttribute('aria-expanded', 'false');
        const a = document.getElementById(q.getAttribute('aria-controls') || '') || q.closest('.faq-item')?.querySelector('.faq-answer');
        if (a) a.setAttribute('aria-hidden', 'true');
      });

      if (!isOpen) {
        btn.setAttribute('aria-expanded', 'true');
        answer.setAttribute('aria-hidden', 'false');
      }
    });

    on(btn, 'keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); btn.click(); }
    });
  });

  // FAQ Live Search
  const faqSearchInput = $('#faqSearch');
  if (faqSearchInput) {
    on(faqSearchInput, 'input', e => {
      const query = e.target.value.toLowerCase().trim();
      $$('.faq-item').forEach(item => {
        const text = item.textContent.toLowerCase();
        if (!query || text.includes(query)) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
      // Also check category headings
      $$('section.container > h2.section-title').forEach(h2 => {
        const nextList = h2.nextElementSibling;
        if (nextList && nextList.classList.contains('faq-list')) {
          const visibleItems = $$('.faq-item', nextList).filter(i => i.style.display !== 'none');
          h2.style.display = visibleItems.length ? '' : 'none';
        }
      });
    });
  }
})();'''

if old_faq_js_pattern.search(js_content):
    js_content = old_faq_js_pattern.sub(new_faq_js, js_content)
    with open(main_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Updated js/main.js with single accordion behavior & FAQ search")

# ---------------------------------------------------------
# 2. Update css/style.css for FAQ Accordion & Responsiveness
# ---------------------------------------------------------
style_css_path = os.path.join(root, "css", "style.css")
with open(style_css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Enhance FAQ CSS for clean spacing, no text overlap, smooth transitions
faq_css_replacement = '''/* ================================================================
   16. FAQ ACCORDION
   ================================================================ */
.faq-list{display:flex;flex-direction:column;gap:.75rem}
.faq-item{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:var(--r-sm);overflow:hidden;transition:border-color var(--dur) var(--ease),box-shadow var(--dur) var(--ease)}
.faq-item:hover{border-color:var(--clr-primary);box-shadow:var(--shadow-sm)}
.faq-question{width:100%;display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1.1rem 1.25rem;font-size:var(--text-base);font-weight:700;font-family:var(--font-heading);color:var(--clr-text);background:none;border:none;cursor:pointer;text-align:left;line-height:1.4;transition:color var(--dur-fast) var(--ease),background var(--dur-fast) var(--ease)}
.faq-question:hover{color:var(--clr-primary);background:var(--clr-primary-tint)}
.faq-question[aria-expanded="true"]{color:var(--clr-primary);background:var(--clr-primary-tint)}
.faq-toggle{width:28px;height:28px;border-radius:50%;background:var(--clr-surface-3);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:background var(--dur) var(--ease),transform var(--dur) var(--ease)}
.faq-toggle svg{width:14px;height:14px;color:var(--clr-text-3);transition:color var(--dur) var(--ease)}
.faq-question[aria-expanded="true"] .faq-toggle{background:var(--clr-primary);transform:rotate(180deg)}
.faq-question[aria-expanded="true"] .faq-toggle svg{color:#fff}
.faq-answer{max-height:0;overflow:hidden;transition:max-height .4s cubic-bezier(0,1,0,1);background:var(--clr-surface-2)}
.faq-answer[aria-hidden="false"]{max-height:1200px;transition:max-height .4s ease-in-out}
.faq-answer__inner{padding:1rem 1.25rem 1.25rem;border-top:1px solid var(--clr-border)}
.faq-answer p{font-size:var(--text-sm);color:var(--clr-text-2);line-height:1.75;margin-bottom:.75rem}
.faq-answer p:last-child{margin-bottom:0}
.faq-answer a{color:var(--clr-primary);text-decoration:underline}'''

old_faq_css_pattern = re.compile(r'/\* =+ *\n *16\. FAQ ACCORDION.*?\n/\* =+', re.DOTALL)
if old_faq_css_pattern.search(css_content):
    css_content = old_faq_css_pattern.sub(faq_css_replacement + "\n\n/* ================================================================", css_content)
    with open(style_css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated css/style.css with FAQ accordion styles")

print("Step 1 & 2 completed.")
