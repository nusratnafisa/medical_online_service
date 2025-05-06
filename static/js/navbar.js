
  // Initialize Bootstrap dropdowns
  $(document).ready(function() {
    // This keeps the click functionality on mobile
    if ($(window).width() > 992) {
      $('.navbar .dropdown').hover(function() {
        $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideDown();
      }, function() {
        $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideUp();
      });
      
      $('.navbar .dropdown > a').click(function() {
        if ($(window).width() > 992) {
          return false; // Prevent default click behavior on desktop
        }
      });
    }
  });
