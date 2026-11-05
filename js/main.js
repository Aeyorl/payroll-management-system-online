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

  // 5. Contact Form Submission - Direct delivery to pmsoinc@mail2usa.com
  const contactForm = document.getElementById('contactForm');
  const contactSuccess = document.getElementById('contactSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('contactName')?.value.trim();
      const email = document.getElementById('contactEmail')?.value.trim();
      const phone = document.getElementById('contactPhone')?.value.trim() || 'Not provided';
      const message = document.getElementById('contactMessage')?.value.trim() || '(No message content)';

      if (!name || !email) {
        alert('Please provide your name and a valid email address.');
        return;
      }

      // 1. Save lead to localStorage backup
      try {
        const inquiries = JSON.parse(localStorage.getItem('payroll_management_inquiries') || '[]');
        inquiries.push({ name, email, phone, message, date: new Date().toISOString() });
        localStorage.setItem('payroll_management_inquiries', JSON.stringify(inquiries));
      } catch (err) {
        console.warn('Could not save inquiry to storage', err);
      }

      // 2. Format mailto link addressed to pmsoinc@mail2usa.com
      const subject = encodeURIComponent(`New Inquiry from ${name} - PMSO Inc.`);
      const body = encodeURIComponent(
        `Full Name: ${name}\n` +
        `Email: ${email}\n` +
        `Phone: ${phone}\n\n` +
        `Message:\n${message}\n\n` +
        `----------------------------------------\n` +
        `Submitted via PMSO Inc. Website`
      );

      const mailtoUrl = `mailto:pmsoinc@mail2usa.com?subject=${subject}&body=${body}`;

      // 3. Trigger email composer directly to pmsoinc@mail2usa.com
      window.location.href = mailtoUrl;

      // 4. Update UI confirmation
      contactForm.reset();
      if (contactSuccess) {
        contactSuccess.innerHTML = `
          <div style="font-size: 1.05rem; margin-bottom: 0.4rem; color: #1e6939;">
            <strong>Thank you, ${name}!</strong> Your inquiry has been routed to our office email.
          </div>
          <p style="margin-bottom: 0.75rem; font-size: 0.95rem; color: #2e5739;">
            If your email app did not open automatically, click the button below to send your message directly to us:
          </p>
          <a href="${mailtoUrl}" class="nav-cta-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none; padding: 0.55rem 1.15rem; font-size: 0.95rem;">
            <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
            Send Email Now
          </a>
        `;
        contactSuccess.style.display = 'block';
        contactSuccess.scrollIntoView({ behavior: 'smooth' });
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

