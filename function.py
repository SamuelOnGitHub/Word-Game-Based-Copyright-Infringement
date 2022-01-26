def funko(c):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    homeless = "🄰 🄱 🄲 🄳 🄴 🄵 🄶 🄷 🄸 🄹 🄺 🄻 🄼 🄽 🄾 🄿 🅀 🅁 🅂 🅃 🅄 🅅 🅆 🅇 🅈 🅉".replace(" ", "")
    wrong = "🅐 🅑 🅒 🅓 🅔 🅕 🅖 🅗 🅘 🅙 🅚 🅛 🅜 🅝 🅞 🅟 🅠 🅡 🅢 🅣 🅤 🅥 🅦 🅧 🅨 🅩".replace(" ", "")
    right = c.upper()
    return(right, homeless[alphabet.index(c)], wrong[alphabet.index(c)])
def rules(num):
  right = "CORRECT LETTERS"
  misplaced = "🄼🄸🅂🄿🄻🄰🄲🄴🄳 🄻🄴🅃🅃🄴🅁🅂"
  wrong = "🅦🅡🅞🅝🅖 🅛🅔🅣🅣🅔🅡🅢"

  respones = (right, misplaced, wrong)
  return respones[num]
