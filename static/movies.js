var $dialog = document.getElementById('mydialog');
var image = document.getElementById('film-notes');
var list_image = document.getElementById('film-notes').getElementsByTagName('img');


   for(var i = 0; i < list_image.length; i++){
      console.log(list_image[i].src);
   }


image.addEventListener('click', function() {
          $dialog.showModal();
});