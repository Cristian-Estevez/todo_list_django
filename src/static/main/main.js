$(document).ready(function () {
  $('.checkbox-blank').on('click', function (event) {
    $(event.target).html = 'check_box'  aca revisar funcion
  })
})

function toggleTheme() {
  let currentTheme = document.getElementById('body').classList[0];
  if (currentTheme == 'light') {
    document.getElementById('body').classList.remove('light');
    document.getElementById('body').classList.add('dark');
    $('#theme-toggler-icon').html('light_mode');
    document.getElementById('theme-toggler-icon').title = 'Light mode';
  } else {
    document.getElementById('body').classList.remove('dark');
    document.getElementById('body').classList.add('light');
    $('#theme-toggler-icon').html('dark_mode');
    document.getElementById('theme-toggler-icon').title = 'Dark mode';
  }
}