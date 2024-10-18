const CACHE_NAME = 'offline-cache-v1';
const urlsToCache = [
    '/',
    '/static/Favicon.png',
    '/static/css/botones.css',
    '/static/css/boot/bootstrap.css',
    '/static/css/boot/bootstrap.min.css',
    '/static/fonts/neutraface2display_thin.otf',
    '/static/fonts/Novecento CondUltraBold.otf',
    '/static/img/imagenes_CP50/CAMPO/btndomingo.png',
    '/static/img/imagenes_CP50/CAMPO/btnjueves.png',
    '/static/img/imagenes_CP50/CAMPO/btnMapa01.png',
    '/static/img/imagenes_CP50/CAMPO/btnmiercoles.png',
    '/static/img/imagenes_CP50/CAMPO/btnsabado.png',
    '/static/img/imagenes_CP50/CAMPO/btnviernes.png',
    '/static/img/imagenes_CP50/CAMPO/btn_cancionero2.png',
    '/static/img/imagenes_CP50/CAMPO/btn_eucaristia.png',
    '/static/img/imagenes_CP50/CAMPO/btn_eucaristia_claro.png',
    '/static/img/imagenes_CP50/CAMPO/btn_liturgia_manana_claro.png',
    '/static/img/imagenes_CP50/CAMPO/btn_oracion_manana.png',
    '/static/img/imagenes_CP50/CP50/ceferinosinfondo01.png',
    '/static/img/imagenes_CP50/CP50/circulo_01.png',
    '/static/img/imagenes_CP50/CP50/dbmm.png',
    '/static/img/imagenes_CP50/CP50/DBStefan.png',
    '/static/img/imagenes_CP50/CP50/domingosavio01.png',
    '/static/img/imagenes_CP50/CP50/donboscofrente.png',
    '/static/img/imagenes_CP50/CP50/gente_bosco.png',
    '/static/img/imagenes_CP50/CP50/laurasinfondo01.png',
    '/static/img/imagenes_CP50/CP50/logocampobosco.png',
    '/static/img/imagenes_CP50/CP50/logoredondo01.png',
    '/static/img/imagenes_CP50/CP50/mariamazarello01.png',
    '/static/img/imagenes_CP50/CP50/santos_salesianos.png',
    '/static/img/imagenes_CP50/cpb50_sin.png',
    '/static/img/atras.png',
    '/static/js/jquery.min.js',
    '/static/js/service-worker.js',
    '/static/js/sweetalert2.all.min.js',
    '/static/js/bootjs/bootstrap.min.js',
    '/inicio',
    '/miercoles',
    '/miercoles/laudes',
    '/miercoles/misa',
    '/jueves',
    '/jueves/laudes',
    '/jueves/misa',
    '/viernes',
    '/viernes/laudes',
    '/viernes/misa',
    '/sabado',
    '/sabado/laudes',
    '/sabado/misa',
    '/domingo',
    '/domingo/laudes',
    '/domingo/misa',
    '/cancionero',
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                return response || fetch(event.request);
            })
    );
});


