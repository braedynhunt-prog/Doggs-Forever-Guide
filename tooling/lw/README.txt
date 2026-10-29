Leatherworking / Skinning data pulled from Wowhead Forever on 27 Oct 2026 via the Claude desktop built-in browser
(www.wowhead.com blocks scripts; these are the pages' embedded Listview tables, dumped with JS in the page).

lw_recipes_forever.json   spells[]: every Leatherworking recipe on wowhead.com/forever/spells/professions/leatherworking (601 rows, 590 craftable)
                          id = spell id, learnedat = orange skill, colors = [orange, yellow, green, grey], reagents = [[itemId, count], ...],
                          creates = [itemId, min, max], source (5 = recipe item / vendor, 6 = trainer), status = new/updated/unchanged in Forever.
                          items{} is empty (names resolve from tooling\qdb\item.json or nether.wowhead.com/forever/tooltip/item/<id>).
skill_page_items.json     recipeItems[] (461 Pattern: items with the skill they require and source) and crafted[] (512 craftable items with
                          reqlevel, slot, quality, armor, spell id) from wowhead.com/forever/skill=165/leatherworking.
leather_sources_forever.json  per item id: skinned-from / dropped-by / contained-in-object rows (count/outof = all-time Wowhead samples,
                          fcount/foutof = Forever-only samples where Wowhead has them, pctstack = stack-size split), created-by-spell,
                          and the Pristine Leather comments. Items: 2318 Light Leather, 783 Light Hide, 2319 Medium Leather, 4232 Medium Hide,
                          4234 Heavy Leather, 249427 Pristine Leather, 249410 Sulfuric Acid.
