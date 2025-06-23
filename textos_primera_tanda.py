class PrimeraTanda():
    def __init__(self):
        inicio=""


    def lecturadomingo(self):
        return """
        <div class="contenido-homilia">
    <h1>Evangelio de hoy y lecturas</h1>
    <h2>Primera lectura</h2>
    <h3>Lectura del libro de los Hechos de los apóstoles 12, 1-11</h3>
    <p></p>
    <p>En aquellos días, el rey Herodes decidió arrestar a algunos miembros de la Iglesia para maltratarlos. Hizo pasar
        a cuchillo a Santiago, hermano de Juan. Al ver que esto agradaba a los judíos, decidió detener a Pedro. Eran los
        días de los Ácimos. Después de prenderlo, lo metió en la cárcel, entregándolo a la custodia de cuatro piquetes
        de cuatro soldados cada uno; tenía intención de presentarlo al pueblo pasadas las fiestas de Pascua. Mientras
        Pedro estaba en la cárcel bien custodiado, la Iglesia oraba insistentemente a Dios por él.</p>
    <p>Cuando Herodes iba a conducirlo al tribunal, aquella misma noche, estaba Pedro durmiendo entre dos soldados,
        atado con cadenas. Los centinelas hacían guardia a la puerta de la cárcel.</p>
    <p>De repente, se presentó el ángel del Señor, y se iluminó la celda. Tocando a Pedro en el costado, lo despertó y
        le dijo:<br>«Date prisa, levántate».</p>
    <p>Las cadenas se le cayeron de las manos, y el ángel añadió:<br>«Ponte el cinturón y las sandalias».</p>
    <p>Así lo hizo, y el ángel le dijo:<br>«Envuélvete en el manto y sígueme».</p>
    <p>Salió y lo seguía sin acabar de creerse que era realidad lo que hacía el ángel, pues se figuraba que estaba
        viendo una visión. Después de atravesar la primera y la segunda guardia, llegaron al portón de hierro que daba a
        la ciudad, que se abrió solo. ante ellos. Salieron, y anduvieron una calle y de pronto se marchó el ángel.</p>
    <p>Pedro volvió en sí y dijo:<br>«Ahora sé realmente que el Señor ha enviado a su ángel para librarme de las manos
        de Herodes y de toda la expectación del pueblo de los judíos».</p>
    <p></p>
    <h2>Salmo</h2>
    <h3>Salmo 33, 2-3. 4-5. 6-7. 8-9 R/. El Señor me libró de todas mis ansias.</h3>
    <p></p>
    <p>Bendigo al Señor en todo momento,<br>su alabanza está siempre en mi boca;<br>mi alma se gloría en el
        Señor:<br>que los humildes lo escuchen y se alegren. R/.</p>
    <p>Proclamad conmigo la grandeza del Señor,<br>ensalcemos juntos su nombre.<br>Yo consulté al Señor, y me
        respondió,<br>me libró de todas mis ansias. R/.</p>
    <p>Contempladlo, y quedaréis radiantes,<br>vuestro rostro no se avergonzará.<br>El afligido invocó al Señor,<br>él
        lo escuchó y lo salvó de sus angustias. R/.</p>
    <p>El ángel del Señor acampa en torno a quienes lo temen<br>y los protege.<br>Gustad y ved qué bueno es el
        Señor,<br>dichoso el que se acoge a él. R/.</p>
    <p></p>
    <h2>Segunda lectura</h2>
    <h3>Lectura de la segunda carta del apóstol san Pablo a Timoteo 4, 6-8. 17-18</h3>
    <p></p>
    <p>Querido hermano:<br>Yo estoy a punto de ser derramado en libación y el momento de mi partida es inminente.</p>
    <p>He combatido el noble combate, he acabado la carrera, he conservado la fe.</p>
    <p>Por lo demás, me está reservada la corona de la justicia, que el Señor, juez justo, me dará en aquel día; y no
        sólo a mí, sino también a todos los que hayan aguardado con amor su manifestación.</p>
    <p>Mas el Señor me estuvo a mi lado y me dio fuerzas para que, a través de mí, se proclamara plenamente el mensaje y
        lo oyeran todas las naciones. Y fui librado de la boca del león.</p>
    <p>El Señor me librará de toda obra mal y me salvará llevándome a su reino celestial.</p>
    <p>A él la gloria por los siglos de los siglos. Amén.</p>
    <p></p>
    <h2>Evangelio del día</h2>
    <h3>Lectura del santo evangelio según san Mateo 16, 13-19</h3>
    <p></p>
    <p>En aquel tiempo, al llegar a la región de Cesárea de Filipo, Jesús preguntó a sus discípulos:<br>«¿Quién dice la
        gente que es el Hijo del hombre?»</p>
    <p>Ellos contestaron:<br>«Unos que Juan Bautista, otros que Elías, otros que Jeremías o uno de los profetas».</p>
    <p>Él les preguntó:<br>«Y vosotros, ¿quién decís que soy yo?»</p>
    <p>Simón Pedro tomó la palabra y dijo:<br>«Tú eres el Mesías, el Hijo de Dios vivo».</p>
    <p>Jesús le respondió:<br>«¡Bienaventurado tú, Simón, hijo de Jonás!, porque eso no te lo ha revelado nadie de carne
        y hueso, sino mi Padre que está en el cielo.</p>
    <p>Ahora yo te digo: tú eres Pedro, y sobre esta piedra edificaré mi Iglesia, y el poder del infierno no la
        derrotará.</p>
    <p>Te daré las llaves del reino de los cielos; lo que ates en la tierra quedará atado en el cielo, y lo que desates
        en la tierra quedará desatado en los cielos».</p>
    <p></p>
</div>" 
"""

    def lunes(self):
        return ""

    def martes(self):
        return ""

    def miercoles(self):
        return ""

    def jueves(self):
        return ""

    def viernes(self):
        return ""

    def sabado(self):
        return ""

    def procesar(self):
        # Aquí se pueden agregar más métodos para procesar el texto
        return self.texto.upper()  # Ejemplo de procesamiento: convertir a mayúsculas

    def __str__(self):
        return f"Texto procesado: {self.procesar()}"
