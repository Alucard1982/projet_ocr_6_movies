var $dialog = document.getElementById('mydialog');
var image = document.getElementById('film-notes');
var button_play = document.getElementById('button-best');


var carousel_best_movies_position1 = document.getElementById('film-notes').getElementsByClassName('slider_best_movies')[0]
var carousel_best_movies_position2 = document.getElementById('film-notes').getElementsByClassName('slider_best_movies')[1]
var carousel_best_movies_position3 = document.getElementById('film-notes').getElementsByClassName('slider_best_movies')[2]
var carousel_best_movies_position4 = document.getElementById('film-notes').getElementsByClassName('slider_best_movies')[3];
var click_forward_best_movies = document.getElementById('click_forward');
var click_back_best_movies = document.getElementById('click_back');

var carousel_familly_position1 = document.getElementById('film-categorie1').getElementsByClassName('slider_familly')[0]
var carousel_familly_position2 = document.getElementById('film-categorie1').getElementsByClassName('slider_familly')[1]
var carousel_familly_position3 = document.getElementById('film-categorie1').getElementsByClassName('slider_familly')[2]
var carousel_familly_position4 = document.getElementById('film-categorie1').getElementsByClassName('slider_familly')[3];
var click_forward_familly= document.getElementById('click_forward_familly');
var click_back_familly = document.getElementById('click_back_familly');

var carousel_horror_position1 = document.getElementById('film-categorie2').getElementsByClassName('slider_horror')[0]
var carousel_horror_position2 = document.getElementById('film-categorie2').getElementsByClassName('slider_horror')[1]
var carousel_horror_position3 = document.getElementById('film-categorie2').getElementsByClassName('slider_horror')[2]
var carousel_horror_position4 = document.getElementById('film-categorie2').getElementsByClassName('slider_horror')[3];
var click_forward_horror= document.getElementById('click_forward_horror');
var click_back_horror = document.getElementById('click_back_horror');

var carousel_music_position1 = document.getElementById('film-categorie3').getElementsByClassName('slider_music')[0]
var carousel_music_position2 = document.getElementById('film-categorie3').getElementsByClassName('slider_music')[1]
var carousel_music_position3 = document.getElementById('film-categorie3').getElementsByClassName('slider_music')[2]
var carousel_music_position4 = document.getElementById('film-categorie3').getElementsByClassName('slider_music')[3];
var click_forward_music= document.getElementById('click_forward_music');
var click_back_music = document.getElementById('click_back_music');

var image_best_movies = [];
var list_img_familly = [];
var list_img_horror = [];
var list_img_music = [];
var position = 0;

var data_list_best_movie = [];

function ajax_best_movies(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          data_list_best_movie=JSON.parse(this.responseText);

      }
    };
    xmlhttp.open("GET","http://127.0.0.1:5000/best_movie/", true);
    xmlhttp.send();
}
function ajax_best_movies(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          data_list=JSON.parse(this.responseText);
          for(var i = 0; i < data_list.length; i++){
            image_best_movies.push(data_list[i]['image_url'])
          }
      }
    };
    xmlhttp.open("GET","http://127.0.0.1:5000/best_movies/", true);
    xmlhttp.send();
}
function ajax_categorie_familly(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          data_list=JSON.parse(this.responseText);
          for(var i = 0; i < data_list.length; i++){
            list_img_familly.push(data_list[i]['image_url'])
          }
      }
    };
    xmlhttp.open("GET","http://127.0.0.1:5000/familly/", true);
    xmlhttp.send();
}
function ajax_categorie_horror(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          data_list=JSON.parse(this.responseText);
          for(var i = 0; i < data_list.length; i++){
            list_img_horror.push(data_list[i]['image_url'])
          }
      }
    };
    xmlhttp.open("GET","http://127.0.0.1:5000/horror/", true);
    xmlhttp.send();
}
function ajax_categorie_music(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          data_list=JSON.parse(this.responseText);
          for(var i = 0; i < data_list.length; i++){
            list_img_music.push(data_list[i]['image_url'])
          }
      }
    };
    xmlhttp.open("GET","http://127.0.0.1:5000/music/", true);
    xmlhttp.send();
}
function forwardClick(list, carousel1, carousel2, carousel3, carousel4){
    position++;
    carousel1.src=list[position%7];
    carousel2.src=list[(position+1)%7];
    carousel3.src=list[(position+2)%7];
    carousel4.src=list[(position+3)%7];
}
function backClick(list, carousel1, carousel2, carousel3, carousel4){
    if (position == 0){
        position=list.length;
    }
    position--;
    carousel1.src=list[position%7];
    carousel2.src=list[(position+1)%7];
    carousel3.src=list[(position+2)%7];
    carousel4.src=list[(position+3)%7];
}

function modal_best_movie(data_list_best_movie, $dialog ){
        $dialog.innerHTML="<p>looooooooooooooool</p>"
        $dialog.showModal()


}


image.addEventListener('click', function(){ $dialog.showModal();});
button_play.addEventListener('click', function(){ modal_best_movie(data_list_best_movie, $dialog );});


click_forward_best_movies.addEventListener('click',function (){forwardClick(image_best_movies, carousel_best_movies_position1,
carousel_best_movies_position2, carousel_best_movies_position3, carousel_best_movies_position4);});
click_back_best_movies.addEventListener('click',function (){backClick(image_best_movies, carousel_best_movies_position1,
carousel_best_movies_position2, carousel_best_movies_position3, carousel_best_movies_position4);});

click_forward_familly.addEventListener('click',function (){forwardClick(list_img_familly, carousel_familly_position1,
carousel_familly_position2, carousel_familly_position3, carousel_familly_position4);});
click_back_familly.addEventListener('click',function (){backClick(list_img_familly, carousel_familly_position1,
carousel_familly_position2, carousel_familly_position3, carousel_familly_position4);});

click_forward_horror.addEventListener('click',function (){forwardClick(list_img_horror, carousel_horror_position1,
carousel_horror_position2, carousel_horror_position3, carousel_horror_position4);});
click_back_horror.addEventListener('click',function (){backClick(list_img_horror, carousel_horror_position1,
carousel_horror_position2, carousel_horror_position3, carousel_horror_position4);});

click_forward_music.addEventListener('click',function (){forwardClick(list_img_music, carousel_music_position1,
carousel_music_position2, carousel_music_position3, carousel_music_position4);});
click_back_music.addEventListener('click',function (){backClick(list_img_music, carousel_music_position1,
carousel_music_position2, carousel_music_position3, carousel_music_position4);});

document.addEventListener ("DOMContentLoaded", function (){ajax_best_movies();});
document.addEventListener ("DOMContentLoaded", function (){ajax_categorie_familly();});
document.addEventListener ("DOMContentLoaded", function (){ajax_categorie_horror();});
document.addEventListener ("DOMContentLoaded", function (){ajax_categorie_music();});


