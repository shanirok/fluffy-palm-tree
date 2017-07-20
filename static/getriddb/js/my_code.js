
$(document).ready(function() {
    
    $('fieldset.module.aligned.forsale').hide(); //Hiding the "If item is for sale" fieldset
    $('fieldset.module.aligned.upforsale').hide(); //Hiding the "Up for sale" fieldset
    $('div.form-row.field-indate').hide();
    $('label[for=donationvalue], input#donationvalue').hide(); //Hiding the Donation value field

    $('#firstassessment').change(function() {
	console.log("Firstassess");
	if ($('#firstassessment').val() == "Donation") { //If firstassessment==Donation show donationvalue field

	    $('label[for=donationvalue], input#donationvalue').show();
	}
	else 
	{
	    $('label[for=donationvalue], input#donationvalue').hide();
	}
	
	if ($('#firstassessment').val() == "Sale") { //If firstassessment==Sale show  the "If item is for sale" fieldset

	    $('fieldset.module.aligned.forsale').show();
	    $('fieldset.module.aligned.upforsale').show();
	}
	else 
	{
	    $('fieldset.module.aligned.forsale').hide();
	    $('fieldset.module.aligned.upforsale').hide();
	}
    });				  
});

/*
`$('#selector').on('change', function() {
       if ($(this).val() == "A"))  {
             $('#inputA').prop('required', true);
             $('#inputB').removeAttr('required');
        }
        if ($(this).val() == "B"))  {
             $('#inputB').prop('required', true);
             $('#inputA').removeAttr('required');
        }
  });
*/
