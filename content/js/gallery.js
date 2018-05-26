$(document).ready(function() {
  $('.gallery').each(function() {
    $(this).magnificPopup({
      delegate: 'a',
      type: 'image',
      gallery: {
        enabled:true
      }
    });
  });
});
