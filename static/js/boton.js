document.querySelectorAll('.decrease').forEach(button => {
    button.addEventListener('click', function() {
      decreaseQuantity(this);
    });
  });
  
  document.querySelectorAll('.increase').forEach(button => {
    button.addEventListener('click', function() {
      increaseQuantity(this);
    });
  });