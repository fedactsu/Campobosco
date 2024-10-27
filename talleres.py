class talleres():
    def __init__(self):

        self.talleres = [
            [1, "Fútbol", "18 - 29 años", " Cancha 1 del sector acampada"],
            [2, "Fútbol", "12 - 17 años", " Cancha 2 del sector acampada"],
            [3, "Volleyball femenino", "12 - 17 años", " Costado módulo 1 "],
            [4, "Volleyball 1", "18 - 29 años", " Costado módulo 2 "],
            [5, "Volleyball 2", "18 - 29 años", " Multicancha "],
            [6, "Basketball", "14 - 22 años", " Multicancha"],
            [7, "Quemadas", "12 - 16 años", " Costado módulo 2"],
            [8, "Tenis de Campo", "12 - 16 años", " Rotonda / cerca de turín"],
            [9, "Pesca con mosca", "12 - 16 años", " Costado módulo 3"],
            [10, "Trekking", "17 - 29 años", " Zona Nizza"],
            [11, "Taekwondo", "15 - 20 años", " Costado módulo 1"],
            [12, "Cheerleader", "15 - 20 años", " Costado módulo 2"],
            [13, "Acondicionamiento Físico", "15 - 20 años", " Costado módulo 3"],
            [14, "Orientación Terrestre",
                "todas las edades (12 - 29)", "Zona Mornese"],
            [15, "Nudos", "todas las edades (12 - 29)", " Costado comedor "],
            [16, "Escultismo",
                "todas las edades (12 - 29)", " Costado comedor"],
            [17, "Coro Litúrgico 1", "17 - 29 años", " Zona Turín "],
            [18, "Coro Litúrgico 2", "17 - 29 años", " Zona Turín "],
            [19, "Coro", "12 - 16 años", " Zona Turín "],
            [20, "Canto", "12 - 16 años", " Zona Nizza "],
            [21, "Canto", "17 - 22 años", " Zona Nizza"],
            [22, "Manualidades",
                "todas las edades (12 - 29)", " Patio techado módulo 1"],
            [23, "Manualidades",
                "todas las edades (12 - 29)", " Sala 2 (módulo 1)"],
            [24, "Manualidades", "12 - 16 años", " Sala 1 (módulo 2) "],
            [25, "Manualidades", "12 - 16 años", "Sala 2 (módulo 2) "],
            [26, "Mandalas",
                "todas las edades (12 - 29)", " Sala 1 (módulo 3)"],
            [27, "Dibujo con patrones en tiza", "12 - 16 años", " Sector capilla"],
            [28, "Origami", "12 - 16 años", " Patio techado módulo 1"],
            [29, "Origami", "17 - 29 años", " Patio techado módulo 2"],
            [30, "Fotografía e I.A.",
                "todas las edades (12 - 29)", " Zona Roma"],
            [31, "Fotografía", "12 - 16 años", " Zona Roma "],
            [32, "Autoconocimiento", "17 - 29 años", " Zona Roma"],
            [33, "Desarrollo Personal", "17 - 29 años", " Zona Ibecchi"],
            [34, "Liderazgo", "12 - 18 años", " Patio techado módulo 3"],
            [35, "Cueca", "todas las edades (12 - 29)", " Zona Mornese"],
            [36, "Cueca", "todas las edades (12 - 29)", " Zona Roma"],
            [37, "Danza contemporánea",
                "todas las edades (12 - 29)", " Zona Mornese"],
            [38, "Danza contemporánea", "12 - 16 años", " Zona Ibecchi"],
            [39, "Salsa", "12 - 16 años", " Zona Turín"],
            [40, "Reciclaje", "12 - 16 años", " Patio techado módulo 3"],
            [41, "Agroecología y plantación sustentable",
                "12 - 16 años", " Zona Nizza"],
            [42, "Jardinería", "12 - 20 años", " Zona Mornese"],
            [43, "Tallado en madera", "12 - 17 años", " Patio techado módulo 2"],
            [44, "Encuadernación", "17 - 29 años", " Sala 2 (módulo 3)"],
            [45, "Electricidad domiciliaria",
                "15 - 20 años", " Sala 1 (módulo 1)"],
            [46, "Introducción a la liturgia",
                "todas las edades (12 - 29)", " Capilla del encuentro"],
            [47, "Animación", "15 - 20 años", " Sector comedor"],
            [48, "Malabarismo artístico",
                "todas las edades (12 - 29)", " Zona Roma "],
            [49, "Mimos / Sketches",
                "todas las edades (12 - 29)", " Zona Turín "],
            [50, "Mate y truco",
                "todas las edades (12 - 29)", " Zona Mornese "],
            [51, "Lengua de Señas", "16 - 29 años", " Costado módulo 1"],
            [52, "Magia", "12 - 16 años", " Costado módulo 2"],
            [53, "Animé y religión",
                "todas las edades (12 - 29)", " Costado módulo 3"],
            [54, "Wash Prevention",
                "todas las edades (12 - 29)", " Sector enfermería"],
            [55, "Primeros auxilios psicológico",
                "todas las edades (12 - 29)", " Sector enfermería"],
            [56, "Primeros auxilios comunitarios", "todas las edades (12 - 29)", " Sector enfermería"]]

    def main(self, id):
        if id == 1:
            return self.futbol1829()
        if id == 2:
            return self.futbol1217()
        if id == 3:
            return self.volleyfemenino()
        if id == 4:
            return self.volley1()
        if id == 5:
            return self.volley2()
        if id == 6:
            return self.Basketball()
        if id == 7:
            return self.Quemadas()
        if id == 8:
            return self.Tenis_de_Campo()
        if id == 9:
            return self.Pesca_con_mosca()
        if id == 10:
            return self.Trekking()
        if id == 11:
            return self.Taekwondo()
        if id == 12:
            return self.Cheerleader()
        if id == 13:
            return self.AcondicionamientoFisico()
        if id == 14:
            return self.OrientacionTerrestre()
        if id == 15:
            return self.Nudos()
        if id == 16:
            return self.Escultismo()
        if id == 17:
            return self.Coro_liturgico1()
        if id == 18:
            return self.Coro_liturgico2()

    def futbol1829(self):
        id_taller = 1
        nombre_taller = "Fútbol"
        edad = "18 - 29 años"
        lugar = " Cancha 1 del sector acampada"
        tallerista = "Peter Vu Duc"
        integrantes = [["Bastian Balvoa", "Linares"],
                       ["Martin alonso mendez crespo ", "Linares "],
                       ["Jose Valdes", "Linares"],
                       ["Fabián Maldonado", "Valparaíso"],
                       ["Nicolas Sáez ", "Valparaiso "],
                       ["Edgard Rodriguez Naiman", "Punta Arenas "],
                       ["Erick Jaime ", "Santiago "],
                       ["Vicente Rodríguez ", "Iquique "],
                       ["felipe Nuñez ", "Santiago "],
                       ["Martin Lara", "Linares "],
                       ["Sebastián Díaz", "Antofagasta"],
                       ["philipp reynuaba", "copiapo"],
                       ["Bastian ramirez ", "Copiapo"],
                       ["Fernando Cortes ", "Copiapo "],
                       ["Cristóbal Paez", "Copiapo"],
                       ["Franco Valdés ", "Copiapo"],
                       ["Joaquin Bascur ", "Santiago"],
                       ["Victor peres ", "Alto hospicio"],
                       ["Alberto sepulveda", "Concepcion"],
                       ["Cristobal Alvear ", "Santiago"],
                       ["Jhairo Céspedes ", "La cisterna "],
                       ["Mateo Alonso Arancibia Miranda ", "La Cisterna "],
                       ["Pedro Montecino", "Concepcion"],
                       ["Guillermo Campos", "Santiago"],
                       ["Felipe rojas", "Colina "],
                       ["Diego Huaccha ", "Santiago "],
                       ["lukas cepeda", "santiago"],
                       ["Lucian guzmán ", "Santiago "],
                       ["Benjhamin Rivera ", "Santiago centro "]]
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes

    def futbol1217(self):
        id_taller = 2
        nombre_taller = "Fútbol"
        edad = "12 - 17 años"
        lugar = "Cancha 2 del sector acampada"
        tallerista = "Juan Domingo Salinas"
        integrantes = [["Benjamin pastor", "Linares"],
                       ["Jose Moya", "Talca"],
                       ["Julio Sánchez", "Linares"],
                       ["Damián Vergara Escobar", "Linares"],
                       ["Lindsay Rodriguez", "Punta Arenas"],
                       ["Bastian Balvoa", "Linares"],
                       ["Hector Gutierrez jara", "Linares"],
                       ["Martin Alonso Mendez Crespo", "Linares"],
                       ["Lucas Bustamante", "linares"],
                       ["Maximiliano alejandro gutierrez lagos", "Linares"],
                       ["Martin jaque bello", "Linares"],
                       ["Jose Valdes", "Linares"],
                       ["Martin Herrera", "Valparaíso"],
                       ["Benjamin stull", "Talca"],
                       ["Cristobal Muñoz", "Linares"],
                       ["Jonathan domenes", "Punta arenas"],
                       ["Tomas donicke", "Punta arenas"],
                       ["Vicente ponce manque", "Calama"],
                       ["Benjamín Toro Soto", "Linares"],
                       ["Sebastien cárdenas", "Punta arenas"],
                       ["Sebastián Norambuena", "Linares"],
                       ["Ethan alcarraz", "Calama"],
                       ["Alonso Reyes", "Santiago"],
                       ["Angel castillo", "Punta Arenas"],
                       ["Paul Peralta", "Iquique"],
                       ["Agustín Pardo", "iquique"],
                       ["Luckas Varela", "Iquique"],
                       ["Joaquín Ferreira", "Iquique"],
                       ["Alexander Astudillo", "Iquique"],
                       ["Eduardo Barraza", "Iquique"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes

    def volleyfemenino(self):
        id_taller = 3
        nombre_taller = "Volleyball femenino"
        edad = "12 - 17 años"
        lugar = "Costado Miguel Magone"
        tallerista = "Natalia Ponce"
        integrantes = [["Victoria Tapia", "los andes"],
                       ["Francisca Segovia", "Los Andes"],
                       ["Iska Lopez", "Los andes"],
                       ["Isidora Montoya", "Los Andes"],
                       ["Martina Trinidad Solís", "Los andes"],
                       ["Florencia Oyarzo", "Punta arenas"],
                       ["Martina Lazo", "Los Andes"],
                       ["Sebastian Cisterna", "Linares"],
                       ["Matilda Xiomara Lupallante Alarcón", "Linares"],
                       ["Catalina Vergara", "Santiago"],
                       ["Catalina Duque", "Curicó"],
                       ["Julieta Freire", "Colbun"],
                       ["Catalina Riquelme", "Los Andes"],
                       ["Monserrat Gutiérrez", "Molina"],
                       ["Katherine garces", "Linares"],
                       ["Maite Urra", "Molina"],
                       ["Laura Gómez", "Puerto Natales"],
                       ["Victoria Pinto", "Maule"],
                       ["Sofia riffo", "santa cruz"],
                       ["Javiera Canales", "Talca"],
                       ["Felipe Vergara", "Talca"],
                       ["Cristobal Garrido", "Maule"],
                       ["Alan ogaz Suazo", "Talca"],
                       ["Elizabeth Beatriz Reyes González", "Santa cruz"],
                       ["Ignacia Carolina Farias Alegria", "Talca"],
                       ["Tania Araya Álvarez", "Punta Arenas"],
                       ["Bárbara Cruzat", "Talca"],
                       ["Josefina Antonia Martínez Muñoz", "Santa Cruz"],
                       ["Renata Illanes", "Talca, maule"],
                       ["Mónica Orellana Contreras", "Talca"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes

    def volley1(self):
        id_taller = 4
        nombre_taller = "Volleyball 1"
        edad = "18 - 29 años"
        lugar = "Multicancha"
        tallerista = "Frank Arriagada"
        integrantes = [["Nancy Barros", ""],
                       ["Yaré Urrutia", ""],
                       ["Josefa Areyte", ""],
                       ["Renato Molina", ""],
                       ["Santiago Muñoz", ""],
                       ["Catalina araya", ""],
                       ["Juaquin Alexander Salas Amigo", ""],
                       ["Salvador Cortes", ""],
                       ["Amalia onetto", ""],
                       ["Almendra Vilches", ""],
                       ["Tomas Arce", ""],
                       ["Juan Pablo Gutiérrez robles", ""],
                       ["alfredo araneda", ""],
                       ["Joaquin Pulgar Z.", ""],
                       ["Sebastian Ruiz", ""],
                       ["Felipe Mendez", ""],
                       ["Benjamin Carter", ""],
                       ["Francisca Gutiérrez Lineros", ""],
                       ["José Paillalef", ""],
                       ["Carlos Reyes", ""],
                       ["Matías Figueroa", ""],
                       ["Fernanda Parra", ""],
                       ["Esteban Valenzuela", ""],
                       ["Benjamin Vilche", ""],
                       ["Francisco Santibáñez", "Concepción"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes

    def volley2(self):
        id_taller = 5  
        nombre_taller = "Volleyball 2"
        edad = "18 - 29 años"
        lugar = "Costado Bartolomé Garelli"
        tallerista = "Carlos Durán"
        integrantes = [["Martina opazo","Hijas de maria auxiliadora"],
                        ["Emilia Sánchez","Voleyball"],
                        ["Martin Jaque bello","Liceo María Auxiliadora"],
                        ["Martin Herrera","Colegio salesiano de Valparaíso"],
                        ["Ignacio Jorquera","Salesiano Valparaíso"],
                        ["Frangellis Schmidt","Salesiano Valparaíso"],
                        ["Fausto Guerra","Colegio Salesiano de Valparaíso"],
                        ["Alanis Meneses","Liceo José Miguel Infante."],
                        ["Constanza Mancilla","Mjs don Bosco"],
                        ["Antonella oliva","Mjs"],
                        ["Isidora Muñoz","Instituto sagrada familia"],
                        ["Francisco Mora","Comunidad misionera Salesiana"],
                        ["Victor Carretero","Comunidad misionera Salesiana Calama"],
                        ["Joaquín Núñez","El patrocinio de san jose"],
                        ["Sergio Parra Ramirez","Colegio Tecnico Industrial Don Bosco Antofagasta"],
                        ["Ignacia carvajal","Salesianos de don Bosco"],
                        ["Belén Cerda","Salesianos Linares"],
                        ["Renato Olave","Centro Educativo Salesianos Talca"],
                        ["Sebastián Ruiz","salesianos alameda"],
                        ["Giovanny Opazo","Salesianos alameda"],
                        ["Israel de los Santos","Escuela industrial Salesianos Copiapó"],
                        ["Mayra Alvarado","MJS/ CAS"],
                        ["Valentina Perez","Liceo Salesiano Monseñor Jose Fagnano"],
                        ["Sofia Arancibia","EJE"],
                        ["Matías Araya","Escuela Industrial Salesiana San Ramón"],
                        ["matias veliz","escuela industrial salesiana san ramon"],
                        ["Sebastian Torrejon","Escuela San Ramón Salesianos La Serena"],
                        ["Benjamin Morales","Salesiano la serena"],
                        ["Sofía Constanzo","cfive"],
                        ["Máximo Valderrama","Voleibol"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Basketball(self):
        id_taller = 6
        nombre_taller = "Basketball"
        edad = "14 - 22 años"
        lugar = "Multicancha"
        tallerista = "Felipe González"
        integrantes = [["Renata Navea","Los Andes"],
                        ["Carolina Pérez","Los Andes"],
                        ["Maite Seco","Los Andes"],
                        ["Javiera Gutiérrez Pizarro","Puerto Montt"],
                        ["Colomba Olmedo","Santa cruz"],
                        ["Renata Acevedo","Los Andes"],
                        ["Fernanda Del Castillo","Linares"],
                        ["Krishna Graces Serón levicán","Puerto montt"],
                        ["maximiliano valdebenito gutierrez","talca"],
                        ["Javiera Letelier","Talca"],
                        ["Francisco Villablanca","Linares"],
                        ["Madeleine Núñez","Talca"],
                        ["Julián Contreras","Linares"],
                        ["Javiera Labra Silva","Santa Cruz"],
                        ["Martina Salas","Los Andes"],
                        ["Danae Arteaga","Puerto montt"],
                        ["Martín Barros Lara","Linares"],
                        ["José Pablo Carrasco Zuñiga","Linares"],
                        ["Thomas Valladares","Valparaíso"],
                        ["Martin Herrera","Valparaíso"],
                        ["Veronica Álvarez","Valparaíso"],
                        ["Harold bobadilla","Talca"],
                        ["Alonso Sanchez Mansilla","Punta Arenas"],
                        ["Agustina Miralles","Puerto Natales"],
                        ["Paloma bahamonde","Puerto Natales"],
                        ["Isabel frias","Puerto natales"],
                        ["Isidora Barra","Santiago"],
                        ["Joaquin Riveros","Santiago"],
                        ["Vicente Ríos","Santiago"],
                        ["Ignacia Paredes","Punta Arenas"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Quemadas(self): 
        id_taller = 7
        nombre_taller = "Quemadas"
        edad = "12 - 16 años"
        lugar = "Costado Bartolomé Garelli"
        tallerista = "Carolina Millán"
        integrantes = [["Martina Bahamondes","Santa Cruz"],
                        ["Krishna Bahamondes","Santa Cruz"],
                        ["Catalina Muñoz","Molina"],
                        ["Amapola Huenchur Suardo","Los andes"],
                        ["Rafaela Paz Lopez Lucero","Los Andes"],
                        ["Pascal Villavicencio","Molina"],
                        ["Renata Jara","Los Andes"],
                        ["Catalina Trujillo","punta arenas"],
                        ["Ignacia paredes","Punta Arenas"],
                        ["Javiera Valenzuela","Iquique"],
                        ["Amanda Velásquez","Iquique"],
                        ["Catalina Contreras","Iquique"],
                        ["Emilia vivar","Iquique"],
                        ["Mia Muñoz","Iquique"],
                        ["Isidora carreñi","iquique"],
                        ["Ámbar García","Iquique"],
                        ["Ema levill","Santiago de chile"],
                        ["Florencia Nieto","Pto. Natales"],
                        ["Josefa Toro","Santiago centro"],
                        ["Maria Fernanda Cárcamo Concha","Punta Arenas"],
                        ["Danitza Copa","Calama"],
                        ["Sebastian apaza","Calama"],
                        ["Tiare caiguan","Punta arenas"],
                        ["Ana Cumare","Punta Arenas"],
                        ["Martina Tapia","Santiago"],
                        ["Gabriel Guerrero","Santiago"],
                        ["Cristofer Peña Garrido","valdivia"],
                        ["Mauroluis almuna san martin","Iquique"],
                        ["Amaru Figueroa","Iquique"],
                        ["Josefa Ignacia areyte Navarro","Santiago"],
                        ["Manuel Delgado","Valdivia"],
                        ["Diego Ortiz","Valparaiso"],
                        ["Constanza Ancamilla","Iquique"],
                        ["Giovanni Contreras","Antofagasta"],
                        ["Felipe ayavire","Calama"],
                        ["Constanza Gahona","Calama"]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Tenis_de_Campo(self): 
        id_taller = 8 
        nombre_taller = "Tenis de Campo"
        edad = "12 - 16 años"
        lugar = "Rotonda cerca de zona Turín"
        tallerista = "Carmen Parada"
        integrantes = [["Martina Carreño","santa cruz"],
                        ["Trinidad Ordoñez","Santa Cruz"],
                        ["Laura Tobar","santa cruz"],
                        ["Giuliana Palavecino","Talca"],
                        ["María_José Loyola","santiago"],
                        ["Isabella Guerrero Ortega","Valparaiso"],
                        ["Vania Fuentes","Valparaíso"],
                        ["Antonella Diaz Castillo","Valparaíso"],
                        ["Arturo Aroca","Santiago"],
                        ["José Llancafil","Colina"],
                        ["Sebastián Moris","Iquique"],
                        ["Rafael Patricio Esteban Quezada Saldías","Iquique"],
                        ["Andreas Werner Pohl Aravena","Santiago"],
                        ["Felipe rojas","colina"],
                        ["Constanza Quiroz Cofré","Santiago"],
                        ["Daniela Iturra","Santiago"],
                        ["blanca rubio","santiago"],
                        ["benjamin castillo","santiago"],
                        ["Michelle Highfield","Antofagasta"],
                        ["Danniza","Antofagasta"],
                        ["Diego Vergara","Santiago"],
                        ["Nicolás Quezada","Santiago"],
                        ["Oriana Policroni","Santiago"],
                        ["Javier lazo","Copiapo"],
                        ["Pedro Puelles rojas","Copiapo"],
                        ["José Tapia","Alto Hospicio"],
                        ["Emmy Catagua","Alto Hospicio"],
                        ["Cristobal sanchez","Copiapo"],
                        ["Catalina Machicado","Iquique"],
                        ["Valentina Hidalgo","Santiago"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Pesca_con_mosca(self): 
        id_taller = 9
        nombre_taller = "Pesca con mosca"
        edad = "12 - 16 años"
        lugar = "Costado Emma Ferrero"
        tallerista = "Luis González "
        integrantes =  [["Augusto Asenjo","Molina"],
                        ["Bastián Alonso León Valdés","Molina"],
                        ["Fernanda Muñoz","Talca"],
                        ["agustin fuentes","molina"],
                        ["Tihare Toro","Valparaíso"],
                        ["Antonella Diaz","Valparaiso"],
                        ["Ema levill","Santiago de chile"],
                        ["Gustavo garrido","Punta Arenas"],
                        ["Ivan Barriga","Calama"],
                        ["Jan Pierre Monsalvez","Calama"],
                        ["Luciano Barra López","Iquique"],
                        ["Nicolas Aguilera","Iquique"],
                        ["Matías Alfaro","Iquique"],
                        ["Benjamin Lopez","Iquique"],
                        ["Héctor Oyarzo","Valdivia"],
                        ["Damian barrientos","Valdivia"],
                        ["Juan Pablo De La Fuente Rodríguez","Iquique"],
                        ["Cristóbal Espinoza","Valdivia"],
                        ["Benjamín aros","Valdivia"],
                        ["Esteban gatica","Valdivia"],
                        ["Sebastian Fuenzalida","Iquique"],
                        ["Benjamin Gutierrez","Santiago"],
                        ["Juan Pablo Tapia","Santiago"],
                        ["Sophia Rozas","Santiago"],
                        ["Alfredo Araneda Méndez","santiago"],
                        ["Juan Pablo Gutiérrez robles","Santiago"],
                        ["Tomas Arce","Santiago"],
                        ["Thomas morales","Santiago"],
                        ["joaquin sanhueza","Santiago"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes

    def Trekking(self): 
        id_taller = 10
        nombre_taller = "Trekking"
        edad = "17 a 21 años"
        lugar = "Zona Nizza"
        tallerista = "Alonso Moena"
        integrantes =  [["Libertad Medina Urtubia","Los Andes"],
                        ["Flor Muñoz","Linares"],
                        ["Daniela Rodriguez","Puerto Montt"],
                        ["Constanza Donoso","Santa Cruz"],
                        ["Sofía Ponce","Punta Arenas"],
                        ["Juan Pedro Catepillan","Punta Arenas"],
                        ["Lucas","Sta Cruz"],
                        ["Florencia Hernández","Punta arenas"],
                        ["Esteban Cifuentes","Punta Arenas"],
                        ["Maira Sanchez","Talca"],
                        ["Bianca jara","Talca"],
                        ["Antonia Araya Sepúlveda","Linares"],
                        ["Ayelén González","Punta Arenas"],
                        ["Zahira gallardo gonzalez","Puerto natales"],
                        ["Juan Miguel Sanhueza","Linares"],
                        ["Belén Araya Ibáñez","Linares"],
                        ["Aylin Reyes Lipán","Linares"],
                        ["Brayan Peralta","Maule"],
                        ["Benjamin Alarcon","Linares"],
                        ["Anaís Ayleen Vargas Maldonado","Puerto Montt"],
                        ["Yasmin Silva Chavez","Maule"],
                        ["Renata rojas","Talca"],
                        ["Camila Orellana","Maule"],
                        ["pascale huenten","punta arenas"],
                        ["Diego Soto","Punta Arenas"],
                        ["MaríaJosé Sepúlveda","Punta Arenas"],
                        ["ignacia soto","punta arenas"],
                        ["Benjamín Jorquera","Santiago"],
                        ["Millaray Rojas","Linares"],
                        ["Christobal Velozo Valdés","Linares"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Taekwondo(self): 
        id_taller = 11
        nombre_taller = "Taekwondo"
        edad = "15 - 20 años"
        lugar = "Costado Migel Magone"
        tallerista = "Felipe Andrade"
        integrantes = [["Constanza Alfaro","Santiago"],
                        ["Anneth Subiabre","Puerto Natales"],
                        ["Antonella Muñoz","Puerto natales"],
                        ["Dalexa Roca","Iquique"],
                        ["Fernanda Riffo","Santiago"],
                        ["Maira Miranda","Santiago, Chile"],
                        ["Maite san martín","punta arenas"],
                        ["Juan llaiepn","Punta arenas"],
                        ["Luna lobos","Calama"],
                        ["Alexis Paolo Ayabire Ayabire","Calama"],
                        ["Millaray Vargas","Santiago"],
                        ["Dominique Ávalos","Santiago"],
                        ["Jeanfranco Ojeda Otarola","Punta Arenas"],
                        ["Maximo Sequeida Ulloa","Santiago"],
                        ["Ricardo Barajas","Calama"],
                        ["Jairon Bedel Contreras Contreras","Antofagasta"],
                        ["Juan Ignacio Sáez Prado","Linares"],
                        ["Alexander Rodríguez","Antofagasta"],
                        ["Maximiliano Pérez","Antofagasta"],
                        ["Jordan ruiz","Antofagasta"],
                        ["Sebastian Figueroa","Antofagasta"],
                        ["yermilco molina","antofagasta"],
                        ["Victor Astudillo","Antofagasta"],
                        ["Joaquín Alvarado","Punta arenas"],
                        ["Mariana Fernández","Alto hospicio"],
                        ["Lucas Yoveti Medrano","Alto hospicio"],
                        ["Damian Barria","Santiago"],
                        ["Josepha Sepulveda","Linares"],
                        ["María povea","Linares"],
                        ["Constanza Carcamo Ule","Puerto natales"]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Cheerleader(self): 
        id_taller = 12 
        nombre_taller = "Cheerleader"
        edad = "15 - 20 años"
        lugar = "Costado Bartolomé Garelli"
        tallerista = "Juan Chávez"
        integrantes = [["Ailyn Zambrano","Punta Arenas"],
                        ["Fernanda Muñoz","Punta Arenas"],
                        ["Tamara Valdés","Talca"],
                        ["Renata Jara","Valparaíso"],
                        ["Laura Vilches","La cisterna"],
                        ["Mariana Pinto","Santiago"],
                        ["Amada Cova","Pto. Natales"],
                        ["Juan Miguel Sanhueza","Linares"],
                        ["Tania Araya Álvarez","Punta Arenas"],
                        ["Antonia Araya","Linares"],
                        ["Martyna Iturra Ibáñez","LINARES"],
                        ["Araxi Santos","Linares"],
                        ["Antonia Miranda","Linares"],
                        ["Sofia Elizalde","Iquique"],
                        ["Tamara Ortega","Linares"],
                        ["Fernanda Abigail González Vivar","Puerto Montt"],
                        ["Elizabeth Masyel Olivares Vega","Talca"],
                        ["Ignacia Cortés","Santiago"],
                        ["Jeismar Lucena","Valparaíso"],
                        ["Anais lobos","Valparaiso"],
                        ["Sofía Campos","Linares"],
                        ["Constanza Quiroz","Santiago"],
                        ["Maria Gracia Villagra","Santiago"],
                        ["Maite Alarcon","santiago"],
                        ["Maria jesus hernandez Guajardo","Talca"],
                        ["Camila Marquez","Santiago"],
                        ["Ayelen Ávila Jara","Linares"],
                        ["Valentina Castro","Santiago"],
                        ["Camila Pérez","Santiago"],
                        ["Valentina Villacorta","Copiapó"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def AcondicionamientoFisico(self): 
        id_taller = 13 
        nombre_taller = "Acondicionamiento Físico"
        edad = "15 - 20 años"
        lugar = "Costado Emma Ferrero"
        tallerista = "Matías Garrido"
        integrantes = [["Pia Ignacia Pérez Duarte","Santa Cruz"],
                        ["Consuelo Gutierrez","Santa Cruz"],
                        ["Josefa Gómez Fierro","Santa Cruz"],
                        ["Aylin Vianney Ramirez Negron","Puerto Montt"],
                        ["Josefina Herrera","Santa Cruz"],
                        ["Maximiliano Jesús Marín Rojas","Talca"],
                        ["Javiera Martínez","Linares"],
                        ["Josefa Barañados Rodríguez","Iquique"],
                        ["Martin Herrera","Valparaíso"],
                        ["Esteban ignacio gonzalez bahamondes","Talca-maule"],
                        ["Anahí Pulgar","Santiago"],
                        ["Antonia Navarro","Valparaiso"],
                        ["Danna Rosales","Santiago"],
                        ["Agustina Soto","Talca"],
                        ["Amanda Gonzalez","Talca"],
                        ["Maximiliano alejandro gutierrez lagos","Linares"],
                        ["Martyna Ignacia Iturra Ibáñez","Linares"],
                        ["Lizardo Rebolledo","Iquique"],
                        ["Juan Mancilla","Iquique"],
                        ["Jerry guerrero","Punta arenas"],
                        ["Amalia onetto","Santiago"],
                        ["montserrat cifuentes","santiago"],
                        ["Almendra Vilches","Santiago"],
                        ["Claudia Gutiérrez","Linares"],
                        ["Anayhs Figueroa","Linares"],
                        ["Valken lener","Santiago"],
                        ["Ema levill","Santiago de chile"],
                        ["Alejandro Piñones","Antofagasta"],
                        ["Cristóbal Reyes","Santiago"],
                        ["Jesus Marcano","santiago"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def OrientacionTerrestre(self): 
        id_taller = 14 
        nombre_taller = "Orientación Terrestre"
        edad = "todas las edades (12 - 29)"
        lugar = "Zona Mornese"
        tallerista = "Luz Cubillos "
        integrantes =  [["Mayra Aguilera","Puerto Montt"],
                        ["Valentina Ibacache","Puerto Montt"],
                        ["Sebastián Valenzuela Galvez","Valparaíso"],
                        ["Ámbar Cisterna","Punta Arenas"],
                        ["Sofía González","Valparaíso"],
                        ["Santiago mena","Santiago"],
                        ["Joaquin Trobok","Colina"],
                        ["Constanza jofre","Antofagasta"],
                        ["Alhelí Cortés","Linares"],
                        ["Alondra Cuevas","Copiapó"],
                        ["Javiera Riquelme","Copiapó"],
                        ["Ailyn Ibáñez","Copiapó"],
                        ["Laura Riascos","Copiapo"],
                        ["Martín Martínez","Copiapó"],
                        ["Renato Alvarez Gonzalez","Valparaiso"],
                        ["Victor perez gonzalez","Alto hospicio"],
                        ["Carla Tureo","Valparaiso"],
                        ["Francisca Norambuena","Linares"],
                        ["Anthony Gamboa","Antofagasta"],
                        ["Jhoel rios","Antofagasta"],
                        ["Leonel Rojas","Antofagasta"],
                        ["Yaime Alegría","Puerto montt"],
                        ["Rayén Rodríguez","Puerto Montt"],
                        ["Katherine fuentealba","Valdivia"],
                        ["Vicente González","Valdivia!"],
                        ["Vicente Salas","Valdivia"],
                        ["Nicolás Tiznado Rojas","Concepción"],
                        ["Yacsic Egaña Pinto","Antofagasta"],
                        ["Thomas Maureira","Antofagasta"],
                        ["Juan Paulo Raposo","Concepción"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Nudos(self): 
        id_taller = 15
        nombre_taller = "Nudos"
        edad = "todas las edades (12 - 29)"
        lugar = "Sector Comedor"
        tallerista = "Rodolfo Pereira"
        integrantes =  [["lmedina.la@estudiantesmaux.cl","Los Andes"],
                        ["Catalina Jorquera","Santa Cruz"],
                        ["Valentina Aliaga","Santa cruz"],
                        ["Antonia Tapia","Los Andes"],
                        ["Florencia Bazáez","Los Andes"],
                        ["Joaquín Ojeda","Santiago"],
                        ["Diego Cerda","Linares"],
                        ["Santiago vergara","Santiago"],
                        ["Tomás Espinoza","santiago de chile"],
                        ["Diego San Martín","La cisterna"],
                        ["Cesar Enrique Aponte Bracamonte","Santiago, la cisterna"],
                        ["Daniel Olmos","Alto Hospicio"],
                        ["Cristóbal Pinto","Valparaíso"],
                        ["Benjamín olivares","La serena"],
                        ["Francisco barraza zamora","La serena"],
                        ["Martin Ignacio Arriaza caro","La serena"],
                        ["Maximiliano Villalobos","La Serena"],
                        ["Benjamin Araya Molina","la serena"],
                        ["Emanuel Huerta","La serena"],
                        ["Dylan tapia","La serena"],
                        ["Javier fernandez","La serena"],
                        ["Martin gomez castro","La serena"],
                        ["Bastian Saavedra González","Coquimbo"],
                        ["Yasmín Vargas Aguilar","Puerto Montt"],
                        ["Victoria muñiz","Linares"],
                        ["Nicolás Benavente","Puerto Montt"],
                        ["Nicolás Ulloa Rodrigo Millán","Puerto Montt"],
                        ["matias claveria","la serena"],
                        ["FELIPE IGNACIO TRONCOSO OLEARTE","VALDIVIA"],
                        ["Nicolás Tiznado","Concepción"]]

    def Escultismo(self): 
        id_taller = 16 
        nombre_taller = "Escultismo"
        edad = "todas las edades (12 - 29)"
        lugar = "Sector Comedor"
        tallerista = "Valentina Rifo "
        integrantes =  [["Amelia Camila caneo","Santiago la cisterna"],
                        ["Sofia Millahual","Santiago"],
                        ["Laura Cancino","Santiago"],
                        ["nain valdes","Iquique"],
                        ["Rouss Cárdenas","Punta Arenas"],
                        ["Catalina Vega","Valparaiso"],
                        ["Fernanda Astorga","Valparaíso"],
                        ["Nicolas Gonzalez","Talca"],
                        ["Antonella Rosas","Iquique"],
                        ["mateo Villaseca","Santiago"],
                        ["Rubén Castro","Valparaíso"],
                        ["Antonella Bascuñan","Santiago"],
                        ["Fernanda Arriagada","Santiago"],
                        ["Paula Calfucura","Santiago"],
                        ["Felipe Candia","Santiago"],
                        ["salvador Espinoza","Linares"],
                        ["Diego Núñez","Stgo"],
                        ["Matías Gárate","Santiago de Chile"],
                        ["Darjana Fideli","Punta arenas"],
                        ["Martina carrasco","Santiago"],
                        ["Rosario Gorigoitia","Santiago"],
                        ["Pablo cerpa","Santiago"],
                        ["Brandon Santos Carlos","Alto hospicio"],
                        ["Agustin Arias","Alto hospicio"],
                        ["Belén Rodríguez","Iquique"],
                        ["Catalina Wimmer","Santiago"],
                        ["Martin rojas","Puerto natales"],
                        ["Maria Jose Carvajal","Calama"],
                        ["María Fernanda Campo Mosquera","Calama"],
                        ["Benjamin Vicencio","calama"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Coro_liturgico1(self): 
        id_taller = 17
        nombre_taller = "Coro Litúrgico 1"
        edad = "17 - 29 años"
        lugar = "Zona Turín"
        tallerista = "Pedro Ramírez "
        integrantes = [["Amaya Chota","Linares"],
                    ["Mauricio Bustos","Santiago"],
                    ["Francisco Bravo","Copiapo"],
                    ["Mariam Álvarez","Fernando de la Mora - Paraguay"],
                    ["Lorena Pelusa","Córdoba- Argentina"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Coro_liturgico2(self): 
        id_taller = 18
        nombre_taller = "Coro Litúrgico 2"
        edad = "17 - 29 años"
        lugar = "Zona Turín"
        tallerista = "Ariel Solís"
        integrantes = [["Nicol Jeldres","Linares"],
                    ["Amelia Chodil","Punta Arenas"],
                    ["Francisca Iturra","Punta arenas"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Coro_liturgico2(self): 
        id_taller = 19, "Coro", "12 - 16 años", " Zona Turín "
        nombre_taller = "Coro Litúrgico 2"
        edad = "17 - 29 años"
        lugar = "Zona Turín"
        tallerista = "Ariel Solís"
        integrantes = [["Nicol Jeldres","Linares"],
                    ["Amelia Chodil","Punta Arenas"],
                    ["Francisca Iturra","Punta arenas"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes