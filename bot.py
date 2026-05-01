import logging
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ─────────────────────────────────────────
# Configura tu token aquí
# ─────────────────────────────────────────
TOKEN = "8640868141:AAGS1OgvoMl_VJydMG1pt55Ig03VYsQ5RKo"  # Reemplaza con el token de BotFather

# ─────────────────────────────────────────
# Datos del proyecto  ← edita a tu gusto
# ─────────────────────────────────────────
PROYECTO = {
    "nombre": "Sistema de Inferencia Lógica con Prolog",
    "descripcion": (
        "Proyecto de Inteligencia Artificial que modela bases de conocimiento "
        "usando Prolog, con hechos, reglas y predicados recursivos para resolver "
        "problemas de inferencia lógica."
    ),
    "integrantes": [
        {"nombre": "Jorge Alejandro De León Batres", "carnet": "202111277"},
        {"nombre": "Carlos José Blanco Guzmán", "carnet": "202100250"},
        {"nombre": "Carlos Fernando Enrique López García", "carnet": "202210108"},
        {"nombre": "Diego Andre Gomez Esturban", "carnet": "201908327"},
    ],
}

CONTACTO = {
    "correo": "3009537710101@ingenieria.usac.edu.gt",
    "telegram": "@IA1_G9_T5BOT",
    "github": "https://github.com/JorgeBa3/IA1_Tarea5_Grupo9",
}

# ─────────────────────────────────────────
# Logging
# ─────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# ─────────────────────────────────────────
# Handlers
# ─────────────────────────────────────────
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(
        f" ¡Hola, {user}! Soy el bot asistente del proyecto de IA1.\n\n"
        "Comandos disponibles:\n"
        "/hola     – Saludo\n"
        "/hora     – Hora actual\n"
        "/contacto – Info de contacto\n"
        "/proyecto – Info del proyecto"
    )


async def hora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    await update.message.reply_text(f" Fecha y hora actual (servidor):\n`{ahora}`", parse_mode="Markdown")


async def contacto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📬 *Información de contacto*\n\n"
        f" Correo: {CONTACTO['correo']}\n"
        f" Telegram: {CONTACTO['telegram']}\n"
        f" GitHub: {CONTACTO['github']}"
    )
    await update.message.reply_text(msg, parse_mode="Markdown")


async def proyecto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    integrantes_str = "\n".join(
        f"  • {i['nombre']} – {i['carnet']}" for i in PROYECTO["integrantes"]
    )
    msg = (
        f"*{PROYECTO['nombre']}*\n\n"
        f"{PROYECTO['descripcion']}\n\n"
        f" *Integrantes:*\n{integrantes_str}"
    )
    await update.message.reply_text(msg, parse_mode="Markdown")


# ─────────────────────────────────────────
# Main
# ─────────────────────────────────────────
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("hola", hola))
    app.add_handler(CommandHandler("hora", hora))
    app.add_handler(CommandHandler("contacto", contacto))
    app.add_handler(CommandHandler("proyecto", proyecto))

    print(" Bot corriendo... Presiona Ctrl+C para detener.")
    app.run_polling()


if __name__ == "__main__":
    main()