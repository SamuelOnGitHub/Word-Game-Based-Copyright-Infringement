def funko(c):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    homeless = "π° π± π² π³ π΄ π΅ πΆ π· πΈ πΉ πΊ π» πΌ π½ πΎ πΏ π π π π π π π π π π".replace(" ", "")
    wrong = "π π π π π π π π π π π π π π π π π  π‘ π’ π£ π€ π₯ π¦ π§ π¨ π©".replace(" ", "")
    right = c.upper()
    return(right, homeless[alphabet.index(c)], wrong[alphabet.index(c)])
def rules(num):
  right = "CORRECT LETTERS"
  misplaced = "πΌπΈππΏπ»π°π²π΄π³ π»π΄πππ΄ππ"
  wrong = "π¦π‘πππ πππ£π£ππ‘π’"

  respones = (right, misplaced, wrong)
  return respones[num]
