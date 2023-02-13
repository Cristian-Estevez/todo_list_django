
function toggleTheme() {
  let currentTheme = document.getElementById('body').classList[0];
  if (currentTheme == "light") {
    document.getElementById('body').classList.remove('light');
    document.getElementById('body').classList.add('dark');
    $('#theme-toggler-text').html('Light mode');
    $('#theme-toggler-icon').html('light_mode');
  } else {
    document.getElementById('body').classList.remove('dark');
    document.getElementById('body').classList.add('light');
    $('#theme-toggler-text').html('Dark mode');
    $('#theme-toggler-icon').html('dark_mode');
  }
}