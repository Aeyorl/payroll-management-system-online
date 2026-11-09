import os
import urllib.parse

# Complete locations dataset combining existing directory and user's service locations
# Handled duplicates:
# - NYC: 277 Park Ave (HQ kept, duplicate skipped)
# - Atlanta: Updated to 2233 Peachtree Road, Atlanta, GA 30309 + Perimeter + Columbus + Savannah
# - Nashville: Updated to 1801 West End Avenue, Nashville, TN 37203
# - All new states (TX, PA, IL, OH, NC, MI, WA, IN, SC) and Buffalo, NY added cleanly

LOCATIONS = [
    # 1. New York
    {
        "region": "ny",
        "state_name": "New York",
        "city": "New York City",
        "title": "New York Headquarters",
        "subtitle": "Corporate Headquarters & Mid-Atlantic Hub",
        "address_line": "277 Park Ave",
        "city_state_zip": "New York, NY 10172",
        "services": ["Executive Payroll", "Corporate Tax", "IRS Audit Defense", "Bookkeeping"],
        "is_hq": True
    },
    {
        "region": "ny",
        "state_name": "New York",
        "city": "Buffalo",
        "title": "Buffalo Regional Office",
        "subtitle": "Western New York & Niagara Frontier Hub",
        "address_line": "672 Delaware Avenue",
        "city_state_zip": "Buffalo, NY 14209",
        "services": ["Small Business Payroll", "Individual Tax", "Sales Tax Compliance", "Bookkeeping"],
        "is_hq": False
    },

    # 2. Georgia
    {
        "region": "ga",
        "state_name": "Georgia",
        "city": "Atlanta",
        "title": "Atlanta Peachtree Office",
        "subtitle": "Buckhead & Midtown Metro Business Hub",
        "address_line": "2233 Peachtree Road",
        "city_state_zip": "Atlanta, GA 30309",
        "services": ["Multi-State Tax", "Payroll Processing", "CFO Advisory", "Corporate 1120"],
        "is_hq": False
    },
    {
        "region": "ga",
        "state_name": "Georgia",
        "city": "Atlanta (Perimeter)",
        "title": "Perimeter Atlanta Office",
        "subtitle": "North Metro, Sandy Springs & Dunwoody",
        "address_line": "4408 Perimeter Lofts Circle",
        "city_state_zip": "Atlanta, GA 30346",
        "services": ["Small Business Tax", "Direct Deposit", "Monthly Accounting", "Quarterly Filings"],
        "is_hq": False
    },
    {
        "region": "ga",
        "state_name": "Georgia",
        "city": "Columbus",
        "title": "Columbus Regional Office",
        "subtitle": "Chattahoochee Valley Regional Office",
        "address_line": "2357 Warm Springs Road",
        "city_state_zip": "Columbus, GA 31904",
        "services": ["Payroll Management", "State & Federal Tax", "Business Bookkeeping"],
        "is_hq": False
    },
    {
        "region": "ga",
        "state_name": "Georgia",
        "city": "Savannah",
        "title": "Savannah Coastal Office",
        "subtitle": "Coastal Georgia & Savannah Port Commercial Hub",
        "address_line": "1901 Waters Avenue, Suite C",
        "city_state_zip": "Savannah, GA 31401",
        "services": ["Logistics & Port Payroll", "Business Tax Filing", "Financial Reporting"],
        "is_hq": False
    },

    # 3. Texas
    {
        "region": "tx",
        "state_name": "Texas",
        "city": "Houston",
        "title": "Houston Energy Corridor Office",
        "subtitle": "Greater Houston & Gulf Coast Commercial Center",
        "address_line": "11767 Katy Freeway",
        "city_state_zip": "Houston, TX 77079",
        "services": ["Corporate Tax Planning", "Commercial Payroll", "Franchise Tax Filing", "Bookkeeping"],
        "is_hq": False
    },
    {
        "region": "tx",
        "state_name": "Texas",
        "city": "Dallas",
        "title": "Dallas Spring Valley Office",
        "subtitle": "DFW Metroplex & North Texas Regional Hub",
        "address_line": "4201 Spring Valley Road",
        "city_state_zip": "Dallas, TX 75244",
        "services": ["Direct Deposit Payroll", "Partnership 1065", "IRS Representation", "Ledger Review"],
        "is_hq": False
    },
    {
        "region": "tx",
        "state_name": "Texas",
        "city": "Austin",
        "title": "Austin Technology Corridor Office",
        "subtitle": "Silicon Hills & Central Texas Regional Hub",
        "address_line": "9430 Research Blvd",
        "city_state_zip": "Austin, TX 78759",
        "services": ["Scale-Up Payroll", "Entity Formation Tax", "Multi-State Compliance", "Bookkeeping"],
        "is_hq": False
    },

    # 4. Pennsylvania
    {
        "region": "pa",
        "state_name": "Pennsylvania",
        "city": "Philadelphia",
        "title": "Philadelphia Center City Office",
        "subtitle": "Center City & Delaware Valley Commercial Hub",
        "address_line": "30 S 17th St",
        "city_state_zip": "Philadelphia, PA 19103",
        "services": ["City Wage Tax Advisory", "Corporate Payroll", "Federal & State Filing", "Financial Review"],
        "is_hq": False
    },
    {
        "region": "pa",
        "state_name": "Pennsylvania",
        "city": "Pittsburgh",
        "title": "Pittsburgh Parkway Office",
        "subtitle": "Foster Plaza & Western PA Regional Center",
        "address_line": "750 Holiday Dr",
        "city_state_zip": "Pittsburgh, PA 15220",
        "services": ["Commercial Payroll", "Corporate 1120", "Small Business Accounting"],
        "is_hq": False
    },
    {
        "region": "pa",
        "state_name": "Pennsylvania",
        "city": "Erie",
        "title": "Erie Lakefront Office",
        "subtitle": "Lake Erie Regional & Tri-State Center",
        "address_line": "3126 Peach St",
        "city_state_zip": "Erie, PA 16508",
        "services": ["Individual Tax Prep", "Weekly/Bi-Weekly Payroll", "Local Compliance"],
        "is_hq": False
    },

    # 5. Illinois
    {
        "region": "il",
        "state_name": "Illinois",
        "city": "Chicago",
        "title": "Chicago River North Office",
        "subtitle": "Downtown Chicago & Cook County Business Hub",
        "address_line": "620 N LaSalle Dr",
        "city_state_zip": "Chicago, IL 60654",
        "services": ["Midwest Corporate Payroll", "IL-1120 Filing", "IRS Audit Defense", "CFO Advisory"],
        "is_hq": False
    },
    {
        "region": "il",
        "state_name": "Illinois",
        "city": "Rockford",
        "title": "Rockford Regional Office",
        "subtitle": "Northern Illinois Commercial Center",
        "address_line": "483 N Mulford Rd",
        "city_state_zip": "Rockford, IL 61107",
        "services": ["Small Business Payroll", "Tax Returns", "Year-End W-2/1099 Prep"],
        "is_hq": False
    },

    # 6. Ohio
    {
        "region": "oh",
        "state_name": "Ohio",
        "city": "Columbus",
        "title": "Columbus Broad Street Office",
        "subtitle": "Downtown Columbus & State Capital Hub",
        "address_line": "10 W Broad St",
        "city_state_zip": "Columbus, OH 43215",
        "services": ["State Tax Compliance", "Corporate Payroll", "Municipal Tax Advisory", "Bookkeeping"],
        "is_hq": False
    },
    {
        "region": "oh",
        "state_name": "Ohio",
        "city": "Cincinnati",
        "title": "Cincinnati Downtown Office",
        "subtitle": "Greater Cincinnati & Tri-State Regional Hub",
        "address_line": "310 Culvert St",
        "city_state_zip": "Cincinnati, OH 45202",
        "services": ["Direct Deposit", "Multi-State Payroll", "Individual & Corp Tax"],
        "is_hq": False
    },
    {
        "region": "oh",
        "state_name": "Ohio",
        "city": "Toledo",
        "title": "Toledo Southwyck Office",
        "subtitle": "Northwest Ohio & Lake Erie Commerce Hub",
        "address_line": "5660 Southwyck Blvd",
        "city_state_zip": "Toledo, OH 43614",
        "services": ["Manufacturing Payroll", "Quarterly Filings", "Small Business Accounting"],
        "is_hq": False
    },
    {
        "region": "oh",
        "state_name": "Ohio",
        "city": "Akron",
        "title": "Akron Peninsula Office",
        "subtitle": "Northeast Ohio & Summit County Office",
        "address_line": "1640 Akron Peninsula Rd",
        "city_state_zip": "Akron, OH 44313",
        "services": ["Business Tax Filings", "Payroll Solutions", "Financial Consultation"],
        "is_hq": False
    },

    # 7. North Carolina
    {
        "region": "nc",
        "state_name": "North Carolina",
        "city": "Charlotte",
        "title": "Charlotte Mallard Creek Office",
        "subtitle": "University City & Queen City Financial Hub",
        "address_line": "10130 Mallard Creek Rd #300",
        "city_state_zip": "Charlotte, NC 28262",
        "services": ["Executive Payroll", "Banking & Finance Tax", "Multi-Entity Accounting", "Audit Shield"],
        "is_hq": False
    },
    {
        "region": "nc",
        "state_name": "North Carolina",
        "city": "Raleigh",
        "title": "Raleigh Brier Creek Office",
        "subtitle": "Research Triangle & Capital Metro Hub",
        "address_line": "8801 Fast Park Dr",
        "city_state_zip": "Raleigh, NC 27617",
        "services": ["Tech Payroll Solutions", "State Return Prep", "Corporate Tax 1120S", "Bookkeeping"],
        "is_hq": False
    },
    {
        "region": "nc",
        "state_name": "North Carolina",
        "city": "Greensboro",
        "title": "Greensboro Triad Office",
        "subtitle": "Piedmont Triad Regional Office",
        "address_line": "204 Muirs Chapel Rd, Suite 100",
        "city_state_zip": "Greensboro, NC 27410",
        "services": ["Small Business Payroll", "Income Tax Filing", "Quarterly Estimates"],
        "is_hq": False
    },
    {
        "region": "nc",
        "state_name": "North Carolina",
        "city": "Durham",
        "title": "Durham RTP Corridor Office",
        "subtitle": "Research Triangle Park Tech & Life Sciences Hub",
        "address_line": "68 TW Alexander Dr",
        "city_state_zip": "Durham, NC 27713",
        "services": ["Automated Payroll", "Corporate 1120", "R&D Accounting Advisory"],
        "is_hq": False
    },
    {
        "region": "nc",
        "state_name": "North Carolina",
        "city": "Winston-Salem",
        "title": "Winston-Salem Regional Office",
        "subtitle": "Twin City & Forsyth County Commercial Hub",
        "address_line": "1665 Westbrook Plaza Dr",
        "city_state_zip": "Winston-Salem, NC 27103",
        "services": ["Commercial Payroll", "Individual Tax", "Business Bookkeeping"],
        "is_hq": False
    },

    # 8. Michigan
    {
        "region": "mi",
        "state_name": "Michigan",
        "city": "Detroit",
        "title": "Detroit Woodward Office",
        "subtitle": "New Center & Metro Detroit Commercial Hub",
        "address_line": "7375 Woodward Ave",
        "city_state_zip": "Detroit, MI 48202",
        "services": ["Automotive & Trade Payroll", "Corporate Tax", "City of Detroit Tax", "IRS Defense"],
        "is_hq": False
    },
    {
        "region": "mi",
        "state_name": "Michigan",
        "city": "Grand Rapids",
        "title": "Grand Rapids Broadmoor Office",
        "subtitle": "West Michigan & Grand Valley Regional Hub",
        "address_line": "4595 Broadmoor Ave SE",
        "city_state_zip": "Grand Rapids, MI 49512",
        "services": ["Full-Service Payroll", "Business Tax Filing", "Ledger Management"],
        "is_hq": False
    },
    {
        "region": "mi",
        "state_name": "Michigan",
        "city": "Sterling Heights",
        "title": "Sterling Heights Regional Office",
        "subtitle": "Macomb County Commercial & Industrial Hub",
        "address_line": "9001 15 Mile Rd",
        "city_state_zip": "Sterling Heights, MI 48312",
        "services": ["Direct Deposit", "Quarterly Payroll Tax", "Small Business Accounting"],
        "is_hq": False
    },

    # 9. Washington
    {
        "region": "wa",
        "state_name": "Washington",
        "city": "Seattle",
        "title": "Seattle Waterfront Office",
        "subtitle": "Pioneer Square & Pacific Northwest Hub",
        "address_line": "450 Alaskan Way S",
        "city_state_zip": "Seattle, WA 98104",
        "services": ["WA B&O Tax Advisory", "Tech & Enterprise Payroll", "Federal Tax Prep", "CFO Consulting"],
        "is_hq": False
    },
    {
        "region": "wa",
        "state_name": "Washington",
        "city": "Spokane",
        "title": "Spokane Regional Office",
        "subtitle": "Inland Northwest Regional Center",
        "address_line": "620 S Washington St",
        "city_state_zip": "Spokane, WA 99204",
        "services": ["Small Business Payroll", "Individual Tax", "Bookkeeping Services"],
        "is_hq": False
    },
    {
        "region": "wa",
        "state_name": "Washington",
        "city": "Tacoma",
        "title": "Tacoma South Sound Office",
        "subtitle": "South Sound & Pierce County Hub",
        "address_line": "5439 S Tacoma Way",
        "city_state_zip": "Tacoma, WA 98409",
        "services": ["Commercial Payroll", "Corporate Filing", "Sales Tax Compliance"],
        "is_hq": False
    },

    # 10. Indiana
    {
        "region": "in",
        "state_name": "Indiana",
        "city": "Indianapolis",
        "title": "Indianapolis Fort Harrison Office",
        "subtitle": "Fort Harrison & Circle City Regional Hub",
        "address_line": "9165 Otis Ave",
        "city_state_zip": "Indianapolis, IN 46216",
        "services": ["Indiana County Tax Prep", "Direct Deposit Payroll", "Corporate 1120S", "Monthly Ledger"],
        "is_hq": False
    },
    {
        "region": "in",
        "state_name": "Indiana",
        "city": "Fort Wayne",
        "title": "Fort Wayne Regional Office",
        "subtitle": "Northeast Indiana Commercial Center",
        "address_line": "4310 Illinois Rd",
        "city_state_zip": "Fort Wayne, IN 46804",
        "services": ["Small Business Payroll", "Tax Filing", "W-2 & 1099 Generation"],
        "is_hq": False
    },
    {
        "region": "in",
        "state_name": "Indiana",
        "city": "Evansville",
        "title": "Evansville Main Street Office",
        "subtitle": "Tri-State Southwest Indiana Hub",
        "address_line": "915 Main St",
        "city_state_zip": "Evansville, IN 47708",
        "services": ["Payroll Solutions", "Individual & Business Tax", "Financial Planning"],
        "is_hq": False
    },
    {
        "region": "in",
        "state_name": "Indiana",
        "city": "Fishers",
        "title": "Fishers Techway Office",
        "subtitle": "Hamilton County & Tech Corridor Hub",
        "address_line": "11650 Lantern Rd",
        "city_state_zip": "Fishers, IN 46037",
        "services": ["Automated Payroll", "State Tax Filing", "Corporate Accounting"],
        "is_hq": False
    },

    # 11. South Carolina
    {
        "region": "sc",
        "state_name": "South Carolina",
        "city": "Charleston",
        "title": "Charleston King Street Office",
        "subtitle": "Upper King & Lowcountry Commercial Hub",
        "address_line": "677 King St",
        "city_state_zip": "Charleston, SC 29403",
        "services": ["Hospitality & Trade Payroll", "SC Entity Tax Filing", "IRS Representation", "Bookkeeping"],
        "is_hq": False
    },
    {
        "region": "sc",
        "state_name": "South Carolina",
        "city": "Columbia",
        "title": "Columbia Midlands Office",
        "subtitle": "Midlands & Capital Regional Office",
        "address_line": "140 Stoneridge Dr",
        "city_state_zip": "Columbia, SC 29210",
        "services": ["Small Business Payroll", "State Return Prep", "Quarterly Filings"],
        "is_hq": False
    },

    # 12. Tennessee
    {
        "region": "tn",
        "state_name": "Tennessee",
        "city": "Nashville",
        "title": "Nashville Midtown Office",
        "subtitle": "Palmer Plaza / Midtown & Music Row Commercial Hub",
        "address_line": "1801 West End Avenue",
        "city_state_zip": "Nashville, TN 37203",
        "services": ["Entertainment & Corporate Payroll", "Franchise & Excise Tax", "IRS Audit Defense", "CFO Advisory"],
        "is_hq": False
    }
]

# Unique regions in order
REGIONS = [
    ("all", "All Locations"),
    ("ny", "New York (HQ)"),
    ("ga", "Georgia"),
    ("tx", "Texas"),
    ("pa", "Pennsylvania"),
    ("il", "Illinois"),
    ("oh", "Ohio"),
    ("nc", "North Carolina"),
    ("mi", "Michigan"),
    ("wa", "Washington"),
    ("in", "Indiana"),
    ("sc", "South Carolina"),
    ("tn", "Tennessee"),
]

def generate_card_html(loc):
    encoded_addr = urllib.parse.quote(f"{loc['address_line']}, {loc['city_state_zip']}")
    maps_url = f"https://maps.google.com/?q={encoded_addr}"
    
    services_html = "".join([f'                <span class="location-service-tag">{s}</span>\n' for s in loc["services"]])
    
    search_keywords = f"{loc['city']} {loc['state_name']} {loc['city_state_zip']} {loc['address_line']} {' '.join(loc['services'])}".lower()
    
    return f'''          <!-- {loc["state_name"]} - {loc["city"]} -->
          <article class="location-card" data-region="{loc["region"]}" data-search="{search_keywords}">
            <div class="location-card-header">
              <span class="location-state-pill">{loc["state_name"]}</span>
              <h3 class="location-card-title">{loc["title"]}</h3>
              <div class="location-card-subtitle">{loc["subtitle"]}</div>
            </div>
            <div class="location-card-body">
              <div class="location-address-box">
                <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 0 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>
                <div>
                  <strong>{loc["address_line"]}</strong><br />
                  {loc["city_state_zip"]}
                </div>
              </div>
              <div class="location-services-tags">
{services_html}              </div>
            </div>
            <div class="location-card-footer">
              <a href="{maps_url}" target="_blank" rel="noopener noreferrer" class="location-directions-link">
                Get Directions &rarr;
              </a>
              <a href="contact-us.html" class="location-action-btn">Contact Office</a>
            </div>
          </article>'''

def generate_filter_buttons():
    btns = []
    for code, label in REGIONS:
        active_cls = " active" if code == "all" else ""
        count_str = f" ({len(LOCATIONS)})" if code == "all" else ""
        btns.append(f'          <button type="button" class="location-filter-btn{active_cls}" data-filter="{code}">{label}{count_str}</button>')
    return "\n".join(btns)

def build_locations_page():
    cards_html = "\n\n".join([generate_card_html(loc) for loc in LOCATIONS])
    filters_html = generate_filter_buttons()
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Our Locations | PMSO Inc. - Payroll Management System Online</title>
  <meta name="description" content="Find a PMSO Inc. office near you. Providing professional payroll management, tax preparation, and corporate bookkeeping across our regional offices and nationwide remotely." />
  <meta name="author" content="PMSO Inc." />
  <meta name="theme-color" content="#0069C8" />

  <!-- Open Graph -->
  <meta property="og:url" content="https://www.pmso.live/locations" />
  <meta property="og:site_name" content="PMSO Inc." />
  <meta property="og:title" content="Our Locations | PMSO Inc. - Payroll Management System Online" />
  <meta property="og:description" content="Find a PMSO Inc. office near you. Providing professional payroll management, tax preparation, and corporate bookkeeping across our regional offices and nationwide remotely." />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="assets/images/pmso-logo.png" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Our Locations | PMSO Inc. - Payroll Management System Online" />
  <meta name="twitter:description" content="Find a PMSO Inc. office near you. Providing professional payroll management, tax preparation, and corporate bookkeeping across our regional offices and nationwide remotely." />
  <meta name="twitter:image" content="assets/images/pmso-logo.png" />

  <!-- Favicon & Touch Icons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/images/apple-touch-icon.png" />
  <link rel="manifest" href="site.webmanifest" />

  <!-- Stylesheet -->
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>

  <!-- Site Header -->
  <header class="site-header">
    <div class="top-bar">
      <div class="container top-bar-content">
        <a href="mailto:pmsoinc@mail2usa.com" class="top-bar-email-btn" title="Email PMSO Inc." aria-label="Email PMSO Inc.">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
      </div>
    </div>

    <div class="container navbar">
      <a href="index.html" class="nav-brand" title="PMSO Inc. | Payroll Management System Online" aria-label="PMSO Inc. - Payroll Management System Online">
        <img src="assets/images/pmso-logo-horizontal.png" alt="PMSO Inc. - Payroll Management System Online" class="brand-logo-header" />
      </a>

      <!-- Desktop Nav -->
      <nav class="nav-menu">
        <div class="nav-item">
          <a href="index.html" class="nav-link">Home</a>
        </div>
        <div class="nav-item">
          <a href="about-us.html" class="nav-link">About us</a>
        </div>
        <div class="nav-item">
          <a href="tax-services.html" class="nav-link">Tax Services</a>
        </div>
        <div class="nav-item">
          <a href="payroll-services.html" class="nav-link">Payroll Services</a>
        </div>
        <div class="nav-item">
          <a href="locations.html" class="nav-link active">Locations</a>
        </div>
        <div class="nav-item dropdown">
          <a href="#" class="nav-link">
            <span>More</span>
            <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M18.605 7l-6.793 7.024-6.375-7.002L4 8.467 11.768 17l.485-.501L20 8.489z"></path></svg>
          </a>
          <div class="nav-dropdown">
            <a href="accounting-services.html" class="dropdown-link">Accounting Services</a>
            <a href="contact-us.html" class="dropdown-link">Contact Us</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="contact-us.html" class="nav-cta-btn">Contact Us</a>
        </div>
      </nav>

      <!-- Mobile Hamburger Button -->
      <button class="mobile-toggle" id="mobileToggle" aria-label="Open Navigation Menu">
        <svg viewBox="0 0 24 24" fill="currentColor"><g><path fill-rule="evenodd" d="M4 8h16V6H4z"></path><path fill-rule="evenodd" d="M4 13.096h16v-2.001H4z"></path><path fill-rule="evenodd" d="M4 18.346h16v-2H4z"></path></g></svg>
      </button>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div class="mobile-drawer" id="mobileDrawer">
    <div class="mobile-drawer-header">
      <div class="mobile-drawer-brand">
        <img src="assets/images/pmso-logo-horizontal.png" alt="PMSO Inc. - Payroll Management System Online" class="brand-logo-drawer" />
      </div>
      <button class="mobile-drawer-close" id="drawerClose" aria-label="Close Navigation Menu">
        <svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M17.999 4l-6.293 6.293L5.413 4 4 5.414l6.292 6.293L4 18l1.413 1.414 6.293-6.292 6.293 6.292L19.414 18l-6.294-6.293 6.294-6.293z"></path></svg>
      </button>
    </div>
    <ul class="mobile-nav-list">
      <li><a href="index.html" class="mobile-nav-link">Home</a></li>
      <li><a href="about-us.html" class="mobile-nav-link">About us</a></li>
      <li><a href="tax-services.html" class="mobile-nav-link">Tax Services</a></li>
      <li><a href="payroll-services.html" class="mobile-nav-link">Payroll Services</a></li>
      <li><a href="accounting-services.html" class="mobile-nav-link">Accounting Services</a></li>
      <li><a href="locations.html" class="mobile-nav-link active">Locations</a></li>
      <li><a href="contact-us.html" class="mobile-nav-link">Contact Us</a></li>
    </ul>
    <div class="mobile-drawer-footer">
      <a href="contact-us.html" class="nav-cta-btn" style="width: 100%; justify-content: center;">Contact Us</a>
      <div style="display: flex; justify-content: center; margin-top: 0.75rem;">
        <a href="mailto:pmsoinc@mail2usa.com" class="drawer-email-btn" title="Email PMSO Inc." aria-label="Email PMSO Inc.">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
      </div>
    </div>
  </div>
  <div class="drawer-backdrop" id="drawerBackdrop"></div>

  <main>
    <!-- Page Banner -->
    <section class="page-banner" style="background-image: url('assets/images/stock_106509_1920.jpg');">
      <div class="page-banner-overlay"></div>
      <div class="page-banner-content">
        <h1 class="page-banner-title">Our Locations</h1>
        <div class="page-banner-breadcrumb">
          <a href="index.html">Home</a> &nbsp;/&nbsp; Locations
        </div>
      </div>
    </section>

    <!-- Main Locations Directory Section -->
    <section class="section-pad bg-light">
      <div class="container">
        <h2 class="section-title">Regional Offices &amp; Nationwide Reach</h2>
        <p class="section-subtitle">
          Whether you need local in-person tax and payroll advisory across our regional hubs or seamless digital support across our remote-first infrastructure, our dedicated teams are ready to serve you.
        </p>

        <!-- Search Bar -->
        <div class="locations-search-container">
          <svg class="locations-search-icon" viewBox="0 0 24 24" fill="currentColor" width="20" height="20" aria-hidden="true">
            <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
          </svg>
          <input type="text" id="locationSearchInput" class="locations-search-input" placeholder="Search by city, state, or ZIP code (e.g. Dallas, Seattle, Chicago, 30309)..." aria-label="Search locations by city, state, or ZIP code" />
        </div>

        <!-- Interactive Region Filter Pills -->
        <div class="locations-filter-bar">
{filters_html}
        </div>

        <!-- No Results Message (Hidden by default) -->
        <div id="noLocationsMessage" class="no-locations-message" style="display: none;">
          <p>No office locations match your search query. Please try searching another city, state, or ZIP code.</p>
          <p style="margin-top: 0.5rem; font-size: 0.95rem; color: var(--text-muted);">
            Remember: We serve clients nationwide remotely across all 50 U.S. states.
          </p>
        </div>

        <!-- Locations Grid -->
        <div class="locations-grid" id="locationsGrid">
{cards_html}
        </div>

        <!-- Nationwide Remote Services Banner -->
        <div class="remote-banner-box">
          <h3>Don't See Your City? We Serve Clients Nationwide.</h3>
          <p>
            Operating on a modern, secure remote-first architecture, PMSO Inc. works with businesses, contractors, and individuals across more than 40 states. Enjoy encrypted cloud document exchange, seamless online payroll management, and responsive virtual consultations anytime.
          </p>
          <a href="contact-us.html" class="remote-banner-btn">
            Get Started Online &rarr;
          </a>
        </div>

      </div>
    </section>
  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container footer-content">
      <div class="footer-social-links">
        <span class="footer-social-link">
          <svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M22 12.061C22 6.505 17.523 2 12 2S2 6.505 2 12.061c0 5.022 3.657 9.184 8.438 9.939v-7.03h-2.54v-2.91h2.54V9.845c0-2.522 1.492-3.915 3.777-3.915 1.094 0 2.238.197 2.238.197v2.476h-1.26c-1.243 0-1.63.775-1.63 1.57v1.888h2.773l-.443 2.908h-2.33V22c4.78-.755 8.437-4.917 8.437-9.939z"></path></svg>
        </span>
        <span class="footer-social-link">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.604 8.516c.13.35.198.719.203 1.091.033.622.033.811.033 2.386 0 1.574-.004 1.763-.033 2.385a3.273 3.273 0 0 1-.203 1.091 1.956 1.956 0 0 1-1.12 1.12c-.35.13-.719.198-1.091.204-.622.032-.811.032-2.386.032-1.574 0-1.763-.003-2.385-.032a3.273 3.273 0 0 1-1.091-.204 1.956 1.956 0 0 1-1.12-1.12 3.273 3.273 0 0 1-.204-1.09c-.032-.623-.032-.812-.032-2.386 0-1.575.003-1.764.032-2.386.006-.372.074-.741.204-1.09a1.956 1.956 0 0 1 1.12-1.12c.35-.13.718-.199 1.09-.204.623-.033.812-.033 2.386-.033 1.575 0 1.764.004 2.386.033.372.005.741.074 1.09.203.515.2.922.606 1.12 1.12zM12 15.033a3.033 3.033 0 1 0 0-6.066 3.033 3.033 0 0 0 0 6.066zm3.153-5.477a.71.71 0 1 0 0-1.418.71.71 0 0 0 0 1.418zM12 13.967a1.967 1.967 0 1 1 0-3.934 1.967 1.967 0 0 1 0 3.934zM12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10A10 10 0 0 0 12 2zm5.87 12.433c-.01.49-.102.974-.274 1.432a3.018 3.018 0 0 1-1.727 1.728 4.335 4.335 0 0 1-1.433.272c-.629.03-.829.037-2.432.037-1.604 0-1.819 0-2.433-.037a4.335 4.335 0 0 1-1.433-.272 3.018 3.018 0 0 1-1.727-1.728 4.335 4.335 0 0 1-.273-1.432c-.029-.63-.036-.83-.036-2.433 0-1.604 0-1.818.036-2.433.01-.49.102-.974.273-1.432a3.018 3.018 0 0 1 1.727-1.728 4.335 4.335 0 0 1 1.433-.272c.629-.03.829-.037 2.433-.037 1.603 0 1.818 0 2.432.037.49.009.974.101 1.433.272.794.307 1.42.934 1.727 1.728.172.458.264.943.273 1.432.03.63.036.83.036 2.433 0 1.604-.007 1.804-.036 2.433z"></path></svg>
        </span>
        <span class="footer-social-link">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.236 2.636 7.858 6.356 9.315-.088-.791-.167-2.008.034-2.872.182-.78 1.173-4.97 1.173-4.97s-.3-.6-.3-1.485c0-1.39.807-2.428 1.81-2.428.854 0 1.266.64 1.266 1.408 0 .858-.547 2.14-.829 3.33-.235.995.5 1.807 1.481 1.807 1.778 0 3.144-1.874 3.144-4.58 0-2.394-1.72-4.068-4.177-4.068-2.846 0-4.516 2.134-4.516 4.34 0 .86.331 1.78.745 2.282a.3.3 0 01.069.287c-.076.316-.245.995-.278 1.134-.043.183-.145.222-.334.133-1.25-.58-2.03-2.407-2.03-3.873 0-3.155 2.292-6.052 6.607-6.052 3.47 0 6.165 2.472 6.165 5.776 0 3.446-2.173 6.22-5.19 6.22-1.012 0-1.965-.527-2.291-1.149l-.623 2.378c-.226.868-.835 1.957-1.243 2.621.936.29 1.93.446 2.961.446 5.523 0 10-4.477 10-10S17.523 2 12 2z"></path></svg>
        </span>
        <span class="footer-social-link">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M14.933 17.2645L7.44211 6.77221H9.06447L16.5654 17.2645H14.933Z"></path><path fill-rule="evenodd" d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22ZM10.6893 12.6803L6 6H9.58023L12.6597 10.42L16.5504 6H17.6019L13.148 11.1015L18 18H14.4348L11.165 13.3471L7.07907 18H6L10.6893 12.6803Z"></path></svg>
        </span>
        <span class="footer-social-link">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10A10 10 0 0 0 12 2zM7.055 13.745a.97.97 0 0 1-.073-.509l.182-2.072a.687.687 0 0 1 .29-.364c.182-.11.582.036.582.036l2.619 1.31s.4.181.4.509c-.037.436-.219.436-.364.509l-3.055.654s-.436.146-.581-.073zm4.945.473l-.036 3.018s.036.437-.219.51c-.144.02-.291.02-.436 0l-2.036-.655a.6.6 0 0 1-.291-.364c-.073-.218.182-.545.182-.545l2.036-2.255s.327-.29.582-.145c.254.145.254.436.218.436zm-.364-3.236a.687.687 0 0 1-.581-.182l-2.51-3.418s-.363-.4-.181-.691a.64.64 0 0 1 .363-.291l2.4-.873c.11-.036.218-.145.582.073.255.145.291.655.291.655l.036 4.145s-.072.51-.4.582zm1.419.582l1.636-2.582s.145-.364.436-.327c.152.002.29.085.364.218l1.382 1.636a.676.676 0 0 1 .072.473c-.072.218-.472.363-.472.363l-2.91.837s-.4.073-.545-.182c-.145-.255 0-.51.037-.436zm3.781 3.309L15.6 16.655a.815.815 0 0 1-.436.181c-.219 0-.473-.327-.473-.327l-1.564-2.618s-.182-.364.037-.582c.218-.218.472-.109.509-.145l2.909.945s.4.073.4.364a1.942 1.942 0 0 1-.146.4z"></path></svg>
        </span>
      </div>
      <p class="footer-copyright">Copyright &copy; 2024 PMSO Inc. - Payroll Management System Online - All Rights Reserved.</p>
    </div>
  </footer>

  <!-- Cookie Policy Banner -->
  <aside class="cookie-banner" id="cookieBanner" aria-label="Cookie consent banner">
    <div class="cookie-content">
      <h4>Cookie Policy</h4>
      <p>This website uses cookies. By continuing to use this site, you accept our use of cookies.</p>
    </div>
    <button class="cookie-btn" id="cookieAcceptBtn" type="button">Accept &amp; Close</button>
  </aside>

  <!-- Main JavaScript -->
  <script src="js/main.js"></script>
</body>
</html>'''
    return html

def main():
    html_content = build_locations_page()
    
    paths = [
        r"c:\Users\aeyon\payroll-management-system-online\locations.html",
        r"c:\Users\aeyon\crystaltaxinc-clone\locations.html"
    ]
    
    for path in paths:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {path} with {len(LOCATIONS)} locations.")

if __name__ == "__main__":
    main()

