
$(document).ready(function() {
    
   $('fieldset.module.aligned.forsale').hide(); //Hiding the "If item is for sale" fieldset
//    $('label[for=status], select#status').hide();
    $('div.form-row.field-status').hide();
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
	    //	    $('label[for=status], select#status').show();
	    $('div.form-row.field-status').show();
	}
	else 
	{
	    $('fieldset.module.aligned.forsale').hide();
	    //   $('label[for=status], select#status').hide();
	    $('div.form-row.field-status').hide();
	}
    });				  
});
