
$(document).ready(function() {
    
    if ($('#item_firstassessment').val() == "Sale") { //If firstassessment==Donation show donationvalue field
	$('fieldset.module.aligned.forsale').show(); //Hiding the "If item is for sale" fieldset
	$('fieldset.module.aligned.upforsale').show(); //Hiding the "Up for sale" fieldset
	$('label[for=item_donationvalue], input#item_donationvalue').hide(); //Hiding the Donation value field
    }
    else {
	$('fieldset.module.aligned.forsale').hide(); //Hiding the "If item is for sale" fieldset
	$('fieldset.module.aligned.upforsale').hide(); //Hiding the "Up for sale" fieldset
	if ($('#item_firstassessment').val() == "Donation") { //If firstassessment==Donation show donationvalue field
	    $('label[for=item_donationvalue], input#item_donationvalue').show();
	}
	else 
	{
	    $('label[for=item_donationvalue], input#item_donationvalue').hide();
	}
    }
    
    $('div.form-row.field-indate').hide();
    

    $('#item_firstassessment').change(function() {
	console.log("Firstassess");
	if ($('#item_firstassessment').val() == "Donation") { //If firstassessment==Donation show donationvalue field

	    $('label[for=item_donationvalue], input#item_donationvalue').show();
	}
	else 
	{
	    $('label[for=item_donationvalue], input#item_donationvalue').hide();
	}
	
	if ($('#item_firstassessment').val() == "Sale") { //If firstassessment==Sale show  the "If item is for sale" fieldset

	    $('fieldset.module.aligned.forsale').show();
	    $('fieldset.module.aligned.upforsale').show();
	}
	else 
	{
	    $('fieldset.module.aligned.forsale').hide();
	    $('fieldset.module.aligned.upforsale').hide();
	}
    });

    $('#item_status').change(function() {
	
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
