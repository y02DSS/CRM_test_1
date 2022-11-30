alert('error')

var elem = document.getElementById('id_name');

$('input[name="name"]').keyup(function(){
    var $that = $(this).val();
    $('input[name="comment"]').val($that);
    });
