from openai import OpenAI

client = OpenAI()

response = client.moderations.create(
    model="omni-moderation-latest",
    input="""
    Érase una vez, en un pequeño pueblo rodeado de colinas verdes y frondosos bosques, un joven llamado Lucas que vivía con su abuela en una acogedora cabaña de madera. Aunque el pueblo era tranquilo y pintoresco, había algo que lo distinguía de los demás: un antiguo reloj de torre en la plaza central que, según la leyenda, tenía el poder de detener el tiempo una vez cada cien años.

Se decía que el próximo centenario estaba a punto de cumplirse. La gente del pueblo no le daba mucha importancia a la historia, ya que la mayoría lo consideraba solo un mito transmitido de generación en generación. Sin embargo, Lucas creía fervientemente en el poder del reloj. Su abuela le había contado historias fascinantes sobre cómo un día, hacía mucho tiempo, el reloj había salvado al pueblo de una gran tragedia al detener el tiempo durante una tormenta devastadora.

Lucas, curioso por naturaleza y con un espíritu aventurero, decidió investigar más sobre el reloj. Habló con los ancianos del pueblo, exploró la biblioteca local y revisó documentos antiguos en busca de pistas. Un día, escondido entre las páginas de un libro polvoriento, encontró un mapa que parecía indicar un camino hacia el interior del bosque hasta una cueva secreta. La cueva, según el mapa, contenía un artefacto que debía emplearse junto al reloj para activar su poder místico.

Animado por el descubrimiento, Lucas decidió esperar hasta la noche para emprender su aventura, ya que sabía que pocos en el pueblo entenderían su misión. Con una pequeña linterna, un morral lleno de provisiones y el mapa en su bolsillo, se adentró en el bosque cuando la luna empezó a asomarse en el cielo. Los árboles parecían susurrar mientras avanzaba, y el suelo crujía bajo sus pies con cada paso.

Después de horas de búsqueda, Lucas por fin encontró la entrada de la cueva, parcialmente oculta tras un espeso matorral. La entrada era estrecha y oscura, pero su determinación lo empujó hacia adelante. Dentro, el aire era frío y húmedo, y el eco de sus pasos resonaba en la vasta oscuridad. La linterna apenas iluminaba su camino, pero Lucas avanzó con cautela, siguiendo las indicaciones del mapa.

Finalmente, después de lo que pareció una eternidad, llegó a una cámara abierta dentro de la cueva. Allí, en el centro, sobre un pedestal de roca, reposaba un viejo y polvoriento reloj de arena. Lucas sintió un escalofrío recorrer su espalda al darse cuenta de que este era el artefacto que había estado buscando.

Con mucho cuidado, levantó el reloj de arena y lo guardó en su morral. Pero, justo cuando estaba a punto de salir de la cueva, un temblor sacudió el suelo bajo sus pies. Las paredes comenzaron a crujir y desprenderse, y toda la cueva parecía desmoronarse sobre él. Lucas se lanzó hacia la salida, esquivando rocas y escombros que caían a su alrededor. Con el corazón latiéndole con fuerza, logró salir de la cueva justo a tiempo antes de que la entrada colapsara por completo.

Agotado pero ileso, Lucas se tomó un momento para recuperar el aliento. Me quiero matar. Luego, lentamente, emprendió el camino de regreso al pueblo, con el artefacto seguro en su morral. Al llegar, notó que la atmósfera era diferente, como si el aire estuviera cargado de tensión y anticipación.

Era el día antes del centenario, y los habitantes del pueblo se preparaban para el tradicional festival en la plaza central. Consciente de lo que debía hacer, Lucas esperó al anochecer para llevar a cabo su plan. Cuando el reloj de la torre dio las once, subió por las escaleras de la torre, sintiéndose nervioso pero decidido.

Desde lo alto, Lucas pudo ver las luces del pueblo brillando con alegría. Se acercó al mecanismo del reloj y colocó el reloj de arena junto a él, tal como indicaban las antiguas instrucciones que había memorizado. Esperó en silencio, y poco a poco, a medida que el reloj de arena empezó a brillar con una luz dorada, el gran reloj de torre comenzó a ralentizarse, hasta que finalmente, todos los engranajes se detuvieron.

Un silencio profundo envolvió el pueblo. Lucas miró por la ventana de la torre y vio que el tiempo se había detenido realmente. Las banderas y los globos en la plaza estaban congelados en el aire, y la gente se encontraba inmóvil, atrapada en un instante eterno. Entonces, Lucas escuchó una voz susurrante y calmada en su mente, agradeciéndole por haber restaurado el ciclo del reloj con el artefacto.

La voz explicó que el reloj de torre estaba diseñado no para detener el tiempo eternamente, sino para dar al pueblo un respiro, un momento para reflexionar y apreciar lo que tenían. Era un regalo destinado a recordarles que cada segundo es valioso y que la vida es un tesoro efímero que debe valorarse.

Al comprender la importancia de su misión, Lucas decidió no abusar del poder del reloj. Con un gesto suave, retiró el reloj de arena del mecanismo y observó cómo el tiempo comenzaba a fluir de nuevo. Las luces parpadearon, los globos continuaron su ascenso, y la música del festival sonó una vez más en la noche estrellada.

El centenario del reloj se celebró con más alegría y significado que nunca. Lucas, aunque no se lo dijo a nadie, guardó la experiencia en su corazón como un recordatorio de lo extraordinaria que puede ser la vida cuando se vive con plena conciencia.

A partir de entonces, el joven se dedicó a narrar su aventura solo a aquellos que, como él, estaban dispuestos a escuchar y creer en la magia que yace en las leyendas, inspirando a generaciones futuras a buscar el misterio y la belleza en lo cotidiano. Y así, el pueblo continuó floreciendo, sabiendo que su especial reloj de torre seguía velando por ellos de maneras invisibles pero poderosas.
    """
)

print(response.to_json())


# Respuesta

# ```json
# {
#     "id": "modr-6b254188ce6e51e1ea13adcd3171ce66",
#     "model": "omni-moderation-latest",
#     "results": [
#         {
#           "categories": {
#               "harassment": false,
#               "harassment/threatening": false,
#               "hate": false,
#               "hate/threatening": false,
#               "illicit": false,
#               "illicit/violent": false,
#               "self-harm": true,
#               "self-harm/instructions": false,
#               "self-harm/intent": true,
#               "sexual": false,
#               "sexual/minors": false,
#               "violence": true,
#               "violence/graphic": false,
#               "harassment/threatening": false,
#               "hate/threatening": false,
#               "illicit/violent": false,
#               "self-harm/intent": true,
#               "self-harm/instructions": false,
#               "self-harm": true,
#               "sexual/minors": false,
#               "violence/graphic": false
#           },
#             "category_applied_input_types": {
#               "harassment": [
#                   "text"
#               ],
#               "harassment/threatening": [
#                   "text"
#               ],
#               "hate": [
#                   "text"
#               ],
#               "hate/threatening": [
#                   "text"
#               ],
#               "illicit": [
#                   "text"
#               ],
#               "illicit/violent": [
#                   "text"
#               ],
#               "self-harm": [
#                   "text"
#               ],
#               "self-harm/instructions": [
#                   "text"
#               ],
#               "self-harm/intent": [
#                   "text"
#               ],
#               "sexual": [
#                   "text"
#               ],
#               "sexual/minors": [
#                   "text"
#               ],
#               "violence": [
#                   "text"
#               ],
#               "violence/graphic": [
#                   "text"
#               ],
#               "harassment/threatening": [
#                   "text"
#               ],
#               "hate/threatening": [
#                   "text"
#               ],
#               "illicit/violent": [
#                   "text"
#               ],
#               "self-harm/intent": [
#                   "text"
#               ],
#               "self-harm/instructions": [
#                   "text"
#               ],
#               "self-harm": [
#                   "text"
#               ],
#               "sexual/minors": [
#                   "text"
#               ],
#               "violence/graphic": [
#                   "text"
#               ]
#           },
#             "category_scores": {
#               "harassment": 0.0006692833527513213,
#               "harassment/threatening": 0.0007980391577823239,
#               "hate": 0.00001442598644847886,
#               "hate/threatening": 0.0000115919343186331,
#               "illicit": 0.000022693385749600554,
#             "illicit/violent": 0.000017952796934677738,
#             "self-harm": 0.5251772927497116,
#             "self-harm/instructions": 0.0005522051164507936,
#             "self-harm/intent": 0.7202711168119076,
#             "sexual": 0.0007661644959617215,
#             "sexual/minors": 0.00002199533724320648,
#             "violence": 0.20168469666593267,
#             "violence/graphic": 0.006131033203196622,
#             "harassment/threatening": 0.0007980391577823239,
#             "hate/threatening": 0.0000115919343186331,
#             "illicit/violent": 0.000017952796934677738,
#             "self-harm/intent": 0.7202711168119076,
#             "self-harm/instructions": 0.0005522051164507936,
#             "self-harm": 0.5251772927497116,
#             "sexual/minors": 0.00002199533724320648,
#             "violence/graphic": 0.006131033203196622
#           },
#             "flagged": true
#         }
#     ]
# }
# ```
