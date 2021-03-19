const backButton = document.getElementById("back-button");
const transcribeButton = document.getElementById("transcribe");
const translateButton = document.getElementById("translate");

backButton.addEventListener('click', goToHomeScreen);
transcribeButton.addEventListener('click', transcribeAudio);
translateButton.addEventListener('click', translate);

function goToHomeScreen(event) {
  window.location.href = '/';
}

function transcribeAudio(event) {
  transcribeButton.setAttribute('disabled', true);
  fetch('/convert_to_text').then(function(data) {
    return data.blob().then((data)=>{
        var a = document.createElement("a");
        a.href = URL.createObjectURL(data);
        a.setAttribute("download", "transcribed_pdf.pdf");
        a.click();
        transcribeButton.removeAttribute('disabled');
    }
    );
});
}

function translate(event) {
  translateButton.setAttribute('disabled', true);
  fetch('/translate_text').then(function(data) {
    return data.blob().then((data)=>{
        var a = document.createElement("a");
        a.href = URL.createObjectURL(data);
        a.setAttribute("download", "translated_pdf.pdf");
        a.click();
        translateButton.removeAttribute('disabled');
    }
    );
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
  const audioBlob = new Blob(audio.audioChunks, { 'type' : 'audio/wav'});
  let url = window.URL.createObjectURL(audioBlob);
  saveFile('recorded_audio',url);
});

function saveFile(fileName,urlFile){
  let a = document.createElement("a");
  a.style = "display: none";
  document.body.appendChild(a);
  a.href = urlFile;
  a.download = fileName;
  a.click();
  window.URL.revokeObjectURL(url);
  a.remove();
}