pogoda = int(input("Погода? "))

if pogoda < -30:
    print("🧊☠️ ❄️")
elif pogoda < -5 and pogoda > -30:
    print("❄️ 🌨️")
elif pogoda < 11 and pogoda > -5:
    print("⛈️ 🌧️")
elif pogoda < 16 and pogoda > 10:
    print("🌥️ 🌦️")
elif pogoda < 26 and pogoda > 15:
    print("😎☀️")
elif pogoda < 50 and pogoda > 25:
    print("🔥☀️ 🥵")
elif pogoda < 100 and pogoda > 49:
    print("🔥☠️ 🏜️")
elif pogoda > 99:
    print("🔥🔥🔥🔥🔥🔥🔥🔥")