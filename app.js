// DCS Booklet Interactive Functionality
class DCSBooklet {
  constructor() {
    this.currentSection = 0;
    this.totalSections = 16;
    this.sections = document.querySelectorAll('.section');
    this.navigationHistory = [0]; // Track navigation history for back button
    this.isAnimating = false;

    this.init();
  }

  init() {
    // Ensure only the first section is active on load
    this.sections.forEach((section, index) => {
      if (index === 0) {
        section.classList.add('active');
      } else {
        section.classList.remove('active');
      }
    });
  
    this.bindEvents();
    this.updateUI();
    this.setupIntersectionObserver();
    this.initializeAnimations();
    console.log('DCS Booklet initialized with', this.totalSections, 'sections');
  }

  bindEvents() {
    // Navigation buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const menuBtn = document.getElementById('menuBtn');
    const closeModal = document.getElementById('closeModal');
    const backBtn = document.getElementById('backBtn');
    const printBtn = document.getElementById('printBtn');

    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.previousSection();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.nextSection();
      });
    }

    if (menuBtn) {
      menuBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.toggleModal();
      });
    }

    if (closeModal) {
      closeModal.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.hideModal();
      });
    }

    // Back button functionality
    if (backBtn) {
      backBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        console.log('Back button clicked');
        this.goBack();
      });
    }

    // Print button functionality
    if (printBtn) {
      printBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        this.printEntireBooklet();
      });
    }

    // Table of contents navigation - use event delegation
    document.addEventListener('click', (e) => {
      const tocItem = e.target.closest('.toc-item, .toc-visual-item');
      if (tocItem && tocItem.hasAttribute('data-section')) {
        e.preventDefault();
        e.stopPropagation();

        const sectionIndex = parseInt(tocItem.getAttribute('data-section'));
        console.log('TOC clicked - going to section:', sectionIndex);

        if (!isNaN(sectionIndex) && sectionIndex >= 0 && sectionIndex < this.totalSections) {
          this.goToSection(sectionIndex, true);
          this.hideModal();
        }
      }
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => this.handleKeyboard(e));

    // Modal background click
    const modal = document.getElementById('tocModal');
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          this.hideModal();
        }
      });
    }

    // Window resize handler
    window.addEventListener('resize', () => this.handleResize());

    // Touch/swipe support
    this.setupTouchEvents();
  }

  setupTouchEvents() {
    let startX = 0;
    let startY = 0;
    let isScrolling = false;

    document.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
      isScrolling = false;
    });

    document.addEventListener('touchmove', (e) => {
      if (!startX || !startY) return;

      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const diffX = startX - currentX;
      const diffY = startY - currentY;

      if (Math.abs(diffY) > Math.abs(diffX)) {
        isScrolling = true;
      }
    });

    document.addEventListener('touchend', (e) => {
      if (!startX || !startY || isScrolling) return;

      const currentX = e.changedTouches[0].clientX;
      const diffX = startX - currentX;

      // Minimum swipe distance
      if (Math.abs(diffX) > 50) {
        if (diffX > 0) {
          // Swipe left - next section
          this.nextSection();
        } else {
          // Swipe right - previous section
          this.previousSection();
        }
      }

      startX = 0;
      startY = 0;
    });
  }

  goToSection(index, addToHistory = true) {
    if (this.isAnimating || index < 0 || index >= this.totalSections || index === this.currentSection) {
      return;
    }
  
    console.log('Going to section:', index, 'from:', this.currentSection);
  
    this.isAnimating = true;
  
    // Add to navigation history
    if (addToHistory && index !== this.currentSection) {
      this.navigationHistory.push(this.currentSection);
      if (this.navigationHistory.length > 20) {
        this.navigationHistory.shift();
      }
    }
  
    // Hide ALL sections first
    this.sections.forEach(section => {
      section.classList.remove('active');
    });
  
    // Update current section
    this.currentSection = index;
  
    // Show new section with delay for animation
    setTimeout(() => {
      if (this.sections[this.currentSection]) {
        this.sections[this.currentSection].classList.add('active');
      }
      this.updateUI();
      this.isAnimating = false;
    }, 100);
  }

  goBack() {
    console.log('Going back. History:', this.navigationHistory);
    if (this.navigationHistory.length > 0) {
      const previousSection = this.navigationHistory.pop();
      console.log('Going back to section:', previousSection);
      this.goToSection(previousSection, false);
    } else {
      // Fallback to previous section if no history
      this.previousSection();
    }
  }

  nextSection() {
    if (this.currentSection < this.totalSections - 1) {
      this.goToSection(this.currentSection + 1);
    }
  }

  previousSection() {
    if (this.currentSection > 0) {
      this.goToSection(this.currentSection - 1);
    }
  }

  updateUI() {
    // Update section counter
    const currentSectionEl = document.getElementById('currentSection');
    const totalSectionsEl = document.getElementById('totalSections');

    if (currentSectionEl) {
      currentSectionEl.textContent = this.currentSection + 1;
    }
    if (totalSectionsEl) {
      totalSectionsEl.textContent = this.totalSections;
    }

    // Update progress bar
    const progressFill = document.getElementById('progressFill');
    if (progressFill) {
      const progress = ((this.currentSection) / (this.totalSections - 1)) * 100;
      progressFill.style.width = `${Math.max(0, Math.min(100, progress))}%`;
    }

    // Update navigation buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (prevBtn) {
      prevBtn.disabled = this.currentSection === 0;
    }
    if (nextBtn) {
      nextBtn.disabled = this.currentSection === this.totalSections - 1;
    }

    // Show/hide back button (hide on home page)
    const backBtn = document.getElementById('backBtn');
    if (backBtn) {
      if (this.currentSection === 0) {
        backBtn.classList.add('hidden');
      } else {
        backBtn.classList.remove('hidden');
      }
    }

    // Update page title
    const pageTitle = this.getPageTitle(this.currentSection);
    if (pageTitle) {
      document.title = `${pageTitle} - डिजिटल क्रॉप सर्वे (DCS)`;
    }
  }

  getPageTitle(index) {
    const titles = [
      'मुख्य पृष्ठ',
      'विषय सूची',
      'परिचय',
      'DCS से पहले',
      'विकास यात्रा',
      'तकनीकी आधार',
      'प्रक्रिया प्रवाह',
      'हितधारक',
      'उपलब्धियां',
      'डेटा संग्रह',
      'डेटा इंटीग्रेशन',
      'भविष्य तकनीक',
      'चुनौतियां',
      'आर्थिक प्रभाव',
      'सफलता कहानियां',
      'संपर्क जानकारी'
    ];
    return titles[index] || '';
  }

  toggleModal() {
    const modal = document.getElementById('tocModal');
    if (modal) {
      modal.classList.toggle('hidden');

      if (!modal.classList.contains('hidden')) {
        // Focus management for accessibility
        const firstTocItem = modal.querySelector('.toc-item');
        if (firstTocItem) {
          firstTocItem.focus();
        }
      }
    }
  }

  hideModal() {
    const modal = document.getElementById('tocModal');
    if (modal) {
      modal.classList.add('hidden');
    }
  }

  printEntireBooklet() {
    console.log('Preparing to print entire booklet...');

    // Show all sections temporarily for printing
    const originalStates = [];
    this.sections.forEach((section, index) => {
      originalStates[index] = section.style.display;
      section.style.display = 'block';
      section.classList.add('active');
    });

    // Add print-specific styles
    document.body.classList.add('printing');

    // Small delay to ensure all content is rendered
    setTimeout(() => {
      // Trigger the print dialog
      window.print();

      // Restore original states after printing
      setTimeout(() => {
        this.sections.forEach((section, index) => {
          if (index !== this.currentSection) {
            section.style.display = originalStates[index] || 'none';
            section.classList.remove('active');
          }
        });
        document.body.classList.remove('printing');
        console.log('Print completed, restored original state');
      }, 1000);
    }, 500);
  }

  handleKeyboard(e) {
    // Prevent navigation when typing in input fields
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      return;
    }

    switch (e.key) {
      case 'ArrowRight':
      case ' ': // Spacebar
        e.preventDefault();
        this.nextSection();
        break;
      case 'ArrowLeft':
        e.preventDefault();
        this.previousSection();
        break;
      case 'Home':
        e.preventDefault();
        this.goToSection(0);
        break;
      case 'End':
        e.preventDefault();
        this.goToSection(this.totalSections - 1);
        break;
      case 'Escape':
        e.preventDefault();
        this.hideModal();
        break;
      case 'Enter':
        // Handle enter key on focused TOC items
        if (e.target.classList.contains('toc-item') || e.target.classList.contains('toc-visual-item')) {
          e.preventDefault();
          e.target.click();
        }
        break;
    }
  }

  handleResize() {
    // Handle responsive behavior on window resize
    clearTimeout(this.resizeTimeout);
    this.resizeTimeout = setTimeout(() => {
      // Recalculate layouts if needed
      this.updateUI();
    }, 250);
  }

  setupIntersectionObserver() {
    // Set up intersection observer for better performance
    if ('IntersectionObserver' in window) {
      const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
      };

      this.observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            // Add any intersection-based animations here
            entry.target.classList.add('in-view');
          }
        });
      }, options);

      // Observe all sections
      this.sections.forEach(section => {
        this.observer.observe(section);
      });
    }
  }

  initializeAnimations() {
    // Initialize any CSS animations or transitions
    const animatedElements = document.querySelectorAll('.content-card, .stat-card, .story-card, .timeline-item');
    animatedElements.forEach((el, index) => {
      el.style.animationDelay = `${index * 0.1}s`;
    });
  
    // Set dynamic year offset for horizontal timeline
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach((item, index) => {
      const year = parseInt(item.getAttribute('data-year') || '2017');
      const baseYear = 2017;
      const offset = year ? (year - baseYear) : index; // Calculate offset from 2017
      item.style.setProperty('--year-offset', offset);
    });
  }

  
  // Cleanup method
  destroy() {
    if (this.observer) {
      this.observer.disconnect();
    }

    // Remove event listeners
    window.removeEventListener('resize', this.handleResize);
    document.removeEventListener('keydown', this.handleKeyboard);
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM loaded, initializing DCS Booklet...');
  window.dcsBooklet = new DCSBooklet();
});

// Handle page visibility changes
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && window.dcsBooklet) {
    window.dcsBooklet.updateUI();
  }
});

// Handle print events
window.addEventListener('beforeprint', () => {
  console.log('Before print event triggered');
  document.body.classList.add('printing');
});

window.addEventListener('afterprint', () => {
  console.log('After print event triggered');
  document.body.classList.remove('printing');
});

// Export for potential external use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = DCSBooklet;
}


