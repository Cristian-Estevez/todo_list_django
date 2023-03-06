$(document).ready(function () {
  //checkbox click event
  $('.checkbox-blank').on('click', function (event) {
    event.stopPropagation();
    let iconText = event.target.innerHTML;
    if (iconText === 'check_box_outline_blank') {
      event.target.innerHTML = 'check_box';
      event.target.classList.add('task-done')
    } else {
      event.target.innerHTML = 'check_box_outline_blank';
      event.target.classList.remove('task-done')
    }
  });

  // hover effects
  $('.folder').hover(function (event) {
    $(event.currentTarget).find(".folder-container").css('background-color', 'rgba(0, 0, 0, .15)');
    $(event.currentTarget).find(".folder-container").css('color', 'rgb(255, 255, 255)');
    $(event.currentTarget).find(".folder-container:last-child").css('border-radius', '0 0 16px 16px');
  }, function (event) {
    $(event.currentTarget).find(".folder-container").css('background-color', '');
    $(event.currentTarget).find(".folder-container").css('color', '');
    $(event.currentTarget).find(".folder-container").css('border-radius', '');
  });

  // open folder
  $('.folder').on('click', function () {
    if (!$(this).find('.folder-tasks-container').attr('class').includes('max-height-40')) {
      $(this).find('.folder-tasks-container').addClass('max-height-40 mb-3');
      $(this).css('background-color', 'rgb(0, 0, 0, .15)');
      $(this).find(".folder-container .featured-icon-container .list-icon").text('folder_open');
    } else {
      $(this).find('.folder-tasks-container').removeClass('max-height-40 mb-3');
      $(this).css('background-color', '')
      $(this).find(".folder-container .featured-icon-container .list-icon").text('folder');
    };
  });

  $('.task').hover(function (event) {
    $(event.currentTarget).css('background-color', 'rgba(0, 0, 0, .15)');
  }, function (event) {
    $(event.currentTarget).css('background-color', '');
  });

  /**
   * login
  */
  $('#login-icon, #login-close').on('click', toggleLoginModal);

  $('.task').on('click', showDescription);
})

function showDescription(event) {
  event.stopPropagation();
  Array.from($(this).parent().find('.task')).forEach(task => {
    task.classList.remove('max-height-40');
  });
  $(this).toggleClass('max-height-40');
}

function toggleLoginModal() {
  $('.login-section').toggleClass('flex');
}

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

