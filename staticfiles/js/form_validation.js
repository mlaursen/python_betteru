/**
 * Checks if a str matches a regex pattern.
 */
function matchRegex( pattn, str ) {
	var pattern = new RegExp(pattn);
	return pattern.test(str);
}


/**
 * Reports an error to a field with the ending '-help'
 * var field:  field to add error message
 * var msg:    The message to be applied
 * return: none
 */
function reportError( field, msg ) {
	$('#' + field + '-help').html(msg);
}


/**
 * Removes all errors from a field.
 * var field: Field to remove errors from
 * return: none
 */
function removeError( field ) {
	$('#' + field + '-help').html('');
}


/**
 * Checks if a field is empty.  Reports an error if it is.
 * var field:  field to check
 * var name:   name of the field to report error to
 * return: Boolean
 */
function emptyField( field, name ) {
	if(field.length == 0) {
		reportError( name, 'Field must not be blank.' );
		return true;
	}
	else
		return false;
}


/**
 * Checks if a field is only letters and numbers
 * var field: 
 * var name:
 * return: Boolean
 */
function onlyLettersNums( field, name ) {
	if( matchRegex( "^[A-z][A-z0-9]{6,}$", field ) ) {
		return true;
	}
	else {
		reportError( name, 'Only letters and numbers are allowed and a minimum length of 6.');
		return false;
	}
}


/**
 * Helper to check if a field meets a certain length
 * var field:
 * var len: length
 * return: Boolean
 */
function meetsLength( field, len ) {
	return field.length >= len;
}


/**
 * Checks if a field is only word characters
 * var field:
 * var name:
 * return: Boolean
 */
function wordsOnly( field, name ) {
	if(matchRegex( "^[- a-zA-Z]+$", field ))
		return true;
	else {
		reportError( name, 'Only letters, hyphens, and spaces are allowed.');
		return false;
	}
}


/**
 * Checks if a field is numeric
 * var field:
 * var name:
 * return Boolean
 */
function isNumeric( field, name ) {
	if(isNumber(field))
		return true;
	else {
		reportError( name, 'Only a valid number is allowed.' );
		return false;
	}
}


/**
 * Checks if a field is only one word. (no spaces)
 * var field:
 * var name:
 * return Boolean
 */
function oneWord( field, name ) {
	if( matchRegex( "^[A-z]+$", field ) )
		return true;
	else {
		reportError( name, 'Must be at least one character and only contain letters.');
		return false;
	}
}





