from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(Body: str = Form(...)):
    mensaje_usuario = Body.strip().lower()

    if "hola" in mensaje_usuario or "buenas" in mensaje_usuario:
        respuesta = "¡Hola! 👋 ¿En qué puedo ayudarte hoy?"
    elif "precio" in mensaje_usuario or "cuánto cuesta" in mensaje_usuario:
        respuesta = "Tenemos varias opciones. ¿Qué producto te interesa?"
    elif "presupuesto" in mensaje_usuario or "lista" in mensaje_usuario:
        respuesta = "📋 Claro, adjuntanos el listado de lo que necesitás"
    elif "entrega" in mensaje_usuario:
        respuesta = "🚚 Realizamos entregas en el día según la zona"
    elif "pago" in mensaje_usuario or "forma de pago" in mensaje_usuario:
        respuesta = "💰 Aceptamos efectivo, transferencia y pagos por link"
    elif "gracias" in mensaje_usuario:
        respuesta = "🙏 ¡Gracias a vos por comunicarte con nosotros!"
    else:
        respuesta = "❓ Lo siento, no entendí tu mensaje. ¿Podés repetirlo?"

    return PlainTextResponse(content=respuesta) 
