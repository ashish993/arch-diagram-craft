// Give keyboard users a predictable way to inspect wide diagram regions.
document.querySelectorAll('[role="region"][tabindex="0"]').forEach((region) => {
  region.addEventListener('keydown', (event) => {
    const step = Math.max(120, Math.round(region.clientWidth * 0.7));
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      region.scrollBy({ left: event.key === 'ArrowRight' ? step : -step });
    } else if (event.key === 'Home') {
      event.preventDefault();
      region.scrollTo({ left: 0 });
    } else if (event.key === 'End') {
      event.preventDefault();
      region.scrollTo({ left: region.scrollWidth });
    }
  });
});
