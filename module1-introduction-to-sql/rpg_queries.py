import sqlite3
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

# 1How many total characters are there?
chars = 'SELECT COUNT(*) FROM charactercreator_character'

result1 = curs.execute(chars).fetchall()
print("Question 1", result1)


# 2 How many of each specific subclass?
cleric_count = 'SELECT COUNT(*) FROM charactercreator_cleric'
fighter_count = 'SELECT COUNT(*) FROM charactercreator_fighter'
mage_count = 'SELECT COUNT(*) FROM charactercreator_mage'
thief_count = 'SELECT COUNT(*) FROM charactercreator_thief'

cler = curs.execute(cleric_count).fetchall()
fight = curs.execute(fighter_count).fetchall()
mage = curs.execute(mage_count).fetchall()
thief = curs.execute(thief_count).fetchall()

print("Question 2", 'Clerics', cler, 'Fighters', fight, 'Mages', mage, 'Thiefs', thief)

#3 How many total items?

items = 'SELECT COUNT(*) FROM armory_item'

item_result = curs.execute(items).fetchall()

print("Question 3 - How many items total", item_result)

#4 How many of the items are weapons? How many are not?

weapons = 'SELECT COUNT(*) FROM armory_weapon'
wepcount = curs.execute(weapons).fetchall()

non_weapons = (174 - 37)
print("Question 4", "Weapon Count", wepcount, "Non-Weapon Count", non_weapons)

#5 How many items does each character have?

item_count = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory c GROUP BY c.character_id LIMIT 20'

### EASTER EGG - THIS WORKS TOO! ##############################
# SELECT c.character_id, COUNT(inv.item_id) as item_count   ###
# FROM charactercreator_character c                         ###
# LEFT JOIN charactercreator_character_inventory inv        ###
# ON c.character_id = inv.character_id                      ###
# GROUP BY c.character_id                                   ###
# LIMIT 20                                                  ###
###############################################################


item_countz = curs.execute(item_count).fetchall()
print("Question 5 - Char ID's with item totals", item_countz)

#6 How many weapons does each character have?
weapons_per_char = """
SELECT 
      c.character_id
      -- ,c."name"
      --,inv.*
      --,w.*
      ,count(distinct w.item_ptr_id) as weapon_count
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
    LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id
    GROUP BY c.character_id
    LIMIT 20
    """

weapons_answer = curs.execute(weapons_per_char).fetchall()

print("Question 6 - How many weapons does each character have?", weapons_answer)

#7 On average, how many items does each character have?
answer0 = """
SELECT AVG(item_count) as avg_items_per_char
FROM (
    SELECT 
      c.character_id
      -- ,c."name"
      --,inv.*
      --,i.*
      ,count(distinct i.item_id) as item_count
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
    LEFT JOIN armory_item i ON inv.item_id = i.item_id
    GROUP BY c.character_id
) subq
"""
da_answer0 = curs.execute(answer0).fetchall()

print("Question 7 - AVERAGE ITEMS PER CHAR", da_answer0)

# 8 On average, how many weapons does each character have?
answer = """
SELECT AVG(weapon_count) as avg_weapons_per_char
FROM (
    SELECT 
      c.character_id
      -- ,c."name"
      --,inv.*
      --,w.*
      ,count(distinct w.item_ptr_id) as weapon_count
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
    LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id
    GROUP BY c.character_id
) subq
"""
da_answer = curs.execute(answer).fetchall()

print("Question 8 - AVERAGE WEAPONS PER CHAR", da_answer)