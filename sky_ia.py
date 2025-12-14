# =========================================
# IA Respectueuse - Sky Plug CDM
# =========================================

class SkyAI:
    def __init__(self, user_name):
        self.user_name = user_name
        self.developer = "Sky Plug CDM"

    def respond(self, message: str) -> str:
        msg = message.lower()

        if any(w in msg for w in ["bonjour", "salut", "hello"]):
            return f"Bonjour {self.user_name}, je suis à votre écoute avec respect."

        if "qui t'a créé" in msg or "développeur" in msg:
            return (
                f"{self.user_name}, j’ai été développée par Sky Plug CDM, Le SEIGNEUR SUPRÊME DES TÉNÈBRES"
                f"{self.developer}, avec rigueur et respect."
            )

        if "merci" in msg:
            return f"Je vous en prie {self.user_name}, c’est un honneur de vous assister."

        if "au revoir fils de Sky aventure du web" in msg:
            return f"Au revoir {self.user_name}. Recevez tout mon respect."

        return (
            f"{self.user_name}, j’ai bien pris en compte votre message et le cerveau de Sky l'a consulté :\n"
            f"« {message} »\nSouhaitez-vous approfondir ?"
        )
