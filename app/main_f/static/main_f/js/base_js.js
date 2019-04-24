function hide(){
  $('.userexit').css({
    'display': 'none'
  });
  $('.exists_user').css({
    'display': 'none'
  });
  $('.empty_user').css({
    'display': 'inline-block'
  });
}

function show(){
  $('.userexit').css({
    'display': 'inline-block'
  });
  $('.exists_user').css({
    'display': 'inline-block'
  });
  $('.empty_user').css({
    'display': 'none'
  });
}


function ajax_post(type){
  if (type == 'log_in'){
    console.log('login is working!')
    var _url = 'user_in';
    var _data_1 = $('#id_login').val();
    var _data_2 = $('#id_password').val();
  }
  if (type == 'log_out'){
    console.log('logout is working!')
    var _url = 'user_out';
    var _data_1 = '';
    var _data_2 = '';
  }
  if (type == 'send_message'){
    console.log('send is working!')
    var _url = 'message';
    var _data_1 = $('#id_reciever').val();
    var _data_2 = $('#id_text').val();
  }

  $.ajax({
    url : _url,
    type : 'POST',
    data : { data_1 : _data_1, data_2 : _data_2 },

    success : function(json) {
        console.log('success');
        console.log(json);
        if (type == 'log_in'){
          if (json['status'] != 'wrong password'){
            show();
          }
        }
        else if (type == 'log_out'){
          hide();
        }
    },

    error : function() {
        console.log('failed');
        console.log(json);
    }
  });
}


$(document).ready(function() {
  if ( $('.username').text() == '' ){
    hide();
  }
  else{
    show();
  }

  $('.ajax_form').on('submit', function(event){
    event.preventDefault();
    ajax_post($(this).attr('id'));
  });
})
