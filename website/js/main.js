// Mobile nav toggle
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
if (menuBtn && mobileMenu) {
  menuBtn.addEventListener('click', () => {
    const isOpen = mobileMenu.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    mobileMenu.style.maxHeight = isOpen ? mobileMenu.scrollHeight + 'px' : '0px';
    mobileMenu.style.opacity = isOpen ? '1' : '0';
  });
}

// Footer year
document.querySelectorAll('[data-year]').forEach(el => {
  el.textContent = new Date().getFullYear();
});

// Registration form (placeholder — no backend wired up yet)
const regForm = document.getElementById('registration-form');
if (regForm) {
  regForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!regForm.checkValidity()) {
      regForm.reportValidity();
      return;
    }
    const data = Object.fromEntries(new FormData(regForm).entries());
    const successBox = document.getElementById('registration-success');
    const summary = document.getElementById('registration-summary');
    if (summary) {
      summary.textContent = `${data.boatName} — Captain ${data.captainName}, ${data.anglerCount} angler(s)`;
    }
    regForm.classList.add('hidden');
    if (successBox) successBox.classList.remove('hidden');
  });
}

// Merch "Add to Cart" placeholder (store not wired up yet)
document.querySelectorAll('[data-merch-cta]').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.textContent = 'Thanks — we’ll email you when the store opens!';
    btn.disabled = true;
    btn.classList.add('opacity-70', 'cursor-not-allowed');
  });
});
