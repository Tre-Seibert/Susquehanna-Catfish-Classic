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

// Registration form — show a name field for as many anglers as selected
const anglerCountSelect = document.getElementById('anglerCount');
const anglerBlocks = document.querySelectorAll('.angler-block');
if (anglerCountSelect && anglerBlocks.length) {
  const updateAnglerFields = () => {
    const count = parseInt(anglerCountSelect.value, 10) || 1;
    anglerBlocks.forEach((block) => {
      const index = parseInt(block.dataset.anglerIndex, 10);
      const active = index <= count;
      block.classList.toggle('hidden', !active);
      block.querySelectorAll('input').forEach((input) => {
        input.disabled = !active;
        input.required = active;
      });
    });
  };
  anglerCountSelect.addEventListener('change', updateAnglerFields);
  updateAnglerFields();
}

const REG_OPEN = new Date('2027-01-01T00:00:00-05:00');
const REG_CLOSE = new Date('2027-08-25T16:00:00-04:00');
const registrationIsOpen = () => {
  const now = new Date();
  return now >= REG_OPEN && now < REG_CLOSE;
};

// Registration form — closed until January 2027
const regForm = document.getElementById('registration-form');
const regClosed = document.getElementById('registration-closed');
if (regForm) {
  const setRegistrationAvailability = () => {
    const open = registrationIsOpen();
    regForm.hidden = !open;
    regForm.classList.toggle('hidden', !open);
    regForm.querySelectorAll('input, select, textarea, button').forEach((el) => {
      el.disabled = !open;
    });
    if (regClosed) regClosed.classList.toggle('hidden', open);
  };
  setRegistrationAvailability();

  regForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!registrationIsOpen()) {
      setRegistrationAvailability();
      return;
    }
    if (!regForm.checkValidity()) {
      regForm.reportValidity();
      return;
    }
    const data = Object.fromEntries(new FormData(regForm).entries());
    const successBox = document.getElementById('registration-success');
    const summary = document.getElementById('registration-summary');
    if (summary) {
      summary.textContent = `${data.boatName} (${data.boatRegNumber}) — Captain ${data.angler1Name}, fishing ${data.fishingLocation}`;
    }
    regForm.classList.add('hidden');
    if (successBox) successBox.classList.remove('hidden');
  });
}

// Sponsor form (placeholder — no backend wired up yet)
const sponsorForm = document.getElementById('sponsor-form');
if (sponsorForm) {
  sponsorForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!sponsorForm.checkValidity()) {
      sponsorForm.reportValidity();
      return;
    }
    const data = Object.fromEntries(new FormData(sponsorForm).entries());
    const successBox = document.getElementById('sponsor-success');
    const summary = document.getElementById('sponsor-summary');
    if (summary) {
      summary.textContent = `${data.sponsorBusiness} — $250 tee sponsor`;
    }
    sponsorForm.classList.add('hidden');
    if (successBox) successBox.classList.remove('hidden');
  });
}

// Countdown to check-in — split-flap style tiles
(function initCountdown() {
  const countdownEl = document.getElementById('countdown');
  if (!countdownEl) return;

  const CHECK_IN = new Date('2027-08-27T16:00:00-04:00');

  const digits = {
    days: countdownEl.querySelector('[data-unit="days"]'),
    hours: countdownEl.querySelector('[data-unit="hours"]'),
    minutes: countdownEl.querySelector('[data-unit="minutes"]'),
    seconds: countdownEl.querySelector('[data-unit="seconds"]'),
  };

  const regNote = document.getElementById('countdown-reg-note');
  const liveNote = document.getElementById('countdown-live-note');
  const srLive = document.getElementById('countdown-sr-live');

  const pad = (n) => String(n).padStart(2, '0');

  function setDigit(unit, value) {
    const el = digits[unit];
    const next = pad(value);
    if (el.textContent === next) return;
    const tile = el.closest('.flip-tile');
    tile.classList.remove('is-flipping');
    void tile.offsetWidth; // restart animation
    tile.classList.add('is-flipping');
    setTimeout(() => { el.textContent = next; }, 250);
  }

  function updateRegNote() {
    if (!regNote) return;
    const diff = REG_CLOSE - new Date();
    const now = new Date();
    if (now < REG_OPEN) {
      regNote.textContent = 'Registration opens January 2027.';
      return;
    }
    if (diff <= 0) {
      regNote.textContent = 'Registration is closed.';
      return;
    }
    const days = Math.ceil(diff / 86400000);
    regNote.textContent = days <= 1
      ? 'Registration closes today at 4:00 PM.'
      : `Registration closes in ${days} days — Wed, Aug 25 at 4:00 PM.`;
  }

  let timer;
  let lastAnnouncedMinute = null;

  function tick() {
    const diff = CHECK_IN - new Date();

    if (diff <= 0) {
      countdownEl.classList.add('hidden');
      if (regNote) regNote.classList.add('hidden');
      if (liveNote) {
        liveNote.textContent = 'Lines are in — good luck out there.';
        liveNote.classList.remove('hidden');
      }
      clearInterval(timer);
      return;
    }

    const totalSeconds = Math.floor(diff / 1000);
    const days = Math.floor(totalSeconds / 86400);
    const hours = Math.floor((totalSeconds % 86400) / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    setDigit('days', days);
    setDigit('hours', hours);
    setDigit('minutes', minutes);
    setDigit('seconds', seconds);
    updateRegNote();

    if (srLive && minutes !== lastAnnouncedMinute) {
      lastAnnouncedMinute = minutes;
      srLive.textContent = `${days} days, ${hours} hours, ${minutes} minutes until check-in`;
    }
  }

  tick();
  timer = setInterval(tick, 1000);
})();

// Merch "Add to Cart" placeholder (store not wired up yet)
document.querySelectorAll('[data-merch-cta]').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.textContent = 'Thanks — we’ll email you when the store opens!';
    btn.disabled = true;
    btn.classList.add('opacity-70', 'cursor-not-allowed');
  });
});
