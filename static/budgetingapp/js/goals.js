function hideCard(idText) { 
  document.getElementById(idText).style.display="none"; 
}

/* JQuery
*/
$(function () {
  $("#id_end_date").datetimepicker({
    format: 'Y-m-d H:i',
  });
});



