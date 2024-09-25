const left = document.querySelector('.left')
const right = document.querySelector('.right')
const wrapper = document.querySelector('.wrapper')

left.addEventListener('mouseenter', () => wrapper.classList.add('hover-left'))
left.addEventListener('mouseleave', () => wrapper.classList.remove('hover-left'))

right.addEventListener('mouseenter', () => wrapper.classList.add('hover-right'))
right.addEventListener('mouseleave', () => wrapper.classList.remove('hover-right'))