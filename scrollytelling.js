
  const sections = document.querySelectorAll('.section');
  let currentSectionIndex = 0;

  function scrollToSection(index) {
    sections[index].scrollIntoView({ behavior: 'smooth' });
  }

  function handleScroll(event) {
    const scrollPosition = window.scrollY;
    const windowHeight = window.innerHeight;
    const sectionHeight = sections[currentSectionIndex].offsetHeight;
    const sectionTop = sections[currentSectionIndex].offsetTop;

    if (scrollPosition >= sectionTop + sectionHeight - windowHeight) {
      currentSectionIndex++;
      scrollToSection(currentSectionIndex);
    }
  }

  window.addEventListener('scroll', handleScroll);
