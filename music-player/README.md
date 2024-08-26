# Music Player

### How to Add More Songs
- To add more songs to the playlist, modify the tracks array in the `script.js` file:
```
const tracks = [
    {
        path: '/path/to/your/song1.mp3',
        title: 'Song Title 1',
        cover: '/path/to/your/cover1.jpg',
        artist: 'Artist Name 1',
    },
    {
        path: '/path/to/your/song2.mp3',
        title: 'Song Title 2',
        cover: '/path/to/your/cover2.jpg',
        artist: 'Artist Name 2',
    },
    // Add more songs here
];
```

- path: The relative path to the audio file.
- title: The name of the song.
- cover: The relative path to the cover image for the song.
- artist: The name of the artist.