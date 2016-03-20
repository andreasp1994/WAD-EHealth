/**
 * Created by Andreas on 20/03/2016.
 */
$('.result-details').hide();
$('.fav-more-icon').hover(
  function () {

    $('.result-details').fadeIn();
  },
  function () {
    $('.result-details').fadeOut();
  }
);