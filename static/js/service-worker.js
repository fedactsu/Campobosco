const CACHE_VERSION = 'V1.27.10.2024.12.54';
const urlsToCache = [
    '/',
    '/static/Favicon.png',
    '/static/css/botones.css',
    '/static/css/boot/bootstrap.css',
    '/static/css/boot/bootstrap.min.css',
    '/static/css/leaflet.css',
    '/static/fonts/neutraface2display_thin.otf',
    '/static/fonts/NovecentoCondUltraBold.otf',
    '/static/img/atras.png',
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
    '/static/img/imagenes_CP50/CAMPO/btn_campobosco_acerca.png',
    '/static/img/imagenes_CP50/CAMPO/btn_oracion_manana.png',
    '/static/img/imagenes_CP50/CAMPO/horario_claro_1.png',
    '/static/img/imagenes_CP50/CAMPO/horario_rosado_1.png',
    '/static/img/imagenes_CP50/CAMPO/btn_turin.png',
    '/static/img/imagenes_CP50/CAMPO/btn_roma.png',
    '/static/img/imagenes_CP50/CAMPO/btn_nizza.png',
    '/static/img/imagenes_CP50/CAMPO/btn_mornese.png',
    '/static/img/imagenes_CP50/CAMPO/btn_ibecchi.png',
    '/static/img/imagenes_CP50/CAMPO/atras.png',
    '/static/img/imagenes_CP50/CAMPO/vocacional.png',
    '/static/img/imagenes_CP50/CAMPO/btn_mapa_offline.png',
    '/static/img/imagenes_CP50/CAMPO/btn_mapa_online.png',
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
    '/static/img/imagenes_CP50/vocacional/1_fma.png',
    '/static/img/imagenes_CP50/vocacional/2_fma.png',
    '/static/img/imagenes_CP50/vocacional/2_sdb.png',
    '/static/img/imagenes_CP50/vocacional/3_fma.png',
    '/static/img/imagenes_CP50/vocacional/3_sdb.png',
    '/static/img/imagenes_CP50/vocacional/4_fma.png',
    '/static/img/imagenes_CP50/vocacional/4_sdb.png',
    '/static/img/imagenes_CP50/vocacional/5_fma.png',
    '/static/img/imagenes_CP50/vocacional/5_sdb.png',
    '/static/img/imagenes_CP50/vocacional/sdb.png',
    '/static/img/imagenes_CP50/mapa/mapa_picarquin.jpeg',
    '/static/img/imagenes_CP50/mapa/norte.png',
    '/static/img/imagenes_CP50/documentos/btn_carta_identidad.png',
    '/static/img/imagenes_CP50/documentos/btn_documentos_gnral.png',
    '/static/img/imagenes_CP50/documentos/btn_protocolo.png',
    '/static/img/imagenes_CP50/talleres/btn_talleres.png',
    '/static/img/imagenes_CP50/talleres/talleres.jpeg',
    '/static/img/imagenes_CP50/cpb50_sin.png',
    '/static/img/imagenes_CP50/10240por1024.png',
    '/static/js/jquery.min.js',
    '/static/js/leaflet.js',
    '/static/js/holder.js',
    '/static/js/service-worker.js',
    '/static/js/sweetalert2.all.min.js',
    '/static/js/bootjs/bootstrap.min.js',
    '/static/js/bootjs/bootstrap.min.js.map',
    '/static/js/bootjs/bootstrap.bundle.min.js',
    '/static/js/bootjs/popper.min.js',
    '/static/js/tamanoletra.js',
    '/static/js/bootjs/jquery.mlens-1.7.min.js',
    '/inicio',
    '/miercoles',
    '/miercoles/laudes',
    '/miercoles/misa',
    '/miercoles/horario',
    '/jueves',
    '/jueves/laudes',
    '/jueves/misa',
    '/jueves/horario',
    '/viernes',
    '/viernes/laudes',
    '/viernes/misa',
    '/viernes/horario',
    '/sabado',
    '/sabado/laudes',
    '/sabado/misa',
    '/sabado/horario',
    '/domingo',
    '/domingo/laudes',
    '/domingo/misa',
    '/domingo/horario',
    '/mapalugar',
    '/mapalugar/online',
    '/mapalugar/offline',
    '/vocacional',
    '/acercade',
    '/documentos',
    '/documentos/carta_identidad',
    '/documentos/protocolo_campamento',
    '/talleres',
    '/cancionero',
    '/cancionero/0',
    '/cancionero/1',
    '/cancionero/2',
    '/cancionero/3',
    '/cancionero/4',
    '/cancionero/5',
    '/cancionero/6',
    '/cancionero/7',
    '/cancionero/8',
    '/cancionero/9',
    '/cancionero/10',
    '/cancionero/11',
    '/cancionero/12',
    '/cancionero/13',
    '/cancionero/14',
    '/cancionero/15',
    '/cancionero/16',
    '/cancionero/17',
    '/cancionero/18',
    '/cancionero/19',
    '/cancionero/20',
    '/cancionero/21',
    '/cancionero/22',
    '/cancionero/23',
    '/cancionero/24',
    '/cancionero/25',
    '/cancionero/26',
    '/taller/1',
    '/taller/2',
    '/taller/3',
    '/taller/4',
    '/taller/5',
    '/taller/6',
    '/taller/7',
    '/taller/8',
    '/taller/9',
    '/taller/10',
    '/taller/11',
    '/taller/12',
    '/taller/13',
    '/taller/14',
    '/taller/15',
    '/taller/16',
    '/taller/17',
    '/taller/18',
    '/taller/19',
    '/taller/20',
    '/taller/21',
    '/taller/22',
    '/taller/23',
    '/taller/24',
    '/taller/25',
    '/taller/26',
    '/taller/27',
    '/taller/28',
    '/taller/29',
    '/taller/30',
    '/taller/31',
    '/taller/32',
    '/taller/33',
    '/taller/34',
    '/taller/35',
    '/taller/36',
    '/taller/37',
    '/taller/38',
    '/taller/39',
    '/taller/40',
    '/taller/41',
    '/taller/42',
    '/taller/43',
    '/taller/44',
    '/taller/45',
    '/taller/46',
    '/taller/47',
    '/taller/48',
    '/taller/49',
    '/taller/50',
    '/taller/51',
    '/taller/52',
    '/taller/53',
    '/taller/54',
    '/taller/55',
    '/taller/56',
    '/taller/57',


];

async function updateCacheIfNeeded() {
    try {
        // Obtén la versión del caché desde el servidor
        const response = await fetch('/cache-version.json');
        const config = await response.json();

        // Compara la versión en el servidor con la versión local
        if (config.cacheVersion !== CACHE_VERSION) {
            console.log(`Nueva versión de caché detectada: ${config.cacheVersion}. Actualizando...`);

            // Limpia el caché antiguo
            const cacheNames = await caches.keys();
            await Promise.all(
                cacheNames.map(cacheName => caches.delete(cacheName))
            );

            // Crea un nuevo caché
            const cache = await caches.open(config.cacheVersion);
            await cache.addAll(urlsToCache);

            console.log('Caché actualizado con éxito');
        }
    } catch (error) {
        console.log('Error al actualizar el caché:', error);
    }
}

// Evento de instalación
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_VERSION)
            .then((cache) => cache.addAll(urlsToCache))
    );
});

// Evento de activación: Actualiza el caché si hay una nueva versión
self.addEventListener('activate', (event) => {
    event.waitUntil(updateCacheIfNeeded());
});

// Evento fetch para interceptar las solicitudes
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => response || fetch(event.request))
    );

    // Intenta actualizar el caché en cada fetch si hay conexión
    event.waitUntil(
        fetch('/cache-version.json')
            .then(response => response.json())
            .then(config => {
                if (config.cacheVersion !== CACHE_VERSION) {
                    return updateCacheIfNeeded();
                }
            })
            .catch(error => console.log("Sin conexión. Usando caché existente.", error))
    );
});