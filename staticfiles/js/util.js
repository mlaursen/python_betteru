
/**
 * Source: http://stackoverflow.com/questions/18082/validate-numbers-in-javascript-isnumeric
 */
function isNumber(n) {
	return !isNaN(parseFloat(n)) && isFinite(n);
}




function selectItem(id, name) {
  $('#' + name + '_button').html(id + ' <span class="caret"></span>');
  if(id === 'New Brand') {
    $('input[name=' + name + ']').val('');
    $('input[name=' + name + ']').removeAttr('readonly');
  }
  else {
    $('input[name=' + name + ']').val(id);
    $('input[name=' + name + ']').attr('readonly', 'readonly');
  }
}

function selectItemDropdown(field) {
  var name = field.parentElement.parentElement.id.replace('_choices', '');
  $('#'+name+'_button').html(field.text+' <span class="caret"></span>');
  $('input[name='+name+']').attr('value', field.id.replace('id_', ''));
}



