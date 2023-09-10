let vh = window.innerHeight * 0.01; document.documentElement.style.setProperty('--vh', vh+"px");
window.addEventListener("resize", ()=>{ let vh = window.innerHeight * 0.01; document.documentElement.style.setProperty('--vh', vh+"px"); })

// Service Worker 등록
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('service-worker.js')
      .then(function(registration) {
        console.log('Service Worker 등록 성공:', registration.scope);
      })
      .catch(function(error) {
        console.log('Service Worker 등록 실패:', error);
      });
  });
}