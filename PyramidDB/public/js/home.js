// let theURL = "https://www.googleapis.com/books/v1/volumes?q=isbn:0553275860";
let theURL = 'http://127.0.0.1:8080/users/4'

function callApi(anElement) {  
  fetch(theURL).then(function(response) {
    return response.json();
  }).then(function(data) {
    // anElement.innerHTML=data.items[0].volumeInfo.title;
    anElement.innerHTML =
      "<p>Name: " + data.user_info.name + "</p>" +
      "<p>Superpower: " + data.user_info.superpower + "</p>";
  }); 
}

document.addEventListener("DOMContentLoaded", function() {
  let btn = document.querySelector('#burger');
  let sb = document.querySelector('.overlay_sidebar');  

  btn.onclick = function toggle() {
    sb.classList.toggle('closed'); 
    if(!sb.classList.contains('closed'))
      callApi(sb);
  }
});