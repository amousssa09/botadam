from tabnanny import check
import os
import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Ahora sí leemos el token de forma segura
TOKEN = os.getenv("DISCORD_TOKEN")
print("TOKEN:", TOKEN)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    try:
        # Sincronización global para que aparezcan en servidores y MDs
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos de barra diagonal de forma global.")
    except Exception as e:
        print(f"Error sincronizando comandos: {e}")

@bot.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Espera {round(error.retry_after, 1)} segundos antes de usarlo otra vez.")

# Comandos basicos

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def hola(ctx):
    await ctx.send("Quihubo parcero")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def prueba(ctx):
    await ctx.send("tamo activo papi")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def adios(ctx):
    await ctx.send("que Dios me lo bendiga")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def decir(ctx, *, mensaje):
    if ctx.interaction:
        # Si es comando Slash (/), solo enviamos el mensaje sin intentar borrar
        await ctx.send(mensaje)
    else:
        # Si es comando normal (!), borramos el mensaje original
        await ctx.message.delete()
        await ctx.send(mensaje)

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def saludar(ctx):
    await ctx.send(
        f"Hola {ctx.author.mention}, en primer lugar no me obligues a saludarte que te doy dos vueltas, y en segundo lugar, que dios lo bendiga."
    )

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def evento(ctx):
    try:
        personas = ["Adam", "Wick", "Cuervo", "Luuc", "Monsi", "Sanax", "Lucia"]

        situaciones = [
            "{persona1} está tranquilamente sentada viendo anime hasta que de repente viene {persona2} y le recomienda un hentai.",
            "{persona1} fue al baño y {persona2} le empezó a narrar la partida.",
            "{persona1} estaba en su funeral hasta que llegó {persona2} a pedir cargador.",
            "{persona1} abrió TikTok y apareció {persona2} bailando en su para ti.",
            "{persona1} estaba jugando al escondite hasta que {persona2} dijo 'como mi papá'.",
            "{persona1} estaba viendo Doraemon hasta que {persona2} preguntó si tenía bolsillo para órganos.",
            "{persona1} estaba viendo Bob Esponja hasta que {persona2} preguntó '¿por qué no se ahoga?'."
        ]

        persona1, persona2 = random.sample(personas, 2)

        situacion = random.choice(situaciones)
        mensaje_final = situacion.format(persona1=persona1, persona2=persona2)

        await ctx.send(mensaje_final)

    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def insultar(ctx, usuario: discord.Member):
    insultos = [
        "Tu cara es fácil de dibujar",
        "Cuando te pones en la balanza, la balanza dice de uno en uno porfavor",
        "Tu madre te queria abortar pero no tenia dinero",
        "Tu padre dijo que iria a por la leche y aun le sigues esperando en la puerta",
        "Eres el motivo por el que el champú tiene instrucciones",
        "En el esquema evolucion humana, te quedaste en la segunda etapa",
        "Eres muy bueno, llegarás muy cerca",
    ]
    
    insulto = random.choice(insultos)
    await ctx.send(f"{usuario.mention}, {insulto}")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def consejo(ctx):
    consejos = [
        "Si tienes hambre, come",
        "Si la vida te da limones, devuelvelos porque están caros",
        "Si se rompe, pégalo con cinta",
        "Si te falta tiempo, usa reloj",
        "Nunca aceptes consejos de este bot",
        "Si estas aburrido, encuentrate",
        "Si no puedes dormir, entonces cierra los ojos",
        "Si no lo puedes ver con claridad, abre los ojos",
    ]

    consejo = random.choice(consejos)

    await ctx.send(consejo)

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def miish(ctx):
    await ctx.send("bah ya vino una autista ya me voy")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def preguntar(ctx, *, pregunta):
    respuestas = [
        "Sí",
        "Por mis muertos que si",
        "Nah",
        "No",
        "Podria ser",
        "Eso es mas imposible que tener una relacion con Megan Fox",
        "Buscalo en google",
        "En otra vida",
        "Confia en el proceso, al menos eso dijo mi abuelo y ahora está sin brazos ni piernas",
        "Si eso pasara, el mundo ya estaria en quinta guerra mundial",
        "Pregunta en otro momento",
        "Preguntale a tu mama",
    ]

    respuesta = random.choice(respuestas)
    await ctx.send(respuesta)

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def caraocruz(ctx):
    preguntas = [
        "Cual es tu red flag más grande?",
        "Qué es la cosa más rara que hiciste que no contaste a nadie?",
        "Si pudieras decirle algo que no pudiste a alguien, a quién y qué le dirías?",
        "Qué es algo que nunca le has contado a casi nadie?",     
        "¿Cuál es tu peor arrepentimiento?",   
        "¿Qué es algo que te gustaría cambiar de tu pasado?",
    ]

    pregunta = random.choice(preguntas)
    await ctx.send(pregunta)

    await ctx.send("Si sale cara, respondes, si sale cruz, te salvas")
    
    resultado = random.choice(["cara", "cruz"])
    await ctx.send(f"Salió {resultado}")

    if resultado == "cara":
        await ctx.send("Te toca responder")

    else: 
        await ctx.send("Salio cruz, te salvaste de la pregunta")
        
@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def expansiondedominio(ctx, usuario: discord.User):
    embed = discord.Embed(description=f"{ctx.author.mention} activa su expansión de dominio: Torsión testicular contra {usuario.mention}", color = discord.Color.purple())
    embed.set_image(url="https://media.tenor.com/MuMLDWrW95gAAAAd/gojo-domain-expansion.gif")

    vista = discord.ui.View()

    boton = discord.ui.Button(
        label = "Contraatacar",
        style = discord.ButtonStyle.red
    )

    async def respuesta_boton(interaction):
        
        embed_contra = discord.Embed(description = f"{usuario.mention} decide contraatacar y expandir su dominio!", color = discord.Color.red())
        embed_contra.set_image(url = "https://media.tenor.com/IshTvIE9w0UAAAAd/sukuna-domain-expansion.gif")

        await interaction.response.send_message(embed=embed_contra)
    
    boton.callback = respuesta_boton

    vista.add_item(boton)

    await ctx.send(embed=embed, view=vista)


@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def ahorcado(ctx):
    # Evita el error de "La aplicación no ha respondido" dándole tiempo al bot
    if ctx.interaction:
        await ctx.interaction.response.defer()

    palabras = [
        "esternocleidomastoideo",
        "barrabasadas",
        "espantaviejas",
        "claudia",
        "uik",
        "conanemia",
        "bodadoble",
        "cipote",
        "aparatoreproductormasculino",
        "glandulasmamarias", 
        "elpreciodelamor",
        "cuervo",
        "Ultracrepidario",
    ]

    palabra_secreta = random.choice(palabras)
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos = 10
   
    # Checkeamos que el usuario escriba en el mismo canal (sirve para servidores y MDs)
    def check(mensaje):
        return mensaje.author == ctx.author and mensaje.channel == ctx.channel

    await ctx.send(f"¡Empezamos! Palabra: `{' '.join(letras_adivinadas)}`")

    # BUCLE DEL JUEGO
    while intentos > 0 and "_" in letras_adivinadas:
        try:
            msg = await bot.wait_for("message", check=check, timeout=30.0)
            intento_usuario = msg.content.lower()

            # Compruena que el down del usuario no escriba mal
            if len(intento_usuario) != 1 or not intento_usuario.isalpha():
                await ctx.send("Por favor, ingresa una sola letra válida.")
                continue
                
            if intento_usuario in palabra_secreta: 
                # comprobamos que la letra esté en la palabra
                # 'enumerate' nos da el número de la caja (i) y lo que hay dentro (letra)
                for i, letra in enumerate(palabra_secreta):
                    if letra == intento_usuario:
                        letras_adivinadas[i] = intento_usuario

                await ctx.send(f"Buena ahi crack, tras una dura conexión neuronal, atinaste una letra.\nPalabra: `{' '.join(letras_adivinadas)}`")

            else: 
                intentos -= 1 # Si no está en la palabra, resta un intento
                await ctx.send(f"Uy, esa letra no está en la palabra, te quedan {intentos} intentos")
                await ctx.send(f"`{' '.join(letras_adivinadas)}`")

        except asyncio.TimeoutError:   
            return await ctx.send("Se acabó el tiempo, mejor suerte la próxima vez.") # Si el usuario pasa el tiempo establecido, se acaba la partida-
        
    if "_" not in letras_adivinadas: # Comprueba si ganó el juego
        await ctx.send(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
    else:
        await ctx.send(f"Has perdido. La palabra era: {palabra_secreta}")

@bot.hybrid_command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def hdp(ctx):
    jugadores = []

    cartas_blancas = [
        "La ada wong",
        "Claire",
        "Sida",
        "Mujer en plena menstruacion",
        "Uik 2023",
        "El precio del amor",
        "Cuervo escribiendote al md",
        "Hacerse la de luuc",
        "El fantasma de tu historial",
    ]

    cartas_negras = [
        "¿Qué es lo que nunca falta en una fiesta de Uik?",
        "¿Qué es lo que más le gusta a Uik en la cama?",
        "Existen muy malas formas de morir, disparado, cayendo en las escaleras, pero tambien esta de___",
        "Que es lo peor de esta vida?",
        "Cual es la mejor epoca de todas?",
        "Lo mejor que puedes hacer hoy es____",
    ]

    embed = discord.Embed(
        title="bienvenido al juego del sexo, donde todas las fantasias como las de uik se cumplen",
        description="quieres fantasear con una pelirroja o una peliverde? de una socio",
        color=discord.Color.red()
    )

    class BotonUnirse(discord.ui.View):
        @discord.ui.button(label="Unirse (que rico)", style=discord.ButtonStyle.green)
        async def unirse(self, interaction, button):
            if interaction.user in jugadores:
                await interaction.response.send_message("no a las barrabasadas socio, ya estás dentro")
            elif len(jugadores) >= 8:
                await interaction.response.send_message("El juego ya está lleno mi pana, tendrás que esperar, te puedes hacer una paja por ejemplo QQQ")
                return
            else: 
                jugadores.append(interaction.user)
                await interaction.response.send_message("bienvenido a la fiestaa, espero que hayas traido aceite de bebé, lo vas a necesitar")
                texto_actualizado = ""
                for jugador in jugadores:
                    texto_actualizado = texto_actualizado + f"{jugador.mention}\n"
                embed_nuevo = discord.Embed(
                    title="bienvenido al juego del sexo, donde todas las fantasias como las de uik se cumplen",
                    description=f"**Jugadores**:\n{texto_actualizado}",
                    color=discord.Color.red()
                )
                await interaction.message.edit(embed=embed_nuevo)

    vista = BotonUnirse()  # <--- Guardas el botón
    mensaje = await ctx.send(embed=embed, view=vista)  # <--- Usas la variable
    
    # COOLDOWN DE 15s
    await asyncio.sleep(15)
    
    for child in vista.children:
        child.disabled = True
    await mensaje.edit(view=vista)
    await ctx.send("ggs socio la partida va a empezar")

# COMPROBAMOS QUE HAYA MAS DE 3 JUGADORES
    if len(jugadores) < 3:
        await ctx.send("pero socio, necesitamos al menos 3 jugadores, vuelve con más gente")
        return # Esto termina el comando

    # PREPARACIÓN INICIAL (fuera del while)
    manos = {}
    puntos = {}
    ronda_actual = 1
    rondas_totales = 5
    mazo = cartas_blancas.copy()
    random.shuffle(mazo)

    # ESCOGEMOS AL HDP FIJO PARA TODA LA PARTIDA
    hdp_actual = random.choice(jugadores)

    # Inicializar puntos
    for jugador in jugadores:
        puntos[jugador] = 0

    # ASIGNAMOS LOS ROLES (UNA SOLA VEZ)
    for jugador in jugadores:
        if jugador == hdp_actual:
            await ctx.send(f"{jugador.mention}, eres el HDP de toda la partida")
        else:
            await ctx.send(f"{jugador.mention} eres un respondedor")

    # REPARTIMOS LAS CARTAS (5 por jugador)
    respondedores = [j for j in jugadores if j != hdp_actual]
    for i, jugador in enumerate(respondedores):
        manos[jugador] = mazo[i*5 : i*5+5]

    # MANDAMOS LAS CARTAS AL DM (solo una vez)
    for jugador, cartas in manos.items():
        try:
            await jugador.send(f"Tus cartas son: {', '.join(cartas)}") # Enviamos las cartas al DM
        except:
            await ctx.send(f"Abre tus DMS para que pueda mandarte tus cartas, {jugador.mention}")

    # BUCLE DE RONDAS
    while ronda_actual <= rondas_totales:
        await ctx.send(f"🔥 RONDA {ronda_actual} DE {rondas_totales}") # Anunciamos la ronda actual

    # SE CREA EL EMBED
        texto_jugadores = ""
        for j in jugadores:
            if j != hdp_actual:  # El HDP no cuenta como jugador en el embed
                texto_jugadores += f"{j.mention}\n"
        
        partida = discord.Embed(
            title="PARTIDA",
            description=f"HDP: {hdp_actual.mention}\nJUGADORES:\n{texto_jugadores}"
        )

        carta_negra = random.choice(cartas_negras)

        partida.add_field(name="🖤 Carta Negra", value=carta_negra, inline=False)

        await ctx.send(embed=partida)

    # EL JUGADOR ELIGE LAS CARTAS PARA LA RONDA (TODOS A LA VEZ)
        cartas_jugadas = {}

        # Función dentro del comando para manejar a un jugador
        async def elegir_carta(jugador):
            cartas = manos[jugador]
            dm_cartas = "Elige tu carta para la ronda:\n"
            for numero, carta in enumerate(cartas, start=1): # Enumerate nos da el número de la carta (numero) y lo que hay dentro (carta)
                dm_cartas += f"{numero}. {carta}\n" # Creamos un string con las opciones para el respondedor
            await jugador.send(dm_cartas)

            respuesta = await bot.wait_for("message", check=lambda msg: msg.author == jugador and isinstance(msg.channel, discord.DMChannel), timeout=60) # Esperamos la respuesta del jugador en su DM
            indice = int(respuesta.content) - 1 # Guardamos el índice de la carta elegida, restando 1 para ajustar el índice
            carta_elegida = cartas[indice] # Guardamos la carta elegida
            cartas_jugadas[jugador] = carta_elegida # Guardamos la carta elegida en el diccionario de cartas jugadas
            await jugador.send(f"Has elegido: {carta_elegida}") # Confirmamos la elección al jugador
            cartas.pop(indice) # Quitar la carta de la mano (descartar)

        # Lanzar todas las elecciones en paralelo
        tareas = []
        for jugador in jugadores:
            if jugador != hdp_actual:
                tareas.append(asyncio.create_task(elegir_carta(jugador))) # Creamos una tarea por cada jugador

        await asyncio.gather(*tareas) # Esperamos a que TODOS los jugadores respondan a la vez

        pares = list(cartas_jugadas.items()) # Guardamos las cartas jugadas en una lista de pares (jugador, carta)
        random.shuffle(pares) # Mezclamos el orden de las cartas para que el HDP no sepa quien jugó cada carta

    # EL HDP ELIGE QUIEN GANA
        opciones_hdp = ""

        for numero, (jugador, carta) in enumerate(pares, start=1): # Enumerate nos da el número de la caja (numero) y lo que hay dentro (carta), con start=1 empezamos a counting desde 1 en vez de 0
            opciones_hdp += f"{numero}. {carta}\n" # Creamos un string con las opciones para el HDP, enumerando las cartas de forma anonima

        await hdp_actual.send(f"Estas son las cartas jugadas por los respondedores:\n{opciones_hdp}\nElige la mejor carta para ganar la ronda") # Enviamos las opciones al HDP para que elija la mejor carta
        respuesta_hdp = await bot.wait_for("message", check=lambda msg: msg.author == hdp_actual and isinstance(msg.channel, discord.DMChannel), timeout=30) # Esperamos la respuesta del HDP, con un timeout de 30 segundos

        ganador, carta_ganadora = pares[int(respuesta_hdp.content) - 1]  # Guardamos el ganador y la carta ganadora, restando 1 para ajustar el índice
        puntos[ganador] += 1 # Sumamos un punto al ganador

        await ctx.send(f"🏆 La carta ganadora es: **{carta_ganadora}**\n¡Gana {ganador.mention}! ({puntos[ganador]} pts)") # Anunciamos la carta ganadora y felicitamos al ganador

        ronda_actual += 1 # Pasamos a la siguiente ronda

    # FINAL DE LA PARTIDA
    ganador_juego = max(puntos, key=puntos.get) # Obtenemos el jugador con más puntos
    await ctx.send(f"🎉 ¡FIN DEL JUEGO! El ganador es {ganador_juego.mention} con {puntos[ganador_juego]} puntos. ¡Este tiene potencial para islas! 🏝️") # Anunciamos al ganador finalx

# El comando con los contextos de instalación para MD habilitados
@bot.tree.command(name="barrabasadometro", description="Mide el calibre de una barrabasada.")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) # <- Permite MDs
@app_commands.allowed_installs(guilds=True, users=True)                     # <- Permite instalar en usuario
# Menu desplegable de opciones
@app_commands.choices(nivel=[
    app_commands.Choice(name="Calibre 1 - Antibarrabasada", value=1), #
    app_commands.Choice(name="Calibre 2 - Minibarrabasadai", value=2),
    app_commands.Choice(name="Calibre 3 - Barrabasada", value=3),
    app_commands.Choice(name="Calibre 4 - Barrabasada de calibres bíblicos", value=4),
    app_commands.Choice(name="Calibre 5 - Barrabasada de calibres INTERDIMENSIONALES", value=5)
])
async def barrabasado_slash(interaction: discord.Interaction, nivel: int):
    # Diccionario con cada una de las imagenes
    imagenes_barrabasada = {
        1: {"url": "https://i.imgur.com/i5rZwbU.jpg", "desc": "Antibarrabasada"},
        2: {"url": "https://i.imgur.com/NzjmlDA.jpg", "desc": "Minibarrabasadai"},
        3: {"url": "https://i.imgur.com/skrXjCH.jpg", "desc": "Barrabasada"},
        4: {"url": "https://i.imgur.com/DWmQWMm.jpg", "desc": "Barrabasada de calibres bíblicos"},
        5: {"url": "https://i.imgur.com/hs20NMf.jpg", "desc": "Barrabasada de calibres INTERDIMENSIONALES"}
    }
    # Obtenemos datos
    datos = imagenes_barrabasada[nivel]
    # Creamos embed
    embed_barrabasada = discord.Embed(
        description=f"🔬 {interaction.user.mention} ha usado el barrabasadómetro y el resultado es:\n**{datos['desc']}**", 
        color=discord.Color.red()
    )
    # MEtemos la imagen
    embed_barrabasada.set_image(url=datos["url"])
    # MANDAMOS
    await interaction.response.send_message(embed=embed_barrabasada)

bot.run(TOKEN)