    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
      const question = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');

      question.addEventListener('click', () => {
        answer.classList.toggle('show');
      });
    });




let trilho = document.getElementById('trilho')
let body = document.querySelector('body')

trilho.addEventListener('click', ()=>{
    trilho.classList.toggle('dark')
    body.classList.toggle('dark')
} )



  const header = document.getElementById('meuHeader');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
      header.classList.add('sombra');
    } else {
      header.classList.remove('sombra');
    }
  });

