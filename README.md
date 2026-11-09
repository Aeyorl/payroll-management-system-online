# PMSO Inc. - Payroll Management System Online

Official website and digital presence for **PMSO Inc. (Payroll Management System Online)**, providing professional payroll management, individual and corporate tax preparation, and comprehensive bookkeeping solutions.

---

## 🎨 Official Brand Identity & Assets

The official brand identity has been integrated across the platform:

| Asset Name | File Path | Usage & Description |
|---|---|---|
| **Primary Logo** | `assets/images/pmso-logo.png` | Stacked brand lockup with full emblem, wordmark, and tagline. Used for brand showcases, Open Graph preview, and high-fidelity presentation. |
| **Horizontal Logo** | `assets/images/pmso-logo-horizontal.png` | Horizontal brand lockup integrated into main navigation bar and mobile drawer header. |
| **Brand Icon / Symbol** | `assets/images/pmso-icon.png` | Standalone stylized PMSO checkmark monogram symbol for compact brand placements. |
| **Multi-size Favicon** | `favicon.ico` / `assets/images/favicon.ico` | Standard browser tab icon with 16x16, 32x32, and 48x48 formats. |
| **High-DPI Favicons** | `assets/images/favicon-32x32.png`, `assets/images/favicon-16x16.png` | PNG favicons for modern desktop and mobile browsers. |
| **Apple Touch Icon** | `apple-touch-icon.png` / `assets/images/apple-touch-icon.png` | 180×180 high-contrast icon for iOS home screen bookmarks. |
| **PWA App Icons** | `assets/images/icon-192.png`, `assets/images/icon-512.png` | 192×192 and 512×512 icons for Progressive Web App installation. |
| **Web App Manifest** | `site.webmanifest` | W3C Web App Manifest declaring application name, colors, and responsive icons. |

---

## 🎨 Color Palette & Typography

| Element | Specification | Hex / Value | Usage |
|---|---|---|---|
| **Primary Blue** | `--primary` | `#0069C8` | Core brand color, header highlights, CTA buttons, active links |
| **Deep Blue / Hover** | `--primary-hover` / `--primary-dark` | `#084A9C` | Button hover states, dropdown hover, card depth |
| **Accent Blue** | `--accent` | `#0BA5F5` | Focus rings, badges, brand checkmark accent |
| **Neutral Gray** | `--neutral-gray` / `--text-muted` | `#627181` | Subtitles, helper text, neutral borders |
| **White** | `--bg-page` / `--bg-card` | `#FFFFFF` | Page canvas, card backgrounds |
| **Off-White Light Gray** | `--bg-light` | `#F7F9FC` | Section alternating background |
| **Heading Typography** | Google Font | `'Titillium Web', sans-serif` | Modern corporate headers (300, 400, 600, 700) |
| **Body Typography** | Google Font | `'Open Sans', sans-serif` | Crisp, legible body text (300, 400, 500, 600, 700) |

---

## 🌟 Pages & Architecture

1. **Home (`index.html`)**
   - **Top Contact Bar**: Office Email `pmsoinc@mail2usa.com` link.
   - **Header & Navbar**: Integrated horizontal brand logo (`pmso-logo-horizontal.png`), responsive desktop nav, and mobile drawer.
   - **Hero Section**: HTML5 video background (`hero_video.mp4` / `hero_poster.jpg`) with branded gradient overlay and online contact CTA.
   - **What We Offer**: 4 core service cards with interactive Show More / Show Less accordions:
     - Accounting & Bookkeeping
     - Individual Tax Preparation
     - Business Tax Preparation
     - Payroll Services
   - **Subscribe Section**: Interactive newsletter subscription with instant validation and LocalStorage persistence.
   - **Reviews Section**: High-rating client testimonials and ratings.
   - **Footer**: Social icons and official copyright notice.

2. **About Us (`about-us.html`)**
   - Official stacked brand identity showcase (`pmso-logo.png`).
   - Company history (founded 2011), core principles, IRS/FTB/EDD audit representation.
   - Dual feature highlights: *"Your Taxes, Simplified"* & *"Your Business is Ours"*.

3. **Tax Services (`tax-services.html`)**
   - Comprehensive Individual Tax filing breakdown & IRS resolution.
   - 6 Key Advantages Grid: Personalized Support, Due Diligence, Experience, Reduced Audit Risk, Competitive Pricing, Time Savings.
   - Business Tax Preparation (C-Corp 1120, S-Corp 1120S, Partnership 1065, State Returns, Payroll, Sales Tax).
   - 24+ Industry Specializations List.

4. **Payroll Services (`payroll-services.html`)**
   - Detailed payroll processing capabilities for small & medium businesses.
   - Pay frequency matrices (Weekly, Bi-Weekly, Monthly, Quarterly).
   - Direct deposit & printed check processing with full ledger reporting.
   - Year-end tax filing (Forms W-2, 1099, federal & state submissions).

5. **Accounting Services (`accounting-services.html`)**
   - Financial Reporting & Planning services.
   - Bookkeeping & cash flow optimization.
   - Custom business accounting consultation banner.

6. **Contact Us (`contact-us.html`)**
   - Interactive contact form with client-side validation and LocalStorage persistence.
   - Normal business hours breakdown with automatic **"(Today)"** highlight badge.
   - Physical address (`277 Park Ave, New York, NY 10172`) and office email (`pmsoinc@mail2usa.com`).
   - Interactive Google Map embed centered on office location.

7. **Our Locations (`locations.html` / `/locations`)**
   - Interactive regional office directory featuring 43 regional hubs across 15 states and territories (New York HQ, Georgia, Texas, Pennsylvania, Illinois, Ohio, North Carolina, Michigan, Washington, Indiana, South Carolina, Tennessee, Utah, Florida, and Puerto Rico), alongside nationwide remote advisory.
   - Real-time instant search input (searching city, state, address, services, and ZIP code) and responsive state filter pills.
   - Rich office cards complete with addresses, services offered, direct Google Maps directions links, and consultation booking.

---

## 🚀 Running the Site Locally

A local preview server runs on port **3000**:

```bash
# Preview URLs:
http://localhost:3000/
http://localhost:3000/about-us.html
http://localhost:3000/tax-services.html
http://localhost:3000/payroll-services.html
http://localhost:3000/accounting-services.html
http://localhost:3000/contact-us.html
```

To start the server manually anytime:
```bash
python -m http.server 3000 --directory c:\Users\aeyon\crystaltaxinc-clone
```

---

## 📁 Project Structure

```
├── index.html                  # Homepage with video hero & offer cards
├── about-us.html               # About Us & company history with brand showcase
├── tax-services.html           # Tax Services (Individual & Business)
├── payroll-services.html       # Payroll processing & tax filing
├── accounting-services.html    # Accounting & Bookkeeping solutions
├── contact-us.html             # Contact form, office hours & Google map
├── locations.html              # Regional offices directory & interactive state filter
├── favicon.ico                 # Standard multi-res browser favicon
├── apple-touch-icon.png        # Root iOS touch icon (180x180)
├── site.webmanifest            # W3C Web App Manifest
├── css/
│   └── styles.css              # Custom brand stylesheet with official palette
├── js/
│   └── main.js                 # Mobile drawer, form handling, cookies & accordions
└── assets/
    └── images/                 # Brand assets, logos, video, posters & stock imagery
        ├── pmso-logo.png               # Official stacked primary logo
        ├── pmso-logo-horizontal.png    # Official horizontal header logo
        ├── pmso-icon.png               # Official standalone monogram symbol
        ├── favicon.ico                 # Multi-res favicon (16/32/48)
        ├── favicon-32x32.png           # 32x32 PNG favicon
        ├── favicon-16x16.png           # 16x16 PNG favicon
        ├── apple-touch-icon.png        # 180x180 Apple touch icon
        ├── icon-192.png                # 192x192 PWA icon
        ├── icon-512.png                # 512x512 PWA icon
        ├── hero_video.mp4
        ├── hero_poster.jpg
        └── stock_*.jpg
```
