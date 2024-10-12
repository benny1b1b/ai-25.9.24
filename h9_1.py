# .1 רשימות חלק ב'-
# a. ייצר רשימה ריקה של מספרים עשרוניים של טמפרטור ות
# b. קלוט מהמשתמש טמפרטורות עד אשר ייקלט המספר מינוס .999 כל טמפרטורה
# שנקלטה הוסף לרשימה. לא נוסיף טמפרטורה גדולה מ 50 או קטנה ממינוס 50
# c. הוסף את רשימת הטמפרטורות הבאה בסוף הרשימה הנוכחית: ],18.5 ,39.1 -20.0[
# )רמז extend )
# d. מה ההבדל בין extend לבין פעולת ) +( בין רשימות : לדוגמא [4,5,6]+[1,2,3]?
# e. הדפס את הטמפרטורה: הגבוהה ביותר )רמז max), הנמוכה ביותר )רמז min )
# f. בדוק אם הטמפרטורה 18.5 ברשימה )רמז in). אם כן הדפס True אחרת False
# g. ספור כמה פעמים חוזרת הטמפרטורה -20.0 )רמז count)
# h. הדפס את ממוצע הטמפרטורות באמצעות sum ו- len
# i. הדפס כל טמפרטורה בשורה נפרדת ) רמז: each for )
# j. מצא את האינדקס של הטמפרטורה 39.1 )רמז index )
# k. הסר את הטמפרטורה באינדקס 0 )רמז del )
# l. הסר את הטמפרטורה בכל אינדקס זוגי )רמז :2 del )
# m. הסר את טמפרטורה 18.5 )רמז remove ). מדוע כדאי לבדוק אם קיים לפני remove?
# n. שלוף את הטמפרטורה האחרונה ברשימה לתוך תא זיכרון בשם last_temp( רמז pop )
# o. שכפל את הרשימה באמצעות copy, מיין את הרשימה החדשה שיצרת
# p. שכפל את הרשימה שוב באמצעות copy, מיין את הרשימה החדשה שיצרת בסדר הפוך
from itertools import count
from operator import index
from os import times, remove
from pkgutil import extend_path



# a. ייצר רשימה ריקה של מספרים עשרוניים של טמפרטור ות
# b. קלוט מהמשתמש טמפרטורות עד אשר ייקלט המספר מינוס .999 כל טמפרטורה
# שנקלטה הוסף לרשימה. לא נוסיף טמפרטורה גדולה מ 50 או קטנה ממינוס 50
# c. הוסף את רשימת הטמפרטורות הבאה בסוף הרשימה הנוכחית: ],18.5 ,39.1 -20.0[
# )רמז extend )

temp_list: list[float] = []
SENTINEL: int = -999

while True:
    temp: float = float(input("enter your temperature:"))
    if SENTINEL == temp:
        break
    if not -50 < temp < 50:
        continue
    else:
        temp_list.append(temp)

print(temp_list)
temp_list.extend([-20, 39.1, 18.5])
print(temp_list)

#d
# extend- פונקציה שמחברת בין רשימה לאברים אחרים בלי ליצור רשימה חדשה, הפונקציה משנה את תכולתה של הרשימה המקורית.
# בעוד שאופרטואר + מחבר בין רשימות קיימות והחיבור בינהם יוצר רשימה חדשה תוך שהוא שומר את תכולתם של הרשימות המקוריות

print(max(temp_list))
print(min(temp_list))

num= 18.5
print(num in temp_list)

print("temp -20 appears", temp_list.count(-20), "times")


sum_list = sum(temp_list)
avg_temp = sum_list/len(temp_list)
print(f"average temp is: {avg_temp:.2f}")

for temp in temp_list:
    print(temp)

print("index 39.1:", temp_list.index(39.1))

if len(temp_list) >0:
    del temp_list[0]
print(temp_list)

del temp_list[::2]
print(temp_list)

if 18.5 in temp_list:
    temp_list.remove(18.5)
print(temp_list)
#בןדקים לפני הremove שהאיבר קיים כדי שלא תווצר שגיאה

temp_last: float = temp_list.pop()
print(temp_list, temp_last)

clone_temp_list: list[float] = temp_list.copy()
print(clone_temp_list)

clone_temp_list.sort()
print(clone_temp_list)

clone_temp_list1 = clone_temp_list.copy()
print(clone_temp_list1)
clone_temp_list1.sort(reverse=True)
print(clone_temp_list1)

