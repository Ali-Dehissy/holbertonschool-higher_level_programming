const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (movies) {
  for (let i = 0; i < movies.results.length; i++) {
    $('ul#list_movies').append(`<li>${movies.results[i].title}</li>`);
  }
});
