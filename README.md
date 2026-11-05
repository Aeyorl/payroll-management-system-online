# Payroll Management System Online - Site Clone

A pixel-perfect, responsive website for **Payroll Management System Online**, capturing every category, section, image, feature, typography, and color palette.

---

## 🌟 Cloned Categories & Pages

1. **Home (`index.html`)**
   - **Top Contact Bar**: Office Email `pmsoinc@mail2usa.com` link.
   - **Header & Navbar**: Brand logo (`assets/images/logo.webp`), desktop navigation, mobile hamburger drawer, and call-to-action button.
   - **Hero Section**: Full-width HTML5 video background (`hero_video.mp4` / `hero_poster.jpg`) with brand gradient overlay, Titillium Web typography, and primary CTA.
   - **What We Offer**: 4 core service cards with original high-resolution stock photography:
     - Accounting & Bookkeeping (with interactive Show More / Show Less expandable text)
     - Individual Tax Preparation
     - Business Tax Preparation (with interactive Show More / Show Less expandable text)
     - Payroll Services (with interactive Show More / Show Less expandable text)
   - **Subscribe Section**: Interactive newsletter subscription with instant validation and LocalStorage persistence.
   - **Reviews Section**: High-rating client testimonials and ratings.
   - **Footer**: Official SVG social icons (Facebook, Instagram, Pinterest, Twitter/X, Yelp) and copyright info.

2. **About Us (`about-us.html`)**
   - High-resolution hero banner with breadcrumbs.
   - Company history (founded 2011 by Yasser S. Hamed), core principles, IRS/FTB/EDD audit representation.
   - Dual feature highlights: *"Your Taxes, Simplified"* & *"Your Business is Ours"*.

3. **Tax Services (`tax-services.html`)**
   - Top banner & dual service focus cards (Individual Tax Preparation & Business Tax Preparation) with anchor links.
   - Comprehensive Individual Tax filing breakdown & IRS resolution.
   - **6 Key Advantages Grid**: Personalized Support, Due Diligence, Experience, Reduced Audit Risk, Competitive Pricing, Time Savings.
   - **Business Tax Preparation**: Entity returns breakdown (C-Corp 1120, S-Corp 1120S, Partnership 1065, State Returns, Payroll, Sales Tax).
   - **24+ Industry Specializations List**: Healthcare, Construction, Artists, Retail, Manufacturing, Hospitality, Engineering, and more.
   - Corporate Tax Reform focus banner.

4. **Payroll Services (`payroll-services.html`)**
   - Detailed payroll processing capabilities for small & medium businesses.
   - Pay frequency matrices (Weekly, Bi-Weekly, Monthly, Quarterly).
   - Direct deposit & printed check processing with full ledger reporting.
   - Year-end tax filing (Forms W-2, 1099, federal & state submissions).

5. **Accounting Services (`accounting-services.html`)**
   - Financial Reporting & Planning services card with original imagery.
   - Bookkeeping & cash flow optimization services card.
   - Custom business accounting consultation banner.

6. **Contact Us (`contact-us.html`)**
   - Interactive contact form with client-side validation and LocalStorage persistence.
   - Normal business hours breakdown with automatic **"(Today)"** highlight badge.
   - Complete physical address (`277 Park Ave, New York, NY 10172`)  and office email (`pmsoinc@mail2usa.com`).
   - Interactive Google Map embed centered on 277 Park Ave, New York, NY office location.

---

## 🎨 Color Palette & Typography

| Element | Specification | Hex / Font |
|---|---|---|
| **Primary Brand Blue** | `--primary` | `#0075C1` |
| **Hover Brand Blue** | `--primary-hover` | `#005F9E` |
| **Light Blue Accent** | `--primary-light` | `#E8F4FC` |
| **Dark Background / Text** | `--text-dark` | `#161616` |
| **Card / Off-white BG** | `--bg-light` | `#F7F7F7` |
| **Border Light** | `--border-light` | `#E2E2E2` |
| **Heading Typography** | Google Font | `'Titillium Web', sans-serif` |
| **Body Typography** | Google Font | `'Open Sans', sans-serif` |

---

## 🚀 Running the Site Locally

A local preview server is already running on port **3000**:

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
# Using Python:
python -m http.server 3000 --directory c:\Users\aeyon\crystaltaxinc-clone

# Or using Node.js:
npx serve c:\Users\aeyon\crystaltaxinc-clone -p 3000
```

---

## 📁 Project Structure

```
crystaltaxinc-clone/
├── index.html                  # Homepage with video hero & offer cards
├── about-us.html               # About Us & company history
├── tax-services.html           # Tax Services (Individual & Business)
├── payroll-services.html       # Payroll processing & tax filing
├── accounting-services.html    # Accounting & Bookkeeping solutions
├── contact-us.html             # Contact form, office hours & Google map
├── css/
│   └── styles.css              # Complete custom styling matching original
├── js/
│   └── main.js                 # Mobile drawer, form handling, cookies & accordions
└── assets/
    └── images/                 # All original assets, logos, video, posters & stock imagery
        ├── logo.webp
        ├── hero_video.mp4
        ├── hero_poster.jpg
        ├── stock_11637_365.jpg
        ├── stock_8386_365.jpg
        ├── business_tax_prep.jpg
        ├── stock_DdbaNNm_365.jpg
        ├── stock_106509_1920.jpg
        ├── stock_3360_1920.jpg
        ├── stock_8406_600.jpg
        ├── stock_ny4lbOR_600.jpg
        ├── stock_11255_365.jpg
        └── stock_11559_365.jpg
```

