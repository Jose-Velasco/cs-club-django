// uncheck 'toggle' checkbox when maximizeing while in mobile navbar
window.addEventListener('resize', function() {
    if (window.matchMedia('(max-width: 768px)').matches == false) {
        document.getElementById('toggle').checked = false;
    }
}, true);