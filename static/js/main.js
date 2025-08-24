// GSAP Plugins Registration
gsap.registerPlugin(ScrollTrigger, TextPlugin);

// Initialize the application
function initializeApp() {
    initLoadingScreen();
    initCustomCursor();
    initGSAPAnimations();
    initScrollEffects();
    initInteractiveElements();
    initParallaxEffects();
    initFormInteractions();
    initPropertyCardAnimations();
    initServiceCardAnimations();
    initBlogCardAnimations();
    initNavbarEffects();
    initStatsCounterAnimations();
    initCTAAnimations();
    initFooterAnimations();
    initSmoothScrolling();
    initLazyLoading();
    initMicroInteractions();
}

// Loading Screen Animation
function initLoadingScreen() {
    const loadingScreen = document.getElementById('loadingScreen');
    const loadingProgress = document.querySelector('.loading-progress');
    
    if (loadingScreen && loadingProgress) {
        // Simulate loading progress
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 15;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
                
                // Hide loading screen with animation
                gsap.to(loadingScreen, {
                    opacity: 0,
                    duration: 0.5,
                    onComplete: () => {
                        loadingScreen.style.display = 'none';
                        // Start page animations
                        initPageAnimations();
                    }
                });
            }
            loadingProgress.style.width = progress + '%';
        }, 100);
    }
}

// Page Animations
function initPageAnimations() {
    // Hero animations for new theme
    const heroElements = document.querySelectorAll('.hero-badge-new, .hero-title-new, .hero-description-new, .hero-stats-new, .search-card-new');
    
    heroElements.forEach((element, index) => {
        gsap.fromTo(element, 
            { 
                opacity: 0, 
                y: 50 
            },
            { 
                opacity: 1, 
                y: 0, 
                duration: 0.8, 
                delay: index * 0.2,
                ease: "power2.out"
            }
        );
    });
    
    // Animate stats numbers
    animateStats();
}

// Custom Cursor
function initCustomCursor() {
    const cursor = document.getElementById('customCursor');
    const cursorFollower = document.getElementById('customCursorFollower');
    
    if (cursor && cursorFollower) {
        document.addEventListener('mousemove', (e) => {
            gsap.to(cursor, {
                x: e.clientX,
                y: e.clientY,
                duration: 0.1
            });
            
            gsap.to(cursorFollower, {
                x: e.clientX,
                y: e.clientY,
                duration: 0.3
            });
        });
        
        // Add hover effects for interactive elements
        const interactiveElements = document.querySelectorAll('a, button, .property-card-fixed, .service-card-fixed');
        interactiveElements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                cursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
                cursorFollower.style.transform = 'translate(-50%, -50%) scale(1.5)';
            });
            
            element.addEventListener('mouseleave', () => {
                cursor.style.transform = 'translate(-50%, -50%) scale(1)';
                cursorFollower.style.transform = 'translate(-50%, -50%) scale(1)';
            });
        });
    }
}

// GSAP Animations - Optimized for Performance
function initGSAPAnimations() {
    // Disable ScrollTrigger on mobile for better performance
    if (window.innerWidth < 768) {
        return;
    }
    
    // Optimize performance with will-change and transform3d
    gsap.set('.featured-section-fixed, .services-section-fixed, .cta-section-fixed', {
        willChange: 'transform, opacity'
    });
    
    // Featured Properties Animation - Simplified
    gsap.fromTo('.featured-section-fixed', {
        opacity: 0,
        y: 30
    }, {
        opacity: 1,
        y: 0,
        duration: 0.6,
        ease: 'power2.out',
        scrollTrigger: {
            trigger: '.featured-section-fixed',
            start: 'top 85%',
            end: 'bottom 15%',
            toggleActions: 'play none none reverse',
            markers: false
        }
    });
    
    // Services Section Animation - Simplified
    gsap.fromTo('.services-section-fixed', {
        opacity: 0,
        y: 30
    }, {
        opacity: 1,
        y: 0,
        duration: 0.6,
        ease: 'power2.out',
        scrollTrigger: {
            trigger: '.services-section-fixed',
            start: 'top 85%',
            end: 'bottom 15%',
            toggleActions: 'play none none reverse',
            markers: false
        }
    });
    
    // CTA Section Animation - Simplified
    gsap.fromTo('.cta-section-fixed', {
        opacity: 0,
        y: 30
    }, {
        opacity: 1,
        y: 0,
        duration: 0.6,
        ease: 'power2.out',
        scrollTrigger: {
            trigger: '.cta-section-fixed',
            start: 'top 85%',
            end: 'bottom 15%',
            toggleActions: 'play none none reverse',
            markers: false
        }
    });
}

// Scroll Effects - Optimized
function initScrollEffects() {
    // Disable on mobile for better performance
    if (window.innerWidth < 768) {
        return;
    }
    
    // Light parallax effect for hero background
    gsap.to('.hero-bg-new', {
        yPercent: -10,
        ease: 'none',
        scrollTrigger: {
            trigger: '.hero-new',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.5
        }
    });
    
    // Navbar scroll effect - Simplified
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        ScrollTrigger.create({
            trigger: 'body',
            start: 'top -100',
            onUpdate: (self) => {
                if (self.direction === 1) {
                    navbar.classList.add('navbar-scrolled');
                } else {
                    navbar.classList.remove('navbar-scrolled');
                }
            }
        });
    }
}

// Interactive Elements
function initInteractiveElements() {
    // Property card hover effects
    const propertyCards = document.querySelectorAll('.property-card-fixed');
    propertyCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                y: -10,
                duration: 0.3,
                ease: "power2.out"
            });
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                y: 0,
                duration: 0.3,
                ease: "power2.out"
            });
        });
    });

    // Service card hover effects
    const serviceCards = document.querySelectorAll('.service-card-fixed');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                scale: 1.05,
                duration: 0.3,
                ease: "power2.out"
            });
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                scale: 1,
                duration: 0.3,
                ease: "power2.out"
            });
        });
    });
}

// Parallax Effects - Optimized
function initParallaxEffects() {
    // Disable on mobile for better performance
    if (window.innerWidth < 768) {
        return;
    }
    
    // Very light parallax for hero particles
    gsap.to('.hero-particles-new', {
        yPercent: -5,
        ease: 'none',
        scrollTrigger: {
            trigger: '.hero-new',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.3
        }
    });
}

// Form Interactions - Optimized
function initFormInteractions() {
    const inputs = document.querySelectorAll('.form-input-new');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            gsap.to(input, {
                scale: 1.01,
                duration: 0.2,
                ease: 'power2.out'
            });
        });
        
        input.addEventListener('blur', () => {
            gsap.to(input, {
                scale: 1,
                duration: 0.2,
                ease: 'power2.out'
            });
        });
    });
}

// Property Card Animations - Optimized
function initPropertyCardAnimations() {
    // Disable on mobile for better performance
    if (window.innerWidth < 768) {
        return;
    }
    
    gsap.fromTo('.property-card-fixed', {
        opacity: 0,
        y: 40,
        scale: 0.98
    }, {
        opacity: 1,
        y: 0,
        scale: 1,
        duration: 0.5,
        ease: 'power2.out',
        stagger: 0.08,
        scrollTrigger: {
            trigger: '.properties-grid-fixed',
            start: 'top 90%',
            end: 'bottom 10%',
            toggleActions: 'play none none reverse',
            markers: false
        }
    });
}

// Service Card Animations - Optimized
function initServiceCardAnimations() {
    // Disable on mobile for better performance
    if (window.innerWidth < 768) {
        return;
    }
    
    gsap.fromTo('.service-card-fixed', {
        opacity: 0,
        y: 40,
        scale: 0.98
    }, {
        opacity: 1,
        y: 0,
        scale: 1,
        duration: 0.5,
        ease: 'power2.out',
        stagger: 0.08,
        scrollTrigger: {
            trigger: '.services-grid-fixed',
            start: 'top 90%',
            end: 'bottom 10%',
            toggleActions: 'play none none reverse',
            markers: false
        }
    });
}

// Blog Card Animations
function initBlogCardAnimations() {
    const blogCards = document.querySelectorAll('.blog-card');
    blogCards.forEach((card, index) => {
        gsap.fromTo(card,
            { opacity: 0, x: -50 },
            {
                opacity: 1,
                x: 0,
                duration: 0.6,
                delay: index * 0.1,
                scrollTrigger: {
                    trigger: card,
                    start: "top 90%",
                    toggleActions: "play none none reverse"
                }
            }
        );
    });
}

// Navbar Effects
function initNavbarEffects() {
    const navbar = document.getElementById('mainNav');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 100) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        });
    }
}

// Stats Counter Animations
function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-number-new, .stat-number-fixed');
    
    statNumbers.forEach(stat => {
        const target = parseInt(stat.getAttribute('data-target'));
        const duration = 2;
        const increment = target / (duration * 60); // 60fps
        
        let current = 0;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            stat.textContent = Math.floor(current).toLocaleString();
        }, 1000 / 60);
    });
}

function initStatsCounterAnimations() {
    // Trigger stats animation when they come into view
    const statsSection = document.querySelector('.hero-stats-new, .cta-stats-fixed');
    if (statsSection) {
        ScrollTrigger.create({
            trigger: statsSection,
            start: "top 80%",
            onEnter: () => animateStats()
        });
    }
}

// CTA Animations
function initCTAAnimations() {
    const ctaSection = document.querySelector('.cta-section-fixed');
    if (ctaSection) {
        gsap.fromTo(ctaSection,
            { opacity: 0, y: 100 },
            {
                opacity: 1,
                y: 0,
                duration: 1,
                scrollTrigger: {
                    trigger: ctaSection,
                    start: "top 80%",
                    toggleActions: "play none none reverse"
                }
            }
        );
    }
}

// Footer Animations
function initFooterAnimations() {
    const footer = document.querySelector('footer');
    if (footer) {
        gsap.fromTo(footer,
            { opacity: 0, y: 50 },
            {
                opacity: 1,
                y: 0,
                duration: 0.8,
                scrollTrigger: {
                    trigger: footer,
                    start: "top 90%",
                    toggleActions: "play none none reverse"
                }
            }
        );
    }
}

// Smooth Scrolling
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Lazy Loading
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

// Micro Interactions
function initMicroInteractions() {
    // Button hover effects
    const buttons = document.querySelectorAll('.btn-primary-fixed, .btn-secondary-fixed, .search-button-new');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            gsap.to(button, {
                scale: 1.05,
                duration: 0.2,
                ease: "power2.out"
            });
        });
        
        button.addEventListener('mouseleave', () => {
            gsap.to(button, {
                scale: 1,
                duration: 0.2,
                ease: "power2.out"
            });
        });
    });
    
    // Favorite button interactions
    const favoriteButtons = document.querySelectorAll('.favorite-btn-fixed');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', () => {
            const icon = button.querySelector('i');
            if (icon.classList.contains('far')) {
                icon.classList.remove('far');
                icon.classList.add('fas');
                gsap.to(button, {
                    scale: 1.2,
                    duration: 0.2,
                    yoyo: true,
                    repeat: 1
                });
            } else {
                icon.classList.remove('fas');
                icon.classList.add('far');
            }
        });
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeApp);
