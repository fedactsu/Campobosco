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
            [20, "Canto 1", "12 - 16 años", " Zona Nizza "],
            [21, "Canto 2", "17 - 22 años", " Zona Nizza"],
            [22, "Manualidades 4",
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
            [56, "Primeros auxilios comunitarios", "todas las edades (12 - 29)", " Sector enfermería"],
            [57,"Fútbol Femenino","Todas las edades","Costado Miguel Magone"]]

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
        if id == 19:
            return self.Coro()
        if id == 20:
            return self.canto1()
        if id == 21:
            return self.canto2()
        if id == 22:
            return self.Manualidades4()
        if id == 23:
            return self.Manualidades3()
        if id == 24:
            return self.Manualidades2()
        if id == 25:
            return self.Manualidades1()
        if id == 26:
            return self.Mandalas()
        if id == 27:
            return self.dibujoTiza()
        if id == 28:
            return self.Origami1()
        if id == 29:
            return self.Origami2()
        if id == 30:
            return self.FotoIa()
        if id == 31:
            return self.Fotografia()
        if id == 32:
            return self.Autoconocimiento()
        if id == 33:
            return self.DesarrolloPersonal()
        if id == 34:
            return self.Liderazgo()
        if id == 35:
            return self.Cueca1()
        if id == 36:
            return self.Cueca2()
        if id == 37:
            return self.danzaContemporanea()
        if id == 38:
            return self.danzaContemporanea2()
        if id == 39:
            return self.Salsa()
        if id == 40:
            return self.Reciclaje()
        if id == 41:
            return self.Agroecologia()
        if id == 42:
            return self.Jardineria()
        if id == 43:
            return self.TalladoEnMadera()
        if id == 44:
            return self.Encuadernacion()
        if id == 45:
            return self.Electricidad()
        if id == 46:
            return self.introLiturgia()
        if id == 47:
            return self.Animacion()
        if id == 48:
            return self.Malabarismo()
        if id == 49:
            return self.mimossketch()
        if id == 50:
            return self.matetruco()
        if id == 51:
            return self.lengua()
        if id == 52:
            return self.magia()
        if id == 53:
            return self.animereligion()
        if id == 54:
            return self.whasprevention()
        if id == 55:
            return self.primerosauxiliospsicologicos()
        if id == 56:
            return self.primerosauxilioscomunitarios()
        if id == 57:
            return self.futbolfemenino()

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
                       ["Francisco Santibáñez", "Concepción"],
                       ["Fernanda Gutiérrez","Santiago"]]

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
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes

    def Escultismo(self): 
        id_taller = 16 
        nombre_taller = "Escultismo"
        edad = "todas las edades (12 - 29)"
        lugar = "Sector Comedor"
        tallerista = "Maximiliano Aravena"
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
    
    def Coro(self): 
        id_taller = 19
        nombre_taller = "Coro"
        edad = "12 - 16 años"
        lugar = "Zona Turín"
        tallerista = "Sabra Charles"
        integrantes =  [["Emilia Caamaño","Iquique"],
                        ["Fernanda Ruz Milla","Iquique."],
                        ["Catalina Ortiz","Concepción"],
                        ["Josefa Valenzuela","Molina"],
                        ["Matilda Albornoz","Molina"]]
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def canto1(self): 
        id_taller = 20
        nombre_taller = "Canto 1"
        edad = "12 - 16 años"
        lugar = "Zona Nizza"
        tallerista = "Matías Marín"
        integrantes = [["Nicolas Gallardo","Maule"],
                    ["Pascale Perez","Valparaíso"],
                    ["Gabriel Ignacio Orrego Acuña","Santiago"],
                    ["Anaís Araceli Fuentes Sánchez","Santiago, Chile"],
                    ["Antonia Sepúlveda","Linares"],
                    ["Ámbar Amaya","Santiago"],
                    ["Kiara Garcés Astudillo","Santiago"],
                    ["Jose Chung","Antofagasta"],
                    ["Vicente Cañete Garrido","Talca"],
                    ["Daniel Lopez","Antofagasta"],
                    ["Fernanda Lamas","Antofagasta"],
                    ["Agustina Antonia rojas soto","Linares"],
                    ["Naira Conejeros Delgado [Nairita]","Valdivia."],
                    ["Claudio Bustamante","Valdivia"],
                    ["Emilia Baza Garrido","Concepción"],
                    ["Loyzen Zack Pimentel Salas","Antofagasta"],
                    ["Vicente Berrios","Valdivia"],
                    ["Vicente Matamala","Valdivia"],
                    ["Lukas González","Concepción"],
                    ["Josefa Valenzuela","Molina"],
                    ["Sebastián Díaz","Talca"],
                    ["Gabriela cordero","Catemu"],
                    ["Matías Hernández","Valdivia"],
                    ["Antonio Helbig","Santiago"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def canto2(self): 
        id_taller = 21 
        nombre_taller = "Canto 2"
        edad = "17 - 22 años"
        lugar = "Zona Nizza"
        tallerista = "Christianne Neira"
        integrantes = [["Alisson Sánchez Pizarro","Talca"],
                    ["Nicolas Gallardo","Maule"],
                    ["Manuel David Cordova Calcina","Calama"],
                    ["Gabriel Orrego Acuña","Santiago"],
                    ["Claudio Pizarro","Santiago"],
                    ["Ámbar Amaya","Santiago, San Joaquín"],
                    ["Martín Herrera Galleguillos","Valparaíso"],
                    ["Tomás Castro","Talca"],
                    ["Joaquín Ardiles","Santiago"],
                    ["Francisco Bravo","Copiapo"],
                    ["Tomás Páez Carvajal","Iquique / Alto Hospicio"],
                    ["Valentina Salas","Talca"],
                    ["Antonia Román Ramos","Valparaíso"],
                    ["Daniela Gorigoitia Gatica","Recoleta"],
                    ["Macarena Morales","Talca"],
                    ["Maximo Esquivel","La Serena"],
                    ["Claudio Bustamante","Valdivia"],
                    ["Catalina Ortiz","Concepción"],
                    ["Vicente Berrios","Valdivia"],
                    ["Naira Conejeros Delgado","Valdivia."],
                    ["Marcela Ríos","Concepción"],
                    ["Matilda Cisterna","Molina"],
                    ["Sayén Guerrero","Valparaíso"],
                    ["Derrick Chin","Punta arenas"],
                    ["Gabriela cordero","Catemu"],
                    ["Constanza Pino","Santa Cruz"],
                    ["Magdalena Tobar Mejías","Santiago, Chile"],
                    ["Benjamin Ponce","Talca"],
                    ["Benjamin Andre Clery Diaz","Iquique"],
                    ["Adriana Valdés Sánchez","Talca"]]
 

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Manualidades4(self): 
        id_taller = 22
        nombre_taller = "Manualidades 4"
        edad = "todas las edades (12 - 29)"
        lugar = "Sala 2 Miguel Magone"
        tallerista = "Oswaldo Villamar"
        integrantes =  [["Lidia Bascuñan","Linares"],
                        ["Katherine garces","Linares"],
                        ["Constanza Núñez","Santiago"],
                        ["Constanza Núñez Villegas","Santiago"],
                        ["Danae Álvarez","Valparaíso"],
                        ["italo rojas","calama"],
                        ["Catalina Araya","Linares"],
                        ["Eyvann cuchallo","Calama"],
                        ["Consuelo Devia Sanchez","Santiago"],
                        ["Karen González","Linares"],
                        ["María Corina González","Linares"],
                        ["Martina Alveal","Santiago"],
                        ["Benjamin Muñoz","Talca"],
                        ["Antonella Pino","Talca"],
                        ["Florencia Lemus","Alto hospicio"],
                        ["Isadora Moya","Linares"],
                        ["Javiera España","Puerto Montt"],
                        ["Valentina Coronado","Valdivia"],
                        ["Sebastián Coronado","Valdivia"],
                        ["Marcela Lara","Valdivia"],
                        ["Gabriela Luna Castillo","Linares"],
                        ["Florencia Mella","Linares"],
                        ["Samantha Figueroa","Linares"],
                        ["Constanza González Arellano","Linares"],
                        ["Jean carlos","Linares"],
                        ["Sofia Del Valle","Santiago"],
                        ["Antonella Agustinos","Punta Arenas"],
                        ["Valentina Rivas","Linares"],
                        ["Martina Opazo","Santiago"],
                        ["Trinidad Castro","Santiago"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Manualidades3(self): 
        id_taller = 23
        nombre_taller = "Manualidades 3"
        edad = "todas las edades (12 - 29)"
        lugar = "Patio techado Miguel Magone"
        tallerista = "Oswaldo Mora"
        integrantes = [["Emilia Sapiains","Hijas de María Auxiliadora"],
                        ["Camila Núñez","Liceo Santa Teresita de Talca"],
                        ["Paula Camila Molina Rincon","Instituto pol. Maria Auxiliadora"],
                        ["Lucas Siade","Salesiano Valparaiso"],
                        ["Benjamin Claro","Colegio Salesiano de Valparaiso"],
                        ["Fernanda Astorga","Colegio María auxiliadora Valparaíso"],
                        ["Tihare Toro","Colegio María Auxiliadora Valparaíso"],
                        ["Martin Herrera","Colegio salesiano de Valparaíso"],
                        ["Mia Mejias","Maria Auxiliadora de Valparaiso"],
                        ["Belén Estrada","Escuela señors del tránsito de molina"],
                        ["Trinidad Reyes","Escuela particular n°1 nuestra señora del tránsito Molina"],
                        ["Mahily Vergara","Escuela particular n°1 nuestra señora del tránsito Molina"],
                        ["Dayana Villarroel","Colegio Tecnico Industrial Don Bosco Calama"],
                        ["Sofía Tapia Bravo","Liceo María Auxiliadora"],
                        ["Josefa Zarate","Colegio Salesiano PJFP"],
                        ["Sandra Fernández","Liceo josé miguel infante"],
                        ["Walter Agurto","Campo Bosco 2024"],
                        ["Montserrat Riveros Aranda","Colegio Salesiano Santo Domingo Savio"],
                        ["María Fernanda Nahuelhuen","Colegio Salesiano Padre José Fernández Pérez"],
                        ["Catalina Díaz","Comunidad Cristo Joven"],
                        ["Abril Bustamante","El colegio técnico industrial don bosco calama"],
                        ["Javiera Pevez","Voleibol"],
                        ["Kriss Gerson veliz pizarro","Salesianos don Bosco la serena"],
                        ["Sebastian Rivera","Campo bosco"],
                        ["Cristóbal barrios Astudillo","Campo don Bosco"],
                        ["Javier rojas","Misionero"],
                        ["Amaro Muñoz","Campo Bosco"],
                        ["Victoria Tello","Domingo Savio"],
                        ["Jose Vasquez","Scout"],
                        ["Allanys González","Eje"]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Manualidades2(self): 
        id_taller = 24
        nombre_taller = "Manualidades 2"
        edad = "12 - 16 años"
        lugar = "Sala 2 Bartolomé Garelli"
        tallerista = "Constanza Coronado"
        integrantes = [["Marive Aranda Badilla","Santiago"],
                        ["Antonia Cárdenas","Punta Arenas"],
                        ["Ignacia Guardia","Santiago"],
                        ["Trinidad Valenzuela","Santiago"],
                        ["Nicolás Elgueta","Antofagasta"],
                        ["Constanza Serey","Catemu"],
                        ["isidora ramos herrera","catemu"],
                        ["Maria Victoria De los Angeles Avallai Olivares","Catemu"],
                        ["Javiera olmos","Catemu"],
                        ["Allison perez","Catemu"],
                        ["Rosita Herrera","Catemu"],
                        ["Alonso fuentes","Santiago"],
                        ["Javier Morgado","Antofagasta"],
                        ["Aracelly pulgar","Catemu"],
                        ["Martin lopez","Catemu"],
                        ["Dafne Álvarez","Linares"],
                        ["Antonia Hidalgo","Linares"],
                        ["Trinidad Chavol","Santiago"],
                        ["Maite Garces","Santiago De Chile"],
                        ["Patrick cortes","Antofagasta"],
                        ["Agustín Letelier","Santiago"],
                        ["Cristobal Jorquera","Santiago"],
                        ["Benjamin Michea","Antofagasta"],
                        ["Lorenzo Ferrera","Santiago"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Manualidades1(self): 
        id_taller = 25
        nombre_taller = "Manualidades 1"
        edad = "12 - 16 años"
        lugar = "Sala 1 Bartolomé Garelli"
        tallerista = "Helen Pérez"
        integrantes = [["Dafne Cortés","Los andes"],
                    ["Tihare Toro","Valparaiso"],
                    ["Almendra Bórquez","punta arenas"],
                    ["ashly samira avila pasten","calama"],
                    ["Nicol Bautista Donaire","Calama"],
                    ["Dhannae Tripai","Valdivia"],
                    ["Pablo Matos","valdivia"],
                    ["Catalina Velasquez torres","Valdivia"],
                    ["Lourdes benites","Santiago"],
                    ["Belén Valenzuela","Molina"],
                    ["ashley valenzuela","santiago"],
                    ["Isidora Antonia Moya Prieto","Santiago"],
                    ["Emilia Muñoz","linares"],
                    ["Mia Mejias","Valparaíso"],
                    ["Maite Carvajal","Santiago"],
                    ["Montserrath Navarro","Linares"],
                    ["Antonia carter","Linares"],
                    ["Florenccia Romero","Linares"],
                    ["Juan cristóbal munoz bueno","Linares"],
                    ["Ghyannella Vargas","Puerto Montt"],
                    ["Luis Oyarzo","Puerto Montt"],
                    ["Nicolás Ulloa Rodrigo Millán","Puerto Montt"],
                    ["Maximiliano Santana","Linares"],
                    ["Alex Maximo Delgado Ochoa","Puerto Montt"],
                    ["Anahis Cifuentes","Linares"],
                    ["Inti Pascal Huerta Huerta","linares"],
                    ["Tomás Forcael","Puerto Montt"],
                    ["César Sepúlveda","Punta Arenas"],
                    ["Antonia Lizana González","Santiago"],
                    ["Ignacia Olivares","Santiago"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Mandalas(self): 
        id_taller = 26
        nombre_taller = "Mandalas"
        edad = "todas las edades (12 - 29)"
        lugar =  "Sala 1 Emma Ferrero"
        tallerista =  "Gloria Mondaca"
        integrantes =  [["Aramy Riquelme","Santiago"],
                        ["Paula Quintana","Iquique"],
                        ["Constanza caceres","santiago"],
                        ["Abril mendoza","santiago"],
                        ["fabiana fierre","santiago"],
                        ["Sofia González","Santiago"],
                        ["cristobal purcell","santiago"],
                        ["Sophia López Cubillos","Santiago"],
                        ["Carla Lopez","santiago"],
                        ["Tomás Farías","Santiago"],
                        ["Yair Esteban Carrasco Sarmiento","La serena"],
                        ["Eduardo Villalobos","La Serena"],
                        ["Ghyannella Vargas","Puerto Varas"],
                        ["Constanza Monzalve","Puerto Montt"],
                        ["Catalina Martínez","Puerto Montt"],
                        ["Antonella Salazar","Puerto montt"],
                        ["Helena Mesas Oyarzo","Puerto Montt"],
                        ["Patricio Ariel Vargas Aguilar","Puerto Montt"],
                        ["Javier Gatica","Valdivia"],
                        ["Noelia Godoy","Santiago"],
                        ["Francis Gac Villanueva","Santiago"],
                        ["Thiare lienlaf","Valdivia"],
                        ["julieta gonzalez","Punta Arenas"],
                        ["María José Lopez","Punta Arenas"],
                        ["Matias Triviño","Punta Arenas"],
                        ["Agustín Carrasco","Linares"],
                        ["Antonia Olguin","Santiago centro"],
                        ["Gianella Lara","Linares"],
                        ["Pia Hernández","Santiago"],
                        ["Nicol Tapia","Valparaiso"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def dibujoTiza(self): 
        id_taller = 27
        nombre_taller = "Dibujo con patrones en tiza"
        edad = "12 - 16 años"
        lugar =  "Sector Valponasca"
        tallerista = "Fernanda Urra"
        integrantes = [["Ashly Paucar","Talca"],
                    ["esteban lienlaf","valdivia"],
                    ["Diego González","Antofagasta"],
                    ["Martin Aguilera","Valdivia"],
                    ["Francisca salvador","Catemu"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Origami1(self): 
        id_taller = 28
        nombre_taller = "Taller de Origami"
        edad = "12 - 16 años"
        lugar =  "Patio Techado módulo 1 Miguel Magone"
        tallerista = "Adrián Ayala"
        integrantes = [["María Jesús López Gómez","Talca"],
                        ["Leticia Araya","Santiago"],
                        ["Agustin cancino","Santiago"],
                        ["Antonia Campos","Linares"],
                        ["Francisco Bravo","Copiapo"],
                        ["Lucas Yañez","Santiago"],
                        ["Lucas Santibañez","Punta Arenas"],
                        ["Alonso gutierrez","Punta arenas"],
                        ["Renato Molina","La cisterna"],
                        ["Alexandra Brito","Puerto Montt"],
                        ["Fernanda Salazar","La cisterna"],
                        ["Dafne Mora","Valdivia"],
                        ["Gaston Martinez","Valdivia"],
                        ["Matías Pacheco","Valdivia"],
                        ["Gissela manquecoi","Valdivia"],
                        ["Duban Vergara","Linares"],
                        ["Bastian gatica","Alto hospicio"],
                        ["Maria Olaya","santiago"],
                        ["Matias lamas","Antofagasta"],
                        ["Isidora Varas","Catemu"],
                        ["Fernando Nahuelquin","Punta Arenas"],
                        ["Raphael Soares","Punta Arenas"],
                        ["Alonso Fierro","Santiago"],
                        ["Maximiliano Baeza","Stgo"],
                        ["Miguel Larios","Santiago"],
                        ["Benjamin Marchant","santiago"],
                        ["josefa oyarzún","punta arenas"],
                        ["Alonso Barros","Linares"],
                        ["Trinidad Muñoz","Talca"],
                        ["Pablo Arcos Salinas","Talca"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Origami2(self): 
        id_taller =  29
        nombre_taller = "Taller de Origami 2"
        edad =  "17 - 29 años"
        lugar = "Patio techado Bartolomé Garelli"
        tallerista = "Martín Santana"
        integrantes = [["Dayris Roa","Maule"],
                        ["Benjamin Tello Contreras","Copiapó"],
                        ["Ángela López","Alto hospicio-Tarapacá"],
                        ["Monserrat Rifo Arriagada","Concepción"],
                        ["Javiera Ringele Aburto","Concepción"],
                        ["Alberto Urdaneta","Santiago"],
                        ["José Antonio López Cubillos","Santiago"],
                        ["Camila Herrera","Concepción"],
                        ["Byron Arriagada","Concepción"],
                        ["Patricio Rivera Cortés","Antofagasta"],
                        ["Emilio Castillo","Concepción"],
                        ["Angel Ramirez","Linares"],
                        ["Richard Jesús Guevara Perez","Linares"],
                        ["Joaquín Amaro Alegría","Linares"],
                        ["Enzo Rivera","Punta Arenas"],
                        ["Eduardo Escandor","Puntarenas"],
                        ["Yanina Caballero","Villeta"],
                        ["Angel arcos","Talca"],
                        ["Emilio Rebolledo","Santiago"],
                        ["Maria Belen Báez Enciso","San lorenzo Paraguay"],
                        ["Pia Hernández","santiago"],
                        ["Benjamin Marchant","Santiago"],
                        ["javiera salazar","santiago"],
                        ["Ana Victoria Álvarez Ardila","Catemu"],
                        ["Sor Lourdes Enciso","Asunción"],
                        ["Giovani Urrutia","Talca"],
                        ["Sebastian Navarrete","Concepción"],
                        ["Andrés Devia","Santiago"],
                        ["josefina lara","linares"],
                        ["Maila Cabezas","Linares"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def FotoIa(self): 
        id_taller = 30
        nombre_taller = "Fotografía e I.A."
        edad =  "todas las edades (12 - 29)"
        lugar = "Zona Roma"
        tallerista = "Christian Chávez"
        integrantes = [["Libertad Medina Urtubia","Los Andes"],
                        ["victoria tapia","los andes"],
                        ["Vania Fernández","Molina"],
                        ["Antonia Pérez","Iquique"],
                        ["Alonso Ovando","Santiago"],
                        ["Javier Olivares","Santiago"],
                        ["Vicente Poblete","Santiago"],
                        ["lukas cepeda","santiago centro"],
                        ["Benjhamin Rivera","Santiago Centro"],
                        ["Francisco Troncoso","Linares"],
                        ["Francisca Bertolini","Linares"],
                        ["Matías Hormazábal","Linares"],
                        ["José Luis Francisco Morales Campos","Talca"],
                        ["Javiera Tapia","Santiago Centro"],
                        ["Alexander Baeza","Ciudad Iquique, Comuna de Alto Hospicio"],
                        ["Valentina Toro","alto hospicio"],
                        ["Benjamin Ignacio García Díaz","Puerto Montt"],
                        ["Fiorella Salinas","Alto hospicio"],
                        ["Anays ortiz","Alto hospicio"],
                        ["Wiston Meneses","Puerto Montt"],
                        ["Moisés Gutiérrez","Iquique,chile"],
                        ["Joaquin Grimaldosa","Iquique"],
                        ["Ignacio Miranda","Iquique"],
                        ["Javier Ojeda","Puerto Montt"],
                        ["Diego Tapia","Copiapó"],
                        ["Víctor Villagrán Muñoz","Copiapó"],
                        ["Kimberly Diaz","Copiapo"],
                        ["Rodrigo Cerda","Linares"],
                        ["Elías Mora","Santiago"],
                        ["pia riffo","Concepción"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Fotografia(self): 
        id_taller = 31
        nombre_taller = "Fotografía"
        edad = "12 - 16 años"
        lugar = "Zona Roma "
        tallerista = "Ángela Maldonado"
        integrantes = [["Catalina Alejandra Chávez Gómez ","Santa Cruz"],
                        ["Valeria Poblete","Puerto Montt"],
                        ["Sofía Polanco","Santiago"],
                        ["Martina Rojas","Iquique"],
                        ["Catalina Torres ","Iquique "],
                        ["Isidora Castro Valdenegro ","Iquique "],
                        ["jennifer Huanchaco","iquique"],
                        ["Tihare Toro","Valparaiso "],
                        ["Sofía Saavedra","Valparaíso"],
                        ["Nahely Plata ","Iquique "],
                        ["Javiera Sánchez ","Valparaiso "],
                        ["Dayarick Peña","Valparaíso "],
                        ["Violeta Espinoza","Santiago"],
                        ["constanza Ugarte ","Valparaíso "],
                        ["Florencia baack ","Valparaíso "],
                        ["Mariana Canales ","Punta Arenas "],
                        ["Camila Torres","Iquique"],
                        ["Rayén Burgos Jimenez ","Linares "],
                        ["Joaquin vidal","Punta arenas"],
                        ["Sofía ganga","Talca"],
                        ["Sebastian Fuentes ","Santiago"],
                        ["annais melo","valdivia"],
                        ["Agustina martin","Valdivia "],
                        ["Angela cifuentes ","Talca"],
                        ["Scarlett palma","Valdivia "],
                        ["Catalina Romero","Valparaiso "],
                        ["Fernando Coello","Iquique"],
                        ["Pascal Pasten","Talca"],
                        ["Josefa Mercado ","Linares "],
                        ["Sol valdes ","Puerto natales "]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Autoconocimiento(self): 
        id_taller = 32
        nombre_taller = "Autoconocimiento"
        edad = "17 - 29 años"
        lugar = "Zona Roma"
        tallerista = "P. José Ruiz"
        integrantes = [["Abril Rojas","Copiapó "],
                        ["jeremy Hernández Argel ","Punta Arenas "],
                        ["Joaquín Gutiérrez ","Antofagasta "],
                        ["Antonia Hidalgo","Linares"],
                        ["Johana Villanueva ","Villarrica - Paraguay"],
                        ["Camilo Villagra","Talca"],
                        ["francisca gamonal ","santiago "],
                        ["Emiliano Reyes ","Talca "],
                        ["Manuel Cortes","Talca"],
                        ["Thais Arriagada","Talca"],
                        ["Ermelinda Blanca Mamani Liendro ","Sucre - Bolivia"],
                        ["Martina Altamirano ","copiapo "]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def DesarrolloPersonal(self): 
        id_taller = 33 
        nombre_taller = "Desarrollo Personal"
        edad = "17 - 29 años"
        lugar = "Zona Ibecchi"
        tallerista = "Valentina Gallegos"
        integrantes = [["Benjamin Ponce ","Talca"],
                        ["Maximiliano Fernández Samit ","Valparaíso "],
                        ["Martyna Ignacia Iturra Ibáñez ","LINARES "],
                        ["Antonya González ","Maule "],
                        ["Matias Negrete Romero","Copiapo"],
                        ["Francisco moretta","Copiapo"],
                        ["Belén Avello Domínguez","Concepción"],
                        ["Fernanda Juárez ","Concepción"],
                        ["Florencia cerna ","Concepcion "],
                        ["Bastian severino","La serena "],
                        ["Martin Carvallo ","La serena "],
                        ["Yosued Contreras ","La serena "],
                        ["Martin torres","Coquimbo"],
                        ["Isidora Herrera ","Concepción"],
                        ["Marcia Barría ","Santiago "],
                        ["Jorge Vera","Punta Arenas"],
                        ["Marcelo Toro","Punta arenas"],
                        ["Agustín Salas","Punta Arenas "],
                        ["Nicolas Palma ","Santiago "],
                        ["Matias ruz ","Talca "],
                        ["Francisca salvador ","Catemu "],
                        ["Benjamin Castillo","Santiago, chile "],
                        ["Susana Raquel Giménez Acosta","MINGA GUAZÚ - PARAGUAY"],
                        ["Daniel Hernández","Linares"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Liderazgo(self): 
        id_taller = 34 
        nombre_taller = "Liderazgo" 
        edad = "12 - 18 años" 
        lugar =  "Patio Techado Emma Ferrero"
        tallerista =  "María José Jiménez"
        integrantes =  [["Renata Díaz Castro","Santa Cruz "],
                        ["Trinidad Victoriano ","Valparaíso "],
                        ["maría Ignacia Guajardo Jackson ","Iquique"],
                        ["Susana Arancibia Marambio","Santiago"],
                        ["Angela cifuentes ","Talca"],
                        ["Felipe Mendez","Santiago"],
                        ["JORGE ALVAREZ","copiapo"],
                        ["Diego Valenzuela ","Talca"],
                        ["Felipe sandoval","Santiago "],
                        ["Matias Requena Espinoza ","Antofagasta "],
                        ["Amaya Vivanco ","Santiago"],
                        ["Rodrigo Huaman ","Antofagasta "],
                        ["Joaquín Bastian Rojas Cortés","Antofagasta "],
                        ["Martin Fuentes","Santiago"],
                        ["Facundo Ferrera","La cisterna "],
                        ["Vicente Escobar","La cisterna"],
                        ["Sebastián Mora ","PUNTA ARENAS "],
                        ["Franco olivares ","La Serena "],
                        ["Javier Diaz ","La Serena "],
                        ["Cristian Sepúlveda ","Santiago"],
                        ["Matias Carrillo","Valdivia"],
                        ["Alonso Esteban Morales Campos ","Talca "],
                        ["Juan Carlos Ferreira Varela ","Concepción "],
                        ["Jadde Novoa ","Linares "],
                        ["Pauline Mättig","Valdivia "],
                        ["Guillermo Pizarro ","Concepción"],
                        ["Carlos Montero","Punta Arenas"],
                        ["Joaquin de la paz","Punta arenas "],
                        ["Felipe Rosales","Punta Arenas"],
                        ["Agustin Nuñez","Santiago"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Cueca1(self): 
        id_taller = 35
        nombre_taller = "Cueca"
        edad = "todas las edades (12 - 29)"
        lugar = "Zona Mornese"
        tallerista = "Fredy Chamorro"
        integrantes = [["Sofía Ignacia Silva Valenzuela","Santa Cruz"],
                    ["Javiera Lizana","Santa cruz"],
                    ["Matilde Donoso","Los andes"],
                    ["Georgette Bilbao","Natales"],
                    ["Amanda Vasquez","Talca"],
                    ["Isidora Barría","Puerto Natales"],
                    ["Rocio Cisterna","Iquique"],
                    ["Tihare Toro","Valparaíso"],
                    ["Mackarena paredes","Punta Arenas"],
                    ["Benjamin tecay","Punta arenas"],
                    ["Mayra Meneses.","Santiago."],
                    ["Constanza Quintullanca","Punta Arenas"],
                    ["Catalina Cárdenas Villarroel","Valparaíso"],
                    ["Brayan navarro levipichun","Punta arenas"],
                    ["Francisca Rebolledo Ampuero","Punta arenas"],
                    ["Camila Robles Nuñez","Santiago"],
                    ["Trinidad Magdalena Vergara Valderrama","Talca"],
                    ["Diego Velasquez Muñoz","Santiago"],
                    ["Tomás Cárdenas","Santiago"],
                    ["Beatriz Cuellar","Santiago centro"],
                    ["Pascal Pérez Valenzuela","Santiago"],
                    ["Diego Arenas","Iquique"],
                    ["Catalina Nieto","Santiago"],
                    ["Lizardo Rebolledo","Iquique"],
                    ["Paolo González","Iquique"],
                    ["Florencia Martínez","Talca"],
                    ["Sofía Escalona","Talca"],
                    ["Trinidad Monsalvez","Santiago"],
                    ["Martina Valenzuela","Santiago"],
                    ["Enzo Morales","Santiago"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Cueca2(self): 
        id_taller = 36
        nombre_taller = "Cueca 2"
        edad = "todas las edades (12 - 29)"
        lugar = "Zona Roma"
        tallerista = "Pamela Romero"
        integrantes = [["Lenka Reyes","Puerto montt"],
                    ["Matilde Donoso","Los andes"],
                    ["Angelina Molina","Santiago"],
                    ["Paula Vera Álvarez","Santiago Chile"],
                    ["Josefina Cerda","talca"],
                    ["María Isidora Bozo","Los andes"],
                    ["Florencia avila verdugo","Talca"],
                    ["Valentina Herrera","Punta Arenas"],
                    ["Catalina Palacios Tapia","Iquique"],
                    ["Ignacia Pozo","Valparaiso"],
                    ["Dominic Goldschmidt","Valparaíso"],
                    ["Javiera Vergara","Valparaíso"],
                    ["Felipe Soto Villalobos","Linares"],
                    ["Camila risco","Punta Arenas"],
                    ["Francisca Rebolledo Ampuero","Punta arenas"],
                    ["Rocio Ovando","Punta Arenas"],
                    ["Lylian Soza","calama"],
                    ["Vucente Guajardo Pino","Calama"],
                    ["Damián Pincheira","Linares"],
                    ["Benjamin Araya","Linares"],
                    ["Francisca Valenzuela","Santiago, comuna San Miguel"],
                    ["Francisco Díaz","Santiago"],
                    ["Montserrath Navarro","Linares"],
                    ["Javiera Noemí Romero Ortiz","Santiago"],
                    ["Rous Soto","Puerto Montt"],
                    ["Constanza Castillo","Santiago"],
                    ["Emilio Retamal","Linares"],
                    ["Martina Altamirano Valdivia","copiapo"]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def danzaContemporanea(self): 
        id_taller = 37
        nombre_taller = "Danza contemporánea"
        edad = "todas las edades (12 - 29)"
        lugar = "Zona Mornese"
        tallerista = "Karen Dinter"
        integrantes = [["Antonia Lorca Cea","Santa Cruz"],
                    ["Isidora Ramírez ","Santa cruz "],
                    ["Renata Meneses Pérez ","Santa cruz "],
                    ["Maite Contreras","Los Andes"],
                    ["Pía Llanten","Los Andes"],
                    ["Mariangel García ","Talca "],
                    ["Martina Ortega ","Puerto natales "],
                    ["Antonia Moya ","Iquique "],
                    ["Kathalyna Ignacia Mérida Camacho.","Iquique."],
                    ["Sofía Chamorro ","Linares"],
                    ["Laura Maldonado","Santiago"],
                    ["Emilia Palma","puerto natales"],
                    ["Anais Lobos ","Valparaiso "],
                    ["Jeismar Lucena ","Valparaíso "],
                    ["Daniela Iturra ","Santiago "],
                    ["Maite Roman","Talca"],
                    ["Anahí Cea","Linares"],
                    ["Nazareth Hernández","Santiago"],
                    ["soffia alfaro","santiago "],
                    ["Saray Contreras","santiago"],
                    ["Josefa Ledezma ","Antofagasta "],
                    ["Kiara Garces Astudillo","Santiago"],
                    ["Catalina Soto Vidal ","Santiago "],
                    ["Arlette Tabilo","Alto Hospicio"],
                    ["Vielka Catagua ","Alto Hospicio "],
                    ["Josefa Ledezma Concha","Antofagasta"],
                    ["Antonia Muñoz","Iquique"],
                    ["pia herrera rojas","copiapo"],
                    ["Nilson Jofré ","Concepción "],
                    ["Antonia Arias Contreras ","Santiago de Chile "]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def danzaContemporanea2(self): 
        id_taller = 38
        nombre_taller = "Danza contemporánea"
        edad =  "12 - 16 años"
        lugar = "Zona IBecchi"
        tallerista = "Paulina Rivas"
        integrantes = [["Isidora Ramírez ","Santa Cruz "],
                        ["Antonia Lorca Cea","Santa Cruz "],
                        ["Antonella Flores ","Linares "],
                        ["Carynar Sequera ","Linares"],
                        ["Sofía Olave","Talca"],
                        ["Sofia becerra","Iquique"],
                        ["Lucero Herrera ","Iquique"],
                        ["Raffaella Cortés","Iquique"],
                        ["Antonia acuña ortiz","Valparaíso "],
                        ["Anahys Santelices Muñoz","Santiago "],
                        ["Maitty Quilaleo Millalen","SANTIAGO"],
                        ["Sophia Thomassen ","Puerto Montt "],
                        ["Fernanda Oyarzún Zuñiga ","Puerto Montt"],
                        ["Isabella Palma ","Puerto Montt "],
                        ["Sofia Del Valle","Santiago "],
                        ["Dayana Navarro ","Talca"],
                        ["Satefany Ramos Ramos","Santiago"],
                        ["Ariana Huanca","santiago"],
                        ["Rayen Naipayan","Santiago "],
                        ["Josefina Escobar Johnson","Santiago"],
                        ["Jezabel pereira ","Valparaíso "],
                        ["Constanza Olave Román ","Talca "],
                        ["Maida Faúndez ","Molina "],
                        ["Carla basadre ","Valparaíso "],
                        ["Karol Lobos","Catemu"],
                        ["Bastian pinilla","Catemu"],
                        ["Esteban Herrera Sazo ","Catemu"],
                        ["Fernanda carrasco","Santiago"],
                        ["Luciano Roldan","Concepcion"],
                        ["Miranda Suárez","Santiago"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Salsa(self): 
        id_taller = 39
        nombre_taller = "Salsa"
        edad =  "12 - 16 años"
        lugar = "Zona Turín"
        tallerista = "Carolina Barbosa"
        integrantes = [["Ianara Vera Contreras ","Puerto Montt "],
                    ["Freidymar Malave ","Puerto montt "],
                    ["Sofia Cáceres ","Valparaiso "],
                    ["Andrea Holguin ","Santiago "],
                    ["Anais Lobos ","Valparaiso "],
                    ["valentina cavieres","Valparaíso"],
                    ["Genesis Rojas ","Santiago "],
                    ["Antonia Piña","Santiago"],
                    ["Martina Acuña","Valparaíso "],
                    ["Lía Yacsich","Santiago"],
                    ["maythe stange","Puerto Montt"],
                    ["Isidora castillo","Puerto Montt "],
                    ["Joaquín Keim","Puerto Montt"],
                    ["Emilia Barrientos ","Puerto Montt "],
                    ["Emiliana Uribe ","Puerto Montt"],
                    ["Mayra Villarroel","Puerto montt"],
                    ["Constanza Javiera Vidal Hermosilla ","Puerto montt"],
                    ["Kimberly lizama ","Santiago "],
                    ["Emilia Medina ","Puerto Montt "],
                    ["Rodrigo Huaman ","Antofagasta "],
                    ["javiera gallegos ","puerto natales "],
                    ["Antonia Navarro","valparaiso "],
                    ["Paz Oyarzo ","Puerto Montt "],
                    ["Katalina Arana ","Puerto Montt "],
                    ["Catalina Bastias ","Puerto Montt "],
                    ["Isidora Fernández Oyarzo ","Valdivia"],
                    ["Sofhia morales ","Valdivia "],
                    ["Sophia Balboa ","Valdivia "],
                    ["Martin salinas ","Antofagasta"],
                    ["leon domenech","SANTIAGO- LA CISTERNA"]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Reciclaje(self): 
        id_taller = 40
        nombre_taller = "Reciclaje"
        edad = "12 - 16 años"
        lugar = "Patio Techado Emma Ferrero"
        tallerista = "Ivette Rojas"
        integrantes = [["Javier Norambuena ","Linares"],
                        ["Felipe Cáceres","Linares"],
                        ["Neftalí Carcamo","Valdivia"],
                        ["Emilia Fernández nieto ","Catemu "],
                        ["Jorge tapia Toledo ","Catemu "],
                        ["Ricardo Algarañaz ","Antofagasta "],
                        ["Marley Rocha ","Antofagasta"],
                        ["Ozzy Cataldo","Quintero"],
                        ["Juan franke","Copiapo"],
                        ["Agustín Vera ","Talca"],
                        ["Alex espinosa","Catemu"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Agroecologia(self): 
        id_taller = 41
        nombre_taller = "Agroecología y plantación sustentable" 
        edad =  "12 - 16 años"
        lugar =  "Zona Nizza"
        tallerista = "María Garrido"
        integrantes =  [["Antonela Tobar ","Santa Cruz"],
                        ["Sofia Romero","Santa Cruz "],
                        ["Catalina Díaz ","Santiago"],
                        ["Francisco Quezada","Santiago "],
                        ["Dylan almonte ","Antofagasta"],
                        ["Almendra elias ","Santiago "],
                        ["Benjamín Becerra ","Valdivia "],
                        ["Yamil Arancibia Caballero","IQUIQUE"],
                        ["Benjamin Pizarro","La Serena"],
                        ["Luciano zenteno","La serena"],
                        ["Alexander Severino ","La serena "],
                        ["Luciano rodriguez","La serena"],
                        ["Constanza Monzalve ","Puerto Montt "],
                        ["Vicente Suazo ","Puerto montt"],
                        ["Leandro bustamante ","Puerto Montt "],
                        ["Daniel Vargas","Puerto Montt "],
                        ["César Vidal","Puerto Montt"],
                        ["Fernanda Oyarzun","Puerto Montt"],
                        ["Maite Cabrera ","Santiago "],
                        ["Matilde Vera","Santiago "],
                        ["Cristobal galleguillos","La serena"],
                        ["Vicente Valenzuela ","Concepcion "],
                        ["Alexia Ampuero ","Puerto Montt "],
                        ["Joaquin Carvajal ","La serena"],
                        ["Vicente Peña","Alto hospicio"],
                        ["Monserrath Muñoz ","Alto hospicio "],
                        ["Maximiliano Keim","Puerto Montt"],
                        ["Valentina Mora Rocco","Santiago "],
                        ["Marcos gonzalez","Alto hospicio"],
                        ["Lucas Matías Andrés Zárate ","La serena "]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Jardineria(self): 
        id_taller = 42 
        nombre_taller = "Jardinería"
        edad =  "12 - 20 años"
        lugar = "Zona Mornese"
        tallerista = "Natalie Miranda"
        integrantes =  [["Adrian Maldonadl","Santa Cruz"],
                        ["María Ximena Pavez Galaz ","Santa Cruz "],
                        ["Kamilah Toledo ","Santa Cruz "],
                        ["Miranda Moras ","Santa cruz "],
                        ["Teresita Isabel Silva Vera ","Puerto Montt"],
                        ["Tamara González Vargas ","Puerto Montt "],
                        ["Maite Miranda Vargas","Linares"],
                        ["Karola moncerat pinto González ","Talca "],
                        ["Fernanda Astorga","Valparaíso "],
                        ["Emilia Urrutia","Linares"],
                        ["Diana Carolina Valdés Jorquera","Talca, comuna de Maule"],
                        ["Isidora Muñoz ","Punta Arenas "],
                        ["Francisca Trujillo","Punta Arenas"],
                        ["Derly Zúñiga ","Santiago "],
                        ["Pablo Castillo ","Calama "],
                        ["Darien flandes","Valdivia "],
                        ["Nikita pascale mira canales ","Santiago "],
                        ["María Jesús Lazcano Maturana","Santiago"],
                        ["isidora zamora","santiago"],
                        ["mia lopez","santiago"],
                        ["Martin Alonso Morales Gutiérrez ","Linares "],
                        ["Sarita Rodríguez ","Linares"],
                        ["Antonella Pereira ","Copiapó "],
                        ["Francisco Bravo ","Copiapo "],
                        ["Martina lopez ","Copiapó "],
                        ["Pablo Valderrama ","Copiapo "],
                        ["YOSHEF AGUIRRE JELVES","ANTOFAGASTA"],
                        ["Colomba González","Copiapo"],
                        ["Pola Delgado Ochoa","Puerto Montt"],
                        ["Jorge Monge","PUERTO MONTT"]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def TalladoEnMadera(self): 
        id_taller = 43
        nombre_taller =  "Tallado en madera"
        edad = "12 - 17 años"
        lugar = "Patio Techado Bartolomé Garelli"
        tallerista = "Elizabeth Pérez"
        integrantes = [["Sofía Mauna","Los Andes"],
                        ["Macarena Órdenes ","Santa cruz "],
                        ["Catalina Medina Mardones","Santa Cruz"],
                        ["Emilia Sapiains ","Los Andes "],
                        ["francisca florencia monsalvez cid","Puerto Natales"],
                        ["Martina Rodriguez ","Los Andes"],
                        ["Julieta Pulgar Urtubia ","Los Andes "],
                        ["Constanza sepulveda","iquique "],
                        ["Marianela Constanza Aravena Lobos","Linares"],
                        ["Catalina Delgado","Iquique"],
                        ["Martin Herrera ","Valparaíso "],
                        ["Catalina Rodríguez ","Maule "],
                        ["Luciel muñoz","Valparaiso"],
                        ["sofia briceño","Valparaíso "],
                        ["Nayareth Cáceres ","Linares"],
                        ["Constanza Escalona ","Linares "],
                        ["Lucas Siade","Valparaiso "],
                        ["Aleshka Cruz ","Valparaiso "],
                        ["Catalina Vega ","Valparaiso "],
                        ["Ema levill","Santiago de chile"],
                        ["Martina Acuña ","Valparaiso "],
                        ["Constanza Pérez ","Santiago"],
                        ["Vicente Soto ","Valparaíso "],
                        ["Mia Mejias","Valparaíso "],
                        ["Madellyne ravest ","Valparaíso "],
                        ["Julián Precht ","Valparaíso "],
                        ["Antonella tapia","Valparaiso"],
                        ["Ángel Embry","Valparaíso "],
                        ["Dagna Chacón ","Calama "],
                        ["Dulce Barrientos Zarpán ","Calama"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Encuadernacion(self): 
        id_taller = 44
        nombre_taller = "Encuadernación"
        edad = "17 - 29 años"
        lugar = "Sala 2 Emma Ferrero"
        tallerista = "Carlos Cornejo"
        integrantes = [["Martina Donoso ","Santiago "],
                    ["Catalina Araya","Santiago"],
                    ["Dayris Roa","Maule"],
                    ["Oscar Castro","Iquique "],
                    ["Fernanda Valenzuela ","Santiago"],
                    ["Jhon Carrasco ","Puerto Montt"],
                    ["Natalia Salomó ","Santiago "],
                    ["Francisca Rodríguez Gacitúa ","Santiago "],
                    ["Lissett Vidal Alarcón","Puerto Montt"],
                    ["Maria Jose Velásquez ","Concepcion "],
                    ["Nicolás Andrades ","Santiago"],
                    ["Barbara Manzano","Santiago Centro"],
                    ["Alejandra Riquelme Ávila. ","Valparaíso"],
                    ["Valentina Vásquez Castillo ","Linares "],
                    ["Rafaela Pino Gaete","Santa Cruz"],
                    ["Sebastian Neira ","Concepción "],
                    ["Enrique Caro","Santiago"],
                    ["Monserrat Rodríguez ","Santiago"],
                    ["Paloma Rodriguez ","Santiago "],
                    ["Francisco González ","Catemu "],
                    ["Emily Reyes ","Catemu "]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Electricidad(self): 
        id_taller = 45
        nombre_taller ="Electricidad domiciliaria"
        edad = "15 - 20 años"
        lugar = "Sala 1 Miguel Magone"
        tallerista = "Mario Salazar"
        integrantes =[["Jonathan domenes","Punta arenas"],
                    ["Benjamín Ignacio Castillo Gajardo ","Talca"],
                    ["Anahí Sanchez ","Puerto Montt "],
                    ["Benjamin caceres ","Talca "],
                    ["Emanuel Oliva ","Santiago"],
                    ["Bastian Pizarro","Santiago"],
                    ["Natanael Sanhueza ","Santiago "],
                    ["Matías Geraldo ","IQUIQUE"],
                    ["Jordan araya","La serena"],
                    ["Martin bugueño ","La serena"],
                    ["Dylan yanes","La serena"],
                    ["Diego Fajardo ","La Serena "],
                    ["Martin zarate","La serena"],
                    ["Alex dubo","La serena"],
                    ["Alexander Alarcón ","La serena "],
                    ["Raúl González ","La serena"],
                    ["Alfredo Abraham Castillo Díaz ","La Serena "],
                    ["Martin Seron","Puerto Montt"],
                    ["Sebastián Muñoz ","Puerto montt"],
                    ["Tomás Zúñiga ","Puerto montt"],
                    ["Sofia Subiabre","Puerto montt"],
                    ["Benjamin Hernandez","Santiago"],
                    ["Agustin jorquera ","La serena "],
                    ["Felipe valenzuela ","La serena "],
                    ["Eduard Suazo ","Chile "],
                    ["Sebastian Benavides ","Valdivia"],
                    ["Yerko araya","Coquimbo"],
                    ["Santiago Andres Jaramillo Parga","Punta Arenas"],
                    ["angel fuentes ","Punta arenas "]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def introLiturgia(self): 
        id_taller = 46
        nombre_taller = "Introducción a la liturgia"
        edad = "todas las edades (12 - 29)"
        lugar = "Sector Valponasca"
        tallerista = "Francisco Sumonte"
        integrantes = [["Joaquin alexis valdebenito arriagada ","Concepción "],
                        ["Joaquin Bravo","Talca"],
                        ["Tamara Garcia ","Concepción "]]

        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Animacion(self): 
        id_taller = 47
        nombre_taller =  "Animación"
        edad =  "15 - 20 años"
        lugar = "Sector Comedor"
        tallerista = "Elías Contreras"
        integrantes = [["María Esperanza Martínez Brizuela ","Los Andes"],
                        ["Maite Araceli Lemus Olivares ","Los Andes "],
                        ["Sofia celpa","Los andes"],
                        ["Javiera Sánchez ","Valparaiso "],
                        ["Florencia baack ","Valparaíso "],
                        ["Anais Maita","Iquique"],
                        ["Daniel Herrera","Iquique"],
                        ["Matias Zuleta","Iquique"],
                        ["Matias Navia Bustos","Iquique"],
                        ["Constanza Sanhueza","Santiago de Chile"],
                        ["Alan Saez ","Antofagasta"],
                        ["Matias Marambio ","Iquique "],
                        ["Genesis Segura Contreras","Puerto Montt"],
                        ["Martin Subiabre ","Puerto Montt "],
                        ["Silvia Frutos ","Asunción "],
                        ["Javier Arturo Pucheu Córdova ","Concepción "],
                        ["Francisca Hernandez ","Puerto Natales"],
                        ["Tomas Muñoz ","La serena "],
                        ["Rodrigo Castillo","La serena"],
                        ["Cristopher Hernández","Puerto Natales"],
                        ["Simon merino","Concepción "],
                        ["Martina González","Concepción "],
                        ["Diego San Martin ","Concepción "],
                        ["Ruben alonso valladares romero ","Linares "],
                        ["Eduardo Chandía","Concepcion"],
                        ["Cristóbal alegría ","Punta arenas "],
                        ["Axel rozas ","Punta arenas "],
                        ["Francisca Zúñiga ","Linares"],
                        ["Martin lopez ","Punta Arenas "],
                        ["sebastián huenumán","Punta Arenas"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def Malabarismo(self): 
        id_taller = 48
        nombre_taller = "Malabarismo artístico"  
        edad =  "todas las edades (12 - 29)"
        lugar =  "Zona Roma"
        tallerista = "Julian Prech"
        integrantes =  [["Martina Vargas","Puerto Montt"],
                        ["Estefania Katerine Peralta Peralta","Maule"],
                        ["Javiera Sánchez","Valparaiso"],
                        ["Florencia baack","Valparaíso"],
                        ["Benjamín Núñez","Santiago"],
                        ["Paz Cottenie Vargas","Puerto Montt"],
                        ["Sebastian Delgado","Puerto Natales"],
                        ["Casandra Olivares","Punta Arenas"],
                        ["Andree Hormazabal Norambuena","Linares"],
                        ["Mayta Conejeros","Valdivia"],
                        ["Benjamin Inostroza","Concepción"],
                        ["Matias alonso verdugo bravo","Talca"],
                        ["Magaly Rodríguez","La serena"],
                        ["Guido Torres","La Serena"],
                        ["Jeferson Rampos","Santiago"],
                        ["Mariana Salazar","Santiago"],
                        ["Giselle Jofre","Santiago"],
                        ["Cristóbal Ortega","Santiago"],
                        ["Joan Gutiérrez","Antofagasta"],
                        ["Nancy García","Santiago"],
                        ["Diego Mora Michea","Copiapo"],
                        ["Guillermo Henriquez","Talca"],
                        ["Diego Antonio Domingo Alfaro Wagner","Linares"],
                        ["Martin Reveco Villagra","Linares"]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def mimossketch(self): 
        id_taller = 49
        nombre_taller = "Mimos / Sketches"
        edad =  "todas las edades (12 - 29)"
        lugar = "Zona Turín"
        tallerista = "Manuel Aguilar"
        integrantes =  [["Matías Ignacio Barriga Contreras","Santiago de Chile"],
                        ["Vicente Basaure","Santiago de Chile"],
                        ["Sthephano nathano banchieri Suárez ","Santiago de chile"],
                        ["Kevin Gutiérrez López ","Copiapó "],
                        ["Ian Andrés Vilches Órdenes","Copiapó."],
                        ["Alexander pozo","Santiago "],
                        ["Dylan ","Talca"],
                        ["Emilio Ramirez Leiva","Santiago"],
                        ["Alexander Mustafa","Santiago"],
                        ["Valery Castro","santiago"],
                        ["Nicolás Cherme ","Antofagasta "],
                        ["Anyelo mancilla ","Puerto natales "],
                        ["Tomas calisaya alfaro","Alto hospicio"],
                        ["Karol Lobos ","Villa alemana"],
                        ["Carla Flores","Petorquita"],
                        ["Amaro Lobos ","Valparaíso "],
                        ["Rosa Carolina MUÑOZ","TALCA"],
                        ["Franz Yamil Quispe Alave ","La Paz"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def matetruco(self): 
        id_taller = 50
        nombre_taller = "Mate y truco"
        edad = "todas las edades (12 - 29)"
        lugar = "Zona Mornese"
        tallerista = "Kevin Raibaud"
        integrantes = [["Erwin Velasquez","Punta Arenas"],
                        ["Matías Cardenas isla","Punta Arenas"],
                        ["vicente oyarzo","punta arenas"],
                        ["Emily Cáceres","Alto hospicio"],
                        ["Carlos Aranda Badilla","Santiago"],
                        ["Jose luis canuman cardenas","Natales"],
                        ["Sebastián Ferreira Varela","Concepción"],
                        ["Agustín armando Mendoza roman","Concepción"],
                        ["Pablo ojeda ojeda","Punta arenas"],
                        ["Vicente Ferreira","Concepcion"],
                        ["Mariel Raposo","Concepción"],
                        ["Nicolas Fernandez","Alto Hospicio"],
                        ["Cristian Cid","Concepcion"],
                        ["Javier Ignacio Allende Diaz","Concepción"],
                        ["Maximilliano Cuevas","Punta arenas"],
                        ["David Alonso","Punta arenas, LSj"],
                        ["Fernando pizarro","punta arenas"],
                        ["Gabriel Mellado","Punta Arenas"],
                        ["Ditter maximiliano Samuel Cabrera carrasco","Alto hospicio"],
                        ["diego chacana","punta arenas"],
                        ["Juan Pablos Villalba muñoz","Concepción"],
                        ["Ian Chanquey","Punta Arenas"],
                        ["Amaro Carvajal","Concepción"],
                        ["Jorge Cano","Concepción"],
                        ["Benjamín Mora","Concepción"],
                        ["Diego Andrade","Valdivia"],
                        ["Benjamín Pérez","Punta Arenas"],
                        ["Maximiliano González","Santiago"],
                        ["Samuel Moreno Vargas","Punta Arenas"],
                        ["Pedro Ceballos","Punta Arenas"]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def lengua(self): 
        id_taller = 51
        nombre_taller = "Lengua de Señas"
        edad = "16 - 29 años"
        lugar = "Costado de Miguel Magone"
        tallerista = "Constanza Domínguez"
        integrantes = [["Beatriz Barrera Munita","Los Andes"],
                        ["Camila Alfaro ","Santiago "],
                        ["Guilianna Rosas","Los Andes "],
                        ["Michelle Goldschmidt ","Valparaíso "],
                        ["Francisca Julio","Valparaíso"],
                        ["Karolayn Cardenas ","Punta Arenas"],
                        ["Tiare caiguan","Punta Arenas"],
                        ["Fernanda Merino ","Santiago "],
                        ["Ana Cumare","Punta Arenas"],
                        ["Sebastián Alexis Paredes Altamirano ","Punta Arenas"],
                        ["Raimundo Cruz Corvalán","Santiago de Chile"],
                        ["Ignacio Andres Anabalón Mella","Santiago de Chile"],
                        ["Matías Ortiz","Santiago"],
                        ["Maria Ignacia Villalobos Zúñiga ","Talca"],
                        ["Franco Peñaloza","Santiago"],
                        ["Aaron Gallardo ","Santiago"],
                        ["Alonso Orellana","Santiago"],
                        ["Felipe Mendez","Santiago"],
                        ["martina andrade ","copiapó "],
                        ["Agustín Quijada ","Linares"],
                        ["Martín Díaz Pizarro ","Copiapó "],
                        ["MANUEL BARRIA","PUERTO MONTT"],
                        ["Blety Rivera ","Santiago "],
                        ["Anais Aros","Puerto Montt"],
                        ["Fernanda Lagos U. ","Puerto montt"],
                        ["Amaya Vargas","Puerto Montt"],
                        ["Anais Aros","Puerto Montt"],
                        ["Constanza Castillo ","Santiago "],
                        ["Loreto Chepilla ","Copiapó "],
                        ["Fernando maximiliano alcota Alfaro ","Copiapo "]]


        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def magia(self): 
        id_taller = 52
        nombre_taller = "Magia"
        edad = "12 - 16 años"
        lugar = "Costado Bartolomé Garelli"
        tallerista = "Romedil Ilufi"
        integrantes = [["Rocio Cárcamo ","Talca "],
                        ["Gabriella Carbone","Puerto Montt"],
                        ["Jake Hernández","Puerto Montt"],
                        ["Florencia Vergara","Talca"],
                        ["Yoisce Serón ","Puerto Montt "],
                        ["Trinidad Vidal","Puerto Montt"],
                        ["Scarlett Fuentes ","Puerto Montt"],
                        ["Giovanny Opazo","Santiago Centro"],
                        ["Jose Vera","PUERTO MONTT"],
                        ["David Villarroel ","Puerto Montt"],
                        ["Vicente Nuñez","Puerto Montt"],
                        ["Christopher Ávila","Alto Hospicio"],
                        ["Nahún Cantillano","Alto Hospicio"],
                        ["Giuliana Saez","Santiago "],
                        ["Remigio Maidana Arancibia ","Iquique "],
                        ["Kostis opazo","Antofagasta"],
                        ["Ángel Embry","Valparaíso "],
                        ["Anibal Asencio","Puerto montt"],
                        ["José Vera","Puerto Montt"],
                        ["Matias carilao","Puerto natales"],
                        ["Mathias Alfaro","Alto Hospicio"],
                        ["Ruben Segura","La serena"],
                        ["Simon fernandez Sasso","La serena"],
                        ["Tomás Vera","La serena "],
                        ["Sebastián Solís ","Puerto Montt "],
                        ["Sofia","Santiago"],
                        ["Carlos manzano ","Santiago "],
                        ["Tomas Samas","Santiago"],
                        ["Valentina Dinamarca","santiago"],
                        ["Enzo mancilla ","Valdivia "]]



        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def animereligion(self): 
        id_taller = 53
        nombre_taller = "Animé y religión"
        edad =  "todas las edades (12 - 29)"
        lugar =  "Costado Emma Ferrero"
        tallerista = "Matías Cifuentes"
        integrantes =  [["Catalina Valdés","Talca"],
                        ["Constanza Díaz ","Antofagasta "],
                        ["Alexander Lemus","Antofagasta"],
                        ["Martin Guerra ","Antofagasta "],
                        ["JORGE ALVAREZ","copiapo"],
                        ["Ignacio Yañez ","Santiago"],
                        ["Juan Paulo Raposo","Concepción"],
                        ["Joaquín Huamanga ","Santiago "],
                        ["Pedro pizarro","Santiago "],
                        ["Martín Valdés ","Santiago"],
                        ["Franco Muñoz","Santiago "],
                        ["Francisco Perez Aceituno","Santiago"],
                        ["Matilda vejar ","Concepción "],
                        ["Alessandro D'Angelo ","Santiago "],
                        ["Justin Arostica ","Copiapó "],
                        ["Sebastián Abarza","Santiago "]]

        
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def whasprevention(self): 
        id_taller = 54
        nombre_taller = "Wash Prevention"
        edad =  "todas las edades (12 - 29)"
        lugar = "Zona enfermería"
        tallerista = "Cruz Roja"
        integrantes =[["Maximiliano Barrios","Antofagasta"],
                    ["Javier Sanhueza Gutiérrez","Concepción"],
                    ["Justin Arostica","Copiapó"],
                    ["Diego Mora Michea","Copiapo"],
                    ["Emilio Sepulveda","Santiago centro"],
                    ["Valentina Bravo","Santiago"],
                    ["Martín Letelier","Talca"],
                    ["Emilia Taucan","santiago"],
                    ["Antonella Diaz Castillo","Valparaíso"],
                    ["Aleshka Cruz","Valparaiso"],
                    ["Mayra Anacona","Valparaiso"],
                    ["Pascale Pérez","Valparaíso"],
                    ["Danae Álvarez","Valparaiso"],
                    ["Pascale Pérez","Valparaíso"],
                    ["Anaís Echeverría","Valparaíso"],
                    ["Paola Espinoza","Valparaíso"],
                    ["Anaís Cabezas Vera","Valparaíso"],
                    ["Sofia Fernández Jiménez","Valparaíso"],
                    ["Martina Aguirre","Valparaíso"],
                    ["Fernanda Astorga","Valparaíso"]]


        
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def primerosauxiliospsicologicos(self): 
        id_taller = 55
        nombre_taller = "Primeros auxilios psicológico"
        edad =  "todas las edades (12 - 29)"
        lugar = "Zona enfermería"
        tallerista = "Cruz Roja"
        integrantes =[["Martina Alveal ","Santiago "],
                        ["Constanza Cortés ","Santiago "],
                        ["Eduarda Navarro ","Molina"],
                        ["Nicolás Campos ","Linares "],
                        ["Monserrath Tapia","Santiago"],
                        ["Matilda vejar ","Concepción "],
                        ["Nicolas Palma ","Santiago "],
                        ["Martina Opazo","Santiago"],
                        ["Martín Lizana","Santiago"],
                        ["Trinidad Valenzuela ","Santiago "],
                        ["Javiera Muñoz ","Concepción "],
                        ["Fernando Aguayo","Concepcion"],
                        ["Eduardo Ignacio Morán Muñoz","Talca"],
                        ["Juan Pablo Bachmann Saldivia ","Santiago "],
                        ["Beatriz Retamales","Santiago"],
                        ["Felipe Salinas","Santiago de Chile"],
                        ["Fernando Bastian González Droguett ","Santiago "],
                        ["Benjamin Carter","San ramon"],
                        ["María José Núñez ","Santiago "],
                        ["Sebastián Vargas","San Ramón"]]
        
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def primerosauxilioscomunitarios(self): 
        id_taller = 56
        nombre_taller = "Primeros auxilios comunitarios"
        edad =  "todas las edades (12 - 29)"
        lugar = "Zona enfermería"
        tallerista = "Cruz Roja"
        integrantes =[["Isidora Riquelme ","Santiago "],
                    ["Amelia Caneo ","Santiago "],
                    ["Francisca Miranda reyes","Santiago "],
                    ["Benjamín Montalbán ","Antofagasta "],
                    ["Sofia Nuñez C","Linares "],
                    ["Ari Espinoza","Linares "],
                    ["Luisa Ruiz","Puerto Natales"],
                    ["Trinidad castro","Santiago "],
                    ["Trinidad Chavol ","Santiago "],
                    ["Francisca Pinto ","Santiago "],
                    ["Alejandra Muñoz ","Santiago"],
                    ["Antonia Olguin ","Santiago"],
                    ["VALENTINA CONTRERAS","Santiago"],
                    ["Giselle jofre","Santiago "],
                    ["Mathías Piña","Santiago"]]

        
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes
    
    def futbolfemenino(self): 
        id_taller = 57
        nombre_taller = "Fútbol Femenino"
        edad =  "Todas las edades"
        lugar = "Canchas Patio Central"
        tallerista = "Ana Castro"
        integrantes = [["Isidora calderon","Los andes"],
                        ["Francisca Rudolph","Talca"],
                        ["Pia Vidal","Punta Arenas"],
                        ["victoria paredes","santa cruz"],
                        ["Agustina Parraguez","Santa cruz"],
                        ["Fernanda Arce Cabrera","Santa cruz"],
                        ["Constanza Oval","Punta Arenas"],
                        ["María José Rojas Rodríguez","Linares"],
                        ["Francisca Mella","Punta Arenas"],
                        ["Sophia Gonzalez","Puerto montt"],
                        ["Pascal Escobar","Linares"],
                        ["conzuelo caro","linares"],
                        ["Martina Becerra","Linares"],
                        ["Renata nuche","Linares"],
                        ["Constanza Vasquez","Linares"],
                        ["Lindsay Rodriguez","Punta Arenas"],
                        ["Dayana libuy","Santiago"],
                        ["Josefa areyte","Santiago"],
                        ["Camila marquez","Santiago"],
                        ["Pascuala Castillo","Santiago"],
                        ["Catalina Jorquera","Santiago centro"],
                        ["agustina cuevas","santiago"],
                        ["Sofia Cobo","Santiago"],
                        ["Emilia Espinosa","Linares"],
                        ["Barbara castillo","Linares"],
                        ["Samantha Pardo","Antofagasta"],
                        ["Daniela Gallardo","Santa Cruz"],
                        ["Catalina Santibañez","Santiago"],
                        ["Belen Sandoval","alto hospicio"],
                        ["Karol Cuero","Alto Hospicio"],
                        ["Luz Mery Duran","Calama"],
                        ["Fernanda Hernández","Linares"],
                        ["Isidora Alarcón","Linares"],
                        ["Martina Caballería","Valparaiso"],
                        ["tábata canales","valparaiso"]]
        return id_taller, nombre_taller, edad, lugar, tallerista, integrantes