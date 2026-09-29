/**
 * Sreyasee UGC Media Kit - Interactive Script
 * Folder Tabs, Smooth Navigation, and Form Interactions
 */

document.addEventListener("DOMContentLoaded", () => {
  initFolderTabs();
  initMobileNav();
  initContactForm();
  initScrollSpy();
});

/* ================= 1. INTERACTIVE FOLDER TABS ================= */
function initFolderTabs() {
  const folderTabs = document.querySelectorAll(".folder-tab-btn");
  const folderPanes = document.querySelectorAll(".folder-pane");

  folderTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const targetCategory = tab.getAttribute("data-category");

      // Update active tab
      folderTabs.forEach((t) => t.classList.remove("active"));
      tab.classList.add("active");

      // Update active pane
      folderPanes.forEach((pane) => {
        if (pane.id === `folder-${targetCategory}`) {
          pane.classList.add("active");
        } else {
          pane.classList.remove("active");
        }
      });
    });
  });
}

/* ================= 2. MOBILE NAVIGATION ================= */
function initMobileNav() {
  const menuToggle = document.getElementById("menu-toggle");
  const navLinks = document.getElementById("nav-links");

  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
      const icon = menuToggle.querySelector("i");
      if (icon) {
        if (navLinks.classList.contains("active")) {
          icon.classList.remove("fa-bars");
          icon.classList.add("fa-xmark");
        } else {
          icon.classList.remove("fa-xmark");
          icon.classList.add("fa-bars");
        }
      }
    });

    // Close on link click
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        navLinks.classList.remove("active");
        const icon = menuToggle.querySelector("i");
        if (icon) {
          icon.classList.remove("fa-xmark");
          icon.classList.add("fa-bars");
        }
      });
    });
  }
}

/* ================= 3. SCROLL SPY FOR NAVBAR ================= */
function initScrollSpy() {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-links a");

  window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 120;
      if (window.scrollY >= sectionTop) {
        current = section.getAttribute("id");
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove("active");
      if (link.getAttribute("href") === `#${current}`) {
        link.classList.add("active");
      }
    });
  });
}

/* ================= 4. CONTACT FORM HANDLING ================= */
function initContactForm() {
  const form = document.getElementById("sreyasee-connect-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const name = document.getElementById("connect-name")?.value.trim();
    const email = document.getElementById("connect-email")?.value.trim();
    const message = document.getElementById("connect-message")?.value.trim();

    if (!name || !email || !message) {
      alert("Please fill in all fields.");
      return;
    }

    const origText = btn.innerHTML;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
    btn.disabled = true;

    setTimeout(() => {
      btn.innerHTML = '<i class="fa-solid fa-check"></i> Message Sent!';
      alert(`Thank you, ${name}! Your inquiry has been sent to sreyasee31@gmail.com.`);
      form.reset();

      setTimeout(() => {
        btn.innerHTML = origText;
        btn.disabled = false;
      }, 3000);
    }, 1000);
  });
}
