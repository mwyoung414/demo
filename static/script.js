const modal = document.querySelector('.modal');
const modalWrapper = document.querySelector('.modal-wrapper');
const signUpButton = document.getElementById('signUpModalBtn');
const closeButton = document.querySelector('.close');

signUpButton.onclick = () => {
    modal.style.display = 'flex';
    modalWrapper.style.display = 'flex';
};

closeButton.onclick = () => {
    modalWrapper.style.display = 'none';
};

window.onclick = (event) => {
    if (event.target === modalWrapper) {
        modal.style.display = 'none';
    }
};