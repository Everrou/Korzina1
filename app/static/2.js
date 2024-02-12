

document.addEventListener('DOMContentLoaded', function () {
  const starsContainer = document.querySelector('.stars');
  const reviewForm = document.getElementById('reviewForm');
  const userReviewsContainer = document.getElementById('userReviews');

  // Создание звезд для оценки
  for (let i = 1; i <= 5; i++) {
    const star = document.createElement('div');
    star.classList.add('star');
    star.dataset.rating = i;
    star.addEventListener('mouseover', () => highlightStars(i));
    starsContainer.appendChild(star);
  }

  // Обработка отправки отзыва
  window.submitReview = function () {
    const rating = parseInt(starsContainer.dataset.rating);
    const reviewText = document.getElementById('reviewText').value.trim();

    if (rating === 0 || reviewText === '') {
      alert('Пожалуйста, выберите оценку и напишите отзыв.');
      return;
    }

    const review = document.createElement('div');
    review.classList.add('review');
    review.innerHTML = `<div class="rating" data-rating="${rating}"></div><p>${reviewText}</p>`;
    userReviewsContainer.appendChild(review);

    // Сброс формы
    starsContainer.dataset.rating = 0;
    document.getElementById('reviewText').value = '';
    highlightStars(0);
  };

  // Подсветка звезд при наведении
  function highlightStars(num) {
    const stars = starsContainer.querySelectorAll('.star');
    stars.forEach((star, index) => {
      star.classList.toggle('filled', index < num);
    });
    starsContainer.dataset.rating = num;
  }
});
