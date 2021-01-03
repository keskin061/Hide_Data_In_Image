from stegano import lsb

secret = lsb.hide("Ataturk.png", "The supreme guide in life is science.")
secret.save("secret.png")

print(lsb.reveal("secret.png"))
