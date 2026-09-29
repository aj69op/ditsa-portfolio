# 📋 DITSA BAKSHI — PORTFOLIO PROJECT PLAN & REFERENCE GUIDE

> **Project Name:** `PTSD_Ditsa_Qween` / `ditsa-portfolio`  
> **Repository:** [github.com/aj69op/ditsa-portfolio](https://github.com/aj69op/ditsa-portfolio)  
> **Live URL:** [aj69op.github.io/ditsa-portfolio](https://aj69op.github.io/ditsa-portfolio/)  
> **Last Updated:** September 29, 2026  

---

## 🎯 PROJECT GOAL

Build a **premium, award-quality portfolio website** for Ditsa Bakshi inspired by 
**[karolinahess.com](https://karolinahess.com/)** — a Framer Award-winning site featuring 
Swiss editorial minimalism, scroll-driven animations, spring physics interactions, and a 
red + white color palette.

### Design Pillars
| Pillar | Description |
|--------|-------------|
| **Swiss Editorial** | Massive display typography, generous whitespace, structured grid layouts |
| **Red & White Theme** | Crimson `#dc2626` as accent, pure white `#fff` canvas, near-black `#111` type |
| **Framer Motion Feel** | Scroll reveal, spring 3D tilt, magnetic buttons, custom cursor, parallax |
| **Mobile-First** | Responsive across all breakpoints with touch-optimized interactions |
| **Accessibility** | `prefers-reduced-motion` support, ARIA labels, semantic HTML |

---

## 🗂️ FILE STRUCTURE & PURPOSE

```
PTSD_Ditsa_Qween/
│
├── index.html              ← MAIN PORTFOLIO (Karolina Hess-inspired, single page)
├── style.css               ← ALL STYLING (design tokens + animation engine)
├── script.js               ← ALL INTERACTIVITY (18 animation modules)
│
├── index.backup.html       ← Backup of original sreyasee.html-based index
├── sreyasee.html           ← Original UGC Media Kit page (Sreyasee Sar identity)
├── sreyasee.css             ← Styles for sreyasee.html (retro folder theme)
├── sreyasee.js              ← Scripts for sreyasee.html
│
├── ditsa-portfolio.html    ← Legacy: first portfolio attempt (simple grid)
├── about.html              ← Legacy: standalone about page
├── projects.html           ← Legacy: standalone projects page
├── skills.html             ← Legacy: standalone skills page
├── contact.html            ← Legacy: standalone contact page
│
├── karolina_full.html      ← Reference: full HTML snapshot of karolinahess.com
│
├── DB RESUME.pdf           ← Ditsa Bakshi's resume (linked from portfolio)
├── README.md               ← GitHub readme (basic project overview)
├── PROJECT_PLAN.md         ← THIS FILE — full project plan & status
│
├── images/                 ← All portfolio images
│   ├── ditsa.jpg           ← Hero portrait
│   ├── ditsa2.jpeg         ← About section portrait
│   ├── moodscape.png       ← MoodScape project thumbnail
│   ├── cashflow.png        ← CashFlow project thumbnail
│   ├── fashionhub.png      ← FashionHub project thumbnail
│   ├── bookverse.png       ← BookVerse project thumbnail
│   ├── candycrush.png      ← Candy Crush project thumbnail
│   ├── mazerunner.jpeg     ← Maze Runner project thumbnail
│   ├── smartnotes.png      ← SmartNotes project thumbnail
│   ├── favicon.png         ← Custom favicon
│   ├── ktsLtBf...jpeg      ← Framer export portrait image
│   └── sreyasee-*.png      ← UGC media kit images
│
├── fonts/                  ← Local font files (if any)
├── assets/                 ← Misc assets
│   └── searchIndex.json    ← Framer search index
│
└── framer_export/          ← REFERENCE: Framer site export (karolinahess-style)
    ├── index.html          ← Full Framer-generated HTML (176KB, single file)
    ├── HOSTING.md           ← Framer export hosting instructions
    ├── framer-cdn-map.json ← CDN asset mapping for offline use
    ├── vercel.json         ← Vercel deployment config
    ├── _headers            ← Netlify/Cloudflare MIME headers
    ├── _redirects          ← Redirect rules
    ├── assets/
    │   └── searchIndex.json
    ├── fonts/              ← 45 .woff2 files (Inter, Clash Grotesk, Necto Mono)
    └── images/             ← Framer export images
        ├── ktsLtBf...jpeg  ← Ditsa portrait (from Framer)
        ├── default-favicon-*.png
        └── default-touch-icon.v3.png
```

---

## 🎨 DESIGN REFERENCE — KAROLINA HESS

### Source
- **Live site:** [karolinahess.com](https://karolinahess.com/)
- **Local snapshot:** [`karolina_full.html`](karolina_full.html) (250KB HTML capture)
- **Framer export:** [`framer_export/`](framer_export/) (full static export from Framer)

### Key Design Patterns Extracted
| Pattern | Karolina's Implementation | Our Adaptation |
|---------|--------------------------|----------------|
| **Typography** | Clash Grotesk Bold + Inter + Necto Mono | Plus Jakarta Sans + Inter + JetBrains Mono |
| **Hero Layout** | Giant multi-line headline, small eyebrow meta | Same structure, "Creative Frontend Developer & Builder" |
| **Portrait** | B&W grayscale with red drop-shadow, absolute positioned | Same: grayscale filter + red shadow + floating animation |
| **Ticker** | Necto Mono tech keywords, infinite scroll | Same: marquee with tech keywords |
| **Works** | Dark featured card + bordered list items | Masonry grid cards with video mockups |
| **Approach** | 3-column grid with numbered cards | Same: 01/02/03 bento cards |
| **Skills** | Category blocks with inline tech lists | Category cards with pill clouds |
| **Contact** | Giant CTA headline + email link | Split layout: channels + contact form |
| **Availability badge** | Pinned vertical, rotated -90deg | Same with green pulse dot |
| **Color tokens** | White canvas, black type, red accent | `--color-red: #dc2626`, `--color-canvas: #fff` |

### Framer Export Fonts (in `framer_export/fonts/`)
| Font | Weight | Style | Files |
|------|--------|-------|-------|
| **Inter** | 400, 500, 600, 700 | Normal, Italic | 36 woff2 files (unicode subsets) |
| **Clash Grotesk** | 600, 700 | Normal | 2 woff2 files |
| **Necto Mono** | 400 | Normal | 1 woff2 file |

---

## 🎬 ANIMATION SYSTEM — STATUS

All animations from the Framer export have been implemented in pure CSS + vanilla JS.

### CSS Animations (`style.css` — bottom 600 lines)

| # | Animation | CSS Class | Status |
|---|-----------|-----------|--------|
| 1 | Page Load Curtain | `.page-loader` | ✅ Done |
| 2 | Header Drop Entrance | `.editorial-header` `@keyframes headerDrop` | ✅ Done |
| 3 | Hero Eyebrow Fade Up | `.hero-eyebrow` (delay 0.3s) | ✅ Done |
| 4 | Hero Title Slide Up | `.hero-title-wrap` (delay 0.5s) | ✅ Done |
| 5 | Hero Portrait Spring In | `.hero-visual-col` (spring bounce) | ✅ Done |
| 6 | Title Line Slide | `@keyframes heroTextSlide` | ✅ Done |
| 7 | Scroll Reveal (Up) | `.reveal-on-scroll` → `.revealed` | ✅ Done |
| 8 | Scroll Reveal (Left) | `.reveal-from-left` → `.revealed` | ✅ Done |
| 9 | Scroll Reveal (Right) | `.reveal-from-right` → `.revealed` | ✅ Done |
| 10 | Scroll Reveal (Scale) | `.reveal-scale-up` → `.revealed` | ✅ Done |
| 11 | Stagger Delays | `.stagger-1` through `.stagger-8` | ✅ Done |
| 12 | Text Split Word-by-Word | `.text-split-reveal .word .word-inner` | ✅ Done |
| 13 | Section Header Line Grow | `.editorial-section-header::after` | ✅ Done |
| 14 | Card Hover Lift | `.work-card:hover` (+shadow) | ✅ Done |
| 15 | Card Image Zoom | `.card-media-wrap img:hover` | ✅ Done |
| 16 | Portrait Float | `@keyframes portraitFloat` (6s) | ✅ Done |
| 17 | Ticker Marquee | `@keyframes tickerScroll` (30s) | ✅ Done |
| 18 | About Photo Clip-Path | `.about-photo-block` clip-path wipe | ✅ Done |
| 19 | Footer CTA Scale In | `.footer-hero-cta` (spring) | ✅ Done |
| 20 | Badge Slide In | `@keyframes badgeSlideIn` (1.5s delay) | ✅ Done |
| 21 | Button Press `:active` | `scale(0.95)` on all CTAs | ✅ Done |
| 22 | Magnetic Button Glow | `.magnetic-btn::after` | ✅ Done |
| 23 | Shine Sweep Badge | `@keyframes shineSweep` | ✅ Done |
| 24 | Custom Cursor Dot + Ring | `.cursor-dot`, `.cursor-ring` | ✅ Done |
| 25 | Focus Glow on Inputs | `border-color + box-shadow` | ✅ Done |
| 26 | Reduced Motion | `@media (prefers-reduced-motion)` | ✅ Done |

### JS Animation Modules (`script.js` — 18 functions)

| # | Module | Function | Status |
|---|--------|----------|--------|
| 0 | Page Loader | `initPageLoader()` | ✅ Done |
| 1 | Mobile Nav | `initMobileNav()` | ✅ Done |
| 2 | Header Scroll | `initHeaderScroll()` (rAF optimized) | ✅ Done |
| 3 | Active Nav Spy | `initActiveNavSpy()` (IntersectionObserver) | ✅ Done |
| 4 | Works Filter + Search | `initWorksFilteringAndSearch()` | ✅ Done |
| 5 | Email Copy | `initCopyEmail()` (clipboard API) | ✅ Done |
| 6 | Contact Form | `initContactForm()` (validation) | ✅ Done |
| 7 | Reel Modal | `initReelModal()` (fullscreen video) | ✅ Done |
| 8 | Scroll Reveal | `initScrollReveal()` (multi-direction + stagger) | ✅ Done |
| 9 | 3D Card Tilt | `init3DCardTilt()` (spring physics) | ✅ Done |
| 10 | Parallax Depth | `initParallax()` (hero elements) | ✅ Done |
| 11 | Magnetic Buttons | `initMagneticButtons()` (cursor attraction) | ✅ Done |
| 12 | Custom Cursor | `initCustomCursor()` (dot + ring trail) | ✅ Done |
| 13 | Smooth Anchor Scroll | `initSmoothAnchorScroll()` (header offset) | ✅ Done |
| 14 | Counter Animations | `initCounterAnimations()` (count-up) | ✅ Done |
| 15 | Text Split Reveal | `initTextSplitReveal()` (word-by-word) | ✅ Done |
| 16 | Ticker Clone | `initTickerClone()` (infinite marquee) | ✅ Done |
| 17 | Toast Notifications | `showToast()` (utility) | ✅ Done |
| 18 | Current Year | `initCurrentYear()` | ✅ Done |

---

## 📊 CURRENT STATUS

| Task | Status | Notes |
|------|--------|-------|
| Project analysis | ✅ Complete | All files reviewed, content extracted |
| Design inspiration (karolinahess.com) | ✅ Complete | Full site analyzed, patterns documented |
| Red & White editorial design prompt | ✅ Complete | Prompt generated for frontend generators |
| Main portfolio HTML (`index.html`) | ✅ Complete | 895 lines, 9 sections, SEO metadata |
| CSS design system (`style.css`) | ✅ Complete | 2500+ lines with local Clash Grotesk & Necto Mono fonts |
| JS animation engine (`script.js`) | ✅ Complete | 18 modules, spring physics, parallax, video theater |
| Framer site export (`framer_export/`) | ✅ Complete & Fixed | Appear-on-scroll state fixed; all sections 100% visible |
| Animation integration from Framer | ✅ Complete | Hero video pill, living mockups, 3D tilt, marquee |
| Browser testing & visual verification | ✅ Complete | Verified with Chromium & Playwright; screenshots confirmed |
| Deployment to GitHub Pages | 🔲 Ready | Clean build tested on localhost:5500 |

---

## 📦 EXTERNAL RESOURCES USED

### CDN Dependencies
| Resource | URL | Purpose |
|----------|-----|---------|
| Font Awesome 6.5.1 | `cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css` | Icons |
| Google Fonts | `fonts.googleapis.com` | Inter, Plus Jakarta Sans, JetBrains Mono |

### Video Assets (from framerusercontent.com)
| Video | URL | Used In |
|-------|-----|---------|
| Showreel | `nkMLRFn5SpFptEj8CoBM6JrYM34.mp4` | Hero reel pill + fullscreen modal |
| MoodScape demo | `VqdqLMybwzFPePa7dN2k4zp4To.mp4` | Featured project card |
| CashFlow demo | `4Hj42diOmSerwRZbKbPt9v9kdq8.mp4` | CashFlow work card |
| Maze Runner demo | `e9Cqe9ThJUdVFlW38wjlIgYK5U.mp4` | Maze Runner work card |

---

## 🔗 PORTFOLIO OWNER INFO

| Field | Value |
|-------|-------|
| **Name** | Ditsa Bakshi |
| **Title** | Frontend Developer & CSE Undergrad |
| **Education** | B.Tech CSE, Narula Institute of Technology, Kolkata (2024–2028) |
| **Email** | bakshiditsa@gmail.com |
| **GitHub** | [github.com/Ditsa18](https://github.com/Ditsa18) |
| **LinkedIn** | [linkedin.com/in/ditsa-bakshi-578468323](https://www.linkedin.com/in/ditsa-bakshi-578468323/) |
| **X/Twitter** | [@BakshiDitsa](https://x.com/BakshiDitsa) |
| **Phone** | +91 83899 97938 |

### Projects Showcased (7)
| # | Project | Tech | Links |
|---|---------|------|-------|
| 01 | **MoodScape** — Mental Wellness Sanctuary | React, Firebase, Web Audio API | [Live](https://moodscape-457e7.web.app/) · [Code](https://github.com/Ditsa18/MoodScape) |
| 02 | **CashFlow** — Financial Tracker | React, Vite | [Code](https://github.com/Ditsa18/REACT/tree/main/cashflow) |
| 03 | **FashionHub** — Editorial E-Commerce | HTML5, CSS3 | [Code](https://github.com/Ditsa18/HTML_CSS_JAVASCRIPT/tree/main/FashionHub) |
| 04 | **BookVerse** — Literature Discovery | JavaScript, UI/UX | [Code](https://github.com/Ditsa18/HTML_CSS_JAVASCRIPT/tree/main/BookVerse) |
| 05 | **Candy Crush** — Grid Puzzle Game | JavaScript, 2D Matrix | [Code](https://github.com/Ditsa18/JAVASCRIPT/tree/main/Candy%20Crush) |
| 06 | **Maze Runner** — Progressive Levels | JavaScript, Algorithms | [Code](https://github.com/Ditsa18/JAVASCRIPT/tree/main/Maze%20Game) |
| 07 | **SmartNotes** — Contextual Web Notes | Chrome Extension, DOM | [Code](https://github.com/Ditsa18/Browser-Extensions/tree/main/smartnotes) |

---

## 🚀 FRAMER EXPORT ENHANCEMENTS (`framer_export/index.html`)

The raw Framer export from `framerexporter-tc81qh4o7s.zip` has been fully upgraded with all Karolina Hess-inspired animations and media:

| Enhancement | Implementation | Status |
|-------------|----------------|:------:|
| **Hero Action Layout** | Clean layout with "Explore Projects" & "Download Resume [PDF]" (PLAY REEL removed per request) | ✅ Done |
| **FramerExporter Watermark** | Completely removed bootstrap script, floating badge and branding | ✅ Removed |
| **Full Stack Developer Copy** | Hero display headline: `Creative Full Stack Developer & Builder` with `Developer` in bold crimson red | ✅ Tested |
| **Moving Tech Stack Marquee** | Infinite smooth 60fps horizontal scrolling ticker with glowing red star separators (`✦`) and hover pause | ✅ Tested |
| **Red Highlighted Enlarged Animations** | Exact Framer pastel blush red (`rgb(255, 241, 242)` / `#fff1f2`) hover wash + spring scale on toolset cards, approach cards, and editorial project rows matching screen recording | ✅ Verified |
| **Living Video Mockups** | Responsive 16:9 living mockup container inside MoodScape featuring live preview (`VqdqLMybwzFPePa7dN2k4zp4To.mp4`) and pulsing red status pill | ✅ Tested |
| **3D Spring Card Tilt** | Mouse-driven perspective 3D rotation (`rotateX`, `rotateY`) on flagship MoodScape card with smooth spring reset | ✅ Tested |
| **Magnetic Buttons** | Cursor attraction on hero CTAs and primary action buttons | ✅ Tested |
| **Custom Red Cursor Trail** | Hardware-accelerated red dot (`#dc2626`) and lagging ring with hover expansion (68px) on interactive elements | ✅ Tested |
| **Scroll Reveal Animations** | Smooth staggered reveals for `#works`, `How I Work`, `Technical Toolset`, and `Closing Statement` | ✅ Tested |
| **Badge Shine Sweep** | Linear gradient shine sweep on role badges and index tags | ✅ Tested |
| **FramerExporter Syntax Fix** | Resolved syntax error in generated `framexporter-cdn-rewriter` script | ✅ Fixed |
| **Zero Console Errors** | Replaced crashing client React hydration bundle (`script_main.REW2zAW_.mjs`) with lightweight vanilla JS engine for 100% stability | ✅ 0 Errors |

---

## 🎬 VIDEO HOVER EFFECT ANALYSIS & IMPLEMENTATION
- **Source Video:** `Screen Recording 2026-09-29 055710.mp4` (~9 seconds demonstrating `second-spinosaurus-955504.framer.app/#works`)
- **Framer Motion Component Spec:** Inspected `shared-lib.BtvjrWkA.mjs` directly from Framer CDN:
  - Technical Toolset cards (`Frontend`, `Cloud & Backend`, `Programming Languages`, `Workflow`):
    - `backgroundColor: rgb(255, 241, 242)` (`#fff1f2` - soft pastel blush red)
    - `scale: 1.06` spring physics with `cubic-bezier(0.16, 1, 0.3, 1)`
    - Elevation: `box-shadow: 0 16px 36px rgba(220, 38, 38, 0.1)` with subtle red-tinted hairline border `rgba(220, 38, 38, 0.32)`
  - Approach Cards (`01 Thoughtful UI`, `02 Clean Architecture`, `03 Engineering Mindset`):
    - `backgroundColor: rgb(255, 241, 242)`, `transform: translateY(-6px) scale(1.03)`
  - Editorial Project Rows (`CashFlow`, `FashionHub`, `BookVerse`):
    - `backgroundColor: rgb(255, 241, 242)`, `transform: translateY(-3px) scale(1.02)`, padding expansion
- **Verified via Playwright:**
  - `Frontend card HOVERED background: rgb(255, 241, 242)`
  - `Cloud & Backend card HOVERED background: rgb(255, 241, 242)`
  - `Approach card HOVERED background: rgb(255, 241, 242)`
  - `CashFlow row HOVERED background: rgb(255, 241, 242)`
  - Root `index.html` skill cards also updated to match

---

## 🚧 STATUS & NEXT STEPS

- [x] Test all animations in browser with Playwright (`scratch_test_framer_screenshots.py`, `scratch_test_modal.py`, `verify_hover_effects.py`)
- [x] Implement exact video hover effect (`rgb(255, 241, 242)`) across both `framer_export/index.html` and `index.html`
- [x] Fix FramerExporter syntax error and React hydration crash
- [x] Remove PLAY REEL button and FramerExporter watermark badge completely
- [x] Build and verify Framer export with all animations (`framer_export/index.html`)
- [x] Standalone Karolina Hess-inspired site complete (`index.html`)
- [ ] Optimize images (compress fashionhub.png from 7MB)
- [ ] Add `og:image` social preview screenshot
- [ ] Deploy updated site to GitHub Pages / Vercel
- [ ] Connect contact form to actual email backend (Formspree / EmailJS)

---

> **Color Theme:** 🔴 Red `#dc2626` + 🌸 Blush Red `#fff1f2` + ⬜ White `#ffffff` + ⬛ Black `#111111`  
> **Design Inspiration:** [karolinahess.com](https://karolinahess.com/) & [second-spinosaurus-955504.framer.app](https://second-spinosaurus-955504.framer.app/)  
> **Animation Style:** Framer Motion — Spring Physics + Soft Blush Tint + Scroll Reveal + Parallax


