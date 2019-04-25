
'check_out_btn' = document.querySelector('check_out_btn')
'checked_out' = document.querySelector('checked_out')
if ('checked_out' == false) {
  document.getElementById('check_out_btn').disabled = false
} else if ('checked_out' == true) {
  document.getElementById('check_out_btn').disabled = true
}
