/**
 * DITSA BAKSHI — KAROLINA HESS FRAMER MOTION ANIMATION ENGINE
 * Full-spectrum animation system: page loader, scroll reveals with stagger,
 * text split word-by-word, parallax depth, magnetic buttons, custom cursor,
 * smooth counters, spring 3D tilt, ticker marquee, and more.
 */

document.addEventListener("DOMContentLoaded", () => {
  initPageLoader();
  initMobileNav();
  initHeaderScroll();
  initWorksFilteringAndSearch();
  initCopyEmail();
  initContactForm();
  initCurrentYear();
  initActiveNavSpy();
  initReelModal();
  initScrollReveal();
  init3DCardTilt();
  initParallax();
  initMagneticButtons();
  initCustomCursor();
  initSmoothAnchorScroll();
  initCounterAnimations();
  initTextSplitReveal();
  initTickerClone();
});

/* ==========================================================================
   0. PAGE LOADER — CINEMATIC ENTRANCE CURTAIN
   ========================================================================== */
function initPageLoader() {
  // Create loader element
  const loader = document.createElement("div");
  loader.classList.add("page-loader");
  loader.innerHTML = `<div class="loader-brand">Ditsa Bakshi<span class="red-dot"></span></div>`;
  document.body.prepend(loader);
  document.body.classList.add("loading");

  window.addEventListener("load", () => {
    setTimeout(() => {
      loader.classList.add("loaded");
      document.body.classList.remove("loading");
      // Remove loader from DOM after transition
      setTimeout(() => loader.remove(), 800);
    }, 1200);
  });
}

/* ==========================================================================
   1. MOBILE NAVIGATION
   ========================================================================== */
function initMobileNav() {
  const hamburger = document.getElementById("hamburger-btn");
  const navMenu = document.getElementById("nav-menu");

  if (!hamburger || !navMenu) return;

  hamburger.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("active");
    hamburger.classList.toggle("active");
    hamburger.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });

  // Close nav on click outside or on a link
  navMenu.querySelectorAll(".nav-item").forEach((link) => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("active");
      hamburger.classList.remove("active");
      hamburger.setAttribute("aria-expanded", "false");
    });
  });
}

/* ==========================================================================
   2. HEADER SCROLL SHADOW + BLUR
   ========================================================================== */
function initHeaderScroll() {
  const header = document.getElementById("editorial-header");
  if (!header) return;

  let ticking = false;
  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        if (window.scrollY > 30) {
          header.classList.add("scrolled");
        } else {
          header.classList.remove("scrolled");
        }
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}

/* ==========================================================================
   3. ACTIVE NAV LINK ON SCROLL (INTERSECTION OBSERVER BASED)
   ========================================================================== */
function initActiveNavSpy() {
  const sections = document.querySelectorAll("section[id], footer[id]");
  const navLinks = document.querySelectorAll(".nav-menu .nav-item");

  if (!sections.length || !navLinks.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute("id");
        navLinks.forEach((link) => {
          link.classList.remove("active");
          if (link.getAttribute("href") === `#${id}`) {
            link.classList.add("active");
          }
        });
      }
    });
  }, {
    threshold: 0.2,
    rootMargin: "-80px 0px -40% 0px"
  });

  sections.forEach((section) => observer.observe(section));
}

/* ==========================================================================
   4. WORKS FILTERING & LIVE SEARCH
   ========================================================================== */
function initWorksFilteringAndSearch() {
  const filterBtns = document.querySelectorAll(".cat-tab-btn");
  const searchInput = document.getElementById("works-search-input");
  const clearBtn = document.getElementById("clear-search-btn");
  const featuredCard = document.getElementById("featured-moodscape");
  const workCards = document.querySelectorAll(".work-card");
  const noResults = document.getElementById("no-search-results");
  const resetBtn = document.getElementById("reset-search-btn");

  let activeFilter = "all";
  let searchQuery = "";

  function applyFilters() {
    let visibleCount = 0;
    const query = searchQuery.trim().toLowerCase();

    // 1. Featured card check
    if (featuredCard) {
      const category = featuredCard.getAttribute("data-category") || "";
      const title = (featuredCard.getAttribute("data-title") || "").toLowerCase();
      const content = featuredCard.textContent.toLowerCase();

      const matchesFilter = activeFilter === "all" || category.includes(activeFilter);
      const matchesSearch = !query || title.includes(query) || content.includes(query);

      if (matchesFilter && matchesSearch) {
        featuredCard.style.display = "block";
        visibleCount++;
      } else {
        featuredCard.style.display = "none";
      }
    }

    // 2. Regular work cards check
    workCards.forEach((card) => {
      const category = card.getAttribute("data-category") || "";
      const title = (card.getAttribute("data-title") || "").toLowerCase();
      const content = card.textContent.toLowerCase();

      const matchesFilter = activeFilter === "all" || category.includes(activeFilter);
      const matchesSearch = !query || title.includes(query) || content.includes(query);

      if (matchesFilter && matchesSearch) {
        card.style.display = "flex";
        visibleCount++;
      } else {
        card.style.display = "none";
      }
    });

    // 3. No results state
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? "block" : "none";
    }
  }

  // Filter Buttons Click
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      activeFilter = btn.getAttribute("data-filter") || "all";
      applyFilters();
    });
  });

  // Search Input
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value;
      if (clearBtn) {
        clearBtn.style.display = searchQuery ? "block" : "none";
      }
      applyFilters();
    });
  }

  // Clear Search
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (searchInput) searchInput.value = "";
      searchQuery = "";
      clearBtn.style.display = "none";
      applyFilters();
      if (searchInput) searchInput.focus();
    });
  }

  // Reset Filters Button
  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      activeFilter = "all";
      searchQuery = "";
      if (searchInput) searchInput.value = "";
      if (clearBtn) clearBtn.style.display = "none";
      filterBtns.forEach((b) => {
        b.classList.toggle("active", b.getAttribute("data-filter") === "all");
      });
      applyFilters();
    });
  }
}

/* ==========================================================================
   5. ONE-CLICK EMAIL COPY
   ========================================================================== */
function initCopyEmail() {
  const copyButtons = [
    document.getElementById("hero-copy-email"),
    document.getElementById("footer-copy-email")
  ];

  copyButtons.forEach((btn) => {
    if (!btn) return;
    btn.addEventListener("click", () => {
      const email = btn.getAttribute("data-email") || "bakshiditsa@gmail.com";
      navigator.clipboard.writeText(email).then(() => {
        showToast("Email copied to clipboard: " + email);
      }).catch(() => {
        // Fallback
        const tempInput = document.createElement("input");
        tempInput.value = email;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
        showToast("Email copied to clipboard: " + email);
      });
    });
  });
}

/* ==========================================================================
   6. CONTACT FORM SUBMISSION
   ========================================================================== */
function initContactForm() {
  const form = document.getElementById("contact-form");
  const submitBtn = document.getElementById("submit-btn");

  if (!form || !submitBtn) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = document.getElementById("form-name").value.trim();
    const email = document.getElementById("form-email").value.trim();
    const message = document.getElementById("form-message").value.trim();

    if (!name || !email || !message) {
      showToast("Please fill in your name, email, and message.", "warning");
      return;
    }

    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      showToast("Please provide a valid email address.", "warning");
      return;
    }

    // Visual loading state
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<span>Sending Message...</span> <i class="fa-solid fa-spinner fa-spin"></i>';
    submitBtn.disabled = true;

    // Simulate reliable dispatch
    setTimeout(() => {
      submitBtn.innerHTML = originalText;
      submitBtn.disabled = false;
      form.reset();
      showToast("Thank you, " + name + "! Your note has been dispatched.", "success");
    }, 900);
  });
}

/* ==========================================================================
   7. FULLSCREEN SHOWREEL MODAL (KAROLINA HESS REEL PLAYER)
   ========================================================================== */
function initReelModal() {
  const openBtn = document.getElementById("open-reel-btn");
  const modal = document.getElementById("reel-modal");
  const closeBtn = document.getElementById("close-reel-btn");
  const backdrop = document.getElementById("close-reel-backdrop");
  const modalVideo = document.getElementById("modal-video-player");

  if (!openBtn || !modal) return;

  function openReel() {
    modal.classList.add("active");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    if (modalVideo) {
      modalVideo.currentTime = 0;
      modalVideo.play().catch(e => console.log('Autoplay blocked:', e));
    }
  }

  function closeReel() {
    modal.classList.remove("active");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (modalVideo) {
      modalVideo.pause();
    }
  }

  openBtn.addEventListener("click", openReel);
  if (closeBtn) closeBtn.addEventListener("click", closeReel);
  if (backdrop) backdrop.addEventListener("click", closeReel);

  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("active")) {
      closeReel();
    }
  });
}

/* ==========================================================================
   8. SCROLL REVEAL — ENHANCED INTERSECTION OBSERVER WITH STAGGER
   ========================================================================== */
function initScrollReveal() {
  const revealSelectors = [
    ".reveal-on-scroll",
    ".reveal-from-left",
    ".reveal-from-right",
    ".reveal-scale-up",
    ".text-split-reveal",
    ".footer-hero-cta",
    ".about-photo-block"
  ];

  const allRevealElements = document.querySelectorAll(revealSelectors.join(", "));
  if (!allRevealElements.length || !("IntersectionObserver" in window)) return;

  // Stagger siblings inside the same parent
  function assignStaggerDelays(elements) {
    const parentGroups = new Map();
    elements.forEach((el) => {
      const parent = el.parentElement;
      if (!parentGroups.has(parent)) {
        parentGroups.set(parent, []);
      }
      parentGroups.get(parent).push(el);
    });

    parentGroups.forEach((siblings) => {
      siblings.forEach((el, i) => {
        if (!el.style.transitionDelay && !el.classList.toString().includes("stagger-")) {
          el.style.transitionDelay = `${i * 0.08}s`;
        }
      });
    });
  }

  assignStaggerDelays(allRevealElements);

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("revealed");
        obs.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.02,
    rootMargin: "0px 0px 50px 0px"
  });

  allRevealElements.forEach((el) => {
    observer.observe(el);
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight + 100) {
      el.classList.add("revealed");
    }
  });

  // Safety fallback: reveal all remaining sections after 1.8s
  setTimeout(() => {
    allRevealElements.forEach((el) => el.classList.add("revealed"));
  }, 1800);
}

/* ==========================================================================
   9. 3D CARD TILT — SPRING PHYSICS PARALLAX (MOUSEMOVE)
   ========================================================================== */
function init3DCardTilt() {
  // Only enable on desktop with pointer
  if (window.matchMedia("(pointer: coarse)").matches) return;

  const tiltCards = document.querySelectorAll(".tilt-card");
  tiltCards.forEach((card) => {
    let currentX = 0, currentY = 0;
    let targetX = 0, targetY = 0;
    let animating = false;

    function springAnimate() {
      const damping = 0.08; // Spring damping factor
      currentX += (targetX - currentX) * damping;
      currentY += (targetY - currentY) * damping;

      card.style.transform = `perspective(1000px) rotateX(${currentY}deg) rotateY(${currentX}deg)`;

      if (Math.abs(targetX - currentX) > 0.01 || Math.abs(targetY - currentY) > 0.01) {
        requestAnimationFrame(springAnimate);
      } else {
        animating = false;
      }
    }

    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      targetX = (x / (rect.width / 2)) * 5;
      targetY = (-y / (rect.height / 2)) * 5;

      if (!animating) {
        animating = true;
        requestAnimationFrame(springAnimate);
      }
    });

    card.addEventListener("mouseleave", () => {
      targetX = 0;
      targetY = 0;
      if (!animating) {
        animating = true;
        requestAnimationFrame(springAnimate);
      }
    });
  });
}

/* ==========================================================================
   10. PARALLAX DEPTH LAYERS — SCROLL-DRIVEN
   ========================================================================== */
function initParallax() {
  // Apply parallax to specific elements
  const heroPortrait = document.querySelector(".editorial-portrait-card");
  const heroTitle = document.querySelector(".hero-huge-title");

  if (!heroPortrait && !heroTitle) return;
  if (window.matchMedia("(pointer: coarse)").matches) return;

  let ticking = false;

  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollY = window.scrollY;

        if (heroPortrait && scrollY < window.innerHeight) {
          heroPortrait.style.transform = `translateY(${scrollY * 0.08}px)`;
        }

        if (heroTitle && scrollY < window.innerHeight) {
          heroTitle.style.transform = `translateY(${scrollY * 0.03}px)`;
        }

        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}

/* ==========================================================================
   11. MAGNETIC BUTTON EFFECT — CURSOR ATTRACTION PHYSICS
   ========================================================================== */
function initMagneticButtons() {
  if (window.matchMedia("(pointer: coarse)").matches) return;

  // Add magnetic class to interactive buttons
  const magneticTargets = document.querySelectorAll(
    ".btn-editorial-red, .btn-editorial-outline, .btn-primary-action, .btn-secondary-action, .hero-reel-pill, .link-btn-red"
  );

  magneticTargets.forEach((btn) => {
    btn.classList.add("magnetic-btn");

    btn.addEventListener("mousemove", (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;

      // Pull effect (magnetic attraction toward cursor)
      const pullStrength = 0.25;
      btn.style.transform = `translate(${x * pullStrength}px, ${y * pullStrength}px)`;
    });

    btn.addEventListener("mouseleave", () => {
      btn.style.transform = "translate(0, 0)";
    });
  });
}

/* ==========================================================================
   12. CUSTOM CURSOR TRAIL — RED DOT + RING
   ========================================================================== */
function initCustomCursor() {
  if (window.matchMedia("(pointer: coarse)").matches) return;

  const dot = document.createElement("div");
  dot.classList.add("cursor-dot");
  document.body.appendChild(dot);

  const ring = document.createElement("div");
  ring.classList.add("cursor-ring");
  document.body.appendChild(ring);

  let mouseX = 0, mouseY = 0;
  let ringX = 0, ringY = 0;

  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = `${mouseX}px`;
    dot.style.top = `${mouseY}px`;
  });

  // Smooth ring follow with lerp
  function animateRing() {
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;
    ring.style.left = `${ringX}px`;
    ring.style.top = `${ringY}px`;
    requestAnimationFrame(animateRing);
  }
  animateRing();

  // Expand ring on hover over interactive elements
  const hoverTargets = document.querySelectorAll(
    "a, button, .work-card, .approach-card, .hero-reel-pill, input, textarea, .cat-tab-btn"
  );
  hoverTargets.forEach((el) => {
    el.addEventListener("mouseenter", () => ring.classList.add("hovering"));
    el.addEventListener("mouseleave", () => ring.classList.remove("hovering"));
  });

  // Hide on mouse leave
  document.addEventListener("mouseleave", () => {
    dot.style.opacity = "0";
    ring.style.opacity = "0";
  });
  document.addEventListener("mouseenter", () => {
    dot.style.opacity = "1";
    ring.style.opacity = "1";
  });
}

/* ==========================================================================
   13. SMOOTH ANCHOR SCROLL — ENHANCED WITH OFFSET
   ========================================================================== */
function initSmoothAnchorScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href");
      if (!targetId || targetId === "#") return;

      const targetEl = document.querySelector(targetId);
      if (!targetEl) return;

      e.preventDefault();

      const headerHeight = document.getElementById("editorial-header")?.offsetHeight || 80;
      const targetPosition = targetEl.getBoundingClientRect().top + window.scrollY - headerHeight - 20;

      window.scrollTo({
        top: targetPosition,
        behavior: "smooth"
      });
    });
  });
}

/* ==========================================================================
   14. COUNTER ANIMATIONS — NUMBERS COUNT UP ON SCROLL
   ========================================================================== */
function initCounterAnimations() {
  const counters = document.querySelectorAll(".counter-animate");
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute("data-target") || el.textContent, 10);
        if (isNaN(target)) return;

        animateCounter(el, 0, target, 1200);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach((el) => observer.observe(el));
}

function animateCounter(el, start, end, duration) {
  const startTime = performance.now();
  const range = end - start;

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(start + range * eased);

    el.textContent = current.toString().padStart(2, "0");

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

/* ==========================================================================
   15. TEXT SPLIT REVEAL — WORD-BY-WORD ENTRANCE
   ========================================================================== */
function initTextSplitReveal() {
  const splitElements = document.querySelectorAll(".hero-manifesto");

  splitElements.forEach((el) => {
    const text = el.textContent.trim();
    const words = text.split(/\s+/);

    el.innerHTML = "";
    el.classList.add("text-split-reveal");

    words.forEach((word) => {
      const wordSpan = document.createElement("span");
      wordSpan.classList.add("word");
      const inner = document.createElement("span");
      inner.classList.add("word-inner");
      inner.textContent = word;
      wordSpan.appendChild(inner);
      el.appendChild(wordSpan);
    });

    // The reveal-on-scroll observer will handle triggering the `revealed` class
    // We re-add reveal-on-scroll so the observer picks it up
    el.classList.add("reveal-on-scroll");
  });
}

/* ==========================================================================
   16. TICKER MARQUEE — AUTO-CLONE FOR INFINITE LOOP
   ========================================================================== */
function initTickerClone() {
  const track = document.querySelector(".ticker-track");
  if (!track) return;

  const content = track.querySelector(".ticker-content");
  if (!content) return;

  // Ensure we have enough clones for seamless looping
  const cloneCount = Math.ceil(window.innerWidth / content.offsetWidth) + 2;
  for (let i = 0; i < cloneCount; i++) {
    const clone = content.cloneNode(true);
    clone.setAttribute("aria-hidden", "true");
    track.appendChild(clone);
  }
}

/* ==========================================================================
   17. TOAST NOTIFICATION UTILITY
   ========================================================================== */
let toastTimeout;
function showToast(message, type = "success") {
  const toast = document.getElementById("toast-notification");
  if (!toast) return;

  clearTimeout(toastTimeout);

  const icon = type === "warning"
    ? '<i class="fa-solid fa-triangle-exclamation" style="color: #f59e0b;"></i>'
    : '<i class="fa-solid fa-circle-check" style="color: #dc2626;"></i>';

  toast.innerHTML = `${icon} <span>${message}</span>`;
  toast.classList.add("show");

  toastTimeout = setTimeout(() => {
    toast.classList.remove("show");
  }, 3500);
}

/* ==========================================================================
   18. CURRENT YEAR IN FOOTER
   ========================================================================== */
function initCurrentYear() {
  const yearSpan = document.getElementById("current-year");
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }
}
