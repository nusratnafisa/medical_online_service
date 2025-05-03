document.addEventListener('DOMContentLoaded', function() {
    // Format phone number input
    const phoneInput = document.getElementById('id_phone');
    if (phoneInput) {
      phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length > 0) {
          value = '+' + value;
        }
        e.target.value = value;
      });
    }
    
    // Hide the clear checkbox label if it exists
    const clearLabel = document.querySelector('label[for*="clear"]');
    if (clearLabel) {
      clearLabel.style.display = 'none';
    }
  });