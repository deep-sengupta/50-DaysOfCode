const albumArt = document.getElementById('album-art'),
trackTitle = document.getElementById('track-title'),
trackArtist = document.getElementById('track-artist'),
currentTimeDisplay = document.getElementById('current-time-display'),
totalTimeDisplay = document.getElementById('total-time-display'),
seekProgress = document.getElementById('seek-progress'),
seekBar = document.getElementById('seek-bar'),
previousButton = document.getElementById('previous-button'),
nextButton = document.getElementById('next-button'),
playToggleButton = document.getElementById('play-toggle-button'),
backgroundImage = document.getElementById('background-image');

const audio = new Audio();

const tracks = [
    {
        path: '/music-player/music/Ben10.mp3',
        title: 'Ben 10',
        cover: '/music-player/images/Ben10.jpg',
        artist: 'Moxie, Andy Sturmer',
    },
    {
        path: '/music-player/music/NinjaHattori.mp3',
        title: 'Ninja Hattori',
        cover: '/music-player/images/NinjaHattori.jpg',
        artist: 'Sonoko Kawai',
    },
    {
        path: '/music-player/music/Shinchan.mp3',
        title: 'Shinchan',
        cover: '/music-player/images/Shinchan.jpeg',
        artist: 'Akiko Yajima',
    }
];

let currentTrackIndex = 0;
let isPlaying = false;

function togglePlayback(){
    if(isPlaying){
        pauseAudio();
    } else{
        playAudio();
    }
}

function playAudio(){
    isPlaying = true;
    playToggleButton.classList.replace('fa-circle-play', 'fa-circle-pause');
    playToggleButton.setAttribute('title', 'Pause');
    audio.play();
}

function pauseAudio(){
    isPlaying = false;
    playToggleButton.classList.replace('fa-circle-pause', 'fa-circle-play');
    playToggleButton.setAttribute('title', 'Play');
    audio.pause();
}

function loadTrack(track){
    albumArt.classList.remove('active-album-art');
    audio.src = track.path;
    trackTitle.textContent = track.title;
    trackArtist.textContent = track.artist;
    albumArt.src = track.cover;
    backgroundImage.src = track.cover;

    setTimeout(() => {
        albumArt.classList.add('active-album-art');
    }, 100);
}

function changeTrack(direction){
    currentTrackIndex = (currentTrackIndex + direction + tracks.length) % tracks.length;
    loadTrack(tracks[currentTrackIndex]);
    playAudio();
}

function updateSeekBar(){
    const { duration, currentTime } = audio;
    const progressPercent = (currentTime / duration) * 100;
    seekProgress.style.width = `${progressPercent}%`;

    const formatTime = (time) => String(Math.floor(time)).padStart(2, '0');
    totalTimeDisplay.textContent = `${formatTime(duration / 60)}:${formatTime(duration % 60)}`;
    currentTimeDisplay.textContent = `${formatTime(currentTime / 60)}:${formatTime(currentTime % 60)}`;
}

function setSeekPosition(e){
    const width = seekBar.clientWidth;
    const clickX = e.offsetX;
    audio.currentTime = (clickX / width) * audio.duration;
}

playToggleButton.addEventListener('click', togglePlayback);
previousButton.addEventListener('click', () => changeTrack(-1));
nextButton.addEventListener('click', () => changeTrack(1));
audio.addEventListener('ended', () => changeTrack(1));
audio.addEventListener('timeupdate', updateSeekBar);
seekBar.addEventListener('click', setSeekPosition);

loadTrack(tracks[currentTrackIndex]);