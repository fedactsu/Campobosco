
const CACHE_VERSION = 'V1.27.10.2024.14.35';
const CACHE_NAME = `my-cache-${CACHE_VERSION}`;


self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return fetch('/cache-version.json')
                .then((response) => response.json())
                .then((data) => {
                    return cache.addAll(data.files);
                });
        })
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});

self.addEventListener('message', (event) => {
    if (event.data === 'checkForUpdate') {
        fetch('/cache-version.json')
            .then((response) => response.json())
            .then((data) => {
                if (data.version !== CACHE_VERSION) {
                    self.clients.matchAll().then((clients) => {
                        clients.forEach((client) => {
                            client.postMessage('updateAvailable');
                        });
                    });
                }
            });
    } else if (event.data === 'skipWaiting') {
        self.skipWaiting();
    }
});