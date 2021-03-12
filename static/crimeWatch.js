const backButton = document.getElementById("back-button");

backButton.addEventListener('click', goToHomeScreen)

function goToHomeScreen(event) {
  window.location.href = '/';
}

var divElement = document.getElementById('viz1615211158697');                    
var vizElement = divElement.getElementsByTagName('object')[0];                    
vizElement.style.width='1016px';vizElement.style.height='991px';                    
var scriptElement = document.createElement('script');                    
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
vizElement.parentNode.insertBefore(scriptElement, vizElement);