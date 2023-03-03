function getUserData(username, password) {
  const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
  document.cookie = `password=${password}`;

  // Make an AJAX request to the server to get the user's data.
  $.ajax({
    url: '/getUserData',
    method: 'POST',
    data: { query },
    success: (data) => {
      console.log(data);
    },
    error: (err) => {
      console.error(err);
    }
  });
}
