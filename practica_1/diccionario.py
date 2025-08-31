#El programa va a funcionar consultando constantemente un diccionara para poder saber si el objeto en el que el usuario esta pensando cumple con las caracteristicas


#Estas son las carecteristicas principales que describen a las cosas que puede tener el usuario en mente
caracteristicas = ["objeto", "persona", "lugar", "vivo", "animal", "tecnologico","famoso",
"natural", "comestible", "transporte", "humano", "lugar_cerrado", "escribir", "entretenimiento",
"pequenio", "grande", "antiguo", "util_diario","humano_creo","semillas","crece_tierra","animal_proviene","escuela","investigacion"
,"aportacion", "actual" ,"1900", "1800", "1700", "1600", "1500","inventor","artista","filosofo", "escritor","musico","politico",
"empresario", "preparado","aprender","pintor","oficina"]

pensamiento = {


	#objetos
	"lapiz" : {"objeto": True, "oficina": True, "escuela": True,  "escribir": True, "humano_creo":True},
	"celular" : {"objeto": True, "tecnologico": True, "util_diario": True, "pequenio": True, "humano_creo": True, "escribir":True,"aprender":True},
	"silla" : {"objeto": True, "humano_creo": True, "util_diario": True},
	"automovil" : {"objeto": True, "transporte": True, "tecnologico":True, "humano_creo": True, "grande":True,"util_diario":True},
	"balon" : {"objeto": True, "entretenimiento": True, "pequenio": True},
	"teclado" : {"objeto": True, "escribir": True	, "tecnologico": True, "humano_creo": True, "util_diario": True, },
	"reloj" : {"objeto":True, "tecnologico": True, "pequenio": True, "util_diario":True, "humano_creo": True},
	"computadora" : {"objeto": True, "tecnologico":True, "escribir":True, "entretenimiento": True, "util_diario":True,"humano_creo": True,"aprender":True },
	"cubierto" : {"objeto": True,  "util_diario": True, "pequenio": True, "humano_creo":True},
	"television" : {"objeto": True, "tecnologico": True, "entretenimiento": True, "humano_creo": True},
	"fruta" : {"objeto": True, "comestible": True, "natural": True, "semillas":True},
	"verdura" : {"objeto": True, "comestible": True, "natural":True},
	"tuberculo" : {"objeto": True, "comestible": True, "natural":True, "crece_tierra":True},
	"carne" : {"objeto": True, "comestible":True, "natural": True, "animal_proviene": True},
	"botella" : {"objeto":True, "humano_creo":True, "util_diario": True},
	"leche" : {"objeto": True, "animal_proviene": True, "comestible": True, "natural": True},
	"huevo" : {"objeto": True, "animal_proviene": True, "comestible": True, "natural": True, "pequenio": True},
	"sandwich":{"objeto": True, "comestible":True, "preparado":True },
	"taco":{"objeto":True, "comestible":True, "preparado":True},
	"torta":{"objeto":True, "comestible": True, "preparado":True},
	"taza":{"objeto":True, "oficina":True, "escuela":True, "humano_creo":True, "util_diario":True},
	"ventilador": {"objeto": True, "oficina": True, "humano_creo":True, "tecnologico": True, "util_diario":True},
	"libro": {"objeto": True, "oficina":True, "escuela":True, "humano_creo": True, "aprender":True, "pequenio": True},
	"audifonos": {"objeto":True, "oficina":True, "escuela":True,"humano_creo":True, "tecnologico": True, "pequenio": True},
	"libreta": {"objeto": True, "oficina": True, "escuela":True, "humano_creo":True, "escribir":True, "aprender": True},

 	#lugares

	"paris" : {"lugar": True, "famoso": True, "lugar_cerrado": False},
	"playa" : {"lugar": True, "natural": True, "entretenimiento": True},
	"cine" : {"lugar": True, "lugar_cerrado": True, "entretenimiento": True},
	"escuela" : {"lugar": True, "lugar_cerrado": True, "util_diario": True},
	"museo" : {"lugar": True, "lugar_cerrado": True, "antiguo": True},
	"desierto" : {"lugar": True, "natural": True, "grande": True},
	"volcan" : {"lugar": True, "natural": True, "grande": True},
	"oficina" : {"lugar": True, "lugar_cerrado": True, "util_diario": True},
	"parque" : {"lugar": True, "natural": True, "entretenimiento": True},
	"marte" : {"lugar": True, "natural": True, "famoso": True},
	"escom" : {"lugar": True, "escribir":True, "humano_creo":True, "escuela": True, 'investigacion': True, "lugar":True},
	"cic" : {"lugar":True, "escribir": True, "humano_creo":True, "investigacion": True, 'escuela': True, "lugar_cerrado":True},


	#personas

	"Einstein": {"persona": True, "famoso": True, "aportacion": True, "1800": True, "1900": True},
	"Gauss": {"persona": True, "famoso": True, "aportacion": True, "1700":True, "1800": True},
	"Fourier": {"persona": True, "famoso": True, "aportacion":True, "1700":True, "1800":True},
	"Laplace": {"persona": True, "famoso":True, "aportacion":True,"1700":True, "1800": True},
	"Curie": {"persona": True, "famoso": True, "aportacion": True, "cientifico": True, "1900": True},
	"Tesla": {"persona": True, "famoso": True, "aportacion": True, "inventor": True, "cientifico": True, "1800": True, "1900": True},
    "Edison": {"persona": True, "famoso": True, "aportacion": True, "inventor": True, "1800": True, "1900": True},
    "Da Vinci": {"persona": True, "famoso": True, "aportacion": True, "inventor": True, "artista": True, "cientifico": True, "1500": True, "siglo_XVI": True},
	"Picasso": {"persona": True, "famoso": True, "artista": True, "1900": True, "pintor": True},
    "Van Gogh": {"persona": True, "famoso": True, "artista": True, "1800": True, "pintor": True},
    "Camus": {"persona": True, "famoso": True, "escritor": True, "1900": True, "filosofo": True}, 
    "Schopenhauer": {"persona": True, "famoso":True, "escritor":True, "1800":True, "1700": True, "filosofo": True},
    "John Lennon": {"persona": True, "famoso": True, "escritor":True, "1900":True, "artista": True, "musico": True},
    "Thom Yorke": {"persona":True, "famoso":True, "escritor": True, "1900":True, "2000":True, "musico":True, "artista":True},
    "Gustavo Cerati": {"persona":True, "famoso":True, "escritor":True, "1900":True, "2000":True, "musico":True, "artista":True},
  	"Charly Garcia": {"persona": True, "famoso": True, "escritor": True, "1900":True, "2000":True, "musico":True, "artista":True},
  	"AMLO": {"persona":True, "famoso":True, "escritor": True, "politico":True, "1900":True, "2000":True},
  	"Trump": {"persona": True, "famoso":True, "politico":True, "empresario":True, "1900":True, "2000": True},

}

#Las preguntas que se hacen con base en las caracteristicas.
#"¿? (s/n): ",

preguntas = {
	"objeto" :"¿Es un objeto fisico? (s/n): ",
	"persona" : "¿Es una persona real o ficticia? (s/n): ",
	"lugar" : "¿Es un lugar? (s/n): ",
	"animal":  "¿Es algun tipo de animal? (s/n): " ,
	"vivo": "¿Es algo que esta o estuvo vivo? (s/n): ",
	"tecnologico": "¿Esta relacionado con la tecnologia? (s/n): ",
	"famoso": "¿Es algun lugar o persona famosos? (s/n): ",
	"natural": "¿Es algo que se obtiene directamente de la naturaleza? (s/n): ",
	"comestible": "¿Es algo comestible para el ser humano? (s/n): ",
	"transporte": "¿Es algun medio de transporte? (s/n): ",
	"humano": "¿Es un ser humano? (s/n): ",
	"lugar_cerrado": "¿Es un lugar cerrado (no cuenta con espacios abiertos) ? (s/n): ",
	"escribir": "¿Sirve para escribir, o se puede escribir en el? (s/n): ",
	"entretenimiento": "¿Es alguna forma de entretenimiento? (s/n): ",
	"pequenio": "¿Es un objeto pequenio? (s/n): ",
	"grande": "¿Es un objeto grande? (s/n): ",
	"antiguo": "¿Es algo antiguo o historico? (s/n): ",
	"util_diario": "¿Es algo que se le puede sacar provecho en el dia a dia (una herramienta)? (s/n): ",
	"humano_creo": "¿Fue creado por los humanos? (s/n): ",
	"semillas": "¿Contiene semillas? (s/n): ",
	"crece_tierra": "¿Es algo que crece dentro de la tierra(bajo tierra)? (s/n): ",
	"animal_proviene": "¿Es algo que proviene de un animal? (s/n): ",
	"escuela": "¿Es una escuela? (s/n): ",
	"investigacion": "¿Es un centro de investigacion? (s/n): ",
	"aportacion": "¿La persona hizo alguna aportacion a la ciencia o tecnologia? (s/n): ",
	"actual" : "¿La persona es de la epoca contemporane (1980-2025)? (s/n): ",
	"1900": "¿La persona estuvo vivo durante los anios entre  1900-1980)? (s/n): ",
	"1800": "¿La persona estuvo vivo durante los anios entre 1800-1900)? (s/n): ",
	"1700": "¿La persona estuvo vivo durante los anios entre 1700-1800)? (s/n): ",
	"1600": "¿La persona estuvo vivo durante los anios entre 1600-1700)? (s/n): ",
	"1500": "¿La persona estuvo vivo durante los anios entre 1500-1600)? (s/n): ",
	"inventor": "¿La persona invento algo tangible? (s/n): ",
	"artista": "¿La persona es algun tipo de artista? (s/n): ",
	"escritor": "¿La persona es un escritor? (s/n): ",
	"filosofo":"¿La persona es un filosofo? (s/n): ",
	"musico": "¿La persona es un musico? (s/n): ",	
	"politico": "¿La persona es un politico o esta relacionad con la politica? (s/n):",
	"empresario": "¿La persona es un empresario? (s/n):",
	"preparado": "¿Es un alimento preparado? (s/n):",
	"aprender": "¿Es un objeto que sirve para aprender? (s/n): ",
	"pintor": "¿La persona es un pintor? (s/n): ",
	"oficina": "¿El objeto se puede encontrar en alguna oficina	? (s/n): "
	}

