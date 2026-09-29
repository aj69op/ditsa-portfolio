import re

# Read clean baseline HTML
with open('framer_export/clean_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. FIX SYNTAX ERROR IN CD REWRITER
# =========================================================================
html = html.replace('return p.charAt(0)==="/")?p:', 'return (p.charAt(0)==="/")?p:')

# =========================================================================
# 2. REMOVE CRASHING CLIENT BUNDLE & EXTERNAL MODULE PRELOADS
# =========================================================================
html = re.sub(r'<script type="module"[^>]*data-framer-bundle="main"[^>]*></script>', '', html)
html = re.sub(r'<link rel="modulepreload"[^>]*>', '', html)

# =========================================================================
# 3. CLEAN UP ALL FRAMER WATERMARKS, BADGES, AND GENERATOR TAGS
# =========================================================================
# Remove Framer comments
html = html.replace('<!-- Made in Framer · framer.com ✨ -->', '')
html = re.sub(r'<!-- Published [^>]*-->', '', html)

# Remove generator and search index
html = re.sub(r'<meta name="generator" content="[^"]*">\s*', '', html)
html = re.sub(r'<meta name="framer-search-index" content="[^"]*">\s*', '', html)

# Update Title to clean brand title
html = re.sub(r'<title>.*?</title>', '<title>Ditsa Bakshi • Full Stack Developer & Builder</title>', html)

# Update SEO & Social Meta tags
html = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Portfolio of Ditsa Bakshi — Creative Full Stack Developer & Computer Science Engineering student crafting thoughtful, aesthetic, and high-performance digital experiences.">',
    html
)
html = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="Ditsa Bakshi • Full Stack Developer & Builder">',
    html
)
html = re.sub(
    r'<meta property="og:description" content="[^"]*">',
    '<meta property="og:description" content="Portfolio of Ditsa Bakshi — Creative Full Stack Developer & Builder.">',
    html
)
html = re.sub(
    r'<meta name="twitter:title" content="[^"]*">',
    '<meta name="twitter:title" content="Ditsa Bakshi • Full Stack Developer & Builder">',
    html
)
html = re.sub(
    r'<meta name="twitter:description" content="[^"]*">',
    '<meta name="twitter:description" content="Portfolio of Ditsa Bakshi — Creative Full Stack Developer & Builder.">',
    html
)
html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="./">', html)
html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="./">', html)

# Completely remove the Made in Framer badge container element
start_badge = html.find('<div id="__framer-badge-container">')
if start_badge != -1:
    end_badge = html.find('<script>var animator', start_badge)
    if end_badge != -1:
        html = html[:start_badge] + html[end_badge:]

# Remove badge CSS rules
html = re.sub(r'#__framer-badge-container\{[^}]*\}', '', html)
html = re.sub(r'@supports\s*\([^)]*\)\s*\{\s*#__framer-badge-container\{[^}]*\}\s*\}', '', html)

# Completely remove FramerExporter badge script and elements
html = re.sub(r'<script id="framerexporter-badge-bootstrap">.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<a class="framerexporter-badge"[^>]*>.*?</a>', '', html, flags=re.DOTALL)

# Remove unused editorbar styles
html = re.sub(r'<style>\s*#__framer-editorbar.*?/style>', '', html, flags=re.DOTALL)
html = re.sub(r'<style id="framerexporter-hide-framer-badge">.*?</style>', '', html, flags=re.DOTALL)

print("Cleaned up all Framer references, badges, and generator tags")

# =========================================================================
# 4. ADD FONT AWESOME IN HEAD
# =========================================================================
if 'font-awesome' not in html:
    html = html.replace('</head>', '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />\n</head>')

# =========================================================================
# 5. INJECT INTRODUCTION BLACK SCREEN CURTAIN (VIDEO 2)
# =========================================================================
intro_curtain_markup = """
<!-- Introduction Black Screen Curtain (Video 2) -->
<div id="site-intro-curtain" class="site-intro-curtain" aria-hidden="true">
  <div class="intro-brand-wrap">
    <span class="intro-brand-name">Ditsa Bakshi</span><span class="intro-brand-dot">.</span>
  </div>
</div>
"""
# Inject directly after <body> so it displays immediately on page load
html = html.replace('<body>', '<body>\n' + intro_curtain_markup)
print("Injected Introduction Black Screen Curtain (Video 2)")

# =========================================================================
# 6. INJECT AUTHENTIC MACBOOK PRO LAPTOP DEVICE PREVIEW FOR MOODSCAPE
# =========================================================================
moodscape_mockup = """
<div class="laptop-device-showcase" data-framer-name="MoodScape Laptop Device Showcase">
  <div class="laptop-mockup-container">
    <!-- MacBook Pro Display Lid -->
    <div class="macbook-screen-lid">
      <!-- Apple Camera Notch & Status Indicator -->
      <div class="macbook-camera-notch">
        <span class="macbook-camera-lens"></span>
        <span class="macbook-camera-indicator"></span>
      </div>

      <!-- In-Screen Safari / Browser Chrome -->
      <div class="macbook-browser-bar">
        <div class="macbook-browser-dots">
          <span class="m-dot m-dot-red" title="Close"></span>
          <span class="m-dot m-dot-yellow" title="Minimize"></span>
          <span class="m-dot m-dot-green" title="Expand"></span>
        </div>
        <div class="macbook-browser-url">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          <span class="macbook-url-text">moodscape-457e7.web.app</span>
        </div>
        <div class="macbook-live-tag">
          <span class="pulse-dot"></span>
          <span>LIVE SANCTUARY</span>
        </div>
      </div>

      <!-- Liquid Retina XDR Display Viewport -->
      <a href="https://moodscape-457e7.web.app" target="_blank" rel="noopener noreferrer" class="macbook-screen-link" title="Launch MoodScape Live Web Application">
        <div class="macbook-viewport">
          <img
            src="images/moodscape.png"
            alt="MoodScape - Digital Mental Wellness Sanctuary Interface Preview"
            class="macbook-screen-img"
            loading="eager"
          />
          <!-- Specular Glass Reflection Glare -->
          <div class="macbook-screen-glare"></div>
          <!-- Interactive Launch Overlay -->
          <div class="macbook-screen-overlay">
            <span class="macbook-screen-btn">
              <span>VISIT LIVE SANCTUARY</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </span>
          </div>
        </div>
      </a>
    </div>

    <!-- MacBook Dark Anodized Hinge Cylinder -->
    <div class="macbook-hinge"></div>

    <!-- MacBook Unibody Aluminum Base Chassis -->
    <div class="macbook-base-chassis">
      <div class="macbook-base-top-edge"></div>
      <!-- Iconic Centered Thumb Opening Scoop -->
      <div class="macbook-notch-indent"></div>
      <!-- Rubber Non-Slip Feet -->
      <div class="macbook-foot macbook-foot-left"></div>
      <div class="macbook-foot macbook-foot-right"></div>
    </div>

    <!-- Realistic Tabletop Contact & Ambient Drop Shadow -->
    <div class="macbook-ground-shadow"></div>
  </div>
</div>
"""
mood_pos = html.find('data-framer-name="MoodScape"')
if mood_pos != -1:
    links_pos = html.find('data-framer-name="Project Links"', mood_pos)
    if links_pos != -1:
        div_start = html.rfind('<div', mood_pos, links_pos)
        html = html[:div_start] + moodscape_mockup + '\n' + html[div_start:]
        print("Injected authentic MoodScape application interface preview")

# =========================================================================
# 7. INJECT ACTIVE MOVING TECH STACK MARQUEE
# =========================================================================
moving_tech_ticker = """
<div class="moving-tech-ticker-container" data-border="true" data-framer-name="Technology Ticker" aria-label="Technology Ticker Marquee">
  <div class="tech-ticker-track">
    <div class="tech-ticker-content">
      <span class="ticker-tech-item">REACT.JS</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">VITE</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">CLEAN ARCHITECTURE</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">FULL STACK</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">FIREBASE</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">RESPONSIVE DESIGN</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">ACCESSIBILITY</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">MOTION UI</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">JAVASCRIPT ES6+</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">NODE.JS</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">PYTHON</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">GIT &amp; GITHUB</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">WEB APPS</span><span class="ticker-red-dot">&#10022;</span>
    </div>
    <div class="tech-ticker-content" aria-hidden="true">
      <span class="ticker-tech-item">REACT.JS</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">VITE</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">CLEAN ARCHITECTURE</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">FULL STACK</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">FIREBASE</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">RESPONSIVE DESIGN</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">ACCESSIBILITY</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">MOTION UI</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">JAVASCRIPT ES6+</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">NODE.JS</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">PYTHON</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">GIT &amp; GITHUB</span><span class="ticker-red-dot">&#10022;</span>
      <span class="ticker-tech-item">WEB APPS</span><span class="ticker-red-dot">&#10022;</span>
    </div>
  </div>
</div>
"""
ticker_start = html.find('data-framer-name="Technology Ticker"')
if ticker_start != -1:
    div_start = html.rfind('<div', 0, ticker_start)
    works_pos = html.find('data-framer-name="Selected Works"')
    if works_pos != -1:
        sec_start = html.rfind('<section', 0, works_pos)
        html = html[:div_start] + moving_tech_ticker + '\n' + html[sec_start:]
        print("Replaced frozen ticker with active moving tech stack animation")

# =========================================================================
# 8. HEADLINE LINE BREAKS & RED HIGHLIGHTS (VIDEO 1)
# =========================================================================
# Format:
# Creative Full
# Stack
# Developer &
# Builder (with Developer in red)
html = html.replace(
    'Creative Full Stack<br class="framer-text">Developer &amp; Builder',
    'Creative Full<br class="framer-text">Stack<br class="framer-text"><span class="hero-accent-red">Developer</span> &amp;<br class="framer-text">Builder'
)
# Eyebrow tag:
html = html.replace(
    '[ FULL STACK DEVELOPER &amp; CSE STUDENT ]',
    '[ FULL STACK <span class="badge-accent-red">DEVELOPER</span> &amp; CSE STUDENT ]'
)
# Portrait caption:
html = html.replace(
    'DITSA BAKSHI  •  FULL STACK',
    'DITSA BAKSHI  •  <span class="badge-accent-red">FULL STACK</span>'
)
html = html.replace(
    'DITSA BAKSHI &nbsp;&bull;&nbsp; FULL STACK',
    'DITSA BAKSHI &nbsp;&bull;&nbsp; <span class="badge-accent-red">FULL STACK</span>'
)
html = html.replace(
    'DITSA BAKSHI • FULL STACK',
    'DITSA BAKSHI • <span class="badge-accent-red">FULL STACK</span>'
)

# =========================================================================
# 9. COMPLETE CSS SYSTEM (ANIMATIONS, HERO OFFSET SHADOW, INTRO CURTAIN)
# =========================================================================
custom_css = """
<style id="portfolio-premium-enhancements">
  /* --- INTRODUCTION BLACK SCREEN CURTAIN (VIDEO 2) --- */
  .site-intro-curtain {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    background-color: #000000 !important;
    z-index: 2147483647 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    pointer-events: auto !important;
    opacity: 1 !important;
    transform: translateY(0) !important;
    transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1),
                transform 0.65s cubic-bezier(0.16, 1, 0.3, 1),
                visibility 0.65s ease !important;
    visibility: visible !important;
  }
  .site-intro-curtain.hidden-intro {
    opacity: 0 !important;
    transform: translateY(-16px) !important;
    pointer-events: none !important;
    visibility: hidden !important;
  }
  .intro-brand-wrap {
    display: flex !important;
    align-items: baseline !important;
    justify-content: center !important;
    user-select: none !important;
    letter-spacing: -0.02em !important;
  }
  .intro-brand-name {
    font-family: "Clash Grotesk", "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    font-size: clamp(38px, 6vw, 68px) !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    line-height: 1 !important;
    letter-spacing: -0.03em !important;
  }
  .intro-brand-dot {
    display: inline-block !important;
    color: #dc2626 !important;
    font-family: inherit !important;
    font-size: clamp(38px, 6vw, 68px) !important;
    font-weight: 700 !important;
    line-height: 1 !important;
    margin-left: 2px !important;
    animation: intro-dot-pulse 1.4s ease-in-out infinite !important;
  }
  @keyframes intro-dot-pulse {
    0%, 100% {
      opacity: 1;
      transform: scale(1);
      text-shadow: 0 0 14px rgba(220, 38, 38, 0.9);
    }
    50% {
      opacity: 0.4;
      transform: scale(0.85);
      text-shadow: 0 0 3px rgba(220, 38, 38, 0.2);
    }
  }

  /* --- HERO ACCENT RED HIGHLIGHTS --- */
  .hero-accent-red {
    color: #dc2626 !important;
    --framer-text-color: #dc2626 !important;
    -webkit-text-fill-color: #dc2626 !important;
    display: inline-block !important;
    transition: transform 0.3s ease, text-shadow 0.3s ease !important;
  }
  .hero-accent-red:hover {
    transform: scale(1.025);
    text-shadow: 0 0 30px rgba(220, 38, 38, 0.45);
  }
  .badge-accent-red {
    color: #dc2626 !important;
    --framer-text-color: #dc2626 !important;
    -webkit-text-fill-color: #dc2626 !important;
    font-weight: 700 !important;
  }

  /* --- HERO PORTRAIT CARD EFFECT & HOVER INTERACTION (VIDEO 1) --- */
  .framer-w0ddwp,
  [data-framer-name="Ditsa Portrait"] {
    --border-color: #dc2626 !important;
    border: 1px solid #dc2626 !important;
    filter: drop-shadow(10px 10px #dc2626) !important;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                filter 0.4s cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 0.4s ease !important;
    cursor: pointer !important;
    will-change: transform, filter !important;
  }
  .framer-w0ddwp:hover,
  [data-framer-name="Ditsa Portrait"]:hover {
    transform: translate(-6px, -6px) scale(1.02) !important;
    filter: drop-shadow(18px 18px #dc2626) !important;
  }
  .framer-w0ddwp img,
  [data-framer-name="Ditsa Portrait"] img {
    filter: grayscale(100%) brightness(1.02) contrast(1.08) !important;
    transition: filter 0.4s ease, transform 0.4s ease !important;
  }
  .framer-w0ddwp:hover img,
  [data-framer-name="Ditsa Portrait"] img {
    filter: grayscale(100%) brightness(1.05) contrast(1.12) !important;
    transform: scale(1.015) !important;
  }
  .framer-2irs6v {
    background: rgba(10, 10, 12, 0.88) !important;
    backdrop-filter: blur(8px) !important;
    border-top: 1px solid rgba(220, 38, 38, 0.35) !important;
  }

  /* --- TEXT SHINE SWEEP EFFECT --- */
  @keyframes text-shine-sweep {
    0% { background-position: 150% 0; }
    100% { background-position: -150% 0; }
  }
  .shine-badge {
    background: linear-gradient(90deg, #111111 0%, #dc2626 50%, #111111 100%) !important;
    background-size: 200% 100% !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    animation: text-shine-sweep 3s cubic-bezier(0.45, 0, 0.55, 1) infinite !important;
  }

  /* --- MOVING TECH STACK MARQUEE ANIMATION --- */
  @keyframes marquee-scroll-infinite {
    0% { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(-50%, 0, 0); }
  }
  .moving-tech-ticker-container {
    overflow: hidden !important;
    position: relative !important;
    width: 100% !important;
    padding: 18px 0 !important;
    background: #ffffff !important;
    border-top: 1px solid rgba(0, 0, 0, 0.08) !important;
    border-bottom: 1px solid rgba(0, 0, 0, 0.08) !important;
    mask-image: linear-gradient(90deg, transparent 0%, black 5%, black 95%, transparent 100%) !important;
    -webkit-mask-image: linear-gradient(90deg, transparent 0%, black 5%, black 95%, transparent 100%) !important;
    display: flex !important;
    align-items: center !important;
  }
  .tech-ticker-track {
    display: flex !important;
    width: max-content !important;
    animation: marquee-scroll-infinite 25s linear infinite !important;
    will-change: transform !important;
  }
  .moving-tech-ticker-container:hover .tech-ticker-track {
    animation-play-state: paused !important;
  }
  .tech-ticker-content {
    display: flex !important;
    align-items: center !important;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
  }
  .ticker-tech-item {
    font-family: "Necto Mono", monospace !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    color: #111111 !important;
    padding: 6px 14px !important;
    border-radius: 6px !important;
    cursor: default !important;
    transition: color 0.25s ease, transform 0.25s ease, background-color 0.25s ease !important;
  }
  .ticker-tech-item:hover {
    color: #dc2626 !important;
    background-color: rgba(220, 38, 38, 0.08) !important;
    transform: scale(1.12) !important;
  }
  .ticker-red-dot {
    color: #dc2626 !important;
    font-size: 10px !important;
    margin: 0 16px !important;
    display: inline-block !important;
    text-shadow: 0 0 10px rgba(220, 38, 38, 0.8) !important;
    animation: pulse-red-glow 2s infinite ease-in-out !important;
  }
  @keyframes pulse-red-glow {
    0%, 100% { opacity: 0.7; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.3); text-shadow: 0 0 14px #dc2626; }
  }

  /* --- AUTHENTIC MACBOOK PRO LAPTOP DEVICE PREVIEW --- */
  .laptop-device-showcase {
    position: relative !important;
    width: 100% !important;
    margin: 40px 0 28px 0 !important;
    display: flex !important;
    justify-content: center !important;
  }
  .laptop-mockup-container {
    position: relative !important;
    width: 100% !important;
    max-width: 960px !important;
    perspective: 1600px !important;
    transform-style: preserve-3d !important;
    transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }
  .laptop-mockup-container:hover {
    transform: translateY(-6px) rotateX(1.5deg) !important;
  }

  /* MacBook Top Display Lid (Screen Bezel) */
  .macbook-screen-lid {
    position: relative !important;
    background: #0d0d0f !important;
    border-radius: 20px 20px 0 0 !important;
    padding: 12px 14px 0 14px !important;
    border: 2px solid #27272a !important;
    border-bottom: 2px solid #18181b !important;
    box-shadow: 0 0 0 1px #18181b,
                inset 0 1px 1px rgba(255, 255, 255, 0.22),
                0 30px 70px rgba(0, 0, 0, 0.95),
                0 0 45px rgba(220, 38, 38, 0.18) !important;
    overflow: hidden !important;
    transition: border-color 0.35s ease, box-shadow 0.35s ease !important;
  }
  .laptop-mockup-container:hover .macbook-screen-lid {
    border-color: rgba(220, 38, 38, 0.55) !important;
    box-shadow: 0 0 0 1px rgba(220, 38, 38, 0.45),
                inset 0 1px 1px rgba(255, 255, 255, 0.3),
                0 35px 90px rgba(0, 0, 0, 0.98),
                0 0 55px rgba(220, 38, 38, 0.35) !important;
  }

  /* Camera Notch Bezel & Live Indicator */
  .macbook-camera-notch {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 8px !important;
    padding-bottom: 8px !important;
  }
  .macbook-camera-lens {
    width: 7px !important;
    height: 7px !important;
    background: #18181b !important;
    border: 1px solid #3f3f46 !important;
    border-radius: 50% !important;
    display: inline-block !important;
    box-shadow: inset 0 0 2px #000000 !important;
    position: relative !important;
  }
  .macbook-camera-lens::after {
    content: "" !important;
    position: absolute !important;
    top: 1px !important;
    left: 1px !important;
    width: 2.5px !important;
    height: 2.5px !important;
    background: #38bdf8 !important;
    border-radius: 50% !important;
    opacity: 0.75 !important;
  }
  .macbook-camera-indicator {
    width: 3.5px !important;
    height: 3.5px !important;
    background: #22c55e !important;
    border-radius: 50% !important;
    display: inline-block !important;
    box-shadow: 0 0 4px #22c55e !important;
    opacity: 0.8 !important;
  }

  /* Browser Bar inside MacBook Screen */
  .macbook-browser-bar {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 9px 16px !important;
    background: #18181b !important;
    border-radius: 8px 8px 0 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    user-select: none !important;
  }
  .macbook-browser-dots {
    display: flex !important;
    align-items: center !important;
    gap: 7px !important;
  }
  .m-dot {
    width: 10px !important;
    height: 10px !important;
    border-radius: 50% !important;
    display: inline-block !important;
    box-shadow: inset 0 1px 1px rgba(255,255,255,0.25) !important;
  }
  .m-dot-red { background: #ef4444 !important; border: 1px solid #dc2626 !important; }
  .m-dot-yellow { background: #f59e0b !important; border: 1px solid #d97706 !important; }
  .m-dot-green { background: #10b981 !important; border: 1px solid #059669 !important; }

  .macbook-browser-url {
    display: flex !important;
    align-items: center !important;
    gap: 7px !important;
    background: rgba(0, 0, 0, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 6px !important;
    padding: 4px 16px !important;
    font-family: "Necto Mono", monospace !important;
    font-size: 11px !important;
    color: #e4e4e7 !important;
    letter-spacing: 0.3px !important;
  }
  .macbook-live-tag {
    display: flex !important;
    align-items: center !important;
    gap: 6px !important;
    font-family: "Necto Mono", monospace !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    color: #fca5a5 !important;
    letter-spacing: 0.8px !important;
  }

  /* Audio Wave Visualizer Bars */
  .sound-wave-bars {
    display: inline-flex !important;
    align-items: flex-end !important;
    gap: 2px !important;
    height: 11px !important;
    margin: 0 3px !important;
  }
  .sw-bar {
    width: 2px !important;
    background-color: #22c55e !important;
    border-radius: 1px !important;
    animation: sw-bounce 1.2s ease-in-out infinite !important;
  }
  .sw-bar:nth-child(1) { height: 40%; animation-delay: 0.1s !important; }
  .sw-bar:nth-child(2) { height: 90%; animation-delay: 0.3s !important; }
  .sw-bar:nth-child(3) { height: 60%; animation-delay: 0.2s !important; }
  .sw-bar:nth-child(4) { height: 100%; animation-delay: 0.4s !important; }

  @keyframes sw-bounce {
    0%, 100% { transform: scaleY(0.3); }
    50% { transform: scaleY(1); }
  }

  /* Retina Display Viewport */
  .macbook-screen-link {
    display: block !important;
    text-decoration: none !important;
    cursor: pointer !important;
  }
  .macbook-viewport {
    position: relative !important;
    width: 100% !important;
    max-height: 500px !important;
    background: #000000 !important;
    overflow: hidden !important;
    line-height: 0 !important;
  }
  .macbook-screen-img {
    width: 100% !important;
    height: auto !important;
    max-height: 500px !important;
    object-fit: cover !important;
    object-position: top center !important;
    display: block !important;
    transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease !important;
  }
  .laptop-mockup-container:hover .macbook-screen-img {
    transform: scale(1.02) !important;
  }

  /* Glare Overlay with Active Specular Sweep */
  @keyframes screen-specular-sweep {
    0% { transform: translateX(-150%) rotate(25deg); }
    30% { transform: translateX(250%) rotate(25deg); }
    100% { transform: translateX(250%) rotate(25deg); }
  }
  .macbook-screen-glare {
    position: absolute !important;
    inset: 0 !important;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.09) 0%, rgba(255, 255, 255, 0) 50%, rgba(0, 0, 0, 0.15) 100%) !important;
    pointer-events: none !important;
    overflow: hidden !important;
    z-index: 2 !important;
  }
  .macbook-screen-glare::after {
    content: "" !important;
    position: absolute !important;
    top: -50% !important;
    left: 0 !important;
    width: 60% !important;
    height: 200% !important;
    background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.18) 50%, transparent 100%) !important;
    animation: screen-specular-sweep 7s cubic-bezier(0.4, 0, 0.2, 1) infinite !important;
    pointer-events: none !important;
  }

  /* Hover Launch CTA */
  .macbook-screen-overlay {
    position: absolute !important;
    inset: 0 !important;
    background: linear-gradient(180deg, rgba(0, 0, 0, 0) 40%, rgba(0, 0, 0, 0.8) 100%) !important;
    opacity: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: opacity 0.3s ease !important;
    z-index: 3 !important;
    pointer-events: none !important;
  }
  .laptop-mockup-container:hover .macbook-screen-overlay {
    opacity: 1 !important;
  }
  .macbook-screen-btn {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    background: #dc2626 !important;
    color: #ffffff !important;
    font-family: "Necto Mono", monospace !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    padding: 11px 26px !important;
    border-radius: 999px !important;
    box-shadow: 0 8px 25px rgba(220, 38, 38, 0.75) !important;
    transform: translateY(12px) !important;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }
  .laptop-mockup-container:hover .macbook-screen-btn {
    transform: translateY(0) !important;
  }

  /* MacBook Dark Anodized Hinge */
  .macbook-hinge {
    position: relative !important;
    width: 38% !important;
    height: 5px !important;
    margin: 0 auto !important;
    background: linear-gradient(180deg, #18181b 0%, #09090b 100%) !important;
    border-radius: 0 0 3px 3px !important;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.9) !important;
    z-index: 4 !important;
  }

  /* MacBook Lower Aluminum Chassis / Base */
  .macbook-base-chassis {
    position: relative !important;
    width: calc(100% + 56px) !important;
    left: -28px !important;
    height: 20px !important;
    background: linear-gradient(180deg, #e4e4e7 0%, #d4d4d8 15%, #a1a1aa 45%, #71717a 80%, #3f3f46 100%) !important;
    border-radius: 0 0 18px 18px !important;
    box-shadow: inset 0 2px 0 rgba(255, 255, 255, 0.95),
                inset 0 -1px 1px rgba(0, 0, 0, 0.6),
                0 8px 25px rgba(0, 0, 0, 0.75) !important;
    z-index: 5 !important;
    display: flex !important;
    justify-content: center !important;
    align-items: flex-start !important;
  }
  .macbook-base-top-edge {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    height: 2px !important;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.95) 20%, rgba(255, 255, 255, 0.95) 80%, rgba(255, 255, 255, 0.1) 100%) !important;
  }

  /* MacBook Thumb Opening Scoop Notch */
  .macbook-notch-indent {
    position: relative !important;
    width: 110px !important;
    height: 7px !important;
    background: #3f3f46 !important;
    border-radius: 0 0 8px 8px !important;
    box-shadow: inset 0 2px 3px rgba(0, 0, 0, 0.8),
                0 1px 0 rgba(255, 255, 255, 0.4) !important;
  }

  /* Rubber Non-Slip Feet */
  .macbook-foot {
    position: absolute !important;
    bottom: -2px !important;
    width: 45px !important;
    height: 3px !important;
    background: #18181b !important;
    border-radius: 0 0 3px 3px !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.8) !important;
  }
  .macbook-foot-left { left: 40px !important; }
  .macbook-foot-right { right: 40px !important; }

  /* Soft Tabletop Drop Shadow */
  .macbook-ground-shadow {
    position: relative !important;
    width: calc(100% + 80px) !important;
    left: -40px !important;
    height: 28px !important;
    background: radial-gradient(ellipse at 50% 0%, rgba(0, 0, 0, 0.85) 0%, rgba(0, 0, 0, 0.35) 45%, transparent 75%) !important;
    filter: blur(5px) !important;
    margin-top: -3px !important;
  }
  .pulse-dot {
    width: 6px;
    height: 6px;
    background-color: #dc2626;
    border-radius: 50%;
    box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.8);
    animation: pulse-dot 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
  }
  @keyframes pulse-dot {
    0% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.8); }
    70% { box-shadow: 0 0 0 6px rgba(220, 38, 38, 0); }
    100% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }
  }

  /* --- 3D PERSPECTIVE TILT --- */
  article[data-framer-name], .framer-1oihuq7, .framer-1s6g76x > article {
    transform-style: preserve-3d;
    will-change: transform;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.3s ease !important;
  }

  /* --- RED HIGHLIGHTED ENLARGED ANIMATIONS --- */

  /* 1. Project Editorial Rows: CashFlow, FashionHub, BookVerse - Blush Red Hover Effect */
  .framer-60vxi,
  .framer-1ogu2fg,
  .framer-1v4okuu,
  article[data-framer-name="CashFlow"],
  article[data-framer-name="FashionHub"],
  article[data-framer-name="BookVerse"] {
    transition: background-color 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                transform 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                border-color 0.3s ease,
                padding 0.3s ease !important;
    cursor: pointer !important;
    position: relative !important;
    border-radius: 8px !important;
  }
  .framer-60vxi:hover,
  .framer-1ogu2fg:hover,
  .framer-1v4okuu:hover,
  article[data-framer-name="CashFlow"]:hover,
  article[data-framer-name="FashionHub"]:hover,
  article[data-framer-name="BookVerse"]:hover {
    background-color: rgb(255, 241, 242) !important; /* Framer exact pastel blush red #fff1f2 */
    transform: translateY(-3px) scale(1.02) !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
    border-color: rgba(220, 38, 38, 0.35) !important;
    box-shadow: 0 14px 35px rgba(220, 38, 38, 0.1) !important;
    z-index: 10 !important;
  }
  .framer-60vxi:hover h2,
  .framer-60vxi:hover h3,
  .framer-1ogu2fg:hover h2,
  .framer-1ogu2fg:hover h3,
  .framer-1v4okuu:hover h2,
  .framer-1v4okuu:hover h3,
  article[data-framer-name="CashFlow"]:hover h2,
  article[data-framer-name="CashFlow"]:hover h3,
  article[data-framer-name="FashionHub"]:hover h2,
  article[data-framer-name="FashionHub"]:hover h3,
  article[data-framer-name="BookVerse"]:hover h2,
  article[data-framer-name="BookVerse"]:hover h3 {
    color: #dc2626 !important;
    -webkit-text-fill-color: #dc2626 !important;
    transition: color 0.25s ease !important;
  }
  .framer-60vxi:hover [data-framer-name="Index"] p,
  .framer-1ogu2fg:hover [data-framer-name="Index"] p,
  .framer-1v4okuu:hover [data-framer-name="Index"] p,
  article[data-framer-name="CashFlow"]:hover [data-framer-name="Index"] p,
  article[data-framer-name="FashionHub"]:hover [data-framer-name="Index"] p,
  article[data-framer-name="BookVerse"]:hover [data-framer-name="Index"] p {
    color: #dc2626 !important;
    -webkit-text-fill-color: #dc2626 !important;
    font-weight: 800 !important;
    transform: scale(1.15) !important;
    transform-origin: left center;
    transition: transform 0.25s ease, color 0.25s ease !important;
  }

  /* 2. Flagship Project Card: MoodScape */
  .framer-1ll5si8,
  article[data-framer-name="MoodScape"] {
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                border-color 0.3s ease !important;
    cursor: pointer !important;
  }
  .framer-1ll5si8:hover,
  article[data-framer-name="MoodScape"]:hover {
    transform: scale(1.015) translateY(-4px) !important;
    border-color: #dc2626 !important;
    box-shadow: 0px 18px 45px 0px rgba(17, 17, 17, 0.25), 0 0 35px rgba(220, 38, 38, 0.25) !important;
    z-index: 10 !important;
  }
  .framer-1fo0jvx,
  [data-framer-name="Project Links"] {
    display: flex !important;
    gap: 16px !important;
    margin-top: 18px !important;
    padding-bottom: 6px !important;
    flex-wrap: wrap !important;
  }
  .framer-1ly5ore a,
  .framer-simn5p a {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    padding: 10px 22px !important;
    border-radius: 8px !important;
    font-family: "Necto Mono", monospace !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px !important;
    text-decoration: none !important;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease !important;
  }
  .framer-1ly5ore a {
    background: #dc2626 !important;
    color: #ffffff !important;
    box-shadow: 0 4px 18px rgba(220, 38, 38, 0.4) !important;
    border: 1px solid #dc2626 !important;
  }
  .framer-1ly5ore a:hover {
    background: #b91c1c !important;
    transform: translateY(-2px) scale(1.03) !important;
    box-shadow: 0 8px 25px rgba(220, 38, 38, 0.6) !important;
  }
  .framer-simn5p a {
    background: rgba(255, 255, 255, 0.08) !important;
    color: #e4e4e7 !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
  }
  .framer-simn5p a:hover {
    background: rgba(255, 255, 255, 0.16) !important;
    color: #ffffff !important;
    border-color: rgba(220, 38, 38, 0.6) !important;
    transform: translateY(-2px) scale(1.03) !important;
  }

  /* 3. Approach / How I Work Bento Cards - Blush Red Tint & Spring Elevation */
  .framer-6c09oy,
  .framer-1nbv2f4,
  .framer-1eg8tbm,
  [data-framer-name="01 Thoughtful UI"],
  [data-framer-name="02 Clean Architecture"],
  [data-framer-name="03 Engineering Mindset"] {
    background-color: #ffffff;
    transition: background-color 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                transform 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1),
                border-color 0.3s ease !important;
    cursor: pointer !important;
    border-radius: 12px !important;
    position: relative !important;
    z-index: 1;
  }
  .framer-6c09oy:hover,
  .framer-1nbv2f4:hover,
  .framer-1eg8tbm:hover,
  [data-framer-name="01 Thoughtful UI"]:hover,
  [data-framer-name="02 Clean Architecture"]:hover,
  [data-framer-name="03 Engineering Mindset"]:hover {
    background-color: rgb(255, 241, 242) !important; /* Framer exact pastel blush red #fff1f2 */
    transform: translateY(-6px) scale(1.03) !important;
    border-color: rgba(220, 38, 38, 0.35) !important;
    box-shadow: 0 18px 40px rgba(220, 38, 38, 0.12), 0 2px 8px rgba(0, 0, 0, 0.04) !important;
    z-index: 10 !important;
  }
  .framer-6c09oy:hover [data-framer-name="Number"] p,
  .framer-1nbv2f4:hover [data-framer-name="Number"] p,
  .framer-1eg8tbm:hover [data-framer-name="Number"] p,
  [data-framer-name="01 Thoughtful UI"]:hover [data-framer-name="Number"] p,
  [data-framer-name="02 Clean Architecture"]:hover [data-framer-name="Number"] p,
  [data-framer-name="03 Engineering Mindset"]:hover [data-framer-name="Number"] p {
    color: #dc2626 !important;
    -webkit-text-fill-color: #dc2626 !important;
    font-weight: 800 !important;
    transform: scale(1.15) !important;
    transform-origin: left center;
    transition: all 0.3s ease !important;
  }
  .framer-6c09oy:hover [data-framer-name="Title"] h3,
  .framer-1nbv2f4:hover [data-framer-name="Title"] h3,
  .framer-1eg8tbm:hover [data-framer-name="Title"] h3,
  [data-framer-name="01 Thoughtful UI"]:hover [data-framer-name="Title"] h3,
  [data-framer-name="02 Clean Architecture"]:hover [data-framer-name="Title"] h3,
  [data-framer-name="03 Engineering Mindset"]:hover [data-framer-name="Title"] h3 {
    color: #dc2626 !important;
    -webkit-text-fill-color: #dc2626 !important;
    transition: color 0.3s ease !important;
  }

  /* 4. Technical Toolset Bento Cards - Blush Red Tint + Spring Scale */
  .framer-2ms4ce,
  .framer-1g8dimx,
  .framer-1vp6lp5,
  .framer-1dvgglq,
  [data-framer-name="Frontend"],
  [data-framer-name^="Cloud"],
  [data-framer-name="Programming Languages"],
  [data-framer-name="Workflow"] {
    background-color: #ffffff;
    transition: background-color 0.32s cubic-bezier(0.16, 1, 0.3, 1),
                transform 0.32s cubic-bezier(0.16, 1, 0.3, 1),
                box-shadow 0.32s cubic-bezier(0.16, 1, 0.3, 1),
                border-color 0.3s ease !important;
    cursor: pointer !important;
    position: relative !important;
    border-radius: 8px !important;
    z-index: 1;
  }
  .framer-2ms4ce:hover,
  .framer-1g8dimx:hover,
  .framer-1vp6lp5:hover,
  .framer-1dvgglq:hover,
  [data-framer-name="Frontend"]:hover,
  [data-framer-name^="Cloud"]:hover,
  [data-framer-name="Programming Languages"]:hover,
  [data-framer-name="Workflow"]:hover {
    background-color: rgb(255, 241, 242) !important; /* Framer exact pastel blush red #fff1f2 */
    transform: scale(1.06) !important;
    box-shadow: 0 16px 36px rgba(220, 38, 38, 0.1), 0 2px 8px rgba(0, 0, 0, 0.04) !important;
    border-color: rgba(220, 38, 38, 0.32) !important;
    z-index: 10 !important;
  }

  /* 5. CTAs & Capsule Buttons Enlargement */
  a[data-framer-name="Explore Projects"]:hover,
  a[data-framer-name="Let’s Talk"]:hover,
  a[data-reset="button"]:hover,
  button[data-reset="button"]:hover {
    transform: scale(1.07) translateY(-3px) !important;
    border-color: #dc2626 !important;
    box-shadow: 0 12px 35px rgba(220, 38, 38, 0.35) !important;
  }

  /* 6. CUSTOM CURSOR TRAIL WITH EXPANDED RED AURA */
  .cursor-dot {
    position: fixed;
    width: 8px;
    height: 8px;
    background: #dc2626;
    border-radius: 50%;
    pointer-events: none;
    z-index: 999998;
    mix-blend-mode: difference;
    transform: translate(-50%, -50%);
    transition: transform 0.08s ease-out;
  }
  .cursor-ring {
    position: fixed;
    width: 36px;
    height: 36px;
    border: 1.5px solid #dc2626;
    border-radius: 50%;
    pointer-events: none;
    z-index: 999997;
    mix-blend-mode: difference;
    transform: translate(-50%, -50%);
    transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1), height 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease, background 0.3s ease;
  }
  .cursor-ring.hovering {
    width: 68px !important;
    height: 68px !important;
    border-width: 2px !important;
    border-color: #dc2626 !important;
    background: rgba(220, 38, 38, 0.12) !important;
    box-shadow: 0 0 25px rgba(220, 38, 38, 0.5) !important;
  }
  @media (pointer: coarse) {
    .cursor-dot, .cursor-ring { display: none !important; }
  }

  /* --- SCROLL REVEAL SMOOTH TRANSITIONS --- */
  [data-framer-name="Selected Works"],
  [data-framer-name="How I Work"],
  [data-framer-name="Technical Toolset"],
  [data-framer-name="Closing Statement"],
  article[data-framer-name] {
    transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
                transform 0.8s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }

  /* --- BUTTON PRESS MICRO-INTERACTIONS --- */
  button:active, a[data-reset="button"]:active {
    transform: scale(0.96) !important;
  }
</style>
"""

# Inject custom CSS into head
html = html.replace('</head>', custom_css + '\n</head>')

# =========================================================================
# 10. INJECT CURSOR MARKUP BEFORE </body>
# =========================================================================
cursor_markup = """
<!-- Custom Cursor Trail -->
<div class="cursor-dot" id="cursor-dot"></div>
<div class="cursor-ring" id="cursor-ring"></div>
"""

# =========================================================================
# 11. INJECT COMPLETE JAVASCRIPT ANIMATION & INTERACTION ENGINE
# =========================================================================
interactive_script = """
<script id="portfolio-interaction-engine">
(function() {
  // --- 0. Introduction Black Screen Curtain Controller (Video 2) ---
  const curtain = document.getElementById("site-intro-curtain");
  if (curtain) {
    // Show black screen for 1 second, then smoothly transition out
    setTimeout(function() {
      curtain.classList.add("hidden-intro");
      setTimeout(function() {
        if (curtain && curtain.parentNode) {
          curtain.parentNode.removeChild(curtain);
        }
      }, 700);
    }, 1000);
  }

  // --- 1. Reveal All Sections Smoothly ---
  function revealSections() {
    const sections = document.querySelectorAll('[data-framer-name="Selected Works"], [data-framer-name="How I Work"], [data-framer-name="Technical Toolset"], [data-framer-name="Closing Statement"], article[data-framer-name]');
    sections.forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
  }
  revealSections();
  window.addEventListener('DOMContentLoaded', revealSections);
  window.addEventListener('load', revealSections);
  setTimeout(revealSections, 300);
  setTimeout(revealSections, 1000);

  // --- 2. 3D Spring Card Tilt for MoodScape & Laptop Showcase ---
  if (!window.matchMedia("(pointer: coarse)").matches) {
    const laptopContainers = document.querySelectorAll('.laptop-mockup-container');
    laptopContainers.forEach(container => {
      container.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        const rotateX = (-y / (rect.height / 2)) * 4;
        const rotateY = (x / (rect.width / 2)) * 5;
        container.style.transform = `scale(1.02) translateY(-6px) perspective(1200px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        container.style.transition = 'none';
      });
      container.addEventListener('mouseleave', () => {
        container.style.transform = 'scale(1) translateY(0px) perspective(1200px) rotateX(0deg) rotateY(0deg)';
        container.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      });
    });
  }

  // --- 3. Custom Cursor Trail with Enlarging Hover Aura ---
  if (!window.matchMedia("(pointer: coarse)").matches) {
    const dot = document.getElementById("cursor-dot");
    const ring = document.getElementById("cursor-ring");
    let mouseX = -100, mouseY = -100;
    let ringX = -100, ringY = -100;

    window.addEventListener("mousemove", (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (dot) {
        dot.style.left = `${mouseX}px`;
        dot.style.top = `${mouseY}px`;
      }
    });

    function updateRing() {
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;
      if (ring) {
        ring.style.left = `${ringX}px`;
        ring.style.top = `${ringY}px`;
      }
      requestAnimationFrame(updateRing);
    }
    requestAnimationFrame(updateRing);

    const clickables = document.querySelectorAll("a, button, [role='button'], input, article[data-framer-name], .framer-w0ddwp, [data-framer-name='Ditsa Portrait'], [data-framer-name*='0'], .framer-2ms4ce, .framer-1g8dimx, .framer-1vp6lp5, .framer-1dvgglq, [data-framer-name='Frontend'], [data-framer-name^='Cloud'], [data-framer-name='Programming Languages'], [data-framer-name='Workflow'], .ticker-tech-item");
    clickables.forEach((el) => {
      el.addEventListener("mouseenter", () => ring && ring.classList.add("hovering"));
      el.addEventListener("mouseleave", () => ring && ring.classList.remove("hovering"));
    });
  }

  // --- 4. Magnetic Attraction on Buttons ---
  const magneticBtns = document.querySelectorAll("a[data-reset='button'], button[data-reset='button']");
  magneticBtns.forEach(btn => {
    btn.addEventListener("mousemove", (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - (rect.left + rect.width / 2);
      const y = e.clientY - (rect.top + rect.height / 2);
      btn.style.transform = `translate(${x * 0.22}px, ${y * 0.22}px)`;
    });
    btn.addEventListener("mouseleave", () => {
      btn.style.transform = "translate(0px, 0px)";
      btn.style.transition = "transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)";
    });
  });

  // --- 5. Add Shine Badge to Role Index ---
  const roleEl = document.querySelector('[data-framer-name="Role Index"] p');
  if (roleEl) {
    roleEl.classList.add("shine-badge");
  }
})();
</script>
"""

html = html.replace('</body>', cursor_markup + '\n' + interactive_script + '\n</body>')

with open('framer_export/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully written fully enhanced framer_export/index.html with Video 1 portrait effect, Video 2 black screen curtain, and zero Framer branding!")
