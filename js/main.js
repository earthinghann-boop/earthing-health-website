// ============================================
// EARTHING - Main JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavigation();
    initScrollEffects();
    initContactForm();
    initAnimations();
    initCarousels();
});

// ============================================
// Navigation
// ============================================
function initNavigation() {
    const navbar = document.getElementById('navbar');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinks = document.getElementById('navLinks');
    const allNavLinks = navLinks.querySelectorAll('a');

    // Scroll effect for navbar
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile menu toggle
    mobileMenuBtn.addEventListener('click', function() {
        mobileMenuBtn.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close mobile menu on link click
    allNavLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileMenuBtn.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    // Active link on scroll
    const sections = document.querySelectorAll('section[id]');
    
    window.addEventListener('scroll', function() {
        let current = '';
        const scrollY = window.scrollY;

        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;
            
            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        allNavLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });
}

// ============================================
// Scroll Effects
// ============================================
function initScrollEffects() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.scrollY - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ============================================
// Contact Form
// ============================================
function initContactForm() {
    const form = document.getElementById('contactForm');
    
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Validate
        if (!data.name || !data.email || !data.interest || !data.message) {
            showFormMessage('Please fill in all required fields.', 'error');
            return;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(data.email)) {
            showFormMessage('Please enter a valid email address.', 'error');
            return;
        }

        // Simulate form submission
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;

        // In a real implementation, you would send this to your server
        // For now, we'll simulate with mailto
        setTimeout(() => {
            const subject = `Inquiry from ${data.name} - ${data.interest}`;
            const body = `
Name: ${data.name}
Email: ${data.email}
Company: ${data.company || 'Not provided'}
Interest: ${data.interest}

Message:
${data.message}
            `.trim();

            // Create mailto link
            const mailtoLink = `mailto:sale@groundingsafe.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            
            // Show success message
            showFormMessage('Thank you! Your message has been prepared. Click to open your email client to send.', 'success');
            
            // Open email client
            window.location.href = mailtoLink;

            // Reset form
            form.reset();
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }, 1000);
    });
}

function showFormMessage(message, type) {
    // Remove existing message
    const existing = document.querySelector('.form-success, .form-error');
    if (existing) existing.remove();

    // Create message element
    const msgDiv = document.createElement('div');
    msgDiv.className = type === 'success' ? 'form-success' : 'form-error';
    msgDiv.textContent = message;

    // Insert after form
    const form = document.getElementById('contactForm');
    form.parentNode.insertBefore(msgDiv, form.nextSibling);

    // Auto remove after 5 seconds
    setTimeout(() => {
        msgDiv.remove();
    }, 5000);
}

// ============================================
// Animations
// ============================================
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Add fade-in class to elements
    const animatedElements = document.querySelectorAll(
        '.product-card, .tech-card, .oem-feature, .contact-item, .video-item'
    );

    animatedElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

    // Stagger animation for product grids
    const productGrids = document.querySelectorAll('.products-grid');
    productGrids.forEach(grid => {
        const cards = grid.querySelectorAll('.product-card');
        cards.forEach((card, index) => {
            card.style.transitionDelay = `${index * 0.1}s`;
        });
    });
}

// ============================================
// Utility Functions
// ============================================

// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Lazy load images
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

/* ============================================
   Carousel
   ============================================ */
const carouselStates = {};

function initCarousels() {
    document.querySelectorAll('.carousel').forEach(el => {
        const id = el.id;
        carouselStates[id] = { index: 0, timer: null };
        showSlide(id, 0);
        startAutoPlay(id);
    });
}

function showSlide(id, index) {
    const el = document.getElementById(id);
    if (!el) return;
    const slides = el.querySelectorAll('.carousel-slide');
    const dots = el.querySelectorAll('.dot');
    if (slides.length === 0) return;
    if (index < 0) index = slides.length - 1;
    if (index >= slides.length) index = 0;
    slides.forEach(s => s.classList.remove('active'));
    dots.forEach(d => d.classList.remove('active'));
    slides[index].classList.add('active');
    if (dots[index]) dots[index].classList.add('active');
    if (carouselStates[id]) carouselStates[id].index = index;
}

function moveCarousel(id, direction) {
    if (!carouselStates[id]) return;
    showSlide(id, carouselStates[id].index + direction);
    resetAutoPlay(id);
}

function goToSlide(id, index) {
    showSlide(id, index);
    resetAutoPlay(id);
}

function startAutoPlay(id) {
    const state = carouselStates[id];
    if (!state) return;
    clearInterval(state.timer);
    state.timer = setInterval(() => {
        showSlide(id, (state.index + 1) % 3);
    }, 4000);
}

function resetAutoPlay(id) {
    startAutoPlay(id);
}
