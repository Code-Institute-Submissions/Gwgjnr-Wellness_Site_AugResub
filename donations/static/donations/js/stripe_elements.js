// Js file to handle Stripe payment when payment-form is submitted

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

//Set the form and card elements to variables so they can be called throughout Payments intents process

var form = document.getElementById('payment-form');
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Add event listener for changes to the card element to show errors promptly

card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `<span>${event.error.message}</span>`;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});

// Add event listener for form submission to trigger attempt to collect payment

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#submit-button').attr('disabled', true);
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);

  // From using {% csrf_token %} in the form
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
  };
  var url = '/donate/checkout/';

  $.post(url, postData).done(function () {
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
    }).then(function(result) {
      if (result.error) {
        // There was an error with the payment, re-display input fields so new attempt can be made
        var errorDiv = document.getElementById('card-errors');
        var html = `<p class='donate-text'>${result.error.message}</p>`;
        $(errorDiv).html(html);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        card.update({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
      } else {
        // The payment has been processed, redirect to homepage and trigger message to confirm donation completed
        if (result.paymentIntent.status === 'succeeded') {
          location.replace('/?paymentComplete=true');
        }
      }
    });
  });
});
