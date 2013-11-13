
function activateNavPanelItem(id, groupName) {
	$('li[name=' + groupName + ']').removeClass('active');
	$('#'+id).addClass('active');
}


function loadIngredientsTable(id, slimID, groupName){
	activateNavPanelItem(slimID, groupName);

	var active = [];
	$('li.active').each(function() {
        active.push([$(this).attr('name'), $(this).find('a').html()]) 
    });

    if(groupName === active[0][0]) {
        $.get("/table/", {category: id, brand: active[1][1]}, function(data) {
            alert('we hurr son');
            alert(data);
            $("#table_content").hide().html(data).fadeIn('fast')
        });
    }
    else if( groupName === active[1][0]) {
		$.get("/table/", {category: active[0][1], brand: id}, function(data) {
            $("#table_content").hide().html(data).fadeIn('fast')
        });
    }
    else {

    }
}


/*
function selectItem(id, name) {
	$('#' + name + '-button').html(id + ' <span class="caret"></span>');
	if(name==='brand') {
		if(id === 'New Brand') {
			$('input[name=' + name + ']').val('');
			$('input[name=' + name + ']').removeAttr('readonly');
		}
		else {
			$('input[name=' + name + ']').val(id);
			$('input[name=' + name + ']').attr('readonly', 'readonly');
		}
	}
	else if(name==='category') {
		$('input[name=' + name + ']').val(id);
	}
}
*/

function matchRegex( pattn, str ) {
	var pattern = new RegExp(pattn);
	return pattern.test(str);
}

function reportError( field, msg ) {
	$('#' + field + '-help').html(msg);
}

function removeError( field ) {
	$('#' + field + '-help').html('');
}

function emptyField( field, name ) {
	if(field.length == 0) {
		reportError( name, 'Field must not be blank.' );
		return true;
	}
	else
		return false;
}

function onlyLettersNums( field, name ) {
	if( matchRegex( "^[A-z][A-z0-9]{6,}$", field ) ) {
		return true;
	}
	else {
		reportError( name, 'Only letters and numbers are allowed and a minimum length of 6.');
		return false;
	}
}

function selectedCatgegory( field, name ) {
	if(field.length == 0 || field == 'Select Category') {
		reportError( name, 'A category must be selected.' );
		return false;
	}
	else
		return true;
}

function meetsLength( field, len ) {
	return field.length >= len;
}

function wordsOnly( field, name ) {
	if(matchRegex( "^[- a-zA-Z]+$", field ))
		return true;
	else {
		reportError( name, 'Only letters, hyphens, and spaces are allowed.');
		return false;
	}
}

function ingredientName( field, name ) {
	if(matchRegex( "^[- '%A-Za-z0-9]+$", field))
		return true;
	else {
		reportError( name, 'Only letters, hyphens, spaces, numbers, and percent signs are allowed.');
		return false;
	}
}

function brandName( field, name ) {
	if(matchRegex( "^[- 'A-Za-z]+$", field))
		return true;
	else {
		reportError( name, 'Only letters, hyphens, spaces, numbers, and percent signs are allowed.');
		return false;
	}
}
/**
 * Source: http://stackoverflow.com/questions/18082/validate-numbers-in-javascript-isnumeric
 */
function isNumber(n) {
	return !isNaN(parseFloat(n)) && isFinite(n);
}

function isNumeric( field, name ) {
	if(isNumber(field))
		return true;
	else {
		reportError( name, 'Only a valid number is allowed.' );
		return false;
	}
}

function validateIngredientForm() {
	var nameF = $('#name').val();
	var name=false;
	if(!emptyField(nameF, 'name') && ingredientName(nameF, 'name')) {
		removeError( 'name' );
		name=true;
	}


	var brandF = $('#brand').val();
	var brand=false;
	if(!emptyField(brandF, 'brand') && brandName(brandF, 'brand')) {
		removeError( 'brand' );
		brand=true;
	}

	var catgF = $('#category').val();
	var catg=false;
	if( selectedCatgegory(catgF, 'category' ) ) {
		removeError( 'category' );
		catg=true;
	}

	var servSizeF = $('#servingsize').val();
	var servSize=false;
	if( isNumeric(servSizeF, 'servingsize') ) {
		removeError( 'servingsize' );
		servSize=true;
	}
	
	var servUnitF = $('#servingunit').val();
	var servUnit=false;
	if( !emptyField(servUnitF, 'servingunit') && wordsOnly(servUnitF, 'servingunit')) {
		removeError( 'servingunit' );
		servUnit=true;
	}
	
	var calF = $('#calories').val();
	var cal=false;
	if( isNumeric(calF, 'calories') ) {
		removeError( 'calories' );
		cal=true;
	}
	
	var fatF = $('#fat').val();
	var fat=false;
	if( isNumeric(fatF, 'fat') ) {
		removeError( 'fat' );
		fat=true;
	}
	
	var carbF = $('#carbohydrates').val();
	var carb=false;
	if( isNumeric(carbF, 'carbohydrates') ) {
		removeError( 'carbohydrates' );
		carb=true;
	}
	
	var proteinF = $('#protein').val();
	var protein=false;
	if( isNumeric(proteinF, 'protein') ) {
		removeError( 'protein' );
		protein=true;
	}

	return name && brand && catg && servSize && servUnit && cal && fat && carb && protein;

}

function oneWord( field, name ) {
	if( matchRegex( "^[A-z]+$", field ) )
		return true;
	else {
		reportError( name, 'Must be at least one character and only contain letters.');
		return false;
	}
}

function validateCreateAccount() {
	var userF = $('#username').val();
	var user=false;
	if(onlyLettersNums( userF, 'username' ) ) {
		removeError( 'username');
		user=true;
	}

	var passF = $('#password').val();
	var passConfF = $('#password-confirm').val();
	var pass=false;
	if(passF === passConfF && passwordLength()) {
		removeError( 'password' );
		removeError( 'password-confirm' );
		pass=true;
	}
  
  var emailF = $('#email').val();
  var email=false;
  if(emailF.length > 3) {
    removeError( 'email' );
    email=true;
  }
  else {
    reportError( 'email', 'The email is is not valid.' );
  }

/*
	var fnameF = $('#firstname').val();
	var fname=false;
	if( oneWord( fnameF, 'firstname' ) ) {
		removeError( 'firstname' );
		fname=true;
	}

	var lnameF = $('#lastname').val();
	var lname=false;
	if( oneWord( lnameF, 'lastname' ) ) {
		removeError( 'lastname' );
		lname=true;
	}
*/
	//return user && pass && fname && lname;
  return user && pass && email;
}

function passwordLength() {
	var help = $('#password-help').val();
	var len = $('#password').val().length;
	if(len < 8) {
		reportError('password', 'The password must be at least 8 characters.');
		return false;
	}
	else {
		return true;
	}
}

/*
	var userF = $('#username').val();
	var user=false;
	alert(user);
	if( onlyLettersNums( userF, 'username' ) && meetsLength( userF, 6 )) {
		removeError( userF, 'username');
		user=true;
	}

	var pass=true;

	var fname=true;

	var lname=true;

	//return user && pass && fname && lname;
}
*/
