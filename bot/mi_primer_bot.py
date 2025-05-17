from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Hola! Soy tu primer bot de Telegram. Pon /frase, para observar una frase célebre en ciencia,/help para obtener ayuda, /mensaje, para ver los recursos de este bot')

    # Comando /help

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Envía /start para comenzar.')

# Comando/ frases inspiradoras
async def frase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    frase = [
        "Las matemáticas son el alfabeto con el cual Dios ha escrito el universo(Galileo Galilei)",
        "La belleza de las matemáticas sólo se muestra a sus seguidores más pacientes(Maryam Mirzakhani)",
        "La matemática es la ciencia del orden y la medida, de bellas cadenas de razonamientos, todos sencillos y fáciles(René Descartes)",
        "Los problemas matemáticos no son más que ejercicios para entrenar a nuestros cerebros(Albert Einstein).",
        "Las matemáticas pueden ser definidas como aquel tema en el cual no sabemos nunca lo que estamos hablando, ni si lo que decimos es cierto (Bertrand Russell)",
        "Las matemáticas son la puerta y la llave de las ciencias (Roger Bacon)",
        "El lenguaje de la verdad debe ser sencillo y sin adornos (Euclides)",
        "La mente intuitiva es un regalo sagrado y la mente racional es un fiel sirviente. Hemos creado una sociedad que honra al sirviente y ha olvidado el regalo(Albert Einstein)",
        "La matemática es la música de la razón.(James Joseph Sylvester)",
        "Un problema bien planteado es un problema medio resuelto(John Dewey)",
        
    ]
    import random
    await update.message.reply_text(random.choice(frase))

#Comando / Libros - Escoge que libro quieres de que curso
async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Para ver los libros disponibles, tenemos de aritmética, álgebra, geometría, trigonometría. escribe: /curso que prefieras. Ejemplo: /aritmética.')


def main():
    app = ApplicationBuilder().token('7726147210:AAHanuBY9zMwGb86sOYUC-ufBiOUr5sAiQ4').build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("frase", frase))
    app.add_handler(CommandHandler("mensaje", mensaje))
    app.run_polling()

if __name__ == '__main__':
    main()
 