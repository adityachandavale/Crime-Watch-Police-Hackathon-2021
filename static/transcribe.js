const backButton = document.getElementById("back-button");
const transcribeButton = document.getElementById("transcribe");

backButton.addEventListener('click', goToHomeScreen);
transcribeButton.addEventListener('click', transcribeAudio)

function goToHomeScreen(event) {
  window.location.href = '/';
}

function transcribeAudio(event) {
  fetch('/convert_to_text').then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data);
  }).catch(function() {
    console.log("Booo");
  });
}

const recordAudio = () =>
  new Promise(async resolve => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    let audioChunks = [];

    mediaRecorder.addEventListener('dataavailable', event => {
      audioChunks.push(event.data);
    });

    const start = () => {
      audioChunks = [];
      mediaRecorder.start();
    };

    const stop = () =>
      new Promise(resolve => {
        mediaRecorder.addEventListener('stop', () => {
          const audioBlob = new Blob(audioChunks);
          const audioUrl = URL.createObjectURL(audioBlob);
          const audio = new Audio(audioUrl);
          const play = () => audio.play();
          resolve({ audioChunks, audioBlob, audioUrl, play });
        });

        mediaRecorder.stop();
      });

    resolve({ start, stop });
});

const sleep = time => new Promise(resolve => setTimeout(resolve, time));

const recordButton = document.querySelector('#record');
const stopButton = document.querySelector('#stop');
const playButton = document.querySelector('#play');
const saveButton = document.querySelector('#save');
const savedAudioMessagesContainer = document.querySelector('#saved-audio-messages');

let recorder;
let audio;

recordButton.addEventListener('click', async () => {
  recordButton.setAttribute('disabled', true);
  stopButton.removeAttribute('disabled');
  playButton.setAttribute('disabled', true);
  saveButton.setAttribute('disabled', true);
  if (!recorder) {
    recorder = await recordAudio();
  }
  recorder.start();
});

stopButton.addEventListener('click', async () => {
recordButton.removeAttribute('disabled');
stopButton.setAttribute('disabled', true);
playButton.removeAttribute('disabled');
saveButton.removeAttribute('disabled');
audio = await recorder.stop();
});

playButton.addEventListener('click', () => {
  audio.play();
});

saveButton.addEventListener('click', () => {
  const audioBlob = new Blob(audio.audioChunks, { 'type' : 'audio/webm'});
  const reader = new FileReader();
  reader.readAsDataURL(audioBlob);
  reader.onload = () => {
    const base64AudioMessage = reader.result.split(',')[1];
    console.log(reader.result)
    fetch("/saveMessage", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: base64AudioMessage })
    }).then(res => 
      {
        console.log(res)
      }
    );
  }
});