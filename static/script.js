const nav = document.getElementById('nav');
const textBox = document.getElementById('text-box');
const transcribeButton = document.getElementById('transcribeButton');
const crimeWatchButton = document.getElementById('crimeWatchButton');

transcribeButton.addEventListener('click', goToTranscribePage);
crimeWatchButton.addEventListener('click', goToCrimeWatchPage);

function goToTranscribePage(event){
    window.location.href = '/transcribe';
}

async function goToCrimeWatchPage(event){
    window.location.href = '/crimeWatch';
}