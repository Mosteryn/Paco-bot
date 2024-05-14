import org.pircbotx.Configuration;
import org.pircbotx.PircBotX;
import org.pircbotx.hooks.ListenerAdapter;
import org.pircbotx.hooks.events.MessageEvent;

public class TwitchBot extends ListenerAdapter {
    public static void main(String[] args) throws Exception {
        // Configura tu bot
        Configuration configuration = new Configuration.Builder()
                .setName("NombreDeTuBot") // Nombre del bot
                .setServerPassword("oauth:tu_token_oauth") // Token de acceso OAuth
                .addServer("irc.chat.twitch.tv") // Servidor de Twitch IRC
                .addAutoJoinChannel("#nombre_del_canal") // Canal al que se unirá el bot
                .addListener(new TwitchBot()) // Añade el bot como un listener
                .buildConfiguration();

        // Crea el bot
        PircBotX bot = new PircBotX(configuration);

        // Inicia el bot
        bot.startBot();
    }

    @Override
    public void onMessage(MessageEvent event) throws Exception {
        // Si el mensaje es "!hola", el bot responderá "¡Hola, [nombre de usuario]!"
        if (event.getMessage().startsWith("!hola")) {
            event.respond("¡Hola, " + event.getUser().getNick() + "!");
        }
    }
}
