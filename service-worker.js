// 필요한 파일 캐싱
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('my-cache').then(function(cache) {
      return cache.addAll([
        'index-ce7cf7e7.css',
        'script.js',
        'index.html'
        'index-7dc1f56b.js',
        '/',
      ]);
    })
  );
});

// 오프라인 요청 대응
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    }).catch(function() {
      return caches.match('index.html');
    })
  );
});