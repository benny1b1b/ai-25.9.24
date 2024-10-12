# .2 קלוט מספרים מהמשתמש בין .0-10 אם נקלט מספר לא בתחום הזה, התעלם.
# אם ייקלט המספר מינוס 999 צא מהלולאה .
# הוסף כל מספר שנקלט לרשימה
# אחרי כל קלט הדפס כמה מספרים נקלטו מכל אחד )רק אם נקלט אחד או יותר(


l_num: list[int] = []
SENTINEL= -999
statistics= 0
while True:
    num: int = int(input("enter a number: "))
    if num == SENTINEL:
        break
    if not 0 <= num <= 10:
        continue
    l_num.append(num)

    print("statistics: ", end="")
    for i in range(10 + 1):             # הלולאה תרוץ מהמספר 0 עד 10 כולל
        counts: int = l_num.count(i)    # וכל הרצה של הלולאה נבדוק עם counts כמה פעמים המספר מופיע ברשימה עם פקודת count
        if counts >= 1:                 #אם נמצא מספר שנכתב פעם 1 ויותר ציין זאת
            print(f"[{i}]: {counts}", end=" ") #  ונדפיס כך - המספר i, עם כמות החזרות counts וממשיך למספר הבא באותה השורה
    print()