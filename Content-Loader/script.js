const header = document.getElementById('header')
const title = document.getElementById('title')
const excerpt = document.getElementById('excerpt')
const profile_img = document.getElementById('profile_img')
const name = document.getElementById('name')
const date = document.getElementById('date')
const loading_bgs = document.querySelectorAll('.loading-bg')
const loading_texts = document.querySelectorAll('.loading-text')

function loadContent(){
    if(navigator.onLine){
        header.innerHTML = '<img src="./BgImg.jpg" alt="Bg img"/>'
        title.innerHTML = 'Explore the world with us'
        excerpt.innerHTML = 'Join our community to discover amazing places and experiences. Let us help you plan your next adventure.'
        profile_img.innerHTML = '<img src="./ProfileImg.jpg" alt="Profile Image"/>'
        name.innerHTML = 'Doraemon Bhai'
        date.innerHTML = 'Sept 03, 2112'

        loading_bgs.forEach(bg => bg.classList.remove('loading-bg'))
        loading_texts.forEach(text => text.classList.remove('loading-text'))
    } else{
        title.innerHTML = 'Offline mode'
        excerpt.innerHTML = 'Unable to load content. Please check your internet connection.'
        loading_bgs.forEach(bg => bg.classList.remove('loading-bg'))
        loading_texts.forEach(text => text.classList.remove('loading-text'))
    }
}

window.addEventListener('load', () => {
    setTimeout(loadContent, 2000);
})

window.addEventListener('online', loadContent)
window.addEventListener('offline', loadContent)