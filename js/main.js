/**
 * Payroll Management System Online - Core Interactive Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Drawer Navigation
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const drawerClose = document.getElementById('drawerClose');
  const drawerBackdrop = document.getElementById('drawerBackdrop');

  function openDrawer() {
    if (mobileDrawer) mobileDrawer.classList.add('open');
    if (drawerBackdrop) drawerBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (mobileDrawer) mobileDrawer.classList.remove('open');
    if (drawerBackdrop) drawerBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileDrawer && mobileDrawer.classList.contains('open')) {
      closeDrawer();
    }
  });

  // 2. Active Page Highlighting
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link, .dropdown-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkPath = href.split('/').pop() || 'index.html';
    if (linkPath === currentPath || (currentPath === '' && linkPath === 'index.html')) {
      link.classList.add('active');
    }
  });

  // 3. "Show More / Show Less" for Offer Cards
  const toggleButtons = document.querySelectorAll('.show-more-btn');
  toggleButtons.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const cardBody = this.closest('.offer-card-body');
      if (!cardBody) return;
      const expandedBlock = cardBody.querySelector('.offer-card-text-expanded');
      const textSpan = this.querySelector('.btn-text');
      const iconSpan = this.querySelector('.btn-icon');

      if (expandedBlock) {
        const isVisible = expandedBlock.classList.contains('visible');
        if (isVisible) {
          expandedBlock.classList.remove('visible');
          if (textSpan) textSpan.textContent = 'Show More';
          if (iconSpan) {
            iconSpan.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path fill-rule="evenodd" d="M10.9 4v6.899H4v2h6.9v6.9h2v-6.9h6.898v-2H12.9V4z"></path></svg>';
          }
        } else {
          expandedBlock.classList.add('visible');
          if (textSpan) textSpan.textContent = 'Show Less';
          if (iconSpan) {
            iconSpan.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><path fill="currentColor" fill-rule="nonzero" d="M4 13.5h16v-2H4z"></path></svg>';
          }
        }
      }
    });
  });

  // 4. Newsletter Subscription Form
  const subscribeForm = document.getElementById('subscribeForm');
  const subscribeEmail = document.getElementById('subscribeEmail');
  const subscribeMsg = document.getElementById('subscribeMsg');

  if (subscribeForm) {
    subscribeForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = subscribeEmail ? subscribeEmail.value.trim() : '';
      if (!email || !email.includes('@') || !email.includes('.')) {
        alert('Please enter a valid email address.');
        return;
      }

      // Save to local storage
      try {
        const subscribers = JSON.parse(localStorage.getItem('payroll_management_subscribers') || '[]');
        subscribers.push({ email, date: new Date().toISOString() });
        localStorage.setItem('payroll_management_subscribers', JSON.stringify(subscribers));
      } catch (err) {
        console.warn('Could not save subscriber to storage', err);
      }

      if (subscribeMsg) {
        subscribeMsg.style.display = 'block';
        subscribeMsg.textContent = 'Thank you for signing up to hear from Payroll Management System Online!';
      }
      if (subscribeEmail) subscribeEmail.value = '';
    });
  }

  // 5. Contact Form Submission
  const contactForm = document.getElementById('contactForm');
  const contactSuccess = document.getElementById('contactSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('contactName')?.value.trim();
      const email = document.getElementById('contactEmail')?.value.trim();
      const phone = document.getElementById('contactPhone')?.value.trim();
      const message = document.getElementById('contactMessage')?.value.trim();

      if (!name || !email) {
        alert('Please provide your name and a valid email address.');
        return;
      }

      try {
        const inquiries = JSON.parse(localStorage.getItem('payroll_management_inquiries') || '[]');
        inquiries.push({ name, email, phone, message, date: new Date().toISOString() });
        localStorage.setItem('payroll_management_inquiries', JSON.stringify(inquiries));
      } catch (err) {
        console.warn('Could not save inquiry to storage', err);
      }

      contactForm.reset();
      if (contactSuccess) {
        contactSuccess.style.display = 'block';
        contactSuccess.scrollIntoView({ behavior: 'smooth' });
      } else {
        alert('Thank you! Your message has been sent to Payroll Management System Online. We will contact you shortly.');
      }
    });
  }

  // 6. Highlight Today in Business Hours Table
  const daysOfWeek = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'];
  const todayIndex = new Date().getDay();
  const todayKey = daysOfWeek[todayIndex];
  const todayRow = document.querySelector(`.hours-table tr[data-day="${todayKey}"]`);
  if (todayRow) {
    todayRow.classList.add('today');
    const dayCell = todayRow.querySelector('.day');
    if (dayCell) dayCell.textContent += ' (Today)';
  }

  // 7. Cookie Policy Banner
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieAcceptBtn = document.getElementById('cookieAcceptBtn');

  if (cookieBanner) {
    const accepted = localStorage.getItem('payroll_management_cookies_accepted');
    if (!accepted) {
      setTimeout(() => {
        cookieBanner.classList.add('show');
      }, 800);
    }

    if (cookieAcceptBtn) {
      cookieAcceptBtn.addEventListener('click', () => {
        localStorage.setItem('payroll_management_cookies_accepted', 'true');
        cookieBanner.classList.remove('show');
      });
    }
  }

  // 8. Video hero fallback check
  const heroVideo = document.querySelector('.hero-video-bg');
  if (heroVideo) {
    heroVideo.play().catch(err => {
      console.log('Autoplay deferred or requires user interaction');
    });
  }
});

